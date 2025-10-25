```markdown
# st.title

[Original URL](https://docs.streamlit.io/develop/api-reference/text/st.title)

Display text in title formatting.

Each document should have a single `st.title()`, although this is not enforced.

## Function signature

[`st.title(body, anchor=None, *, help=None, width="stretch")`](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/elements/heading.py#L223 "View st.title source code on GitHub")

## Parameters

### `body` (str)

The text to display as GitHub-flavored Markdown. Syntax information can be found at: [https://github.github.com/gfm](https://github.github.com/gfm).

See the `body` parameter of [`st.markdown`](https://docs.streamlit.io/develop/api-reference/text/st.markdown) for additional, supported Markdown directives.

### `anchor` (str or False)

The anchor name of the header that can be accessed with `#anchor` in the URL. If omitted, it generates an anchor using the body. If `False`, the anchor is not shown in the UI.

### `help` (str or None)

A tooltip that gets displayed next to the title. If this is `None` (default), no tooltip is displayed.

The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the `body` parameter of `st.markdown`.

### `width` ("stretch", "content", or int)

The width of the title element. This can be one of the following:

*   `"stretch"` (default): The width of the element matches the width of the parent container.
*   `"content"`: The width of the element matches the width of its content, but doesn't exceed the width of the parent container.
*   An integer specifying the width in pixels: The element has a fixed width. If the specified width is greater than the width of the parent container, the width of the element matches the width of the parent container.

## Examples

```python
import streamlit as st

st.title("This is a title")
st.title("_Streamlit_ is :blue[cool] :sunglasses:")
```
```

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.
