Here is the HTML content converted to clean Markdown:

# Streamlit Docs

## Documentation

### Search

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
			- [Buttons](#buttons)
				- [st.button](/develop/api-reference/widgets/st.button)
				- [st.download_button](/develop/api-reference/widgets/st.download_button)
				- [st.form_submit_button](/develop/api-reference/execution-flow/st.form_submit_button)
				- [st.link_button](/develop/api-reference/widgets/st.link_button)
				- [st.page_link](/develop/api-reference/widgets/st.page_link)
			- [Selections](#selections)
				- [st.checkbox](/develop/api-reference/widgets/st.checkbox)
				- [st.color_picker](/develop/api-reference/widgets/st.color_picker)
				- [st.feedback](/develop/api-reference/widgets/st.feedback)
				- [st.multiselect](/develop/api-reference/widgets/st.multiselect)
				- [st.pills](/develop/api-reference/widgets/st.pills)
				- [st.radio](/develop/api-reference/widgets/st.radio)
				- [st.segmented_control](/develop/api-reference/widgets/st.segmented_control)
				- [st.selectbox](/develop/api-reference/widgets/st.selectbox)
				- [st.select_slider](/develop/api-reference/widgets/st.select_slider)
				- [st.toggle](/develop/api-reference/widgets/st.toggle)
			- [Numeric](#numeric)
				- [st.number_input](/develop/api-reference/widgets/st.number_input)
				- [st.slider](/develop/api-reference/widgets/st.slider)
			- [Date and Time](#date-and-time)
				- [st.date_input](/develop/api-reference/widgets/st.date_input)
				- [st.time_input](/develop/api-reference/widgets/st.time_input)
			- [Text](#text)
				- [st.chat_input](/develop/api-reference/chat/st.chat_input)
				- [st.text_area](/develop/api-reference/widgets/st.text_area)
				- [st.text_input](/develop/api-reference/widgets/st.text_input)
			- [Media and Files](#media-and-files)
				- [st.audio_input](/develop/api-reference/widgets/st.audio_input)
				- [st.camera_input](/develop/api-reference/widgets/st.camera_input)
				- [st.data_editor](/develop/api-reference/data/st.data_editor)
				- [st.file_uploader](/develop/api-reference/widgets/st.file_uploader)
		- [Media elements](/develop/api-reference/media)
		- [Layouts and containers](/develop/api-reference/layout)
		- [Chat elements](/develop/api-reference/chat)
		- [Status elements](/develop/api-reference/status)
		- [Third-party components](https://streamlit.io/components)
		- [Application Logic](#application-logic)
			- [Authentication and user info](/develop/api-reference/user)
			- [Navigation and pages](/develop/api-reference/navigation)
			- [Execution flow](/develop/api-reference/execution-flow)
			- [Caching and state](/develop/api-reference/caching-and-state)
			- [Connections and secrets](/develop/api-reference/connections)
			- [Custom components](/develop/api-reference/custom-components)
			- [Configuration](/develop/api-reference/configuration)
		- [Tools](#tools)
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

### Navigation

* [Home](/)
* [Develop](/develop)
* [API reference](/develop/api-reference)
* [Input widgets](/develop/api-reference/widgets)
* [st.checkbox](/develop/api-reference/widgets/st.checkbox)

## st.checkbox
Display a checkbox widget.

### Function signature
```python
st.checkbox(label, value=False, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible", width="content")
```

### Parameters
* `label` (str): A short label explaining to the user what this checkbox is for. The label can optionally contain GitHub-flavored Markdown.
* `value` (bool): Preselect the checkbox when it first renders.
* `key` (str or int): An optional string or integer to use as the unique key for the widget.
* `help` (str or None): A tooltip that gets displayed next to the widget label.
* `on_change` (callable): An optional callback invoked when this checkbox's value changes.
* `args` (list or tuple): An optional list or tuple of args to pass to the callback.
* `kwargs` (dict): An optional dict of kwargs to pass to the callback.
* `disabled` (bool): An optional boolean that disables the checkbox if set to True.
* `label_visibility` ("visible", "hidden", or "collapsed"): The visibility of the label.
* `width` ("content", "stretch", or int): The width of the checkbox widget.

### Returns
* (bool): Whether or not the checkbox is checked.

### Example
```python
import streamlit as st

agree = st.checkbox("I agree")

if agree:
    st.write("Great!")
```

### Featured Videos
Check out our video on how to use one of Streamlit's core functions, the checkbox! 

In the video below, we'll take it a step further and learn how to combine a [button](/develop/api-reference/widgets/st.button), [checkbox](/develop/api-reference/widgets/st.checkbox) and [radio button](/develop/api-reference/widgets/st.radio)! 

### Still have questions?
Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts. 

Note: I removed the unnecessary links, versions, and other information to make the text cleaner and more readable. I also reformatted the text to follow Markdown conventions. Let me know if you need any further changes!