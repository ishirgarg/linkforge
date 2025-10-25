# st.text

[Original URL](https://docs.streamlit.io/develop/api-reference/text/st.text)

Write text without Markdown or HTML parsing.

For monospace text, use [st.code](https://docs.streamlit.io/develop/api-reference/text/st.code).

## Function signature

[`[source]`](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/elements/text.py#L31 "View st.text source code on GitHub")

```python
st.text(body, *, help=None, width="content")
```

## Parameters

### `body` (`str`)

The string to display.

### `help` (`str` or `None`)

A tooltip that gets displayed next to the text. If this is `None` (default), no tooltip is displayed.

The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of `st.markdown`.

### `width` (`"content"`, `"stretch"`, or `int`)

The width of the text element. This can be one of the following:

*   `"content"` (default): The width of the element matches the width of its content, but doesn't exceed the width of the parent container.
*   `"stretch"`: The width of the element matches the width of the parent container.
*   An integer specifying the width in pixels: The element has a fixed width. If the specified width is greater than the width of the parent container, the width of the element matches the width of the parent container.

## Example

```python
import streamlit as st

st.text("This is text\n[and more text](that's not a Markdown link).")
```
