```markdown
# st.popover - Streamlit

> Source: [https://docs.streamlit.io/develop/api-reference/layout/st.popover](https://docs.streamlit.io/develop/api-reference/layout/st.popover)

## st.popover

*(This is the beginning of the content. More content will be added in the following parts.)*
```


Insert a popover container.

Inserts a multi-element container as a popover. It consists of a button-like element and a container that opens when the button is clicked.

Opening and closing the popover will not trigger a rerun. Interacting with widgets inside of an open popover will rerun the app while keeping the popover open. Clicking outside of the popover will close it.

To add elements to the returned container, you can use the "with" notation (preferred) or just call methods directly on the returned object. See examples below.

**Note:** To follow best design practices, don't nest popovers.

## Function signature

```python
st.popover(label, *, help=None, icon=None, disabled=False, use_container_width=None, width="content")
```

## Parameters

### label (str)

The label of the button that opens the popover container. The label can optionally contain GitHub-flavored Markdown of the following types: Bold, Italics, Strikethroughs, Inline Code, Links, and Images. Images display like icons, with a max height equal to the font height.

Unsupported Markdown elements are unwrapped so only their children (text contents) render. Display unsupported elements as literal characters by backslash-escaping them. E.g., "1\\. Not an ordered list".

See the body parameter of [st.markdown](https://docs.streamlit.io/develop/api-reference/text/st.markdown) for additional, supported Markdown directives.

### help (str or None)

A tooltip that gets displayed when the popover button is hovered over. If this is None (default), no tooltip is displayed.

The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of st.markdown.

### icon (str)

An optional emoji or icon to display next to the button label. If icon is None (default), no icon is displayed. If icon is a string, the following options are valid:

*   A single-character emoji. For example, you can set `icon="🚨"` or `icon="🔥"`. Emoji short codes are not supported.

*   An icon from the Material Symbols library (rounded style) in the format `:material/icon_name:` where "icon_name" is the name of the icon in snake case.

    For example, `icon=":material/thumb_up:"` will display the Thumb Up icon. Find additional icons in the [Material Symbols](https://fonts.google.com/icons?icon.set=Material+Symbols&icon.style=Rounded) font library.

### disabled (bool)

An optional boolean that disables the popover button if set to True. The default is False.

### use\_container\_width (bool)

_delete_

`use_container_width` is deprecated and will be removed in a future release. For `use_container_width=True`, use `width="stretch"`. For `use_container_width=False`, use `width="content"`.

Whether to expand the button's width to fill its parent container. If `use_container_width` is False (default), Streamlit sizes the button to fit its content. If `use_container_width` is True, the width of the button matches its parent container.

In both cases, if the content of the button is wider than the parent container, the content will line wrap.

The popover container's minimum width matches the width of its button. The popover container may be wider than its button to fit the container's content.

### width (int, "stretch", or "content")

The width of the button. This can be one of the following:

*   `"content"` (default): The width of the button matches the width of its content, but doesn't exceed the width of the parent container.
*   `"stretch"`: The width of the button matches the width of the parent container.
*   An integer specifying the width in pixels: The button has a fixed width. If the specified width is greater than the width of the parent container, the width of the button matches the width of the parent container.

The popover container's minimum width matches the width of its button. The popover container may be wider than its button to fit the container's contents.

## Examples

You can use the `with` notation to insert any element into a popover:

```python
import streamlit as st

with st.popover("Open popover"):
    st.markdown("Hello World 👋")
    name = st.text_input("What's your name?")

st.write("Your name:", name)
```

Or you can just call methods directly on the returned objects:

```python
import streamlit as st

popover = st.popover("Filter items")
red = popover.checkbox("Show red items.", True)
blue = popover.checkbox("Show blue items.", True)

if red:
    st.write(":red[This is a red item.]")
if blue:
    st.write(":blue[This is a blue item.]")
```

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.
