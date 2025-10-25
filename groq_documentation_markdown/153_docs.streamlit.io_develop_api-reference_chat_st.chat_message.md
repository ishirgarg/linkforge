Here is the HTML content converted to clean Markdown:

## Streamlit Docs
[![logo](/logo.svg)](/)

### Documentation
#### Search
Search

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

### Navigation
* [Home](/)
* [Develop](/develop)
* [API reference](/develop/api-reference)
* [Chat elements](/develop/api-reference/chat)
* [st.chat_message](/develop/api-reference/chat/st.chat_message)

### Tip
Read the [Build a basic LLM chat app](/develop/tutorials/llms/build-conversational-apps) tutorial to learn how to use `st.chat_message` and `st.chat_input` to build chat-based apps.

## st.chat_message
### Description
Insert a chat message container.

To add elements to the returned container, you can use with notation (preferred) or just call methods directly on the returned object. See the examples below.

**Note**: To follow best design practices and maintain a good appearance on all screen sizes, don't nest chat message containers.

### Function Signature
```python
st.chat_message(name, *, avatar=None, width="stretch")
```
### Parameters

* **name**: The name of the message author. Can be "human"/"user" or "ai"/"assistant" to enable preset styling and avatars. Currently, the name is not shown in the UI but is only set as an accessibility label. For accessibility reasons, you should not use an empty string.
* **avatar**: The avatar shown next to the message. If `avatar` is `None` (default), the icon will be determined from `name` as follows:
	+ If `name` is "user" or "human", the message will have a default user icon.
	+ If `name` is "ai" or "assistant", the message will have a default bot icon.
	+ For all other values of `name`, the message will show the first letter of the name.
	+ In addition to the types supported by `st.image` (except list), the following strings are valid:
		- A single-character emoji (e.g., "🧑‍💻" or "🦖").
		- An icon from the Material Symbols library (rounded style) in the format ":material/icon_name:" where "icon_name" is the name of the icon in snake case.
* **width**: The width of the chat message container. This can be one of the following:
	+ "stretch" (default): The width of the container matches the width of the parent container.
	+ "content": The width of the container matches the width of its content, but doesn't exceed the width of the parent container.
	+ An integer specifying the width in pixels: The container has a fixed width. If the specified width is greater than the width of the parent container, the width of the container matches the width of the parent container.

### Returns
A single container that can hold multiple elements.

### Examples

You can use with notation to insert any element into a chat message:
```python
import streamlit as st
import numpy as np

with st.chat_message("user"):
    st.write("Hello 👋")
    st.line_chart(np.random.randn(30, 3))
```
Or you can just call methods directly on the returned object:
```python
import streamlit as st
import numpy as np

message = st.chat_message("assistant")
message.write("Hello human")
message.bar_chart(np.random.randn(30, 3))
```