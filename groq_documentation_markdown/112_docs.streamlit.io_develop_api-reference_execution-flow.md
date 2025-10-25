Here is the HTML content converted to clean markdown:

### Execution flow - Streamlit Docs
#### Documentation

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

### Links
* [Home](/)
* [Develop](/develop)
* [API reference](/develop/api-reference)
* [Execution flow](/develop/api-reference/execution-flow)

# Execution flow
## Change execution
By default, Streamlit apps execute the script entirely, but we allow some functionality to handle control flow in your applications.

### Modal dialog
Insert a modal dialog that can rerun independently from the rest of the script.
```python
@st.dialog("Sign up")
def email_form():
    name = st.text_input("Name")
    email = st.text_input("Email")
```

### Fragments
Define a fragment to rerun independently from the rest of the script.
```python
@st.fragment(run_every="10s")
def fragment():
    df = get_data()
    st.line_chart(df)
```

### Rerun script
Rerun the script immediately.
```python
st.rerun()
```

### Stop execution
Stops execution immediately.
```python
st.stop()
```

## Group multiple widgets
By default, Streamlit reruns your script every time a user interacts with your app. However, sometimes it's a better user experience to wait until a group of related widgets is filled before actually rerunning the script. That's what `st.form` is for!

### Forms
Create a form that batches elements together with a “Submit" button.
```python
with st.form(key='my_form'):
    name = st.text_input("Name")
    email = st.text_input("Email")
    st.form_submit_button("Sign up")
```

### Form submit button
Display a form submit button.
```python
with st.form(key='my_form'):
    name = st.text_input("Name")
    email = st.text_input("Email")
    st.form_submit_button("Sign up")
```

### Third-party components
These are featured components created by our lovely community. For more examples and inspiration, check out our [Components Gallery](https://streamlit.io/components) and [Streamlit Extras](https://extras.streamlit.app)!

#### Autorefresh
Force a refresh without tying up a script. Created by [@kmcgrady](https://github.com/kmcgrady).
```python
from streamlit_autorefresh import st_autorefresh
st_autorefresh(interval=2000, limit=100, key="fizzbuzzcounter")
```

#### Pydantic
Auto-generate Streamlit UI from Pydantic Models and Dataclasses. Created by [@lukasmasuch](https://github.com/lukasmasuch).
```python
import streamlit_pydantic as sp
sp.pydantic_form(key="my_form", model=ExampleModel)
```

#### Streamlit Pages
An experimental version of Streamlit Multi-Page Apps. Created by [@blackary](https://github.com/blackary).
```python
from st_pages import Page, show_pages, add_page_title
show_pages([
    Page("streamlit_app.py", "Home", "🏠"),
    Page("other_pages/page2.py", "Page 2", ":books:"),
])
```

Still have questions? Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts. 

Home | Contact Us | Community 

GitHub | YouTube | Twitter | LinkedIn | Newsletter 

 Snowflake Inc. | Cookie policy