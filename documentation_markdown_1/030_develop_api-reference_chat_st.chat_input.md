```markdown
# st.chat_input - Streamlit

> **Source:** [https://docs.streamlit.io/develop/api-reference/chat/st.chat_input](https://docs.streamlit.io/develop/api-reference/chat/st.chat_input)

#### Tip

Read the [Build a basic LLM chat app](/develop/tutorials/llms/build-conversational-apps) tutorial to learn how to use `st.chat_message` and `st.chat_input` to build chat-based apps.

## st.chat_input
```


Display a chat input widget.

### Function signature
[[source]](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/elements/widgets/chat.py#L403 "View st.chat_input source code on GitHub")

```python
st.chat_input(placeholder="Your message", *, key=None, max_chars=None, accept_file=False, file_type=None, disabled=False, on_submit=None, args=None, kwargs=None, width="stretch")
```

### Parameters

*   **placeholder** (str)
    A placeholder text shown when the chat input is empty. This defaults to "Your message". For accessibility reasons, you should not use an empty string.
*   **key** (str or int)
    An optional string or integer to use as the unique key for the widget. If this is omitted, a key will be generated for the widget based on its content. No two widgets may have the same key.
*   **max_chars** (int or None)
    The maximum number of characters that can be entered. If this is `None` (default), there will be no maximum.
*   **accept_file** (bool, "multiple", or "directory")
    Whether the chat input should accept files. This can be one of the following values:
    *   `False` (default): No files are accepted and the user can only submit a message.
    *   `True`: The user can add a single file to their submission.
    *   `"multiple"`: The user can add multiple files to their submission.
    *   `"directory"`: The user can add multiple files to their submission by selecting a directory. If `file_type` is set, only files matching those type(s) will be uploaded.

    By default, uploaded files are limited to 200 MB each. You can configure this using the `server.maxUploadSize` config option. For more information on how to set config options, see [config.toml](https://docs.streamlit.io/develop/api-reference/configuration/config.toml).
*   **file_type** (str, Sequence\[str], or None)
    The allowed file extension(s) for uploaded files. This can be one of the following types:
    *   `None` (default): All file extensions are allowed.
    *   A string: A single file extension is allowed. For example, to only accept CSV files, use `"csv"`.
    *   A sequence of strings: Multiple file extensions are allowed. For example, to only accept JPG/JPEG and PNG files, use `["jpg", "jpeg", "png"]`.

    > **Note**
    > This is a best-effort check, but doesn't provide a security guarantee against users uploading files of other types or type extensions. The correct handling of uploaded files is part of the app developer's responsibility.
*   **disabled** (bool)
    Whether the chat input should be disabled. This defaults to `False`.
*   **on_submit** (callable)
    An optional callback invoked when the chat input's value is submitted.
*   **args** (list or tuple)
    An optional list or tuple of args to pass to the callback.
*   **kwargs** (dict)
    An optional dict of kwargs to pass to the callback.
*   **width** ("stretch" or int)
    The width of the chat input widget. This can be one of the following:
    *   `"stretch"` (default): The width of the widget matches the width of the parent container.
    *   An integer specifying the width in pixels: The widget has a fixed width. If the specified width is greater than the width of the parent container, the width of the widget matches the width of the parent container.

### Returns

(None, str, or dict-like)

The user's submission. This is one of the following types:

*   `None`: If the user didn't submit a message or file in the last rerun, the widget returns `None`.
*   A string: When the widget is not configured to accept files and the user submitted a message in the last rerun, the widget returns the user's message as a string.
*   A dict-like object: When the widget is configured to accept files and the user submitted a message and/or file(s) in the last rerun, the widget returns a dict-like object with two attributes, `text` and `files`.

When the widget is configured to accept files and the user submits something in the last rerun, you can access the user's submission with key or attribute notation from the dict-like object. This is shown in Example 3 below.

The `text` attribute holds a string, which is the user's message. This is an empty string if the user only submitted one or more files.

The `files` attribute holds a list of `UploadedFile` objects. The list is empty if the user only submitted a message. Unlike `st.file_uploader`, this attribute always returns a list, even when the widget is configured to accept only one file at a time.

The `UploadedFile` class is a subclass of `BytesIO`, and therefore is "file-like". This means you can pass an instance of it anywhere a file is expected.

#### Examples

**Example 1: Pin the chat input widget to the bottom of your app**

When `st.chat_input` is used in the main body of an app, it will be pinned to the bottom of the page.

```python
import streamlit as st

prompt = st.chat_input("Say something")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")
```

**Example 2: Use the chat input widget inline**

The chat input can also be used inline by nesting it inside any layout container (container, columns, tabs, sidebar, etc) or fragment. Create chat interfaces embedded next to other content, or have multiple chatbots!

```python
import streamlit as st

with st.sidebar:
    messages = st.container(height=300)
    if prompt := st.chat_input("Say something"):
        messages.chat_message("user").write(prompt)
        messages.chat_message("assistant").write(f"Echo: {prompt}")
```

**Example 3: Let users upload files**

When you configure your chat input widget to allow file attachments, it will return a dict-like object when the user sends a submission. You can access the user's message through the `text` attribute of this dictionary. You can access a list of the user's submitted file(s) through the `files` attribute. Similar to `st.session_state`, you can use key or attribute notation.

```python
import streamlit as st

prompt = st.chat_input(
    "Say something and/or attach an image",
    accept_file=True,
    file_type=["jpg", "jpeg", "png"],
)
if prompt and prompt.text:
    st.markdown(prompt.text)
if prompt and prompt["files"]:
    st.image(prompt["files"][0])
```

**Example 4: Programmatically set the text via session state**

You can use `st.session_state` to set the text of the chat input widget.

```python
import streamlit as st

if st.button("Set Value"):
    st.session_state.chat_input = "Hello, world!"
st.chat_input(key="chat_input")
st.write("Chat input value:", st.session_state.chat_input)
```

For an overview of the `st.chat_input` and `st.chat_message` API, check out this video tutorial by Chanin Nantasenamat ([@dataprofessor](https://www.youtube.com/dataprofessor)), a Senior Developer Advocate at Streamlit.

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.
