```markdown
# st.text_input - Streamlit

> Source: [https://docs.streamlit.io/develop/api-reference/widgets/st.text_input](https://docs.streamlit.io/develop/api-reference/widgets/st.text_input)

## st.text_input

Display a single-line text input widget.

```
st.text_input(label, value="", max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, args=None, kwargs=None, *, placeholder=None, disabled=False, label_visibility="visible", icon=None, width="stretch")
```

**Parameters**

*   **label** (str)
```


### Parameters

A short label explaining to the user what this input is for. The label can optionally contain GitHub-flavored Markdown of the following types: Bold, Italics, Strikethroughs, Inline Code, Links, and Images. Images display like icons, with a max height equal to the font height.

Unsupported Markdown elements are unwrapped so only their children (text contents) render. Display unsupported elements as literal characters by backslash-escaping them. E.g., "1\\. Not an ordered list".

See the body parameter of [st.markdown](https://docs.streamlit.io/develop/api-reference/text/st.markdown) for additional, supported Markdown directives.

For accessibility reasons, you should never set an empty label, but you can hide it with `label_visibility` if needed. In the future, we may disallow empty labels by raising an exception.

*   **`value`** (`object` or `None`): The text value of this widget when it first renders. This will be cast to `str` internally. If `None`, will initialize empty and return `None` until the user provides input. Defaults to empty string.
*   **`max_chars`** (`int` or `None`): Max number of characters allowed in text input.
*   **`key`** (`str` or `int`): An optional string or integer to use as the unique key for the widget. If this is omitted, a key will be generated for the widget based on its content. No two widgets may have the same key.
*   **`type`** (`"default"` or `"password"`): The type of the text input. This can be either `"default"` (for a regular text input), or `"password"` (for a text input that masks the user's typed value). Defaults to `"default"`.
*   **`help`** (`str` or `None`): A tooltip that gets displayed next to the widget label. Streamlit only displays the tooltip when `label_visibility="visible"`. If this is `None` (default), no tooltip is displayed.

    The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of `st.markdown`.
*   **`autocomplete`** (`str`): An optional value that will be passed to the `<input>` element's `autocomplete` property. If unspecified, this value will be set to `"new-password"` for `"password"` inputs, and the empty string for `"default"` inputs. For more details, see [https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/autocomplete](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/autocomplete)
*   **`on_change`** (`callable`): An optional callback invoked when this text input's value changes.
*   **`args`** (`list` or `tuple`): An optional list or tuple of args to pass to the callback.
*   **`kwargs`** (`dict`): An optional dict of kwargs to pass to the callback.
*   **`placeholder`** (`str` or `None`): An optional string displayed when the text input is empty. If `None`, no text is displayed.
*   **`disabled`** (`bool`): An optional boolean that disables the text input if set to `True`. The default is `False`.
*   **`label_visibility`** (`"visible"`, `"hidden"`, or `"collapsed"`): The visibility of the label. The default is `"visible"`. If this is `"hidden"`, Streamlit displays an empty spacer instead of the label, which can help keep the widget aligned with other widgets.
*   **`icon`** (`str`, `None`): An optional emoji or icon to display within the input field to the left of the value. If `icon` is `None` (default), no icon is displayed. If `icon` is a string, the following options are valid:
    *   A single-character emoji. For example, you can set `icon="🚨"` or `icon="🔥"`. Emoji short codes are not supported.
    *   An icon from the Material Symbols library (rounded style) in the format `":material/icon_name:"` where `"icon_name"` is the name of the icon in snake case.

        For example, `icon=":material/thumb_up:"` will display the Thumb Up icon. Find additional icons in the [Material Symbols](https://fonts.google.com/icons?icon.set=Material+Symbols&icon.style=Rounded) font library.
*   **`width`** (`"stretch"` or `int`): The width of the text input widget. This can be one of the following:
    *   `"stretch"` (default): The width of the widget matches the width of the parent container.
    *   An integer specifying the width in pixels: The widget has a fixed width. If the specified width is greater than the width of the parent container, the width of the widget matches the width of the parent container.

### Returns

(`str` or `None`)
The current value of the text input widget or `None` if no value has been provided by the user.

### Example

```python
import streamlit as st

title = st.text_input("Movie title", "Life of Brian")
st.write("The current movie title is", title)
```

Text input widgets can customize how to hide their labels with the `label_visibility` parameter. If "hidden", the label doesn’t show but there is still empty space for it above the widget (equivalent to `label=""`). If "collapsed", both the label and the space are removed. Default is "visible". Text input widgets can also be disabled with the `disabled` parameter, and can display an optional placeholder text when the text input is empty using the `placeholder` parameter:

```python
import streamlit as st

# Store the initial value of widgets in session state
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
st.session_state.disabled = False

col1, col2 = st.columns(2)

with col1:
    st.checkbox("Disable text input widget", key="disabled")
    st.radio(
        "Set text input label visibility 👉",
        key="visibility",
        options=["visible", "hidden", "collapsed"],
    )
    st.text_input(
        "Placeholder for the other text input widget",
        "This is a placeholder",
        key="placeholder",
    )

with col2:
    text_input = st.text_input(
        "Enter some text 👇",
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
        placeholder=st.session_state.placeholder,
    )
    if text_input:
        st.write("You entered: ", text_input)
```

### Previous and Next

*   [Previous: st.text_area](/develop/api-reference/widgets/st.text_area)
*   [Next: st.audio_input](/develop/api-reference/widgets/st.audio_input)

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.