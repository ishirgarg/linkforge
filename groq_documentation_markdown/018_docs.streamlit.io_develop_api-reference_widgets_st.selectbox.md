Here is the HTML content converted to clean Markdown:

# st.selectbox - Streamlit Docs
#### Documentation

## Navigation
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

## Breadcrumbs
* [Home](/)
* [Develop](/develop)
* [API reference](/develop/api-reference)
* [Input widgets](/develop/api-reference/widgets)
* [st.selectbox](/develop/api-reference/widgets/st.selectbox)

## st.selectbox
Display a select widget.

### Function Signature
```python
st.selectbox(
    label, 
    options, 
    index=0, 
    format_func=None, 
    key=None, 
    help=None, 
    on_change=None, 
    args=None, 
    kwargs=None, 
    placeholder=None, 
    disabled=False, 
    label_visibility="visible", 
    accept_new_options=False, 
    width="stretch"
)
```

### Parameters

* `label` (str): A short label explaining to the user what this select widget is for. The label can optionally contain GitHub-flavored Markdown.
* `options` (Iterable): Labels for the select options in an Iterable.
* `index` (int or None): The index of the preselected option on first render. If None, will initialize empty and return None until the user selects an option. Defaults to 0 (the first option).
* `format_func` (function): Function to modify the display of the options.
* `key` (str or int): An optional string or integer to use as the unique key for the widget.
* `help` (str or None): A tooltip that gets displayed next to the widget label.
* `on_change` (callable): An optional callback invoked when this selectbox's value changes.
* `args` (list or tuple): An optional list or tuple of args to pass to the callback.
* `kwargs` (dict): An optional dict of kwargs to pass to the callback.
* `placeholder` (str or None): A string to display when no options are selected.
* `disabled` (bool): An optional boolean that disables the selectbox if set to True. The default is False.
* `label_visibility` ("visible", "hidden", or "collapsed"): The visibility of the label. The default is "visible".
* `accept_new_options` (bool): Whether the user can add a selection that isn't included in options.
* `width` ("stretch" or int): The width of the selectbox widget.

### Returns
The selected option or None if no option is selected.

### Examples

#### Example 1: Use a basic selectbox widget
```python
import streamlit as st

option = st.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone"),
)

st.write("You selected:", option)
```

#### Example 2: Use a selectbox widget with no initial selection
```python
import streamlit as st

option = st.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone"),
    index=None,
    placeholder="Select contact method...",
)

st.write("You selected:", option)
```

#### Example 3: Let users add a new option
```python
import streamlit as st

option = st.selectbox(
    "Default email",
    ["foo@example.com", "bar@example.com", "baz@example.com"],
    index=None,
    placeholder="Select a saved email or enter a new one",
    accept_new_options=True,
)

st.write("You selected:", option)
```

Note: You can customize the label visibility and disable the selectbox widget using the `label_visibility` and `disabled` parameters.