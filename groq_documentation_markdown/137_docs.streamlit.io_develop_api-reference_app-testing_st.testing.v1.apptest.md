Here is the HTML content converted to clean markdown:

# st.testing.v1.AppTest
## Overview
A simulated Streamlit app to check the correctness of displayed elements and outputs.

An instance of AppTest simulates a running Streamlit app. This class provides methods to set up, manipulate, and inspect the app contents via API instead of a browser UI. It can be used to write automated tests of an app in various scenarios. These can then be run using a tool like pytest.

## Initialization
AppTest can be initialized by one of three class methods:
* `st.testing.v1.AppTest.from_file` (recommended)
* `st.testing.v1.AppTest.from_string`
* `st.testing.v1.AppTest.from_function`

## Methods
### run()
Run the script from the current state.
```python
AppTest.run(*, timeout=None)
```
### switch_page()
Switch to another page of the app.
```python
AppTest.switch_page(page_path)
```
### get()
Get elements or widgets of the specified type.
```python
AppTest.get(element_type)
```
## Attributes
### secrets
Dictionary of secrets to be used the simulated app.
### session_state
Session State for the simulated app.
### query_params
Dictionary of query parameters to be used by the simluated app.

## Element Properties
The main value of `AppTest` is providing an API to programmatically inspect and interact with the elements and widgets produced by a running Streamlit app. The following properties are available:
* `button`
* `caption`
* `chat_input`
* `chat_message`
* `checkbox`
* `code`
* `color_picker`
* `columns`
* `dataframe`
* `date_input`
* `divider`
* `error`
* `exception`
* `expander`
* `header`
* `info`
* `json`
* `latex`
* `main`
* `markdown`
* `metric`
* `multiselect`
* `number_input`
* `radio`
* `select_slider`
* `selectbox`
* `sidebar`
* `slider`
* `subheader`
* `success`
* `status`
* `table`
* `tabs`
* `text`
* `text_area`
* `text_input`
* `time_input`
* `title`
* `toast`
* `toggle`
* `warning`

Each property returns a sequence of elements or widgets of the specified type. Individual elements can be accessed from the sequence by index (order on the page) or key.