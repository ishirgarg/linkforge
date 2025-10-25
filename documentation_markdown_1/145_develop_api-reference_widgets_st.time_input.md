# st.time_input

[Original URL](https://docs.streamlit.io/develop/api-reference/widgets/st.time_input)

`st.time_input` displays a time input widget.


### Parameters

*   **label** (str): A short label explaining to the user what this time input is for. The label can optionally contain GitHub-flavored Markdown of the following types: Bold, Italics, Strikethroughs, Inline Code, Links, and Images. Images display like icons, with a max height equal to the font height.

    Unsupported Markdown elements are unwrapped so only their children (text contents) render. Display unsupported elements as literal characters by backslash-escaping them. E.g., "1\. Not an ordered list".

    See the body parameter of [st.markdown](https://docs.streamlit.io/develop/api-reference/text/st.markdown) for additional, supported Markdown directives.

    For accessibility reasons, you should never set an empty label, but you can hide it with `label_visibility` if needed. In the future, we may disallow empty labels by raising an exception.

*   **value** ("now", `datetime.time`, `datetime.datetime`, str, or None): The value of this widget when it first renders. This can be one of the following:
    *   "now" (default): The widget initializes with the current time.
    *   A `datetime.time` or `datetime.datetime` object: The widget initializes with the given time, ignoring any date if included.
    *   An ISO-formatted time ("hh:mm", "hh:mm:ss", or "hh:mm:ss.sss") or datetime ("YYYY-MM-DD hh:mm:ss") string: The widget initializes with the given time, ignoring any date if included.
    *   None: The widget initializes with no time and returns `None` until the user selects a time.

*   **key** (str or int): An optional string or integer to use as the unique key for the widget. If this is omitted, a key will be generated for the widget based on its content. No two widgets may have the same key.

*   **help** (str or None): A tooltip that gets displayed next to the widget label. Streamlit only displays the tooltip when `label_visibility="visible"`. If this is `None` (default), no tooltip is displayed.

    The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of `st.markdown`.

*   **on_change** (callable): An optional callback invoked when this `time_input`'s value changes.

*   **args** (list or tuple): An optional list or tuple of args to pass to the callback.

*   **kwargs** (dict): An optional dict of kwargs to pass to the callback.

*   **disabled** (bool): An optional boolean that disables the time input if set to `True`. The default is `False`.

*   **label_visibility** ("visible", "hidden", or "collapsed"): The visibility of the label. The default is `"visible"`. If this is `"hidden"`, Streamlit displays an empty spacer instead of the label, which can help keep the widget aligned with other widgets. If this is `"collapsed"`, Streamlit displays no label or spacer.

*   **step** (int or `timedelta`): The stepping interval in seconds. Defaults to 900, i.e. 15 minutes. You can also pass a `datetime.timedelta` object.

*   **width** ("stretch" or int): The width of the time input widget. This can be one of the following:
    *   "stretch" (default): The width of the widget matches the width of the parent container.
    *   An integer specifying the width in pixels: The widget has a fixed width. If the specified width is greater than the width of the parent container, the width of the widget matches the width of the parent container.

### Returns

(`datetime.time` or None): The current value of the time input widget or `None` if no time has been selected.

### Example

```python
import datetime
import streamlit as st

t = st.time_input("Set an alarm for", datetime.time(8, 45))
st.write("Alarm is set for", t)
```

```python
import datetime
import streamlit as st

t = st.time_input("Set an alarm for", value=None)
st.write("Alarm is set for", t)
```

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.