Here is the HTML converted to clean Markdown:
### st.select_slider - Streamlit Docs
#### Documentation
##### Search
* [Get started](/get-started)
	+ [Installation](/get-started/installation)
	+ [Fundamentals](/get-started/fundamentals)
	+ [First steps](/get-started/tutorials)
* [Develop](/develop)
	+ [Concepts](/develop/concepts)
	+ [API reference](/develop/api-reference)
		- PAGE ELEMENTS
		- [Write and magic](/develop/api-reference/write-magic)
		- [Text elements](/develop/api-reference/text)
		- [Data elements](/develop/api-reference/data)
		- [Chart elements](/develop/api-reference/charts)
		- [Input widgets](/develop/api-reference/widgets)
			- BUTTONS
			- [st.button](/develop/api-reference/widgets/st.button)
			- [st.download_button](/develop/api-reference/widgets/st.download_button)
			- [st.form_submit_button](/develop/api-reference/execution-flow/st.form_submit_button)
			- [st.link_button](/develop/api-reference/widgets/st.link_button)
			- [st.page_link](/develop/api-reference/widgets/st.page_link)
			- SELECTIONS
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
			- NUMERIC
			- [st.number_input](/develop/api-reference/widgets/st.number_input)
			- [st.slider](/develop/api-reference/widgets/st.slider)
			- DATE AND TIME
			- [st.date_input](/develop/api-reference/widgets/st.date_input)
			- [st.time_input](/develop/api-reference/widgets/st.time_input)
			- TEXT
			- [st.chat_input](/develop/api-reference/chat/st.chat_input)
			- [st.text_area](/develop/api-reference/widgets/st.text_area)
			- [st.text_input](/develop/api-reference/widgets/st.text_input)
			- MEDIA AND FILES
			- [st.audio_input](/develop/api-reference/widgets/st.audio_input)
			- [st.camera_input](/develop/api-reference/widgets/st.camera_input)
			- [st.data_editor](/develop/api-reference/data/st.data_editor)
			- [st.file_uploader](/develop/api-reference/widgets/st.file_uploader)
		- [Media elements](/develop/api-reference/media)
		- [Layouts and containers](/develop/api-reference/layout)
		- [Chat elements](/develop/api-reference/chat)
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
* [Deploy](/deploy)
	+ [Concepts](/deploy/concepts)
	+ [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
	+ [Snowflake](/deploy/snowflake)
	+ [Other platforms](/deploy/tutorials)
* [Knowledge base](/knowledge-base)
	+ [FAQ](/knowledge-base/using-streamlit)
	+ [Installing dependencies](/knowledge-base/dependencies)
	+ [Deployment issues](/knowledge-base/deploy)

Note that I've removed the unnecessary HTML tags, images, and icons, and formatted the text using Markdown syntax. I've also removed the `_add_` and `_remove_` comments, as they seem to be internal notes and not relevant to the documentation. Let me know if you need any further assistance!

## st.select_slider
### Description
Display a slider widget to select items from a list. This also allows you to render a range slider by passing a two-element tuple or list as the value.

The difference between `st.select_slider` and `st.slider` is that `select_slider` accepts any datatype and takes an iterable set of options, while `st.slider` only accepts numerical or date/time data and takes a range as input.

### Function signature
```python
st.select_slider(
    label, 
    options=(), 
    value=None, 
    format_func=None, 
    key=None, 
    help=None, 
    on_change=None, 
    args=None, 
    kwargs=None, 
    disabled=False, 
    label_visibility="visible", 
    width="stretch"
)
```
### Parameters

* **label**: A short label explaining to the user what this slider is for. The label can optionally contain GitHub-flavored Markdown.
* **options**: Labels for the select options in an Iterable.
* **value**: The value of the slider when it first renders. If a tuple/list of two values is passed here, then a range slider with those lower and upper bounds is rendered.
* **format_func**: Function to modify the display of the labels from the options.
* **key**: An optional string or integer to use as the unique key for the widget.
* **help**: A tooltip that gets displayed next to the widget label.
* **on_change**: An optional callback invoked when this select_slider's value changes.
* **args**: An optional list or tuple of args to pass to the callback.
* **kwargs**: An optional dict of kwargs to pass to the callback.
* **disabled**: An optional boolean that disables the select slider if set to True.
* **label_visibility**: The visibility of the label.
* **width**: The width of the slider widget.

### Returns
The current value of the slider widget. The return type will match the data type of the value parameter.

### Examples
```python
import streamlit as st

color = st.select_slider(
    "Select a color of the rainbow",
    options=["red", "orange", "yellow", "green", "blue", "indigo", "violet"],
)
st.write("My favorite color is", color)

start_color, end_color = st.select_slider(
    "Select a range of color wavelength",
    options=["red", "orange", "yellow", "green", "blue", "indigo", "violet"],
    value=("red", "blue"),
)
st.write("You selected wavelengths between", start_color, "and", end_color)
```