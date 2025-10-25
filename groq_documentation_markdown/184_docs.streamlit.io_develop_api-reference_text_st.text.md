Here is the HTML converted to clean Markdown:
### st.text
#### Streamlit Version
Version 1.50.0
Version 1.49.0
Version 1.48.0
Version 1.47.0
Version 1.46.0
Version 1.45.0
Version 1.44.0
Version 1.43.0
Version 1.42.0
Version 1.41.0
Version 1.40.0
Version 1.39.0
Version 1.38.0
Version 1.37.0
Version 1.36.0
Version 1.35.0
Version 1.34.0
Version 1.33.0
Version 1.32.0
Version 1.31.0
Version 1.30.0
Version 1.29.0
Version 1.28.0
Version 1.27.0
Version 1.26.0
Version 1.25.0
Version 1.24.0
Version 1.23.0
Version 1.22.0

Write text without Markdown or HTML parsing.

For monospace text, use [st.code](https://docs.streamlit.io/develop/api-reference/text/st.code).

#### Function signature
```python
st.text(body, *, help=None, width="content")
```
#### Parameters

* `body` (str): The string to display.
* `help` (str or None): A tooltip that gets displayed next to the text. If this is None (default), no tooltip is displayed.
* `width` ("content", "stretch", or int): The width of the text element. This can be one of the following:
  * "content" (default): The width of the element matches the width of its content, but doesn't exceed the width of the parent container.
  * "stretch": The width of the element matches the width of the parent container.
  * An integer specifying the width in pixels: The element has a fixed width. If the specified width is greater than the width of the parent container, the width of the element matches the width of the parent container.

#### Example
```python
import streamlit as st
st.text("This is text\n[and more text](that's not a Markdown link).")
```
### Navigation
* [Previous: st.latex](/develop/api-reference/text/st.latex)
* [Next: st.help](/develop/api-reference/text/st.help)

### Still have questions?
Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

### Contact Us
* [Home](/)
* [Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)
* [Community](https://discuss.streamlit.io)
* [GitHub](https://github.com/streamlit)
* [YouTube](https://www.youtube.com/channel/UC3LD42rjj-Owtxsa6PwGU5Q)
* [Twitter](https://twitter.com/streamlit)
* [LinkedIn](https://www.linkedin.com/company/streamlit)
* [Newsletter](https://info.snowflake.com/streamlit-newsletter-sign-up.html)

&copy; 2025 Snowflake Inc.
[Cookie policy](https://www.streamlit.io/cookie-policy)