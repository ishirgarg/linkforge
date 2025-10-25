# st.components.v1.html - Streamlit

> **Source:** [https://docs.streamlit.io/develop/api-reference/custom-components/st.components.v1.html](https://docs.streamlit.io/develop/api-reference/custom-components/st.components.v1.html)

## `st.components.v1.html`

Display an HTML string in an iframe.

To use this function, import it from the `streamlit.components.v1` module.

If you want to insert HTML text into your app without an iframe, try `st.html` instead.

**Warning:** Using `st.components.v1.html` directly (instead of importing its module) is deprecated and will be disallowed in a later version.

### Function signature

```python
st.components.v1.html(html, width=None, height=None, scrolling=False, *, tab_index=None)
```

### Parameters

*   **html** (str): The HTML string to embed in the iframe.
*   **width** (int): The width of the iframe in CSS pixels. By default, this is the app's default element width.
*   **height** (int): The height of the frame in CSS pixels. By default, this is 150.
*   **scrolling** (bool): Whether to allow scrolling in the iframe. If this is `False` (default), Streamlit crops any content larger than the iframe and does not show a scrollbar. If this is `True`, Streamlit shows a scrollbar when the content is larger than the iframe.
*   **tab_index** (int or None): Specifies how and if the iframe is sequentially focusable. Users typically use the Tab key for sequential focus navigation.

    This can be one of the following values:

    *   `None` (default): Uses the browser's default behavior.
    *   `-1`: Removes the iframe from sequential navigation, but still allows it to be focused programmatically.
    *   `0`: Includes the iframe in sequential navigation in the order it appears in the document but after all elements with a positive `tab_index`.
    *   Positive integer: Includes the iframe in sequential navigation. Elements are navigated in ascending order of their positive `tab_index`.

    For more information, see the [tabindex](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/tabindex) documentation on MDN.

### Example

```python
import streamlit.components.v1 as components

components.html(
    "<p><span style='text-decoration: line-through double red;'>Oops</span>!</p>"
)
```

---

**Previous:** [st.components.v1​.declare\_component](/develop/api-reference/custom-components/st.components.v1.declare_component)
**Next:** [st.components.v1.iframe](/develop/api-reference/custom-components/st.components.v1.iframe)
