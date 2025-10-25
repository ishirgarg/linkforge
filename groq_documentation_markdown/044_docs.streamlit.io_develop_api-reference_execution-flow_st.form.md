Here is the HTML content converted to clean Markdown:

# st.form - Streamlit Docs
![Logo](/logo.svg)

## Documentation
### Search
Search

### Menu
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
		- [Media elements](/develop/api-reference/media)
		- [Layouts and containers](/develop/api-reference/layout)
		- [Chat elements](/develop/api-reference/chat)
		- [Status elements](/develop/api-reference/status)
		- [Third-party components](https://streamlit.io/components)
		- APPLICATION LOGIC
		- [Authentication and user info](/develop/api-reference/user)
		- [Navigation and pages](/develop/api-reference/navigation)
		- [Execution flow](/develop/api-reference/execution-flow)
			- [st.dialog](/develop/api-reference/execution-flow/st.dialog)
			- [st.form](/develop/api-reference/execution-flow/st.form)
			- [st.form_submit_button](/develop/api-reference/execution-flow/st.form_submit_button)
			- [st.fragment](/develop/api-reference/execution-flow/st.fragment)
			- [st.rerun](/develop/api-reference/execution-flow/st.rerun)
			- [st.stop](/develop/api-reference/execution-flow/st.stop)
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

### Breadcrumbs
* [Home](/)
* [Develop](/develop)
* [API reference](/develop/api-reference)
* [Execution flow](/develop/api-reference/execution-flow)
* [st.form](/develop/api-reference/execution-flow/st.form)

### Tip
This page only contains information on the `st.forms` API. For a deeper dive into creating and using forms within Streamlit apps, read our guide on [Using forms](/develop/concepts/architecture/forms).

## st.form
#### Streamlit Version: 1.50.0, 1.49.0, 1.48.0, 1.47.0, 1.46.0, 1.45.0, 1.44.0, 1.43.0, 1.42.0, 1.41.0, 1.40.0, 1.39.0, 1.38.0, 1.37.0, 1.36.0, 1.35.0, 1.34.0, 1.33.0, 1.32.0, 1.31.0, 1.30.0, 1.29.0, 1.28.0, 1.27.0, 1.26.0, 1.25.0, 1.24.0, 1.23.0, 1.22.0

Create a form that batches elements together with a "Submit" button.

A form is a container that visually groups other elements and widgets together, and contains a Submit button. When the form's Submit button is pressed, all widget values inside the form will be sent to Streamlit in a batch.

To add elements to a form object, you can use with notation (preferred) or just call methods directly on the form. 

### Constraints
* Every form must contain a `st.form_submit_button`.
* `st.button` and `st.download_button` cannot be added to a form.
* Forms can appear anywhere in your app (sidebar, columns, etc), but they cannot be embedded inside other forms.
* Within a form, the only widget that can have a callback function is `st.form_submit_button`.

### Function Signature
```python
st.form(key, clear_on_submit=False, *, enter_to_submit=True, border=True, width="stretch", height="content")
```

### Parameters
* `key` (str): A string that identifies the form. Each form must have its own key.
* `clear_on_submit` (bool): If True, all widgets inside the form will be reset to their default values after the user presses the Submit button.
* `enter_to_submit` (bool): Whether to submit the form when a user presses Enter while interacting with a widget inside the form.
* `border` (bool): Whether to show a border around the form. Defaults to True.
* `width` ("stretch", "content", or int): The width of the form container.
* `height` ("content", "stretch", or int): The height of the form container.

### Examples
#### Inserting elements using with notation
```python
import streamlit as st

with st.form("my_form"):
    st.write("Inside the form")
    slider_val = st.slider("Form slider")
    checkbox_val = st.checkbox("Form checkbox")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("slider", slider_val, "checkbox", checkbox_val)
st.write("Outside the form")
```

#### Inserting elements out of order
```python
import streamlit as st

form = st.form("my_form")
form.slider("Inside the form")
st.slider("Outside the form")

# Now add a submit button to the form:
form.form_submit_button("Submit")
```