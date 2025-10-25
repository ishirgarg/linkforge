Here is the HTML content converted to clean Markdown:

### Streamlit Docs

* [Get started](/get-started)
	+ [Installation](/get-started/installation)
	+ [Fundamentals](/get-started/fundamentals)
	+ [First steps](/get-started/tutorials)
* [Develop](/develop)
	+ [Concepts](/develop/concepts)
	+ [API reference](/develop/api-reference)
		- [Write and magic](/develop/api-reference/write-magic)
		- [Text elements](/develop/api-reference/text)
		- [Data elements](/develop/api-reference/data)
		- [Chart elements](/develop/api-reference/charts)
		- [Input widgets](/develop/api-reference/widgets)
		- [Media elements](/develop/api-reference/media)
		- [Layouts and containers](/develop/api-reference/layout)
		- [Chat elements](/develop/api-reference/chat)
		- [Status elements](/develop/api-reference/status)
			- [st.success](/develop/api-reference/status/st.success)
			- [st.info](/develop/api-reference/status/st.info)
			- [st.warning](/develop/api-reference/status/st.warning)
			- [st.error](/develop/api-reference/status/st.error)
			- [st.exception](/develop/api-reference/status/st.exception)
			- [st.progress](/develop/api-reference/status/st.progress)
			- [st.spinner](/develop/api-reference/status/st.spinner)
			- [st.status](/develop/api-reference/status/st.status)
			- [st.toast](/develop/api-reference/status/st.toast)
			- [st.balloons](/develop/api-reference/status/st.balloons)
			- [st.snow](/develop/api-reference/status/st.snow)
		- [Third-party components](https://streamlit.io/components)
		- [Application logic](/develop/api-reference/user)
		- [Navigation and pages](/develop/api-reference/navigation)
		- [Execution flow](/develop/api-reference/execution-flow)
		- [Caching and state](/develop/api-reference/caching-and-state)
		- [Connections and secrets](/develop/api-reference/connections)
		- [Custom components](/develop/api-reference/custom-components)
		- [Configuration](/develop/api-reference/configuration)
		- [App testing](/develop/api-reference/app-testing)
		- [Command line](/develop/api-reference/cli)
	+ [Tutorials](/develop/tutorials)
	+ [Quick reference](/develop/quick-reference)
* [Deploy](/deploy)
	+ [Concepts](/deploy/concepts)
	+ [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
	+ [Snowflake](/deploy/snowflake)
	+ [Other platforms](/deploy/tutorials)
* [Knowledge base](/knowledge-base)
	+ [FAQ](/knowledge-base/using-streamlit)
	+ [Installing dependencies](/knowledge-base/dependencies)
	+ [Deployment issues](/knowledge-base/deploy)

Note: I removed the icons and unnecessary HTML tags to convert the content to clean Markdown. Let me know if you need any further assistance!

## st.spinner
### Description
Display a loading spinner while executing a block of code.

### Function Signature
```python
st.spinner(text="In progress...", *, show_time=False, width="content")
```

### Parameters
* **text** (str): The text to display next to the spinner. This defaults to "In progress...". The text can optionally contain GitHub-flavored Markdown.
* **show_time** (bool): Whether to show the elapsed time next to the spinner text. If this is False (default), no time is displayed. If this is True, elapsed time is displayed with a precision of 0.1 seconds.
* **width** ("content", "stretch", or int): The width of the spinner element. This can be one of the following:
	+ "content" (default): The width of the element matches the width of its content, but doesn't exceed the width of the parent container.
	+ "stretch": The width of the element matches the width of the parent container.
	+ An integer specifying the width in pixels: The element has a fixed width. If the specified width is greater than the width of the parent container, the width of the element matches the width of the parent container.

### Example
```python
import streamlit as st
import time

with st.spinner("Wait for it...", show_time=True):
    time.sleep(5)
st.success("Done!")
st.button("Rerun")
```

### Additional Resources
For more information on Streamlit and its features, please visit the [Streamlit documentation](https://docs.streamlit.io). If you have any questions or need further assistance, you can ask on the [Streamlit forums](https://discuss.streamlit.io).