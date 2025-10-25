# st.pdf
Display a PDF viewer.

**Important**: You must install [streamlit-pdf](https://github.com/streamlit/streamlit-pdf) to use this command. You can install it as an extra with Streamlit:
```bash
pip install streamlit[pdf]
```
## Function signature
```python
st.pdf(data, *, height=500, key=None)
```
### Parameters

* **data**: The PDF file to show. This can be one of the following:
	+ A URL (string) for a hosted PDF file.
	+ A path to a local PDF file. If you use a relative path, it must be relative to the current working directory.
	+ A file-like object. For example, this can be an UploadedFile from `st.file_uploader`, or this can be a local file opened with `open()`.
	+ Raw bytes data.
* **height**: The height of the PDF viewer. This can be one of the following:
	+ An integer specifying the height in pixels: The viewer has a fixed height. If the content is larger than the specified height, scrolling is enabled. This is 500 by default.
	+ "stretch": The height of the viewer matches the height of its content or the height of the parent container, whichever is larger. If the viewer is not in a parent container, the height of the viewer matches the height of its content.

## Example
```python
st.pdf("https://example.com/sample.pdf")
st.pdf("https://example.com/sample.pdf", height=600)
```
### Still have questions?
Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

### Useful links

* [Home](/)
* [Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)
* [Community](https://discuss.streamlit.io)
* [GitHub](https://github.com/streamlit)
* [YouTube](https://www.youtube.com/channel/UC3LD42rjj-Owtxsa6PwGU5Q)
* [Twitter](https://twitter.com/streamlit)
* [LinkedIn](https://www.linkedin.com/company/streamlit)
* [Newsletter](https://info.snowflake.com/streamlit-newsletter-sign-up.html)

&copy; 2025 Snowflake Inc. [Cookie policy](/)