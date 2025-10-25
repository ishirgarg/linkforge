```markdown
# st.color_picker

> **Source:** [https://docs.streamlit.io/develop/api-reference/widgets/st.color_picker](https://docs.streamlit.io/develop/api-reference/widgets/st.color_picker)

## Introduction
```


Display a color picker widget.

Function signature ([source](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/elements/widgets/color_picker.py#L66 "View st.color_picker source code on GitHub"))

```python
st.color_picker(label, value=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible", width="content")
```

Parameters

*   `label` (`str`)

    A short label explaining to the user what this input is for. The label can optionally contain GitHub-flavored Markdown of the following types: Bold, Italics, Strikethroughs, Inline Code, Links, and Images. Images display like icons, with a max height equal to the font height.

    Unsupported Markdown elements are unwrapped so only their children (text contents) render. Display unsupported elements as literal characters by backslash-escaping them. E.g., "1\\. Not an ordered list".

    See the body parameter of [st.markdown](https://docs.streamlit.io/develop/api-reference/text/st.markdown) for additional, supported Markdown directives.

    For accessibility reasons, you should never set an empty label, but you can hide it with `label_visibility` if needed. In the future, we may disallow empty labels by raising an exception.
*   `value` (`str`)

    The hex value of this widget when it first renders. If `None`, defaults to black.
*   `key` (`str` or `int`)

    An optional string or integer to use as the unique key for the widget. If this is omitted, a key will be generated for the widget based on its content. No two widgets may have the same key.
*   `help` (`str` or `None`)

    A tooltip that gets displayed next to the widget label. Streamlit only displays the tooltip when `label_visibility="visible"`. If this is `None` (default), no tooltip is displayed.

    The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of `st.markdown`.
*   `on_change` (`callable`)

    An optional callback invoked when this `color_picker`'s value changes.
*   `args` (`list` or `tuple`)

    An optional list or tuple of args to pass to the callback.
*   `kwargs` (`dict`)

    An optional dict of kwargs to pass to the callback.
*   `disabled` (`bool`)

    An optional boolean that disables the color picker if set to `True`. The default is `False`.
*   `label_visibility` (`"visible"`, `"hidden"`, or `"collapsed"`)

    The visibility of the label. The default is `"visible"`. If this is `"hidden"`, Streamlit displays an empty spacer instead of the label, which can help keep the widget aligned with other widgets. If this is `"collapsed"`, Streamlit displays no label or spacer.
*   `width` (`"content"`, `"stretch"`, or `int`)

    The width of the color picker widget. This can be one of the following:

    *   `"content"` (default): The width of the widget matches the width of its content, but doesn't exceed the width of the parent container.
    *   `"stretch"`: The width of the widget matches the width of the parent container.
    *   An integer specifying the width in pixels: The widget has a fixed width. If the specified width is greater than the width of the parent container, the width of the widget matches the width of the parent container.

Returns

(`str`)

The selected color as a hex string.

#### Example

```python
import streamlit as st

color = st.color_picker("Pick A Color", "#00f900")
st.write("The current color is", color)
```

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.
