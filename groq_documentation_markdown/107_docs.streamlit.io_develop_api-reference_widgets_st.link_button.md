Here is the converted HTML to clean markdown:
### Documentation
#### Search
Search

* [Get started](/get-started)
	+ [Installation](/get-started/installation)
	+ [Fundamentals](/get-started/fundamentals)
	+ [First steps](/get-started/tutorials)
* [Develop](/develop)
	+ [Concepts](/develop/concepts)
	+ [API reference](/develop/api-reference)
		- [PAGE ELEMENTS](#)
		- [Write and magic](/develop/api-reference/write-magic)
		- [Text elements](/develop/api-reference/text)
		- [Data elements](/develop/api-reference/data)
		- [Chart elements](/develop/api-reference/charts)
		- [Input widgets](/develop/api-reference/widgets)
			- [BUTTONS](#)
			- [st.button](/develop/api-reference/widgets/st.button)
			- [st.download_button](/develop/api-reference/widgets/st.download_button)
			- [st.form_submit_button](/develop/api-reference/execution-flow/st.form_submit_button)
			- [st.link_button](/develop/api-reference/widgets/st.link_button)
			- [st.page_link](/develop/api-reference/widgets/st.page_link)
			- [SELECTIONS](#)
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
			- [NUMERIC](#)
			- [st.number_input](/develop/api-reference/widgets/st.number_input)
			- [st.slider](/develop/api-reference/widgets/st.slider)
			- [DATE AND TIME](#)
			- [st.date_input](/develop/api-reference/widgets/st.date_input)
			- [st.time_input](/develop/api-reference/widgets/st.time_input)
			- [TEXT](#)
			- [st.chat_input](/develop/api-reference/chat/st.chat_input)
			- [st.text_area](/develop/api-reference/widgets/st.text_area)
			- [st.text_input](/develop/api-reference/widgets/st.text_input)
			- [MEDIA AND FILES](#)
			- [st.audio_input](/develop/api-reference/widgets/st.audio_input)
			- [st.camera_input](/develop/api-reference/widgets/st.camera_input)
			- [st.data_editor](/develop/api-reference/data/st.data_editor)
			- [st.file_uploader](/develop/api-reference/widgets/st.file_uploader)
		- [Media elements](/develop/api-reference/media)
		- [Layouts and containers](/develop/api-reference/layout)
		- [Chat elements](/develop/api-reference/chat)
		- [Status elements](/develop/api-reference/status)
		- [Third-party components](https://streamlit.io/components)
		- [APPLICATION LOGIC](#)
		- [Authentication and user info](/develop/api-reference/user)
		- [Navigation and pages](/develop/api-reference/navigation)
		- [Execution flow](/develop/api-reference/execution-flow)
		- [Caching and state](/develop/api-reference/caching-and-state)
		- [Connections and secrets](/develop/api-reference/connections)
		- [Custom components](/develop/api-reference/custom-components)
		- [Configuration](/develop/api-reference/configuration)
		- [TOOLS](#)
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
* [st.link_button](/develop/api-reference/widgets/st.link_button)

## st.link_button
### Display a Link Button Element

The `st.link_button` function displays a link button element. When clicked, a new tab will be opened to the specified URL. This will create a new session for the user if directed within the app.

### Function Signature
```python
st.link_button(label, url, *, help=None, type="secondary", icon=None, disabled=False, use_container_width=None, width="content")
```
### Parameters

* `label` (str): A short label explaining to the user what this button is for. The label can optionally contain GitHub-flavored Markdown.
* `url` (str): The URL to be opened on user click.
* `help` (str or None): A tooltip that gets displayed when the button is hovered over.
* `type` ("primary", "secondary", or "tertiary"): An optional string that specifies the button type.
	+ "primary": The button's background is the app's primary color for additional emphasis.
	+ "secondary" (default): The button's background coordinates with the app's background color for normal emphasis.
	+ "tertiary": The button is plain text without a border or background for subtlety.
* `icon` (str or None): An optional emoji or icon to display next to the button label.
* `disabled` (bool): An optional boolean that disables the link button if set to True.
* `width` ("content", "stretch", or int): The width of the link button.

### Example
```python
import streamlit as st

st.link_button("Go to gallery", "https://streamlit.io/gallery")
```
### Notes

* The `use_container_width` parameter is deprecated and will be removed in a future release. For `use_container_width=True`, use `width="stretch"`. For `use_container_width=False`, use `width="content"`.