Here is the clean markdown version of the provided HTML:
### st.date_input - Streamlit Docs

#### Documentation
[Home](/)
[Develop](/develop)
[API reference](/develop/api-reference)
[Input widgets](/develop/api-reference/widgets)
[st.date_input](/develop/api-reference/widgets/st.date_input)

### Search
Search
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

## st.date_input
### Description
Display a date input widget.

The date input widget can be configured to accept a single date or a date range. The first day of the week is determined from the user's locale in their browser.

### Function Signature
```python
st.date_input(
    label, 
    value="today", 
    min_value=None, 
    max_value=None, 
    key=None, 
    help=None, 
    on_change=None, 
    args=None, 
    kwargs=None, 
    format="YYYY/MM/DD", 
    disabled=False, 
    label_visibility="visible", 
    width="stretch"
)
```

### Parameters

* **label**: A short label explaining to the user what this date input is for. The label can optionally contain GitHub-flavored Markdown.
* **value**: The value of this widget when it first renders. This can be one of the following:
	+ "today" (default): The widget initializes with the current date.
	+ A datetime.date or datetime.datetime object: The widget initializes with the given date, ignoring any time if included.
	+ An ISO-formatted date ("YYYY-MM-DD") or datetime ("YYYY-MM-DD hh:mm:ss") string: The widget initializes with the given date, ignoring any time if included.
	+ A list or tuple with up to two of the above: The widget will initialize with the given date interval and return a tuple of the selected interval.
	+ None: The widget initializes with no date and returns None until the user selects a date.
* **min_value**: The minimum selectable date. This can be any of the date types accepted by value, except list or tuple.
* **max_value**: The maximum selectable date. This can be any of the date types accepted by value, except list or tuple.
* **key**: An optional string or integer to use as the unique key for the widget.
* **help**: A tooltip that gets displayed next to the widget label.
* **on_change**: An optional callback invoked when this date_input's value changes.
* **args**: An optional list or tuple of args to pass to the callback.
* **kwargs**: An optional dict of kwargs to pass to the callback.
* **format**: A format string controlling how the interface should display dates. Supports "YYYY/MM/DD" (default), "DD/MM/YYYY", or "MM/DD/YYYY".
* **disabled**: An optional boolean that disables the date input if set to True.
* **label_visibility**: The visibility of the label. The default is "visible".
* **width**: The width of the date input widget. This can be one of the following:
	+ "stretch" (default): The width of the widget matches the width of the parent container.
	+ An integer specifying the width in pixels: The widget has a fixed width.

### Returns
The current value of the date input widget or None if no date has been selected.

### Examples

```python
import datetime
import streamlit as st

d = st.date_input("When's your birthday", datetime.date(2019, 7, 6))
st.write("Your birthday is:", d)
```

```python
import datetime
import streamlit as st

today = datetime.datetime.now()
next_year = today.year + 1
jan_1 = datetime.date(next_year, 1, 1)
dec_31 = datetime.date(next_year, 12, 31)

d = st.date_input(
    "Select your vacation for next year",
    (jan_1, datetime.date(next_year, 1, 7)),
    jan_1,
    dec_31,
    format="MM.DD.YYYY",
)
d
```

```python
import datetime
import streamlit as st

d = st.date_input("When's your birthday", value=None)
st.write("Your birthday is:", d)
```