# st.divider - Streamlit

> **Source:** [https://docs.streamlit.io/develop/api-reference/text/st.divider](https://docs.streamlit.io/develop/api-reference/text/st.divider)

## `st.divider`

Displays a horizontal rule.

**Note:** You can achieve the same effect with `st.write("---")` or even just `"---"` in your script (via magic).

### Function signature

```python
st.divider(*, width="stretch")
```

### Parameters

*   **width** (`"stretch"` or `int`): The width of the divider element. This can be one of the following:
    *   `"stretch"` (default): The width of the element matches the width of the parent container.
    *   An integer specifying the width in pixels: The element has a fixed width. If the specified width is greater than the width of the parent container, the width of the element matches the width of the parent container.

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
st.divider()  # 👈 Draws a horizontal rule
st.write("This text is between the horizontal rules.")
st.divider()  # 👈 Another horizontal rule
```

![st.divider example](/images/api/st.divider.png)

---

**Previous:** [st.code](/develop/api-reference/text/st.code)
**Next:** [st.echo](/develop/api-reference/text/st.echo)
