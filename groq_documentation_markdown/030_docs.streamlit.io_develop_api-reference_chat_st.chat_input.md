Here is the HTML content converted to clean Markdown:
### st.chat_input - Streamlit Docs

![logo](/logo.svg)

#### Documentation

[Search](/)

### Menu

* **Get started**
	+ [Installation](/get-started/installation)
	+ [Fundamentals](/get-started/fundamentals)
	+ [First steps](/get-started/tutorials)
* **Develop**
	+ [Concepts](/develop/concepts)
	+ [API reference](/develop/api-reference)
		- PAGE ELEMENTS
		- [Write and magic](/develop/api-reference/write-magic)
		- [Text elements](/develop/api-reference/text)
		- [Data elements](/develop/api-reference/data)
		- [Chart elements](/develop/api-reference/charts)
		- [Input widgets](/develop/api-reference/widgets)
		- [Media elements](/develop/api-reference/media)
		- [Layouts and containers](/develop/api-reference/layout)
		- [Chat elements](/develop/api-reference/chat)
			- [st.chat_input](/develop/api-reference/chat/st.chat_input)
			- [st.chat_message](/develop/api-reference/chat/st.chat_message)
		- [Status elements](/develop/api-reference/status)
		- [Third-party components](https://streamlit.io/components)
		- APPLICATION LOGIC
		- [Authentication and user info](/develop/api-reference/user)
		- [Navigation and pages](/develop/api-reference/navigation)
		- [Execution flow](/develop/api-reference/execution-flow)
		- [Caching and state](/develop/api-reference/caching-and-state)
		- [Connections and secrets](/develop/api-reference/connections)
		- [Custom components](/develop/api-reference/custom-components)
		- [Configuration](/develop/api-reference/configuration)
		- TOOLS
		- [App testing](/develop/api-reference/app-testing)
		- [Command line](/develop/api-reference/cli)
	+ [Tutorials](/develop/tutorials)
	+ [Quick reference](/develop/quick-reference)
* **Deploy**
	+ [Concepts](/deploy/concepts)
	+ [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
	+ [Snowflake](/deploy/snowflake)
	+ [Other platforms](/deploy/tutorials)
* **Knowledge base**
	+ [FAQ](/knowledge-base/using-streamlit)
	+ [Installing dependencies](/knowledge-base/dependencies)
	+ [Deployment issues](/knowledge-base/deploy)

### Breadcrumbs

* [Home](/)
* [Develop](/develop)
* [API reference](/develop/api-reference)
* [Chat elements](/develop/api-reference/chat)
* [st.chat_input](/develop/api-reference/chat/st.chat_input)

### Tip

Read the [Build a basic LLM chat app](/develop/tutorials/llms/build-conversational-apps) tutorial to learn how to use `st.chat_message` and `st.chat_input` to build chat-based apps.

## st.chat_input
### Description
Display a chat input widget.

### Function Signature
```python
st.chat_input(
    placeholder="Your message", 
    *, 
    key=None, 
    max_chars=None, 
    accept_file=False, 
    file_type=None, 
    disabled=False, 
    on_submit=None, 
    args=None, 
    kwargs=None, 
    width="stretch"
)
```

### Parameters
* `placeholder` (str): A placeholder text shown when the chat input is empty. This defaults to "Your message".
* `key` (str or int): An optional string or integer to use as the unique key for the widget.
* `max_chars` (int or None): The maximum number of characters that can be entered. If this is None (default), there will be no maximum.
* `accept_file` (bool, "multiple", or "directory"): Whether the chat input should accept files.
* `file_type` (str, Sequence[str], or None): The allowed file extension(s) for uploaded files.
* `disabled` (bool): Whether the chat input should be disabled. This defaults to False.
* `on_submit` (callable): An optional callback invoked when the chat input's value is submitted.
* `args` (list or tuple): An optional list or tuple of args to pass to the callback.
* `kwargs` (dict): An optional dict of kwargs to pass to the callback.
* `width` ("stretch" or int): The width of the chat input widget.

### Returns
The user's submission. This is one of the following types:
* None: If the user didn't submit a message or file in the last rerun.
* A string: When the widget is not configured to accept files and the user submitted a message in the last rerun.
* A dict-like object: When the widget is configured to accept files and the user submitted a message and/or file(s) in the last rerun.

### Examples
#### Example 1: Pin the chat input widget to the bottom of your app
```python
import streamlit as st

prompt = st.chat_input("Say something")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")
```

#### Example 2: Use the chat input widget inline
```python
import streamlit as st

with st.sidebar:
    messages = st.container(height=300)
    if prompt := st.chat_input("Say something"):
        messages.chat_message("user").write(prompt)
        messages.chat_message("assistant").write(f"Echo: {prompt}")
```

#### Example 3: Let users upload files
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

#### Example 4: Programmatically set the text via session state
```python
import streamlit as st

if st.button("Set Value"):
    st.session_state.chat_input = "Hello, world!"
st.chat_input(key="chat_input")
st.write("Chat input value:", st.session_state.chat_input)
```