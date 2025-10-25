Here is the Markdown version of the provided HTML:
### st.slider - Streamlit Docs
#### Documentation
[Search](/)
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
### Navigation
* [Home](/)
* [Develop](/develop)
* [API reference](/develop/api-reference)
* [Input widgets](/develop/api-reference/widgets)
* [st.slider](/develop/api-reference/widgets/st.slider)

## st.slider
Display a slider widget.

This supports int, float, date, time, and datetime types.

This also allows you to render a range slider by passing a two-element tuple or list as the value.

The difference between st.slider and st.select_slider is that slider only accepts numerical or date/time data and takes a range as input, while select_slider accepts any datatype and takes an iterable set of options.

### Note
Integer values exceeding +/- (1<<53) - 1 cannot be accurately stored or returned by the widget due to serialization constraints between the Python server and JavaScript client. You must handle such numbers as floats, leading to a loss in precision.

### Function signature
```python
st.slider(
    label, 
    min_value=None, 
    max_value=None, 
    value=None, 
    step=None, 
    format=None, 
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

* **label** (str): A short label explaining to the user what this slider is for.
* **min_value** (a supported type or None): The minimum permitted value.
* **max_value** (a supported type or None): The maximum permitted value.
* **value** (a supported type or a tuple/list of supported types or None): The value of the slider when it first renders.
* **step** (int, float, timedelta, or None): The stepping interval.
* **format** (str or None): A printf-style format string controlling how the interface should display numbers.
* **key** (str or int): An optional string or integer to use as the unique key for the widget.
* **help** (str or None): A tooltip that gets displayed next to the widget label.
* **on_change** (callable): An optional callback invoked when this slider's value changes.
* **args** (list or tuple): An optional list or tuple of args to pass to the callback.
* **kwargs** (dict): An optional dict of kwargs to pass to the callback.
* **disabled** (bool): An optional boolean that disables the slider if set to True.
* **label_visibility** ("visible", "hidden", or "collapsed"): The visibility of the label.
* **width** ("stretch" or int): The width of the slider widget.

### Returns
(int/float/date/time/datetime or tuple of int/float/date/time/datetime): The current value of the slider widget.

### Examples

```python
import streamlit as st

age = st.slider("How old are you?", 0, 130, 25)
st.write("I'm ", age, "years old")

values = st.slider("Select a range of values", 0.0, 100.0, (25.0, 75.0))
st.write("Values:", values)

appointment = st.slider(
    "Schedule your appointment:", value=(time(11, 30), time(12, 45))
)
st.write("You're scheduled for:", appointment)

start_time = st.slider(
    "When do you start?",
    value=datetime(2020, 1, 1, 9, 30),
    format="MM/DD/YY - hh:mm",
)
st.write("Start time:", start_time)
```