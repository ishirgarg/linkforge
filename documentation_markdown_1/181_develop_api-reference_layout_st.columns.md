# st.columns - Streamlit API Reference

[Original URL](https://docs.streamlit.io/develop/api-reference/layout/st.columns)

## st.columns

This section provides an overview of the `st.columns` function in the Streamlit API.


Inserts containers laid out as side-by-side columns.

Inserts a number of multi-element containers laid out side-by-side and returns a list of container objects.

To add elements to the returned containers, you can use the `with` notation (preferred) or just call methods directly on the returned object. See examples below.

**Note:** To follow best design practices and maintain a good appearance on all screen sizes, don't nest columns more than once.

### Function signature

```python
st.columns(spec, *, gap="small", vertical_alignment="top", border=False, width="stretch")
```

[Source](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/elements/layouts.py#L331)

### Parameters

*   `spec` (`int` or `Iterable` of numbers)

    Controls the number and width of columns to insert. Can be one of:

    *   An integer that specifies the number of columns. All columns have equal width in this case.
    *   An Iterable of numbers (`int` or `float`) that specify the relative width of each column. E.g. `[0.7, 0.3]` creates two columns where the first one takes up 70% of the available with and the second one takes up 30%. Or `[1, 2, 3]` creates three columns where the second one is two times the width of the first one, and the third one is three times that width.
*   `gap` (`"small"`, `"medium"`, `"large"`, or `None`)

    The size of the gap between the columns. This can be one of the following:

    *   `"small"` (default): 1rem gap between the columns.
    *   `"medium"`: 2rem gap between the columns.
    *   `"large"`: 4rem gap between the columns.
    *   `None`: No gap between the columns.

    The rem unit is relative to the `theme.baseFontSize` configuration option.
*   `vertical_alignment` (`"top"`, `"center"`, or `"bottom"`)

    The vertical alignment of the content inside the columns. The default is `"top"`.
*   `border` (`bool`)

    Whether to show a border around the column containers. If this is `False` (default), no border is shown. If this is `True`, a border is shown around each column.
*   `width` (`int` or `"stretch"`)

    The desired width of the columns expressed in pixels. If this is `"stretch"` (default), Streamlit sets the width of the columns to match the width of the parent container. Otherwise, this must be an integer. If the specified width is greater than the width of the parent container, Streamlit sets the width of the columns to match the width of the parent container.

### Returns

`(list of containers)`

A list of container objects.

### Examples

**Example 1: Use context management**

You can use the `with` statement to insert any element into a column:

```python
import streamlit as st

col1, col2, col3 = st.columns(3)

with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")
```

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen _open\_in\_new_](https://doc-columns1.streamlit.app//?utm_medium=oembed&)

**Example 2: Use commands as container methods**

You can just call methods directly on the returned objects:

```python
import streamlit as st
from numpy.random import default_rng as rng

df = rng(0).standard_normal((10, 1))
col1, col2 = st.columns([3, 1])

col1.subheader("A wide column with a chart")
col1.line_chart(df)

col2.subheader("A narrow column with the data")
col2.write(df)
```

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen _open\_in\_new_](https://doc-columns2.streamlit.app//?utm_medium=oembed&)

**Example 3: Align widgets**

Use `vertical_alignment="bottom"` to align widgets.

```python
import streamlit as st

left, middle, right = st.columns(3, vertical_alignment="bottom")

left.text_input("Write something")
middle.button("Click me", use_container_width=True)
right.checkbox("Check me")
```

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen _open\_in\_new_](https://doc-columns-bottom-widgets.streamlit.app//?utm_medium=oembed&)

**Example 4: Use vertical alignment to create grids**

Adjust vertical alignment to customize your grid layouts.

```python
import streamlit as st

vertical_alignment = st.selectbox(
    "Vertical alignment", ["top", "center", "bottom"], index=2
)

left, middle, right = st.columns(3, vertical_alignment=vertical_alignment)
left.image("https://static.streamlit.io/examples/cat.jpg")
middle.image("https://static.streamlit.io/examples/dog.jpg")
right.image("https://static.streamlit.io/examples/owl.jpg")
```

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen _open\_in\_new_](https://doc-columns-vertical-alignment.streamlit.app//?utm_medium=oembed&)

**Example 5: Add borders**

Add borders to your columns instead of nested containers for consistent heights.

```python
import streamlit as st

left, middle, right = st.columns(3, border=True)

left.markdown("Lorem ipsum " * 10)
middle.markdown("Lorem ipsum " * 5)
right.markdown("Lorem ipsum ")
```

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen _open\_in\_new_](https://doc-columns-borders.streamlit.app//?utm_medium=oembed&)

[Previous: Layouts and containers](/develop/api-reference/layout) | [Next: st.container](/develop/api-reference/layout/st.container)

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.
