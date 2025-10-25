# st.number_input

**URL:** https://docs.streamlit.io/develop/api-reference/widgets/st.number_input

This document provides details on the `st.number_input` widget in Streamlit, which allows users to input numerical values.

---

**Note:** This is the first part of the conversion. The subsequent parts will cover the rest of the content from the original HTML.

Display a numeric input widget.

> **Note**
> Integer values exceeding +/- (1<<53) - 1 cannot be accurately stored or returned by the widget due to serialization constraints between the Python server and JavaScript client. You must handle such numbers as floats, leading to a loss in precision.

### Function signature
[[source]](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/elements/widgets/number_input.py#L216 "View st.number_input source code on GitHub")

```python
st.number_input(label, min_value=None, max_value=None, value="min", step=None, format=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, placeholder=None, disabled=False, label_visibility="visible", icon=None, width="stretch")
```

### Parameters

*   **label** (str)
    A short label explaining to the user what this input is for. The label can optionally contain GitHub-flavored Markdown of the following types: Bold, Italics, Strikethroughs, Inline Code, Links, and Images. Images display like icons, with a max height equal to the font height.

    Unsupported Markdown elements are unwrapped so only their children (text contents) render. Display unsupported elements as literal characters by backslash-escaping them. E.g., "1\. Not an ordered list".

    See the body parameter of [st.markdown](https://docs.streamlit.io/develop/api-reference/text/st.markdown) for additional, supported Markdown directives.

    For accessibility reasons, you should never set an empty label, but you can hide it with `label_visibility` if needed. In the future, we may disallow empty labels by raising an exception.

*   **min_value** (int, float, or None)
    The minimum permitted value. If this is `None` (default), there will be no minimum for float values and a minimum of - (1<<53) + 1 for integer values.

*   **max_value** (int, float, or None)
    The maximum permitted value. If this is `None` (default), there will be no maximum for float values and a maximum of (1<<53) - 1 for integer values.

*   **value** (int, float, "min" or None)
    The value of this widget when it first renders. If this is `"min"` (default), the initial value is `min_value` unless `min_value` is `None`. If `min_value` is `None`, the widget initializes with a value of `0.0` or `0`.

    If `value` is `None`, the widget will initialize with no value and return `None` until the user provides input.

*   **step** (int, float, or None)
    The stepping interval. Defaults to `1` if the value is an `int`, `0.01` otherwise. If the value is not specified, the `format` parameter will be used.

*   **format** (str or None)
    A printf-style format string controlling how the interface should display numbers. The output must be purely numeric. This does not impact the return value of the widget. For more information about the formatting specification, see [sprintf.js](https://github.com/alexei/sprintf.js?tab=readme-ov-file#format-specification).

    For example, `format="%0.1f"` adjusts the displayed decimal precision to only show one digit after the decimal.

*   **key** (str or int)
    An optional string or integer to use as the unique key for the widget. If this is omitted, a key will be generated for the widget based on its content. No two widgets may have the same key.

*   **help** (str or None)
    A tooltip that gets displayed next to the widget label. Streamlit only displays the tooltip when `label_visibility="visible"`. If this is `None` (default), no tooltip is displayed.

    The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of `st.markdown`.

*   **on_change** (callable)
    An optional callback invoked when this `number_input`'s value changes.

*   **args** (list or tuple)
    An optional list or tuple of args to pass to the callback.

*   **kwargs** (dict)
    An optional dict of kwargs to pass to the callback.

*   **placeholder** (str or None)
    An optional string displayed when the number input is empty. If `None`, no placeholder is displayed.

*   **disabled** (bool)
    An optional boolean that disables the number input if set to `True`. The default is `False`.

*   **label_visibility** ("visible", "hidden", or "collapsed")
    The visibility of the label. The default is `"visible"`. If this is `"hidden"`, Streamlit displays an empty spacer instead of the label, which can help keep the widget aligned with other widgets. If this is `"collapsed"`, Streamlit displays no label or spacer.

*   **icon** (str, None)
    An optional emoji or icon to display within the input field to the left of the value. If `icon` is `None` (default), no icon is displayed. If `icon` is a string, the following options are valid:
    *   A single-character emoji. For example, you can set `icon="🚨"` or `icon="🔥"`. Emoji short codes are not supported.
    *   An icon from the Material Symbols library (rounded style) in the format `":material/icon_name:"` where `"icon_name"` is the name of the icon in snake case.
        For example, `icon=":material/thumb_up:"` will display the Thumb Up icon. Find additional icons in the [Material Symbols](https://fonts.google.com/icons?icon.set=Material+Symbols&icon.style=Rounded) font library.

*   **width** ("stretch" or int)
    The width of the number input widget. This can be one of the following:
    *   `"stretch"` (default): The width of the widget matches the width of the parent container.
    *   An integer specifying the width in pixels: The widget has a fixed width. If the specified width is greater than the width of the parent container, the width of the widget matches the width of the parent container.

### Returns

*   **(int or float or None)**
    The current value of the numeric input widget or `None` if the widget is empty. The return type will match the data type of the `value` parameter.

#### Example

```python
import streamlit as st

number = st.number_input("Insert a number")
st.write("The current number is ", number)
```

To initialize an empty number input, use `None` as the value:

```python
import streamlit as st

number = st.number_input(
    "Insert a number", value=None, placeholder="Type a number..."
)
st.write("The current number is ", number)
```

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.