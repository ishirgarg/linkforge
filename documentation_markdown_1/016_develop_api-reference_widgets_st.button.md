```markdown
# st.button - Streamlit

> Source: [https://docs.streamlit.io/develop/api-reference/widgets/st.button](https://docs.streamlit.io/develop/api-reference/widgets/st.button)

## st.button

```


Display a button widget.

### Function signature

```python
st.button(label, key=None, help=None, on_click=None, args=None, kwargs=None, *, type="secondary", icon=None, disabled=False, use_container_width=None, width="content")
```

### Parameters

*   **label** (`str`)
    A short label explaining to the user what this button is for. The label can optionally contain GitHub-flavored Markdown of the following types: Bold, Italics, Strikethroughs, Inline Code, Links, and Images. Images display like icons, with a max height equal to the font height.

    Unsupported Markdown elements are unwrapped so only their children (text contents) render. Display unsupported elements as literal characters by backslash-escaping them. E.g., "1\. Not an ordered list".

    See the body parameter of [st.markdown](https://docs.streamlit.io/develop/api-reference/text/st.markdown) for additional, supported Markdown directives.

*   **key** (`str` or `int`)
    An optional string or integer to use as the unique key for the widget. If this is omitted, a key will be generated for the widget based on its content. No two widgets may have the same key.

*   **help** (`str` or `None`)
    A tooltip that gets displayed when the button is hovered over. If this is `None` (default), no tooltip is displayed.

    The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of st.markdown.

*   **on_click** (`callable`)
    An optional callback invoked when this button is clicked.

*   **args** (`list` or `tuple`)
    An optional list or tuple of args to pass to the callback.

*   **kwargs** (`dict`)
    An optional dict of kwargs to pass to the callback.

*   **type** (`"primary"`, `"secondary"`, or `"tertiary"`)
    An optional string that specifies the button type. This can be one of the following:
    *   `"primary"`: The button's background is the app's primary color for additional emphasis.
    *   `"secondary"` (default): The button's background coordinates with the app's background color for normal emphasis.
    *   `"tertiary"`: The button is plain text without a border or background for subtlety.

*   **icon** (`str` or `None`)
    An optional emoji or icon to display next to the button label. If `icon` is `None` (default), no icon is displayed. If `icon` is a string, the following options are valid:
    *   A single-character emoji. For example, you can set `icon="🚨"` or `icon="🔥"`. Emoji short codes are not supported.
    *   An icon from the Material Symbols library (rounded style) in the format `":material/icon_name:"` where `"icon_name"` is the name of the icon in snake case.

        For example, `icon=":material/thumb_up:"` will display the Thumb Up icon. Find additional icons in the [Material Symbols](https://fonts.google.com/icons?icon.set=Material+Symbols&icon.style=Rounded) font library.

*   **disabled** (`bool`)
    An optional boolean that disables the button if set to `True`. The default is `False`.

*   **use_container_width** (`bool`)
    _deprecated_

    `use_container_width` is deprecated and will be removed in a future release. For `use_container_width=True`, use `width="stretch"`. For `use_container_width=False`, use `width="content"`.

    Whether to expand the button's width to fill its parent container. If `use_container_width` is `False` (default), Streamlit sizes the button to fit its contents. If `use_container_width` is `True`, the width of the button matches its parent container.

    In both cases, if the contents of the button are wider than the parent container, the contents will line wrap.

*   **width** (`"content"`, `"stretch"`, or `int`)
    The width of the button. This can be one of the following:
    *   `"content"` (default): The width of the button matches the width of its content, but doesn't exceed the width of the parent container.
    *   `"stretch"`: The width of the button matches the width of the parent container.
    *   An integer specifying the width in pixels: The button has a fixed width. If the specified width is greater than the width of the parent container, the width of the button matches the width of the parent container.

### Returns

*   **bool**
    `True` if the button was clicked on the last run of the app, `False` otherwise.

### Examples

**Example 1: Customize your button type**

```python
import streamlit as st

st.button("Reset", type="primary")
if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")

if st.button("Aloha", type="tertiary"):
    st.write("Ciao")
```

**Example 2: Add icons to your button**

Although you can add icons to your buttons through Markdown, the `icon` parameter is a convenient and consistent alternative.

```python
import streamlit as st

left, middle, right = st.columns(3)
if left.button("Plain button", width="stretch"):
    left.markdown("You clicked the plain button.")
if middle.button("Emoji button", icon="😃", width="stretch"):
    middle.markdown("You clicked the emoji button.")
if right.button("Material button", icon=":material/mood:", width="stretch"):
    right.markdown("You clicked the Material button.")
```

### Advanced functionality

Although a button is the simplest of input widgets, it's very common for buttons to be deeply tied to the use of [`st.session_state`](/develop/api-reference/caching-and-state/st.session_state). Check out our advanced guide on [Button behavior and examples](/develop/concepts/design/buttons).

### Featured videos

Check out our video on how to use one of Streamlit's core functions, the button!

In the video below, we'll take it a step further and learn how to combine a [button](/develop/api-reference/widgets/st.button), [checkbox](/develop/api-reference/widgets/st.checkbox) and [radio button](/develop/api-reference/widgets/st.radio)!

[Previous: Input widgets](/develop/api-reference/widgets) [Next: st.download_button](/develop/api-reference/widgets/st.download_button)

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.