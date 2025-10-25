Here is the HTML converted to clean markdown:

# Streamlit Docs
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
		- [Write and magic](/develop/api-reference/write-magic)
		- [Text elements](/develop/api-reference/text)
		- [Data elements](/develop/api-reference/data)
		- [Chart elements](/develop/api-reference/charts)
		- [Input widgets](/develop/api-reference/widgets)
		- [Media elements](/develop/api-reference/media)
		- [Layouts and containers](/develop/api-reference/layout)
			- [st.columns](/develop/api-reference/layout/st.columns)
			- [st.container](/develop/api-reference/layout/st.container)
			- [st.dialog](/develop/api-reference/execution-flow/st.dialog)
			- [st.empty](/develop/api-reference/layout/st.empty)
			- [st.expander](/develop/api-reference/layout/st.expander)
			- [st.form](/develop/api-reference/execution-flow/st.form)
			- [st.popover](/develop/api-reference/layout/st.popover)
			- [st.sidebar](/develop/api-reference/layout/st.sidebar)
			- [st.tabs](/develop/api-reference/layout/st.tabs)
		- [Chat elements](/develop/api-reference/chat)
		- [Status elements](/develop/api-reference/status)
		- [Third-party components](https://streamlit.io/components)
		- [Authentication and user info](/develop/api-reference/user)
		- [Navigation and pages](/develop/api-reference/navigation)
		- [Execution flow](/develop/api-reference/execution-flow)
		- [Caching and state](/develop/api-reference/caching-and-state)
		- [Connections and secrets](/develop/api-reference/connections)
		- [Custom components](/develop/api-reference/custom-components)
		- [Configuration](/develop/api-reference/configuration)
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
* [Layouts and containers](/develop/api-reference/layout)
* [st.expander](/develop/api-reference/layout/st.expander)

## st.expander
### Description
Insert a multi-element container that can be expanded/collapsed.

### Parameters
* `label` (str): A string to use as the header for the expander. The label can optionally contain GitHub-flavored Markdown.
* `expanded` (bool): If True, initializes the expander in "expanded" state. Defaults to False (collapsed).
* `icon` (str, None): An optional emoji or icon to display next to the expander label.
* `width` ("stretch" or int): The width of the expander container.

### Notes
* All content within the expander is computed and sent to the frontend, even if the expander is closed.
* To follow best design practices and maintain a good appearance on all screen sizes, don't nest expanders.

### Examples
#### Using the with notation
```python
import streamlit as st

st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})

with st.expander("See explanation"):
    st.write('''
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
    ''')
    st.image("https://static.streamlit.io/examples/dice.jpg")
```

#### Calling methods directly on the returned object
```python
import streamlit as st

st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})

expander = st.expander("See explanation")
expander.write('''
    The chart above shows some numbers I picked for you.
    I rolled actual dice for these, so they're *guaranteed* to
    be random.
''')
expander.image("https://static.streamlit.io/examples/dice.jpg")
```