Here is the converted HTML to clean Markdown:

# st.feedback - Streamlit Docs
## Documentation

### Search
Search

### Navigation
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
			- [Buttons](#)
				- [st.button](/develop/api-reference/widgets/st.button)
				- [st.download_button](/develop/api-reference/widgets/st.download_button)
				- [st.form_submit_button](/develop/api-reference/execution-flow/st.form_submit_button)
				- [st.link_button](/develop/api-reference/widgets/st.link_button)
				- [st.page_link](/develop/api-reference/widgets/st.page_link)
			- [Selections](#)
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
			- [Numeric](#)
				- [st.number_input](/develop/api-reference/widgets/st.number_input)
				- [st.slider](/develop/api-reference/widgets/st.slider)
			- [Date and Time](#)
				- [st.date_input](/develop/api-reference/widgets/st.date_input)
				- [st.time_input](/develop/api-reference/widgets/st.time_input)
			- [Text](#)
				- [st.chat_input](/develop/api-reference/chat/st.chat_input)
				- [st.text_area](/develop/api-reference/widgets/st.text_area)
				- [st.text_input](/develop/api-reference/widgets/st.text_input)
			- [Media and Files](#)
				- [st.audio_input](/develop/api-reference/widgets/st.audio_input)
				- [st.camera_input](/develop/api-reference/widgets/st.camera_input)
				- [st.data_editor](/develop/api-reference/data/st.data_editor)
				- [st.file_uploader](/develop/api-reference/widgets/st.file_uploader)
		- [Media elements](/develop/api-reference/media)
		- [Layouts and containers](/develop/api-reference/layout)
		- [Chat elements](/develop/api-reference/chat)
		- [Status elements](/develop/api-reference/status)
		- [Third-party components](https://streamlit.io/components)
		- [Application Logic](#)
			- [Authentication and user info](/develop/api-reference/user)
			- [Navigation and pages](/develop/api-reference/navigation)
			- [Execution flow](/develop/api-reference/execution-flow)
			- [Caching and state](/develop/api-reference/caching-and-state)
			- [Connections and secrets](/develop/api-reference/connections)
			- [Custom components](/develop/api-reference/custom-components)
			- [Configuration](/develop/api-reference/configuration)
		- [Tools](#)
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

### Links
* [Home](/)
* [Develop](/develop)
* [API reference](/develop/api-reference)
* [Input widgets](/develop/api-reference/widgets)
* [st.feedback](/develop/api-reference/widgets/st.feedback)

## st.feedback
Display a feedback widget.

A feedback widget is an icon-based button group available in three styles, as described in options. It is commonly used in chat and AI apps to allow users to rate responses.

### Function signature
```python
st.feedback(options="thumbs", *, key=None, disabled=False, on_change=None, args=None, kwargs=None, width="content")
```
### Parameters

* **options**: The feedback options displayed to the user. Can be one of the following:
	+ "thumbs" (default): Streamlit displays a thumb-up and thumb-down button group.
	+ "faces": Streamlit displays a row of five buttons with facial expressions depicting increasing satisfaction from left to right.
	+ "stars": Streamlit displays a row of star icons, allowing the user to select a rating from one to five stars.
* **key**: An optional string or integer to use as the unique key for the widget. If this is omitted, a key will be generated for the widget based on its content.
* **disabled**: An optional boolean that disables the feedback widget if set to True. The default is False.
* **on_change**: An optional callback invoked when this feedback widget's value changes.
* **args**: An optional list or tuple of args to pass to the callback.
* **kwargs**: An optional dict of kwargs to pass to the callback.
* **width**: The width of the feedback widget. Can be one of the following:
	+ "content" (default): The width of the widget matches the width of its content, but doesn't exceed the width of the parent container.
	+ "stretch": The width of the widget matches the width of the parent container.
	+ An integer specifying the width in pixels: The widget has a fixed width.

### Returns
An integer indicating the user's selection, where 0 is the lowest feedback. Higher values indicate more positive feedback. If no option was selected, the widget returns None.

* For options="thumbs", a return value of 0 indicates thumbs-down, and 1 indicates thumbs-up.
* For options="faces" and options="stars", return values range from 0 (least satisfied) to 4 (most satisfied).

### Examples

#### Display a feedback widget with stars
```python
import streamlit as st

sentiment_mapping = ["one", "two", "three", "four", "five"]
selected = st.feedback("stars")
if selected is not None:
    st.markdown(f"You selected {sentiment_mapping[selected]} star(s).")
```

#### Display a feedback widget with thumbs
```python
import streamlit as st

sentiment_mapping = [":material/thumb_down:", ":material/thumb_up:"]
selected = st.feedback("thumbs")
if selected is not None:
    st.markdown(f"You selected: {sentiment_mapping[selected]}")
```