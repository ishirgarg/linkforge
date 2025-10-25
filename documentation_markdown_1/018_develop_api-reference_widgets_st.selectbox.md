# st.selectbox

**Source URL:** [https://docs.streamlit.io/develop/api-reference/widgets/st.selectbox](https://docs.streamlit.io/develop/api-reference/widgets/st.selectbox)

This section provides documentation for the `st.selectbox` widget in Streamlit.


Display a select widget.

## Function signature [[source]](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/elements/widgets/selectbox.py#L270 "View st.selectbox source code on GitHub")

```python
st.selectbox(label, options, index=0, format_func=special_internal_function, key=None, help=None, on_change=None, args=None, kwargs=None, *, placeholder=None, disabled=False, label_visibility="visible", accept_new_options=False, width="stretch")
```

## Parameters

**label** (str)
A short label explaining to the user what this select widget is for. The label can optionally contain GitHub-flavored Markdown of the following types: Bold, Italics, Strikethroughs, Inline Code, Links, and Images. Images display like icons, with a max height equal to the font height.

Unsupported Markdown elements are unwrapped so only their children (text contents) render. Display unsupported elements as literal characters by backslash-escaping them. E.g., "1\. Not an ordered list".

See the body parameter of [st.markdown](https://docs.streamlit.io/develop/api-reference/text/st.markdown) for additional, supported Markdown directives.

For accessibility reasons, you should never set an empty label, but you can hide it with `label_visibility` if needed. In the future, we may disallow empty labels by raising an exception.

**options** (Iterable)
Labels for the select options in an Iterable. This can be a list, set, or anything supported by `st.dataframe`. If `options` is dataframe-like, the first column will be used. Each label will be cast to `str` internally by default.

**index** (int or None)
The index of the preselected option on first render. If `None`, will initialize empty and return `None` until the user selects an option. Defaults to 0 (the first option).

**format_func** (function)
Function to modify the display of the options. It receives the raw option as an argument and should output the label to be shown for that option. This has no impact on the return value of the command.

**key** (str or int)
An optional string or integer to use as the unique key for the widget. If this is omitted, a key will be generated for the widget based on its content. No two widgets may have the same key.

**help** (str or None)
A tooltip that gets displayed next to the widget label. Streamlit only displays the tooltip when `label_visibility="visible"`. If this is `None` (default), no tooltip is displayed.

The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of `st.markdown`.

**on_change** (callable)
An optional callback invoked when this selectbox's value changes.

**args** (list or tuple)
An optional list or tuple of args to pass to the callback.

**kwargs** (dict)
An optional dict of kwargs to pass to the callback.

**placeholder** (str or None)
A string to display when no options are selected. If this is `None` (default), the widget displays placeholder text based on the widget's configuration:

*   "Choose an option" is displayed when options are available and `accept_new_options=False`.
*   "Choose or add an option" is displayed when options are available and `accept_new_options=True`.
*   "Add an option" is displayed when no options are available and `accept_new_options=True`.
*   "No options to select" is displayed when no options are available and `accept_new_options=False`. The widget is also disabled in this case.

**disabled** (bool)
An optional boolean that disables the selectbox if set to `True`. The default is `False`.

**label_visibility** ("visible", "hidden", or "collapsed")
The visibility of the label. The default is "visible". If this is "hidden", Streamlit displays an empty spacer instead of the label, which can help keep the widget aligned with other widgets. If this is "collapsed", Streamlit displays no label or spacer.

**accept_new_options** (bool)
Whether the user can add a selection that isn't included in `options`. If this is `False` (default), the user can only select from the items in `options`. If this is `True`, the user can enter a new item that doesn't exist in `options`.

When a user enters a new item, it is returned by the widget as a string. The new item is not added to the widget's drop-down menu. Streamlit will use a case-insensitive match from `options` before adding a new item.

**width** ("stretch" or int)
The width of the selectbox widget. This can be one of the following:

*   "stretch" (default): The width of the widget matches the width of the parent container.
*   An integer specifying the width in pixels: The widget has a fixed width. If the specified width is greater than the width of the parent container, the width of the widget matches the width of the parent container.

## Returns

(any)
The selected option or `None` if no option is selected.

## Examples

### Example 1: Use a basic selectbox widget

If no index is provided, the first option is selected by default.

```python
import streamlit as st

option = st.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone"),
)

st.write("You selected:", option)
```

### Example 2: Use a selectbox widget with no initial selection

To initialize an empty selectbox, use `None` as the index value.

```python
import streamlit as st

option = st.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone"),
    index=None,
    placeholder="Select contact method...",
)

st.write("You selected:", option)
```

### Example 3: Let users add a new option

To allow users to add a new option that isn't included in the options list, use the `accept_new_options=True` parameter. You can also customize the placeholder text.

```python
import streamlit as st

option = st.selectbox(
    "Default email",
    ["foo@example.com", "bar@example.com", "baz@example.com"],
    index=None,
    placeholder="Select a saved email or enter a new one",
    accept_new_options=True,
)

st.write("You selected:", option)
```

Select widgets can customize how to hide their labels with the `label_visibility` parameter. If "hidden", the label doesn’t show but there is still empty space for it above the widget (equivalent to `label=""`). If "collapsed", both the label and the space are removed. Default is "visible". Select widgets can also be disabled with the `disabled` parameter:

```python
import streamlit as st

# Store the initial value of widgets in session state
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

col1, col2 = st.columns(2)

with col1:
    st.checkbox("Disable selectbox widget", key="disabled")
    st.radio(
        "Set selectbox label visibility 👉",
        key="visibility",
        options=["visible", "hidden", "collapsed"],
    )

with col2:
    option = st.selectbox(
        "How would you like to be contacted?",
        ("Email", "Home phone", "Mobile phone"),
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
    )
```

## Example

Here's how to use `st.selectbox`:

```python
import streamlit as st

genre = st.selectbox(
    "What's your favorite movie genre?",
    ("Comedy", "Drama", "Documentary"),
    index=1,
)

st.write("You selected:", genre)
```

And here's another example using a list of dictionaries:

```python
import streamlit as st

movie_genres = {
    "Comedy": "laugh",
    "Drama": "tears",
    "Documentary": "learn",
}

genre = st.selectbox(
    "What's your favorite movie genre?",
    movie_genres.keys(),
    format_func=lambda x: f"{x} ({movie_genres[x]})",
)

st.write("You selected:", genre)
```

## Notes

*   The order of elements in `options` is preserved in the `st.selectbox` widget.
*   If `options` is a list of dictionaries, you can use `format_func` to customize how each option is displayed.

---

[_arrow\_back_Previous: st.segmented\_control](/develop/api-reference/widgets/st.segmented_control)[_arrow\_forward_Next: st.select\_slider](/develop/api-reference/widgets/st.select_slider)

_forum_


### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

[GitHub](https://github.com/streamlit)
[YouTube](https://www.youtube.com/channel/UC3LD42rjj-Owtxsa6PwGU5Q)
[Twitter](https://twitter.com/streamlit)
[LinkedIn](https://www.linkedin.com/company/streamlit)
[Newsletter](https://info.snowflake.com/streamlit-newsletter-sign-up.html)

© 2025 Snowflake Inc. Cookie policy
