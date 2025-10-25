# st.spinner

[Original URL](https://docs.streamlit.io/develop/api-reference/status/st.spinner)

Display a loading spinner while executing a block of code.

## Function signature

[`[source]`](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/elements/spinner.py#L37 "View st.spinner source code on GitHub")

`st.spinner(text="In progress...", *, show_time=False, width="content")`

## Parameters

### `text` (str)

The text to display next to the spinner. This defaults to "In progress...".

The text can optionally contain GitHub-flavored Markdown. Syntax information can be found at: [https://github.github.com/gfm](https://github.github.com/gfm).

See the body parameter of [`st.markdown`](https://docs.streamlit.io/develop/api-reference/text/st.markdown) for additional, supported Markdown directives.

### `show_time` (bool)

Whether to show the elapsed time next to the spinner text. If this is `False` (default), no time is displayed. If this is `True`, elapsed time is displayed with a precision of 0.1 seconds. The time format is not configurable.

### `width` ("content", "stretch", or int)

The width of the spinner element. This can be one of the following:

*   `"content"` (default): The width of the element matches the width of its content, but doesn't exceed the width of the parent container.
*   `"stretch"`: The width of the element matches the width of the parent container.
*   An integer specifying the width in pixels: The element has a fixed width. If the specified width is greater than the width of the parent container, the width of the element matches the width of the parent container.

## Example

```python
import streamlit as st
import time

with st.spinner("Wait for it...", show_time=True):
    time.sleep(5)
st.success("Done!")
st.button("Rerun")
```


Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.
