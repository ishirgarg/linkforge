# st.subheader

**URL Reference:** https://docs.streamlit.io/develop/api-reference/text/st.subheader

## st.subheader

### Parameters

*   **body** (`str`)
    The text to display as GitHub-flavored Markdown. Syntax information can be found at: [https://github.github.com/gfm](https://github.github.com/gfm).

    See the body parameter of [st.markdown](https://docs.streamlit.io/develop/api-reference/text/st.markdown) for additional, supported Markdown directives.

*   **anchor** (`str` or `False`)
    The anchor name of the header that can be accessed with `#anchor` in the URL. If omitted, it generates an anchor using the body. If `False`, the anchor is not shown in the UI.

*   **help** (`str` or `None`)
    A tooltip that gets displayed next to the subheader. If this is `None` (default), no tooltip is displayed.

    The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of `st.markdown`.

*   **divider** (`bool`, `"blue"`, `"green"`, `"orange"`, `"red"`, `"violet"`, `"yellow"`, `"gray"`/`"grey"`, or `"rainbow"`)
    Shows a colored divider below the header. If this is `True`, successive headers will cycle through divider colors, except gray and rainbow. That is, the first header will have a blue line, the second header will have a green line, and so on. If this is a string, the color can be set to one of the following: blue, green, orange, red, violet, yellow, gray/grey, or rainbow.

*   **width** (`"stretch"`, `"content"`, or `int`)
    The width of the subheader element. This can be one of the following:
    *   `"stretch"` (default): The width of the element matches the width of the parent container.
    *   `"content"`: The width of the element matches the width of its content, but doesn't exceed the width of the parent container.
    *   An integer specifying the width in pixels: The element has a fixed width. If the specified width is greater than the width of the parent container, the width of the element matches the width of the parent container.

#### Examples

```python
import streamlit as st

st.subheader("_Streamlit_ is :blue[cool] :sunglasses:")
st.subheader("This is a subheader with a divider", divider="gray")
st.subheader("These subheaders have rotating dividers", divider=True)
st.subheader("One", divider=True)
st.subheader("Two", divider=True)
st.subheader("Three", divider=True)
st.subheader("Four", divider=True)
```

### Conclusion

The `st.subheader` function in Streamlit is used to display text in a subheader format, providing a clear hierarchical structure within your application's content. It supports rich text formatting through Markdown and offers customization options for anchors, tooltips, dividers, and element width.

### Navigation

*   [Previous: st.header](/develop/api-reference/text/st.header)
*   [Next: st.markdown](/develop/api-reference/text/st.markdown)

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.