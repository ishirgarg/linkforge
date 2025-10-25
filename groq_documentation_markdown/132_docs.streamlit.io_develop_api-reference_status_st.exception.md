### st.exception
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

Display an exception.

When accessing the app through localhost, in the lower-right corner of the exception, Streamlit displays links to Google and ChatGPT that are prefilled with the contents of the exception message.

#### Function signature
```python
st.exception(exception, width="stretch")
```
#### Parameters
* `exception` (Exception): The exception to display.
* `width` ("stretch" or int): The width of the exception element. This can be one of the following:
  * "stretch" (default): The width of the element matches the width of the parent container.
  * An integer specifying the width in pixels: The element has a fixed width. If the specified width is greater than the width of the parent container, the width of the element matches the width of the parent container.

#### Example
```python
import streamlit as st

e = RuntimeError("This is an exception of type RuntimeError")
st.exception(e)
```
Still have questions? Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

[Home](/) | [Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20) | [Community](https://discuss.streamlit.io)

[](https://github.com/streamlit) [](https://www.youtube.com/channel/UC3LD42rjj-Owtxsa6PwGU5Q) [](https://twitter.com/streamlit) [](https://www.linkedin.com/company/streamlit) [](https://info.snowflake.com/streamlit-newsletter-sign-up.html)

&copy; 2025 Snowflake Inc. [Cookie policy](/)