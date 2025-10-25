Here is the HTML content converted to clean Markdown:
### st.components.v1.html
#### Streamlit Version
* Version 1.50.0
* Version 1.49.0
* Version 1.48.0
* Version 1.47.0
* Version 1.46.0
* Version 1.45.0
* Version 1.44.0
* Version 1.43.0
* Version 1.42.0
* Version 1.41.0
* Version 1.40.0
* Version 1.39.0
* Version 1.38.0
* Version 1.37.0
* Version 1.36.0
* Version 1.35.0
* Version 1.34.0
* Version 1.33.0
* Version 1.32.0
* Version 1.31.0
* Version 1.30.0
* Version 1.29.0
* Version 1.28.0
* Version 1.27.0
* Version 1.26.0
* Version 1.25.0
* Version 1.24.0
* Version 1.23.0
* Version 1.22.0

Display an HTML string in an iframe.

To use this function, import it from the `streamlit.components.v1` module.

If you want to insert HTML text into your app without an iframe, try `st.html` instead.

**Warning**
Using `st.components.v1.html` directly (instead of importing its module) is deprecated and will be disallowed in a later version.

#### Function signature
```python
st.components.v1.html(html, width=None, height=None, scrolling=False, *, tab_index=None)
```
#### Parameters
* `html` (str): The HTML string to embed in the iframe.
* `width` (int): The width of the iframe in CSS pixels. By default, this is the app's default element width.
* `height` (int): The height of the frame in CSS pixels. By default, this is 150.
* `scrolling` (bool): Whether to allow scrolling in the iframe. If this False (default), Streamlit crops any content larger than the iframe and does not show a scrollbar. If this is True, Streamlit shows a scrollbar when the content is larger than the iframe.
* `tab_index` (int or None): Specifies how and if the iframe is sequentially focusable. Users typically use the Tab key for sequential focus navigation.

#### Example
```python
import streamlit.components.v1 as components

components.html(
    "<p><span style='text-decoration: line-through double red;'>Oops</span>!</p>"
)
```
Still have questions? Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

* [Home](/)
* [Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)
* [Community](https://discuss.streamlit.io)

[GitHub](https://github.com/streamlit)
[YouTube](https://www.youtube.com/channel/UC3LD42rjj-Owtxsa6PwGU5Q)
[Twitter](https://twitter.com/streamlit)
[LinkedIn](https://www.linkedin.com/company/streamlit)
[Newsletter](https://info.snowflake.com/streamlit-newsletter-sign-up.html)

2025 Snowflake Inc.
[Cookie policy](https://www.streamlit.io/cookie-policy)