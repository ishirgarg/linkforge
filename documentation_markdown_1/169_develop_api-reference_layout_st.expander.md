# st.expander

**URL:** https://docs.streamlit.io/develop/api-reference/layout/st.expander

This document describes the `st.expander` function in Streamlit, which allows you to create collapsible sections in your application.

---

## st.expander

The `st.expander` function creates a collapsible container that can be used to hide or reveal content. This is useful for organizing your app and preventing it from becoming too cluttered.

**Syntax:**

```python
st.expander(label, expanded=False, icon=None)
```

**Parameters:**

*   **`label`** (str): The text that will be displayed as the header of the expander.
*   **`expanded`** (bool, optional): If `True`, the expander will be open by default. Defaults to `False`.
*   **`icon`** (str, optional): An emoji to display next to the label.

**Returns:**

*   An `st.delta_generator.DeltaGenerator` object, which can be used to add content within the expander.

**Example:**

```python
import streamlit as st

with st.expander("Click to see more information"):
    st.write("This is the content that will be revealed when the expander is opened.")
    st.image("https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png")
```

Insert a multi-element container that can be expanded/collapsed.

Inserts a container into your app that can be used to hold multiple elements and can be expanded or collapsed by the user. When collapsed, all that is visible is the provided label.

To add elements to the returned container, you can use the `with` notation (preferred) or just call methods directly on the returned object. See examples below.

**Note:** All content within the expander is computed and sent to the frontend, even if the expander is closed.

To follow best design practices and maintain a good appearance on all screen sizes, don't nest expanders.

### Function signature

```python
st.expander(label, expanded=False, *, icon=None, width="stretch")
```

### Parameters

*   `label` (`str`)

    A string to use as the header for the expander. The label can optionally contain GitHub-flavored Markdown of the following types: Bold, Italics, Strikethroughs, Inline Code, Links, and Images. Images display like icons, with a max height equal to the font height.

    Unsupported Markdown elements are unwrapped so only their children (text contents) render. Display unsupported elements as literal characters by backslash-escaping them. E.g., "1\\. Not an ordered list".

    See the body parameter of [`st.markdown`](https://docs.streamlit.io/develop/api-reference/text/st.markdown) for additional, supported Markdown directives.
*   `expanded` (`bool`)

    If `True`, initializes the expander in "expanded" state. Defaults to `False` (collapsed).
*   `icon` (`str, None`)

    An optional emoji or icon to display next to the expander label. If `icon` is `None` (default), no icon is displayed. If `icon` is a string, the following options are valid:

    *   A single-character emoji. For example, you can set `icon="🚨"` or `icon="🔥"`. Emoji short codes are not supported.
    *   An icon from the Material Symbols library (rounded style) in the format `":material/icon_name:"` where `"icon_name"` is the name of the icon in snake case.

        For example, `icon=":material/thumb_up:"` will display the Thumb Up icon. Find additional icons in the [Material Symbols](https://fonts.google.com/icons?icon.set=Material+Symbols&icon.style=Rounded) font library.
*   `width` (`"stretch"` or `int`)

    The width of the expander container. This can be one of the following:

    *   `"stretch"` (default): The width of the container matches the width of the parent container.
    *   An integer specifying the width in pixels: The container has a fixed width. If the specified width is greater than the width of the parent container, the width of the container matches the width of the parent container.

### Examples

You can use the `with` notation to insert any element into an expander

```python
import streamlit as st

st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})

with st.expander("See explanation"):
    st.write('''
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
    ''')
    st.image("https://static.streamlit.io/examples/dice.jpg")
```

Or you can just call methods directly on the returned objects:

```python
import streamlit as st

st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})

expander = st.expander("See explanation")
expander.write('''
    The chart above shows some numbers I picked for you.
    I rolled actual dice for these, so they're *guaranteed* to
    be random.
''')
expander.image("https://static.streamlit.io/examples/dice.jpg")
```

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.
