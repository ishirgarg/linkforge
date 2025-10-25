Here is the HTML content converted to clean Markdown:

# st.segmented_control - Streamlit Docs

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
			- [BUTTONS](#)
				+ [st.button](/develop/api-reference/widgets/st.button)
				+ [st.download_button](/develop/api-reference/widgets/st.download_button)
				+ [st.form_submit_button](/develop/api-reference/execution-flow/st.form_submit_button)
				+ [st.link_button](/develop/api-reference/widgets/st.link_button)
				+ [st.page_link](/develop/api-reference/widgets/st.page_link)
			- [SELECTIONS](#)
				+ [st.checkbox](/develop/api-reference/widgets/st.checkbox)
				+ [st.color_picker](/develop/api-reference/widgets/st.color_picker)
				+ [st.feedback](/develop/api-reference/widgets/st.feedback)
				+ [st.multiselect](/develop/api-reference/widgets/st.multiselect)
				+ [st.pills](/develop/api-reference/widgets/st.pills)
				+ [st.radio](/develop/api-reference/widgets/st radio)
				+ [st.segmented_control](/develop/api-reference/widgets/st.segmented_control)
				+ [st.selectbox](/develop/api-reference/widgets/st.selectbox)
				+ [st.select_slider](/develop/api-reference/widgets/st.select_slider)
				+ [st.toggle](/develop/api-reference/widgets/st.toggle)
			- [NUMERIC](#)
				+ [st.number_input](/develop/api-reference/widgets/st.number_input)
				+ [st.slider](/develop/api-reference/widgets/st.slider)
			- [DATE AND TIME](#)
				+ [st.date_input](/develop/api-reference/widgets/st.date_input)
				+ [st.time_input](/develop/api-reference/widgets/st.time_input)
			- [TEXT](#)
				+ [st.chat_input](/develop/api-reference/chat/st.chat_input)
				+ [st.text_area](/develop/api-reference/widgets/st.text_area)
				+ [st.text_input](/develop/api-reference/widgets/st.text_input)
			- [MEDIA AND FILES](#)
				+ [st.audio_input](/develop/api-reference/widgets/st.audio_input)
				+ [st.camera_input](/develop/api-reference/widgets/st.camera_input)
				+ [st.data_editor](/develop/api-reference/data/st.data_editor)
				+ [st.file_uploader](/develop/api-reference/widgets/st.file_uploader)
		- [Media elements](/develop/api-reference/media)
		- [Layouts and containers](/develop/api-reference/layout)
		- [Chat elements](/develop/api-reference/chat)
		- [Status elements](/develop/api-reference/status)
		- [Third-party components](https://streamlit.io/components)
		- [APPLICATION LOGIC](#)
			+ [Authentication and user info](/develop/api-reference/user)
			+ [Navigation and pages](/develop/api-reference/navigation)
			+ [Execution flow](/develop/api-reference/execution-flow)
			+ [Caching and state](/develop/api-reference/caching-and-state)
			+ [Connections and secrets](/develop/api-reference/connections)
			+ [Custom components](/develop/api-reference/custom-components)
			+ [Configuration](/develop/api-reference/configuration)
		- [TOOLS](#)
			+ [App testing](/develop/api-reference/app-testing)
			+ [Command line](/develop/api-reference/cli)
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

Note that I removed the unnecessary HTML tags and converted the content to Markdown format. I also removed the `_add_` and `_remove_` links as they seemed to be internal links that are not relevant to the Markdown content. Let me know if you need any further assistance!

Here is the content rewritten in clean Markdown:

## st.segmented_control
### Streamlit Version
1.50.0, 1.49.0, 1.48.0, 1.47.0, 1.46.0, 1.45.0, 1.44.0, 1.43.0, 1.42.0, 1.41.0, 1.40.0, 1.39.0, 1.38.0, 1.37.0, 1.36.0, 1.35.0, 1.34.0, 1.33.0, 1.32.0, 1.31.0, 1.30.0, 1.29.0, 1.28.0, 1.27.0, 1.26.0, 1.25.0, 1.24.0, 1.23.0, 1.22.0

Display a segmented control widget.

A segmented control widget is a linear set of segments where each of the passed options functions like a toggle button.

### Function Signature
```python
st.segmented_control(
    label, 
    options, 
    *, 
    selection_mode="single", 
    default=None, 
    format_func=None, 
    key=None, 
    help=None, 
    on_change=None, 
    args=None, 
    kwargs=None, 
    disabled=False, 
    label_visibility="visible", 
    width="content"
)
```

### Parameters

* **label** (str): A short label explaining to the user what this widget is for. The label can optionally contain GitHub-flavored Markdown.
* **options** (Iterable of V): Labels for the select options in an Iterable.
* **selection_mode** ("single" or "multi"): The selection mode for the widget.
* **default** (Iterable of V, V, or None): The value of the widget when it first renders.
* **format_func** (function): Function to modify the display of the options.
* **key** (str or int): An optional string or integer to use as the unique key for the widget.
* **help** (str or None): A tooltip that gets displayed next to the widget label.
* **on_change** (callable): An optional callback invoked when this widget's value changes.
* **args** (list or tuple): An optional list or tuple of args to pass to the callback.
* **kwargs** (dict): An optional dict of kwargs to pass to the callback.
* **disabled** (bool): An optional boolean that disables the widget if set to True.
* **label_visibility** ("visible", "hidden", or "collapsed"): The visibility of the label.
* **width** ("content", "stretch", or int): The width of the segmented control widget.

### Returns
(list of V, V, or None): If the selection_mode is multi, this is a list of selected options or an empty list. If the selection_mode is "single", this is a selected option or None.

### Examples

#### Example 1: Multi-select segmented control
Display a multi-select segmented control widget, and show the selection:
```python
import streamlit as st

options = ["North", "East", "South", "West"]
selection = st.segmented_control("Directions", options, selection_mode="multi")
st.markdown(f"Your selected options: {selection}.")
```

#### Example 2: Single-select segmented control with icons
Display a single-select segmented control widget with icons:
```python
import streamlit as st

option_map = {
    0: ":material/add:",
    1: ":material/zoom_in:",
    2: ":material/zoom_out:",
    3: ":material/zoom_out_map:",
}
selection = st.segmented_control(
    "Tool",
    options=option_map.keys(),
    format_func=lambda option: option_map[option],
    selection_mode="single",
)
st.write(
    "Your selected option: "
    f"{None if selection is None else option_map[selection]}"
)
```

### Still have questions?
Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts. 

* [Home](/)
* [Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)
* [Community](https://discuss.streamlit.io)

[GitHub](https://github.com/streamlit) | [YouTube](https://www.youtube.com/channel/UC3LD42rjj-Owtxsa6PwGU5Q) | [Twitter](https://twitter.com/streamlit) | [LinkedIn](https://www.linkedin.com/company/streamlit) | [Newsletter](https://info.snowflake.com/streamlit-newsletter-sign-up.html)

&copy; 2025 Snowflake Inc. [Cookie policy](https://www.streamlit.io/cookie-policy)