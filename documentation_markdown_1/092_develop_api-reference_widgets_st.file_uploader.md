# st.file_uploader

**URL:** https://docs.streamlit.io/develop/api-reference/widgets/st.file_uploader

This document provides information on the `st.file_uploader` widget in Streamlit, which allows users to upload files to their Streamlit applications.

---

**Note:** This is the first part of the content. The full documentation will be provided in subsequent parts.

Display a file uploader widget.

By default, uploaded files are limited to 200 MB each. You can configure this using the `server.maxUploadSize` config option. For more information on how to set config options, see [config.toml](https://docs.streamlit.io/develop/api-reference/configuration/config.toml).

### Function signature

```python
st.file_uploader(label, type=None, accept_multiple_files=False, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible", width="stretch")
```

### Parameters

*   **label** (`str`)
    A short label explaining to the user what this file uploader is for. The label can optionally contain GitHub-flavored Markdown of the following types: Bold, Italics, Strikethroughs, Inline Code, Links, and Images. Images display like icons, with a max height equal to the font height.

    Unsupported Markdown elements are unwrapped so only their children (text contents) render. Display unsupported elements as literal characters by backslash-escaping them. E.g., "1\. Not an ordered list".

    See the body parameter of [st.markdown](https://docs.streamlit.io/develop/api-reference/text/st.markdown) for additional, supported Markdown directives.

    For accessibility reasons, you should never set an empty label, but you can hide it with `label_visibility` if needed. In the future, we may disallow empty labels by raising an exception.

*   **type** (`str`, `list` of `str`, or `None`)
    The allowed file extension(s) for uploaded files. This can be one of the following types:
    *   `None` (default): All file extensions are allowed.
    *   A string: A single file extension is allowed. For example, to only accept CSV files, use `"csv"`.
    *   A sequence of strings: Multiple file extensions are allowed. For example, to only accept JPG/JPEG and PNG files, use `["jpg", "jpeg", "png"]`.

    **Note:** This is a best-effort check, but doesn't provide a security guarantee against users uploading files of other types or type extensions. The correct handling of uploaded files is part of the app developer's responsibility.

*   **accept\_multiple\_files** (`bool` or `"directory"`)
    Whether to accept more than one file in a submission. This can be one of the following values:
    *   `False` (default): The user can only submit one file at a time.
    *   `True`: The user can upload multiple files at the same time.
    *   `"directory"`: The user can select a directory to upload all files in the directory and its subdirectories. If `type` is set, only files matching those type(s) will be uploaded.

    When this is `True` or `"directory"`, the return value will be a list and a user can additively select files if they click the browse button on the widget multiple times.

*   **key** (`str` or `int`)
    An optional string or integer to use as the unique key for the widget. If this is omitted, a key will be generated for the widget based on its content. No two widgets may have the same key.

*   **help** (`str` or `None`)
    A tooltip that gets displayed next to the widget label. Streamlit only displays the tooltip when `label_visibility="visible"`. If this is `None` (default), no tooltip is displayed.

    The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of `st.markdown`.

*   **on\_change** (`callable`)
    An optional callback invoked when this `file_uploader`'s value changes.

*   **args** (`list` or `tuple`)
    An optional list or tuple of args to pass to the callback.

*   **kwargs** (`dict`)
    An optional dict of kwargs to pass to the callback.

*   **disabled** (`bool`)
    An optional boolean that disables the file uploader if set to `True`. The default is `False`.

*   **label\_visibility** (`"visible"`, `"hidden"`, or `"collapsed"`)
    The visibility of the label. The default is `"visible"`. If this is `"hidden"`, Streamlit displays an empty spacer instead of the label, which can help keep the widget aligned with other widgets. If this is `"collapsed"`, Streamlit displays no label or spacer.

*   **width** (`"stretch"` or `int`)
    The width of the file uploader widget. This can be one of the following:
    *   `"stretch"` (default): The width of the widget matches the width of the parent container.
    *   An integer specifying the width in pixels: The widget has a fixed width. If the specified width is greater than the width of the parent container, the width of the widget matches the width of the parent container.

### Returns

(`None`, `UploadedFile`, or `list` of `UploadedFile`)

*   If `accept_multiple_files` is `False`, returns either `None` or an `UploadedFile` object.
*   If `accept_multiple_files` is `True` or `"directory"`, returns a list with the uploaded files as `UploadedFile` objects. If no files were uploaded, returns an empty list.

The `UploadedFile` class is a subclass of `BytesIO`, and therefore is "file-like". This means you can pass an instance of it anywhere a file is expected.

### Examples

**Example 1: Accept a single file at a time**

```python
import streamlit as st
import pandas as pd
from io import StringIO

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)
```

**Example 2: Accept multiple files at a time**

```python
import pandas as pd
import streamlit as st

uploaded_files = st.file_uploader(
    "Upload data", accept_multiple_files=True, type="csv"
)
for uploaded_file in uploaded_files:
    df = pd.read_csv(uploaded_file)
    st.write(df)
```

**Example 3: Accept an entire directory**

```python
import streamlit as st

uploaded_files = st.file_uploader(
    "Upload images", accept_multiple_files="directory", type=["jpg", "png"]
)
for uploaded_file in uploaded_files:
    st.image(uploaded_file)
```

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.