# st.slider

[Original URL](https://docs.streamlit.io/develop/api-reference/widgets/st.slider)

`st.slider` is a Streamlit command that displays a slider widget in the app.



Display a slider widget.

This supports int, float, date, time, and datetime types.

This also allows you to render a range slider by passing a two-element tuple or list as the value.

The difference between `st.slider` and `st.select_slider` is that slider only accepts numerical or date/time data and takes a range as input, while select_slider accepts any datatype and takes an iterable set of options.

**Note:** Integer values exceeding +/- (1<<53) - 1 cannot be accurately stored or returned by the widget due to serialization constraints between the Python server and JavaScript client. You must handle such numbers as floats, leading to a loss in precision.

## Function signature

```python
st.slider(label, min_value=None, max_value=None, value=None, step=None, format=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible", width="stretch")
```

## Parameters

*   **label** (`str`)

    A short label explaining to the user what this slider is for. The label can optionally contain GitHub-flavored Markdown of the following types: Bold, Italics, Strikethroughs, Inline Code, Links, and Images. Images display like icons, with a max height equal to the font height.

    Unsupported Markdown elements are unwrapped so only their children (text contents) render. Display unsupported elements as literal characters by backslash-escaping them. E.g., "1\\. Not an ordered list".

    See the body parameter of [st.markdown](https://docs.streamlit.io/develop/api-reference/text/st.markdown) for additional, supported Markdown directives.

    For accessibility reasons, you should never set an empty label, but you can hide it with `label_visibility` if needed. In the future, we may disallow empty labels by raising an exception.
*   **min\_value** (`a supported type or None`)

    The minimum permitted value. If this is `None` (default), the minimum value depends on the type as follows:

    *   integer: 0
    *   float: 0.0
    *   date or datetime: `value` - `timedelta(days=14)`
    *   time: `time.min`
*   **max\_value** (`a supported type or None`)

    The maximum permitted value. If this is `None` (default), the maximum value depends on the type as follows:

    *   integer: 100
    *   float: 1.0
    *   date or datetime: `value` + `timedelta(days=14)`
    *   time: `time.max`
*   **value** (`a supported type or a tuple/list of supported types or None`)

    The value of the slider when it first renders. If a tuple/list of two values is passed here, then a range slider with those lower and upper bounds is rendered. For example, if set to `(1, 10)` the slider will have a selectable range between 1 and 10. This defaults to `min_value`. If the type is not otherwise specified in any of the numeric parameters, the widget will have an integer value.
*   **step** (`int`, `float`, `timedelta`, or `None`)

    The stepping interval. Defaults to 1 if the value is an int, 0.01 if a float, `timedelta(days=1)` if a date/datetime, `timedelta(minutes=15)` if a time (or if `max_value` - `min_value` < 1 day)
*   **format** (`str or None`)

    A printf-style format string controlling how the interface should display numbers. This does not impact the return value.

    For information about formatting integers and floats, see [sprintf.js](https://github.com/alexei/sprintf.js?tab=readme-ov-file#format-specification). For example, `format="%0.1f"` adjusts the displayed decimal precision to only show one digit after the decimal.

    For information about formatting datetimes, dates, and times, see [momentJS](https://momentjs.com/docs/#/displaying/format/). For example, `format="ddd ha"` adjusts the displayed datetime to show the day of the week and the hour ("Tue 8pm").
*   **key** (`str or int`)

    An optional string or integer to use as the unique key for the widget. If this is omitted, a key will be generated for the widget based on its content. No two widgets may have the same key.
*   **help** (`str or None`)

    A tooltip that gets displayed next to the widget label. Streamlit only displays the tooltip when `label_visibility="visible"`. If this is `None` (default), no tooltip is displayed.

    The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of `st.markdown`.
*   **on\_change** (`callable`)

    An optional callback invoked when this slider's value changes.
*   **args** (`list or tuple`)

    An optional list or tuple of args to pass to the callback.
*   **kwargs** (`dict`)

    An optional dict of kwargs to pass to the callback.
*   **disabled** (`bool`)

    An optional boolean that disables the slider if set to `True`. The default is `False`.
*   **label\_visibility** (`"visible"`, `"hidden"`, or `"collapsed"`)

    The visibility of the label. The default is `"visible"`. If this is `"hidden"`, Streamlit displays an empty spacer instead of the label, which can help keep the widget aligned with other widgets. If this is `"collapsed"`, Streamlit displays no label or spacer.
*   **width** (`"stretch"` or `int`)

    The width of the slider widget. This can be one of the following:

    *   `"stretch"` (default): The width of the widget matches the width of the parent container.
    *   An integer specifying the width in pixels: The widget has a fixed width. If the specified width is greater than the width of the parent container, the width of the widget matches the width of the parent container.

## Returns

(`int`/`float`/`date`/`time`/`datetime` or `tuple` of `int`/`float`/`date`/`time`/`datetime`)

The current value of the slider widget. The return type will match the data type of the `value` parameter.

## Examples

```python
import streamlit as st

age = st.slider("How old are you?", 0, 130, 25)
st.write("I'm ", age, "years old")
```

And here's an example of a range slider:

```python
import streamlit as st

values = st.slider("Select a range of values", 0.0, 100.0, (25.0, 75.0))
st.write("Values:", values)
```

This is a range time slider:

```python
import streamlit as st
from datetime import time

appointment = st.slider(
    "Schedule your appointment:", value=(time(11, 30), time(12, 45))
)
st.write("You're scheduled for:", appointment)
```

Finally, a datetime slider:

```python
import streamlit as st
from datetime import datetime

start_time = st.slider(
    "When do you start?",
    value=datetime(2020, 1, 1, 9, 30),
    format="MM/DD/YY - hh:mm",
)
st.write("Start time:", start_time)
```
