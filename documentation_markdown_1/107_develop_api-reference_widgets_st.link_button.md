```markdown
# st.link_button - Streamlit

> Source: [https://docs.streamlit.io/develop/api-reference/widgets/st.link_button](https://docs.streamlit.io/develop/api-reference/widgets/st.link_button)

## Introduction
```


Display a link button element.

When clicked, a new tab will be opened to the specified URL. This will create a new session for the user if directed within the app.

## Function signature

```python
st.link_button(label, url, *, help=None, type="secondary", icon=None, disabled=False, use_container_width=None, width="content")
```

## Parameters

### label (str)

A short label explaining to the user what this button is for. The label can optionally contain GitHub-flavored Markdown of the following types: Bold, Italics, Strikethroughs, Inline Code, Links, and Images. Images display like icons, with a max height equal to the font height.

Unsupported Markdown elements are unwrapped so only their children (text contents) render. Display unsupported elements as literal characters by backslash-escaping them. E.g., "1\\. Not an ordered list".

See the body parameter of [st.markdown](https://docs.streamlit.io/develop/api-reference/text/st.markdown) for additional, supported Markdown directives.

### url (str)

The url to be opened on user click

### help (str or None)

A tooltip that gets displayed when the button is hovered over. If this is None (default), no tooltip is displayed.

The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of st.markdown.

### type ("primary", "secondary", or "tertiary")

An optional string that specifies the button type. This can be one of the following:

*   "primary": The button's background is the app's primary color for additional emphasis.
*   "secondary" (default): The button's background coordinates with the app's background color for normal emphasis.
*   "tertiary": The button is plain text without a border or background for subtlety.

### icon (str or None)

An optional emoji or icon to display next to the button label. If icon is None (default), no icon is displayed. If icon is a string, the following options are valid:

*   A single-character emoji. For example, you can set `icon="🚨"` or `icon="🔥"`. Emoji short codes are not supported.

*   An icon from the Material Symbols library (rounded style) in the format `:material/icon_name:` where "icon_name" is the name of the icon in snake case.

    For example, `icon=":material/thumb_up:"` will display the Thumb Up icon. Find additional icons in the [Material Symbols](https://fonts.google.com/icons?icon.set=Material+Symbols&icon.style=Rounded) font library.

### disabled (bool)

An optional boolean that disables the link button if set to True. The default is False.

### use\_container\_width (bool)

_delete_

`use_container_width` is deprecated and will be removed in a future release. For `use_container_width=True`, use `width="stretch"`. For `use_container_width=False`, use `width="content"`.

Whether to expand the button's width to fill its parent container. If `use_container_width` is False (default), Streamlit sizes the button to fit its contents. If `use_container_width` is True, the width of the button matches its parent container.

In both cases, if the contents of the button are wider than the parent container, the contents will line wrap.

### width ("content", "stretch", or int)

The width of the link button. This can be one of the following:

*   "content" (default): The width of the button matches the width of its content, but doesn't exceed the width of the parent container.
*   "stretch": The width of the button matches the width of the parent container.
*   An integer specifying the width in pixels: The button has a fixed width. If the specified width is greater than the width of the parent container, the width of the button matches the width of the parent container.

## Example

```python
import streamlit as st

st.link_button("Go to gallery", "https://streamlit.io/gallery")
```

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.
