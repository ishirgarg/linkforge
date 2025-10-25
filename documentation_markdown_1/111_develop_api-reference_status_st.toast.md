```markdown
# st.toast - Streamlit

**Source:** [https://docs.streamlit.io/develop/api-reference/status/st.toast](https://docs.streamlit.io/develop/api-reference/status/st.toast)

## st.toast

*(This section will be completed in the second part)*
```


Display a short message, known as a notification "toast".

The toast appears in the app's top-right corner and disappears after four seconds.

**Warning**

`st.toast` is not compatible with Streamlit's [caching](https://docs.streamlit.io/develop/concepts/architecture/caching) and cannot be called within a cached function.

## Function signature

[`[source]`](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/elements/toast.py#L38 "View st.toast source code on GitHub")

```python
st.toast(body, *, icon=None, duration="short")
```

## Parameters

### body (str)

The string to display as GitHub-flavored Markdown. Syntax information can be found at: [https://github.github.com/gfm](https://github.github.com/gfm).

See the `body` parameter of [`st.markdown`](https://docs.streamlit.io/develop/api-reference/text/st.markdown) for additional, supported Markdown directives.

### icon (str, None)

An optional emoji or icon to display next to the alert. If `icon` is `None` (default), no icon is displayed. If `icon` is a string, the following options are valid:

*   A single-character emoji. For example, you can set `icon="🚨"` or `icon="🔥"`. Emoji short codes are not supported.

*   An icon from the Material Symbols library (rounded style) in the format `":material/icon_name:"` where `"icon_name"` is the name of the icon in snake case.

    For example, `icon=":material/thumb_up:"` will display the Thumb Up icon. Find additional icons in the [Material Symbols](https://fonts.google.com/icons?icon.set=Material+Symbols&icon.style=Rounded) font library.

### duration ("short", "long", "infinite", or int)

The time to display the toast message. This can be one of the following:

*   `"short"` (default): Displays for 4 seconds.
*   `"long"`: Displays for 10 seconds.
*   `"infinite"`: Shows the toast until the user dismisses it.
*   An integer: Displays for the specified number of seconds.

## Examples

#### Example 1: Show a toast message

```python
import streamlit as st

st.toast("Your edited image was saved!", icon="😍")
```

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen _open\_in\_new_](https://doc-status-toast.streamlit.app//?utm_medium=oembed&)

#### Example 2: Show multiple toasts

When multiple toasts are generated, they will stack. Hovering over a toast will stop it from disappearing. When hovering ends, the toast will disappear after time specified in duration.

```python
import time
import streamlit as st

if st.button("Three cheers"):
    st.toast("Hip!")
    time.sleep(0.5)
    st.toast("Hip!")
    time.sleep(0.5)
    st.toast("Hooray!", icon="🎉")
```

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen _open\_in\_new_](https://doc-status-toast1.streamlit.app//?utm_medium=oembed&)

#### Example 3: Update a toast message

Toast messages can also be updated. Assign `st.toast(my_message)` to a variable and use the `.toast()` method to update it. If a toast has already disappeared or been dismissed, the update will not be seen.

```python
import time
import streamlit as st

def cook_breakfast():
    msg = st.toast("Gathering ingredients...")
    time.sleep(1)
    msg.toast("Cooking...")
    time.sleep(1)
    msg.toast("Ready!", icon="🥞")

if st.button("Cook breakfast"):
    cook_breakfast()
```

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen _open\_in\_new_](https://doc-status-toast2.streamlit.app//?utm_medium=oembed&)

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.
