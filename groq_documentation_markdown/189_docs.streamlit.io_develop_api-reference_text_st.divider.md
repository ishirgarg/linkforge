Here is the converted HTML to clean markdown:

# st.divider - Streamlit Docs
## Overview

Display a horizontal rule.

Note: You can achieve the same effect with `st.write("---")` or even just `"---"` in your script (via magic).

### Function Signature
```python
st.divider(*, width="stretch")
```

### Parameters

* `width`: The width of the divider element. This can be one of the following:
	+ `"stretch"` (default): The width of the element matches the width of the parent container.
	+ An integer specifying the width in pixels: The element has a fixed width. If the specified width is greater than the width of the parent container, the width of the element matches the width of the parent container.

### Example
```python
import streamlit as st

st.divider()
```

Here's what it looks like in action when you have multiple elements in the app:
```python
import streamlit as st

st.write("This is some text.")
st.slider("This is a slider", 0, 100, (25, 75))
st.divider()  # Draws a horizontal rule
st.write("This text is between the horizontal rules.")
st.divider()  # Another horizontal rule
```

### Still have questions?
Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

### Navigation
* [Home](/)
* [Develop](/develop)
* [API reference](/develop/api-reference)
* [Text elements](/develop/api-reference/text)
* [st.divider](/develop/api-reference/text/st.divider)

### Version History
Streamlit Version: 1.50.0, 1.49.0, 1.48.0, 1.47.0, 1.46.0, 1.45.0, 1.44.0, 1.43.0, 1.42.0, 1.41.0, 1.40.0, 1.39.0, 1.38.0, 1.37.0, 1.36.0, 1.35.0, 1.34.0, 1.33.0, 1.32.0, 1.31.0, 1.30.0, 1.29.0, 1.28.0, 1.27.0, 1.26.0, 1.25.0, 1.24.0, 1.23.0, 1.22.0

### Contact Us
[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)
[Community](https://discuss.streamlit.io)

### Social Media
[GitHub](https://github.com/streamlit)
[YouTube](https://www.youtube.com/channel/UC3LD42rjj-Owtxsa6PwGU5Q)
[Twitter](https://twitter.com/streamlit)
[LinkedIn](https://www.linkedin.com/company/streamlit)
[Newsletter](https://info.snowflake.com/streamlit-newsletter-sign-up.html)

&copy; 2025 Snowflake Inc.
[Cookie policy](https://www.streamlit.io/cookie-policy)