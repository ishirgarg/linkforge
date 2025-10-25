Here is the markdown version of the provided HTML:
# st.html
## Streamlit Version
1.50.0
1.49.0
1.48.0
1.47.0
1.46.0
1.45.0
1.44.0
1.43.0
1.42.0
1.41.0
1.40.0
1.39.0
1.38.0
1.37.0
1.36.0
1.35.0
1.34.0
1.33.0
1.32.0
1.31.0
1.30.0
1.29.0
1.28.0
1.27.0
1.26.0
1.25.0
1.24.0
1.23.0
1.22.0

Insert HTML into your app.

Adding custom HTML to your app impacts safety, styling, and maintainability. We sanitize HTML with [DOMPurify](https://github.com/cure53/DOMPurify), but inserting HTML remains a developer risk. Passing untrusted code to `st.html` or dynamically loading external code can increase the risk of vulnerabilities in your app.

`st.html` content is **not** iframed. Executing JavaScript is not supported at this time.

### Function signature
```python
st.html(body, *, width="stretch")
```
#### Parameters
* `body` (any): The HTML code to insert. This can be one of the following:
	+ A string of HTML code.
	+ A path to a local file with HTML code. The path can be a str or Path object. Paths can be absolute or relative to the working directory (where you execute `streamlit run`).
	+ Any object. If `body` is not a string or path, Streamlit will convert the object to a string. `body._repr_html_()` takes precedence over `str(body)` when available.
* `width` ("stretch", "content", or int): The width of the HTML element. This can be one of the following:
	+ "stretch" (default): The width of the element matches the width of the parent container.
	+ "content": The width of the element matches the width of its content, but doesn't exceed the width of the parent container.
	+ An integer specifying the width in pixels: The element has a fixed width. If the specified width is greater than the width of the parent container, the width of the element matches the width of the parent container.

### Example
```python
import streamlit as st

st.html("""
<p><span style='text-decoration: line-through double red;'>Oops</span>!</p>
""")
```
If you still have questions, you can visit our [forums](https://discuss.streamlit.io) for helpful information and Streamlit experts. 

You can also find us on:
* [GitHub](https://github.com/streamlit)
* [YouTube](https://www.youtube.com/channel/UC3LD42rjj-Owtxsa6PwGU5Q)
* [Twitter](https://twitter.com/streamlit)
* [LinkedIn](https://www.linkedin.com/company/streamlit)
* [Newsletter](https://info.snowflake.com/streamlit-newsletter-sign-up.html)

&copy; 2025 Snowflake Inc.
[Cookie policy](https://www.streamlit.io/cookie-policy)