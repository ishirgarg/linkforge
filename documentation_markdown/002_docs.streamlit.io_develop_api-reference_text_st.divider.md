# st.divider
## Streamlit Documentation

### Overview

The `st.divider` function is used to display a horizontal rule in a Streamlit app.

### Note

You can achieve the same effect with `st.write("---")` or even just `"---"` in your script (via magic).

### Function Signature

```python
st.divider(*, width="stretch")
```

### Parameters

* `width` ("stretch" or int): The width of the divider element. This can be one of the following:
	+ "stretch" (default): The width of the element matches the width of the parent container.
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

### Previous and Next

* Previous: [st.code](/develop/api-reference/text/st.code)
* Next: [st.echo](/develop/api-reference/text/st.echo)

### Still Have Questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

### Streamlit Links

* [Home](/)
* [Develop](/develop)
* [API Reference](/develop/api-reference)
* [Text Elements](/develop/api-reference/text)
* [st.divider](/develop/api-reference/text/st.divider)

### Social Media

* [GitHub](https://github.com/streamlit)
* [YouTube](https://www.youtube.com/channel/UC3LD42rjj-Owtxsa6PwGU5Q)
* [Twitter](https://twitter.com/streamlit)
* [LinkedIn](https://www.linkedin.com/company/streamlit)
* [Newsletter](https://info.snowflake.com/streamlit-newsletter-sign-up.html)

&copy; 2025 Snowflake Inc. [Cookie Policy](https://www.streamlit.io/cookie-policy)