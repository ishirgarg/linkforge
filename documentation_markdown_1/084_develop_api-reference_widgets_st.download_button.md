# st.download_button

This is the first part of the documentation for `st.download_button` in Streamlit. It covers the introduction and the main title of the page.

**URL:** https://docs.streamlit.io/develop/api-reference/widgets/st.download_button

---

Display a download button widget.

This is useful when you would like to provide a way for your users to download a file directly from your app.

Note that the data to be downloaded is stored in-memory while the user is connected, so it's a good idea to keep file sizes under a couple hundred megabytes to conserve memory.

If you want to prevent your app from rerunning when a user clicks the download button, wrap the download button in a [fragment](https://docs.streamlit.io/develop/concepts/architecture/fragments).

### Function signature
[[source]](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/elements/widgets/button.py#L283 "View st.download_button source code on GitHub")

```python
st.download_button(label, data, file_name=None, mime=None, key=None, help=None, on_click="rerun", args=None, kwargs=None, *, type="secondary", icon=None, disabled=False, use_container_width=None, width="content")
```

### Parameters

*   **label** (`str`)
    A short label explaining to the user what this button is for. The label can optionally contain GitHub-flavored Markdown of the following types: Bold, Italics, Strikethroughs, Inline Code, Links, and Images. Images display like icons, with a max height equal to the font height.

    Unsupported Markdown elements are unwrapped so only their children (text contents) render. Display unsupported elements as literal characters by backslash-escaping them. E.g., "1\. Not an ordered list".

    See the body parameter of [st.markdown](https://docs.streamlit.io/develop/api-reference/text/st.markdown) for additional, supported Markdown directives.

*   **data** (`str`, `bytes`, or `file`)
    The contents of the file to be downloaded.

    To prevent unnecessary recomputation, use caching when converting your data for download. For more information, see the Example 1 below.

*   **file_name** (`str`)
    An optional string to use as the name of the file to be downloaded, such as "my_file.csv". If not specified, the name will be automatically generated.

*   **mime** (`str` or `None`)
    The MIME type of the data. If this is `None` (default), Streamlit sets the MIME type depending on the value of `data` as follows:

    *   If `data` is a string or textual file (i.e. `str` or `io.TextIOWrapper` object), Streamlit uses the "text/plain" MIME type.
    *   If `data` is a binary file or bytes (i.e. `bytes`, `io.BytesIO`, `io.BufferedReader`, or `io.RawIOBase` object), Streamlit uses the "application/octet-stream" MIME type.

    For more information about MIME types, see [https://www.iana.org/assignments/media-types/media-types.xhtml](https://www.iana.org/assignments/media-types/media-types.xhtml).

*   **key** (`str` or `int`)
    An optional string or integer to use as the unique key for the widget. If this is omitted, a key will be generated for the widget based on its content. No two widgets may have the same key.

*   **help** (`str` or `None`)
    A tooltip that gets displayed when the button is hovered over. If this is `None` (default), no tooltip is displayed.

    The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of `st.markdown`.

*   **on_click** (`callable`, `"rerun"`, `"ignore"`, or `None`)
    How the button should respond to user interaction. This controls whether or not the button triggers a rerun and if a callback function is called. This can be one of the following values:

    *   "rerun" (default): The user downloads the file and the app reruns. No callback function is called.
    *   "ignore": The user downloads the file and the app doesn't rerun. No callback function is called.
    *   A callable: The user downloads the file and app reruns. The callable is called before the rest of the app.
    *   `None`: This is same as `on_click="rerun"`. This value exists for backwards compatibility and shouldn't be used.

*   **args** (`list` or `tuple`)
    An optional list or tuple of args to pass to the callback.

*   **kwargs** (`dict`)
    An optional dict of kwargs to pass to the callback.

*   **type** (`"primary"`, `"secondary"`, or `"tertiary"`)
    An optional string that specifies the button type. This can be one of the following:

    *   "primary": The button's background is the app's primary color for additional emphasis.
    *   "secondary" (default): The button's background coordinates with the app's background color for normal emphasis.
    *   "tertiary": The button is plain text without a border or background for subtlety.

*   **icon** (`str` or `None`)
    An optional emoji or icon to display next to the button label. If `icon` is `None` (default), no icon is displayed. If `icon` is a string, the following options are valid:

    *   A single-character emoji. For example, you can set `icon="🚨"` or `icon="🔥"`. Emoji short codes are not supported.
    *   An icon from the Material Symbols library (rounded style) in the format `":material/icon_name:"` where `"icon_name"` is the name of the icon in snake case.

        For example, `icon=":material/thumb_up:"` will display the Thumb Up icon. Find additional icons in the [Material Symbols](https://fonts.google.com/icons?icon.set=Material+Symbols&icon.style=Rounded) font library.

*   **disabled** (`bool`)
    An optional boolean that disables the download button if set to `True`. The default is `False`.

*   **use_container_width** (`bool`)
    _`use_container_width` is deprecated and will be removed in a future release. For `use_container_width=True`, use `width="stretch"`. For `use_container_width=False`, use `width="content"`._

    Whether to expand the button's width to fill its parent container. If `use_container_width` is `False` (default), Streamlit sizes the button to fit its contents. If `use_container_width` is `True`, the width of the button matches its parent container.

    In both cases, if the contents of the button are wider than the parent container, the contents will line wrap.

*   **width** (`"content"`, `"stretch"`, or `int`)
    The width of the download button. This can be one of the following:

    *   "content" (default): The width of the button matches the width of its content, but doesn't exceed the width of the parent container.
    *   "stretch": The width of the button matches the width of the parent container.
    *   An integer specifying the width in pixels: The button has a fixed width. If the specified width is greater than the width of the parent container, the width of the button matches the width of the parent container.

### Returns

(`bool`)
`True` if the button was clicked on the last run of the app, `False` otherwise.

### Examples

#### Example 1: Download a dataframe as a CSV file

When working with a large dataframe, it's recommended to fetch your data with a cached function. When working with a download button, it's similarly recommended to convert your data into a downloadable format with a cached function. Caching ensures that the app reruns efficiently.

```python
import streamlit as st
import pandas as pd
import numpy as np

@st.cache_data
def get_data():
    df = pd.DataFrame(
        np.random.randn(50, 20), columns=("col %d" % i for i in range(20))
    )
    return df

@st.cache_data
def convert_for_download(df):
    return df.to_csv().encode("utf-8")

df = get_data()
csv = convert_for_download(df)

st.download_button(
    label="Download CSV",
    data=csv,
    file_name="data.csv",
    mime="text/csv",
    icon=":material/download:",
)
```

#### Example 2: Download a string as a text file

If you pass a string to the `data` argument, Streamlit will automatically use the "text/plain" MIME type.

When you have a widget (like a text area) affecting the value of your download, it's recommended to use another button to prepare the download. In this case, use `on_click="ignore"` in your download button to prevent the download button from rerunning your app. This turns the download button into a frontend-only element that can be nested in another button.

Without a preparation button, a user can type something into the text area and immediately click the download button. Because a download is initiated concurrently with the app rerun, this can create a race-like condition where the user doesn't see the updated data in their download.

> **Important**
> Even when you prevent your download button from triggering a rerun, another widget with a pending change can still trigger a rerun. For example, if a text area has a pending change when a user clicks a download button, the text area will trigger a rerun.

```python
import streamlit as st

message = st.text_area("Message", value="Lorem ipsum.\nStreamlit is cool.")

if st.button("Prepare download"):
    st.download_button(
        label="Download text",
        data=message,
        file_name="message.txt",
        on_click="ignore",
        type="primary",
        icon=":material/download:",
    )
```

### Example 3: Download a file

Use a context manager to open and read a local file on your Streamlit server. Pass the `io.BufferedReader` object directly to `data`. Remember to specify the MIME type if you don't want the default type of "application/octet-stream" for generic binary data. In the example below, the MIME type is set to "image/png" for a PNG file.

```python
import streamlit as st

with open("flower.png", "rb") as file:
    st.download_button(
        label="Download image",
        data=file,
        file_name="flower.png",
        mime="image/png",
    )
```

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.