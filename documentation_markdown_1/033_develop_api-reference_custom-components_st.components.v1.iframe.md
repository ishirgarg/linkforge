```markdown
# st.components.v1.iframe - Streamlit

> **Source:** [https://docs.streamlit.io/develop/api-reference/custom-components/st.components.v1.iframe](https://docs.streamlit.io/develop/api-reference/custom-components/st.components.v1.iframe)

## `st.components.v1.iframe`

Load a remote URL in an iframe.

To use this function, import it from the `streamlit.components.v1` module.

**Warning:** Using `st.components.v1.iframe` directly (instead of importing its module) is deprecated and will be disallowed in a later version.

### Function signature

```python
st.components.v1.iframe(src, width=None, height=None, scrolling=False, *, tab_index=None)
```

### Parameters

*   **src** (str): The URL of the page to embed.
*   **width** (int): The width of the iframe in CSS pixels. By default, this is the app's default element width.
*   **height** (int): The height of the frame in CSS pixels. By default, this is 150.
*   **scrolling** (bool): Whether to allow scrolling in the iframe. If this is `False` (default), Streamlit crops any content larger than the iframe and does not show a scrollbar. If this is `True`, Streamlit shows a scrollbar when the content is larger than the iframe.
*   **tab\_index** (int or None): Specifies how and if the iframe is sequentially focusable. Users typically use the Tab key for sequential focus navigation.

    This can be one of the following values:

    *   `None` (default): Uses the browser's default behavior.
    *   `-1`: Removes the iframe from sequential navigation, but still allows it to be focused programmatically.
    *   `0`: Includes the iframe in sequential navigation in the order it appears in the document but after all elements with a positive `tab_index`.
    *   Positive integer: Includes the iframe in sequential navigation. Elements are navigated in ascending order of their positive `tab_index`.

    For more information, see the [tabindex](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/tabindex) documentation on MDN.

### Example

```python
import streamlit.components.v1 as components

components.iframe("https://example.com", height=500)
```
```
