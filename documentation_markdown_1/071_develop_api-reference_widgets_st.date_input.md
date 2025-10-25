```markdown
# st.date_input

## st.date_input

---
**Reference:** [https://docs.streamlit.io/develop/api-reference/widgets/st.date_input](https://docs.streamlit.io/develop/api-reference/widgets/st.date_input)
```

Display a date input widget.

The date input widget can be configured to accept a single date or a date range. The first day of the week is determined from the user's locale in their browser.

Function signature[\[source\]](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/elements/widgets/time_widgets.py#L655 "View st.date_input source code on GitHub")

```python
st.date_input(label, value="today", min_value=None, max_value=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, format="YYYY/MM/DD", disabled=False, label_visibility="visible", width="stretch")
```

Parameters

*   `label` (`str`)

    A short label explaining to the user what this date input is for. The label can optionally contain GitHub-flavored Markdown of the following types: Bold, Italics, Strikethroughs, Inline Code, Links, and Images. Images display like icons, with a max height equal to the font height.

    Unsupported Markdown elements are unwrapped so only their children (text contents) render. Display unsupported elements as literal characters by backslash-escaping them. E.g., "1\\. Not an ordered list".

    See the body parameter of [st.markdown](https://docs.streamlit.io/develop/api-reference/text/st.markdown) for additional, supported Markdown directives.

    For accessibility reasons, you should never set an empty label, but you can hide it with `label_visibility` if needed. In the future, we may disallow empty labels by raising an exception.
*   `value` ("today", `datetime.date`, `datetime.datetime`, `str`, `list`/`tuple` of these, or `None`)

    The value of this widget when it first renders. This can be one of the following:

    *   "today" (default): The widget initializes with the current date.
    *   A `datetime.date` or `datetime.datetime` object: The widget initializes with the given date, ignoring any time if included.
    *   An ISO-formatted date ("YYYY-MM-DD") or datetime ("YYYY-MM-DD hh:mm:ss") string: The widget initializes with the given date, ignoring any time if included.
    *   A list or tuple with up to two of the above: The widget will initialize with the given date interval and return a tuple of the selected interval. You can pass an empty list to initialize the widget with an empty interval or a list with one value to initialize only the beginning date of the iterval.
    *   `None`: The widget initializes with no date and returns `None` until the user selects a date.
*   `min_value` ("today", `datetime.date`, `datetime.datetime`, `str`, or `None`)

    The minimum selectable date. This can be any of the date types accepted by `value`, except `list` or `tuple`.

    If this is `None` (default), the minimum selectable date is ten years before the initial value. If the initial value is an interval, the minimum selectable date is ten years before the start date of the interval. If no initial value is set, the minimum selectable date is ten years before today.
*   `max_value` ("today", `datetime.date`, `datetime.datetime`, `str`, or `None`)

    The maximum selectable date. This can be any of the date types accepted by `value`, except `list` or `tuple`.

    If this is `None` (default), the maximum selectable date is ten years after the initial value. If the initial value is an interval, the maximum selectable date is ten years after the end date of the interval. If no initial value is set, the maximum selectable date is ten years after today.
*   `key` (`str` or `int`)

    An optional string or integer to use as the unique key for the widget. If this is omitted, a key will be generated for the widget based on its content. No two widgets may have the same key.
*   `help` (`str` or `None`)

    A tooltip that gets displayed next to the widget label. Streamlit only displays the tooltip when `label_visibility="visible"`. If this is `None` (default), no tooltip is displayed.

    The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of `st.markdown`.
*   `on_change` (`callable`)

    An optional callback invoked when this `date_input`'s value changes.
*   `args` (`list` or `tuple`)

    An optional list or tuple of args to pass to the callback.
*   `kwargs` (`dict`)

    An optional dict of kwargs to pass to the callback.
*   `format` (`str`)

    A format string controlling how the interface should display dates. Supports "YYYY/MM/DD" (default), "DD/MM/YYYY", or "MM/DD/YYYY". You may also use a period (.) or hyphen (-) as separators.
*   `disabled` (`bool`)

    An optional boolean that disables the date input if set to `True`. The default is `False`.
*   `label_visibility` ("visible", "hidden", or "collapsed")

    The visibility of the label. The default is "visible". If this is "hidden", Streamlit displays an empty spacer instead of the label, which can help keep the widget aligned with other widgets. If this is "collapsed", Streamlit displays no label or spacer.
*   `width` ("stretch" or int)

    The width of the date input widget. This can be one of the following:

    *   "stretch" (default): The width of the widget matches the width of the parent container.
    *   An integer specifying the width in pixels: The widget has a fixed width. If the specified width is greater than the width of the parent container, the width of the widget matches the width of the parent container.

Returns

(`datetime.date` or a tuple with 0-2 dates or `None`)

The current value of the date input widget or `None` if no date has been selected.

#### Examples

```python
import datetime
import streamlit as st

d = st.date_input("When's your birthday", datetime.date(2019, 7, 6))
st.write("Your birthday is:", d)
```

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen _open\_in\_new_](https://doc-date-input.streamlit.app//?utm_medium=oembed&)

```python
import datetime
import streamlit as st

today = datetime.datetime.now()
next_year = today.year + 1
jan_1 = datetime.date(next_year, 1, 1)
dec_31 = datetime.date(next_year, 12, 31)

d = st.date_input(
    "Select your vacation for next year",
    (jan_1, datetime.date(next_year, 1, 7)),
    jan_1,
    dec_31,
    format="MM.DD.YYYY",
)
d
```

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen _open\_in\_new_](https://doc-date-input1.streamlit.app//?utm_medium=oembed&)

To initialize an empty date input, use `None` as the value:

```python
import datetime
import streamlit as st

d = st.date_input("When's your birthday", value=None)
st.write("Your birthday is:", d)
```

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen _open\_in\_new_](https://doc-date-input-empty.streamlit.app//?utm_medium=oembed&)

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.
