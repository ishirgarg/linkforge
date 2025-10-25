Here is the clean markdown version of the provided HTML:

### st.multiselect - Streamlit Docs
#### Documentation

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

### Links
* [Home](/)
* [Develop](/develop)
* [API reference](/develop/api-reference)
* [Input widgets](/develop/api-reference/widgets)
* [st.multiselect](/develop/api-reference/widgets/st.multiselect)

### st.multiselect
#### Display a Multiselect Widget

The multiselect widget starts as empty.

##### Function Signature
```python
st.multiselect(
    label, 
    options, 
    default=None, 
    format_func=special_internal_function, 
    key=None, 
    help=None, 
    on_change=None, 
    args=None, 
    kwargs=None, 
    max_selections=None, 
    placeholder=None, 
    disabled=False, 
    label_visibility="visible", 
    accept_new_options=False, 
    width="stretch"
)
```

##### Parameters

* **label** (str): A short label explaining to the user what this select widget is for. The label can optionally contain GitHub-flavored Markdown.
* **options** (Iterable): Labels for the select options in an Iterable.
* **default** (Iterable of V, V, or None): List of default values. Can also be a single value.
* **format_func** (function): Function to modify the display of the options.
* **key** (str or int): An optional string or integer to use as the unique key for the widget.
* **help** (str or None): A tooltip that gets displayed next to the widget label.
* **on_change** (callable): An optional callback invoked when this widget's value changes.
* **args** (list or tuple): An optional list or tuple of args to pass to the callback.
* **kwargs** (dict): An optional dict of kwargs to pass to the callback.
* **max_selections** (int): The max selections that can be selected at a time.
* **placeholder** (str or None): A string to display when no options are selected.
* **disabled** (bool): An optional boolean that disables the multiselect widget if set to True.
* **label_visibility** ("visible", "hidden", or "collapsed"): The visibility of the label.
* **accept_new_options** (bool): Whether the user can add selections that aren't included in options.
* **width** ("stretch" or int): The width of the multiselect widget.

##### Returns

* (list): A list with the selected options

#### Examples

##### Example 1: Use a Basic Multiselect Widget

You can declare one or more initial selections with the default parameter.
```python
import streamlit as st

options = st.multiselect(
    "What are your favorite colors?",
    ["Green", "Yellow", "Red", "Blue"],
    default=["Yellow", "Red"],
)

st.write("You selected:", options)
```

##### Example 2: Let Users Add New Options

To allow users to enter and select new options that aren't included in the options list, use the `accept_new_options` parameter. To prevent users from adding an unbounded number of new options, use the `max_selections` parameter.
```python
import streamlit as st

options = st.multiselect(
    "What are your favorite cat names?",
    ["Jellybeans", "Fish Biscuit", "Madam President"],
    max_selections=5,
    accept_new_options=True,
)

st.write("You selected:", options)
```