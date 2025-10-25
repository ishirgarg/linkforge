# Streamlit `st.checkbox` API Reference

**URL:** https://docs.streamlit.io/develop/api-reference/widgets/st.checkbox

## st.checkbox

Display a checkbox widget.

**Function signature**

```python
st.checkbox(label, value=False, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible", width="content")
```

**Parameters**

*   `label` (`str`)

    A short label explaining to the user what this checkbox is for. The label can optionally contain GitHub-flavored Markdown of the following types: Bold, Italics, Strikethroughs, Inline Code, Links, and Images. Images display like icons, with a max height equal to the font height.

    Unsupported Markdown elements are unwrapped so only their children (text contents) render. Display unsupported elements as literal characters by backslash-escaping them. E.g., "1\\. Not an ordered list".

    See the body parameter of [st.markdown](https://docs.streamlit.io/develop/api-reference/text/st.markdown) for additional, supported Markdown directives.

    For accessibility reasons, you should never set an empty label, but you can hide it with `label_visibility` if needed. In the future, we may disallow empty labels by raising an exception.

*   `value` (`bool`)

    Preselect the checkbox when it first renders. This will be cast to `bool` internally.

*   `key` (`str` or `int`)

    An optional string or integer to use as the unique key for the widget. If this is omitted, a key will be generated for the widget based on its content. No two widgets may have the same key.

*   `help` (`str` or `None`)

    A tooltip that gets displayed next to the widget label. Streamlit only displays the tooltip when `label_visibility="visible"`. If this is `None` (default), no tooltip is displayed.

    The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of `st.markdown`.

*   `on_change` (`callable`)

    An optional callback invoked when this checkbox's value changes.

*   `args` (`list` or `tuple`)

    An optional list or tuple of args to pass to the callback.

*   `kwargs` (`dict`)

    An optional dict of kwargs to pass to the callback.

*   `disabled` (`bool`)

    An optional boolean that disables the checkbox if set to `True`. The default is `False`.

*   `label_visibility` (`"visible"`, `"hidden"`, or `"collapsed"`)

    The visibility of the label. The default is `"visible"`. If this is `"hidden"`, Streamlit displays an empty spacer instead of the label, which can help keep the widget aligned with other widgets. If this is `"collapsed"`, Streamlit displays no label or spacer.

*   `width` (`"content"`, `"stretch"`, or `int`)

    The width of the checkbox widget. This can be one of the following:

    *   `"content"` (default): The width of the widget matches the width of its content, but doesn't exceed the width of the parent container.
    *   `"stretch"`: The width of the widget matches the width of the parent container.
    *   An integer specifying the width in pixels: The widget has a fixed width. If the specified width is greater than the width of the parent container, the width of the widget matches the width of the parent container.

**Returns**

(`bool`)

Whether or not the checkbox is checked.

#### Example

```python
import streamlit as st

agree = st.checkbox("I agree")

if agree:
    st.write("Great!")
```
