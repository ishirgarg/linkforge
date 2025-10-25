Here is the HTML document converted to Markdown:

# st.testing.v1.AppTest
## Overview
The AppTest class is a simulated Streamlit app that allows you to test the correctness of displayed elements and outputs.

## Initializing AppTest
AppTest can be initialized using one of three class methods:
* `st.testing.v1.AppTest.from_file`: Create an instance of AppTest from a file.
* `st.testing.v1.AppTest.from_string`: Create an instance of AppTest from a string.
* `st.testing.v1.AppTest.from_function`: Create an instance of AppTest from a function.

## Methods
### run
Run the script from the current state.

### switch_page
Switch to another page of the app.

### get
Get elements or widgets of the specified type.

## Attributes
### secrets
Dictionary of secrets to be used by the simulated app.

### session_state
Session State for the simulated app.

### query_params
Dictionary of query parameters to be used by the simulated app.

## Elements
AppTest provides a range of elements that can be accessed, including:
* `button`: Sequence of all st.button and st.form_submit_button widgets.
* `caption`: Sequence of all st.caption elements.
* `chat_input`: Sequence of all st.chat_input widgets.
* `chat_message`: Sequence of all st.chat_message elements.
* `checkbox`: Sequence of all st.checkbox widgets.
* `code`: Sequence of all st.code elements.
* `color_picker`: Sequence of all st.color_picker widgets.
* `columns`: Sequence of all columns within st.columns elements.
* `dataframe`: Sequence of all st.dataframe elements.
* `date_input`: Sequence of all st.date_input widgets.
* `divider`: Sequence of all st.divider elements.
* `error`: Sequence of all st.error elements.
* `exception`: Sequence of all st.exception elements.
* `expander`: Sequence of all st.expander elements.
* `header`: Sequence of all st.header elements.
* `info`: Sequence of all st.info elements.
* `json`: Sequence of all st.json elements.
* `latex`: Sequence of all st.latex elements.
* `main`: Sequence of elements within the main body of the app.
* `markdown`: Sequence of all st.markdown elements.
* `metric`: Sequence of all st.metric elements.
* `multiselect`: Sequence of all st.multiselect widgets.
* `number_input`: Sequence of all st.number_input widgets.
* `radio`: Sequence of all st.radio widgets.
* `select_slider`: Sequence of all st.select_slider widgets.
* `selectbox`: Sequence of all st.selectbox widgets.
* `sidebar`: Sequence of all elements within st.sidebar.
* `slider`: Sequence of all st.slider widgets.
* `subheader`: Sequence of all st.subheader elements.
* `success`: Sequence of all st.success elements.
* `status`: Sequence of all st.status elements.
* `table`: Sequence of all st.table elements.
* `tabs`: Sequence of all tabs within st.tabs elements.
* `text`: Sequence of all st.text elements.
* `text_area`: Sequence of all st.text_area widgets.
* `text_input`: Sequence of all st.text_input widgets.
* `time_input`: Sequence of all st.time_input widgets.
* `title`: Sequence of all st.title elements.
* `toast`: Sequence of all st.toast elements.
* `toggle`: Sequence of all st.toggle widgets.
* `warning`: Sequence of all st.warning elements.

## Example Use Cases
```python
import streamlit as st

# Create an instance of AppTest
app = st.testing.v1.AppTest.from_file("app.py")

# Run the script
app.run()

# Get elements
buttons = app.button
captions = app.caption
```
Note: This is not an exhaustive list of all possible elements and methods. For more information, please refer to the Streamlit documentation.