# st.pdf - Streamlit Documentation

> Reference: [https://docs.streamlit.io/develop/api-reference/media/st.pdf](https://docs.streamlit.io/develop/api-reference/media/st.pdf)

## st.pdf

Display a PDF viewer.

**Important:** You must install [streamlit-pdf](https://github.com/streamlit/streamlit-pdf) to use this command. You can install it as an extra with Streamlit:

```bash
pip install streamlit[pdf]
```

### Function signature

`st.pdf(data, *, height=500, key=None)`

### Parameters

*   **data** (str, Path, BytesIO, or bytes): The PDF file to show. This can be one of the following:
    *   A URL (string) for a hosted PDF file.
    *   A path to a local PDF file. If you use a relative path, it must be relative to the current working directory.
    *   A file-like object. For example, this can be an UploadedFile from `st.file_uploader`, or this can be a local file opened with `open()`.
    *   Raw bytes data.
*   **height** (int or "stretch"): The height of the PDF viewer. This can be one of the following:
    *   An integer specifying the height in pixels: The viewer has a fixed height. If the content is larger than the specified height, scrolling is enabled. This is 500 by default.
    *   "stretch": The height of the viewer matches the height of its content or the height of the parent container, whichever is larger. If the viewer is not in a parent container, the height of the viewer matches the height of its content.

### Example

```python
st.pdf("https://example.com/sample.pdf")
st.pdf("https://example.com/sample.pdf", height=600)
```
