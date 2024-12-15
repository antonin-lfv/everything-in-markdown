from markitdown import MarkItDown
import streamlit as st

st.set_page_config(page_title="MarkItDown", page_icon=":pencil2:", layout="wide")

st.title("MarkItDown")
st.caption("Convert File to Markdown")

col1, _ = st.columns([1, 1])
file_to_convert_in_md = col1.file_uploader(
    "Upload a file to convert to markdown",
    type=["pdf", "pptx", "docx", "xlsx", "html", "csv", "json", "xml"],
)

if st.button("Convert"):
    st.divider()
    if file_to_convert_in_md is None:
        col1.warning("Please upload a file first.")
    else:
        with st.spinner("Converting file to markdown..."):
            markitdown = MarkItDown()
            result = markitdown.convert_stream(file_to_convert_in_md)
            col1.success("File converted successfully.")
            with st.container(border=True):
                st.subheader("Preview of the first 1000 characters")
                st.write(result.text_content[:1000] + "...")

            st.subheader("Download Markdown File")
            st.download_button(
                label="Download",
                data=result.text_content,
                file_name=f"{file_to_convert_in_md.name}.md",
                mime="text/markdown",
            )
