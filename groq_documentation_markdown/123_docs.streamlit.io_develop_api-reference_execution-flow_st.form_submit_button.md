Here is the clean markdown version of the provided HTML:

# st.form_submit_button - Streamlit Docs
![logo](/logo.svg)

## Documentation

### Search
Search

### Navigation
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
* [st.form_submit_button](/develop/api-reference/execution-flow/st.form_submit_button)

### st.form_submit_button
#### Description
Display a form submit button. When this button is clicked, all widget values inside the form will be sent from the user's browser to your Streamlit server in a batch.

#### Important Notes
* Every form must have at least one `st.form_submit_button`.
* An `st.form_submit_button` cannot exist outside of a form.
* For more information about forms, check out the [docs](https://docs.streamlit.io/develop/concepts/architecture/forms).

#### Function Signature
```python
st.form_submit_button(
    label="Submit", 
    help=None, 
    on_click=None, 
    args=None, 
    kwargs=None, 
    key=None, 
    type="secondary", 
    icon=None, 
    disabled=False, 
    use_container_width=None, 
    width="content"
)
```

#### Parameters
* **label** (str): A short label explaining to the user what this button is for. This defaults to "Submit". The label can optionally contain GitHub-flavored Markdown.
* **help** (str or None): A tooltip that gets displayed when the button is hovered over. If this is None (default), no tooltip is displayed.
* **on_click** (callable): An optional callback invoked when this button is clicked.
* **args** (list or tuple): An optional list or tuple of args to pass to the callback.
* **kwargs** (dict): An optional dict of kwargs to pass to the callback.
* **key** (str or int): An optional string or integer to use as the unique key for the widget.
* **type** ("primary", "secondary", or "tertiary"): An optional string that specifies the button type.
* **icon** (str or None): An optional emoji or icon to display next to the button label.
* **disabled** (bool): Whether to disable the button. If this is False (default), the user can interact with the button.
* **width** ("content", "stretch", or int): The width of the button.

#### Returns
* (bool): True if the button was clicked.

#### Example Use Cases
* Create a simple form with a submit button: 
```python
with st.form("my_form"):
    st.text_input("Name")
    st.form_submit_button("Submit")
```