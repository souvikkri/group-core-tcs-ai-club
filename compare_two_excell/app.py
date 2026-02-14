import streamlit as st
import pandas as pd
from comparator import compare_excel
from ai_summary import generate_summary

st.set_page_config(page_title="AI Excel Comparison Agent")

st.title("🤖 AI Excel Comparison Agent")

#Upload Excel files from UI
#file1 = st.file_uploader("Upload Old Excel File", type=["xlsx"])
#file2 = st.file_uploader("Upload New Excel File", type=["xlsx"])

#Read file from local path for testing purpose, you can uncomment above lines and comment below lines to use file uploader in streamlit
file1 = "D:/tcs ai club/group-core-tcs-ai-club/compare_two_excell/files/Sheet 1.xlsx"
file2 = "D:/tcs ai club/group-core-tcs-ai-club/compare_two_excell/files/Sheet 2.xlsx"

primary_key = st.text_input("Enter Primary Key Column Name")

if st.button("Compare Files"):

    if file1 and file2 and primary_key:

        with st.spinner("Processing..."):

            added, deleted, modified = compare_excel(file1, file2, primary_key)

            st.success("Comparison Completed!")

            st.subheader("📈 Summary")
            st.write(f"Added Records: {len(added)}")
            st.write(f"Deleted Records: {len(deleted)}")
            st.write(f"Modified Sections: {len(modified)}")

            if len(added) > 0:
                st.subheader("🟢 Added Records")
                st.dataframe(added)

            if len(deleted) > 0:
                st.subheader("🔴 Deleted Records")
                st.dataframe(deleted)

            if len(modified) > 0:
                st.subheader("🟡 Modified Records")
                for i, df in enumerate(modified):
                    st.dataframe(df)

            # Generate AI Summary
            try:
                summary = generate_summary(added, deleted, modified)
                st.subheader("🧠 AI Business Summary")
                st.write(summary)
            except:
                st.warning("AI summary not generated. Check API key.")

    else:
        st.error("Please upload both files and enter primary key.")
