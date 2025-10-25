```markdown
# st.pills - Streamlit

> **Source:** [https://docs.streamlit.io/develop/api-reference/widgets/st.pills](https://docs.streamlit.io/develop/api-reference/widgets/st.pills)

## Introduction

This document provides an overview of the `st.pills` widget in Streamlit.
```


Display a pills widget.

A pills widget is similar to a `st.selectbox` or `st.multiselect` where the options are displayed as pill-buttons instead of a drop-down list.

## Function signature

[`[source]`](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/elements/widgets/button_group.py#L471 "View st.pills source code on GitHub")

```python
st.pills(label, options, *, selection_mode="single", default=None, format_func=None, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible", width="content")
```

## Parameters

### label (`str`)

A short label explaining to the user what this widget is for. The label can optionally contain GitHub-flavored Markdown of the following types: Bold, Italics, Strikethroughs, Inline Code, Links, and Images. Images display like icons, with a max height equal to the font height.

Unsupported Markdown elements are unwrapped so only their children (text contents) render. Display unsupported elements as literal characters by backslash-escaping them. E.g., "1\\. Not an ordered list".

See the body parameter of [`st.markdown`](https://docs.streamlit.io/develop/api-reference/text/st.markdown) for additional, supported Markdown directives.

For accessibility reasons, you should never set an empty label, but you can hide it with `label_visibility` if needed. In the future, we may disallow empty labels by raising an exception.

### options (`Iterable of V`)

Labels for the select options in an Iterable. This can be a list, set, or anything supported by `st.dataframe`. If options is dataframe-like, the first column will be used. Each label will be cast to `str` internally by default and can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of `st.markdown`.

### selection_mode (`"single"` or `"multi"`)

The selection mode for the widget. If this is `"single"` (default), only one option can be selected. If this is `"multi"`, multiple options can be selected.

### default (`Iterable of V`, `V`, or `None`)

The value of the widget when it first renders. If the `selection_mode` is `multi`, this can be a list of values, a single value, or `None`. If the `selection_mode` is `"single"`, this can be a single value or `None`.

### format_func (`function`)

Function to modify the display of the options. It receives the raw option as an argument and should output the label to be shown for that option. This has no impact on the return value of the command. The output can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of `st.markdown`.

### key (`str` or `int`)

An optional string or integer to use as the unique key for the widget. If this is omitted, a key will be generated for the widget based on its content. Multiple widgets of the same type may not share the same key.

### help (`str` or `None`)

A tooltip that gets displayed next to the widget label. Streamlit only displays the tooltip when `label_visibility="visible"`. If this is `None` (default), no tooltip is displayed.

The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of `st.markdown`.

### on_change (`callable`)

An optional callback invoked when this widget's value changes.

### args (`list` or `tuple`)

An optional list or tuple of args to pass to the callback.

### kwargs (`dict`)

An optional dict of kwargs to pass to the callback.

### disabled (`bool`)

An optional boolean that disables the widget if set to `True`. The default is `False`.

### label_visibility (`"visible"`, `"hidden"`, or `"collapsed"`)

The visibility of the label. The default is `"visible"`. If this is `"hidden"`, Streamlit displays an empty spacer instead of the label, which can help keep the widget aligned with other widgets. If this is `"collapsed"`, Streamlit displays no label or spacer.

### width (`"content"`, `"stretch"`, or `int`)

The width of the pills widget. This can be one of the following:

*   `"content"` (default): The width of the widget matches the width of its content, but doesn't exceed the width of the parent container.
*   `"stretch"`: The width of the widget matches the width of the parent container.
*   An integer specifying the width in pixels: The widget has a fixed width. If the specified width is greater than the width of the parent container, the width of the widget matches the width of the parent container.

## Returns

(`list of V`, `V`, or `None`)

If the `selection_mode` is `multi`, this is a list of selected options or an empty list. If the `selection_mode` is `"single"`, this is a selected option or `None`.

## Examples

**Example 1: Multi-select pills**

Display a multi-select pills widget, and show the selection:

```python
import streamlit as st

options = ["North", "East", "South", "West"]
selection = st.pills("Directions", options, selection_mode="multi")
st.markdown(f"Your selected options: {selection}.")
```

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen _open\_in\_new_](https://doc-pills-multi.streamlit.app//?utm_medium=oembed&)

**Example 2: Single-select pills with icons**

Display a single-select pills widget with icons:

```python
import streamlit as st

option_map = {
    0: ":material/add:",
    1: ":material/zoom_in:",
    2: ":material/zoom_out:",
    3: ":material/zoom_out_map:",
}
selection = st.pills(
    "Tool",
    options=option_map.keys(),
    format_func=lambda option: option_map[option],
    selection_mode="single",
)
st.write(
    "Your selected option: "
    f"{None if selection is None else option_map[selection]}"
)
```

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen _open\_in\_new_](https://doc-pills-single.streamlit.app//?utm_medium=oembed&)

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.
