import pandas as pd

def compare_excel(file1, file2, primary_key):

    df1 = pd.read_excel(file1)
    df2 = pd.read_excel(file2)

    df1.columns = df1.columns.str.strip()
    df2.columns = df2.columns.str.strip()

    if primary_key not in df1.columns or primary_key not in df2.columns:
        raise Exception("Primary key not found in both files.")

    merged = df1.merge(
        df2,
        on=primary_key,
        how="outer",
        indicator=True,
        suffixes=("_old", "_new")
    )

    added = merged[merged["_merge"] == "right_only"]
    deleted = merged[merged["_merge"] == "left_only"]
    common = merged[merged["_merge"] == "both"]

    modified_rows = []

    for col in df1.columns:
        if col != primary_key:
            old_col = f"{col}_old"
            new_col = f"{col}_new"

            if old_col in common.columns and new_col in common.columns:
                changes = common[common[old_col] != common[new_col]]
                if not changes.empty:
                    modified_rows.append(changes)

    return added, deleted, modified_rows
