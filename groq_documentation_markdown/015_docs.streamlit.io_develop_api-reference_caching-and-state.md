Here is the HTML converted to clean Markdown:

# Caching and state - Streamlit Docs

## Documentation
### Search

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
		- [Caching and state](/develop/api-reference/caching-and-state)
			- SERVER
			- [st.cache_data](/develop/api-reference/caching-and-state/st.cache_data)
			- [st.cache_resource](/develop/api-reference/caching-and-state/st.cache_resource)
			- [st.session_state](/develop/api-reference/caching-and-state/st.session_state)
			- BROWSER
			- [st.context](/develop/api-reference/caching-and-state/st.context)
			- [st.query_params](/develop/api-reference/caching-and-state/st.query_params)
			- [st.experimental_get_query_params](/develop/api-reference/caching-and-state/st.experimental_get_query_params)
			- [st.experimental_set_query_params](/develop/api-reference/caching-and-state/st.experimental_set_query_params)
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

[Home](/)/
[Develop](/develop)/
[API reference](/develop/api-reference)/
[Caching and state](/develop/api-reference/caching-and-state)

## Caching and state
Optimize performance and add statefulness to your app!

### Caching
Streamlit provides powerful cache primitives for data and global resources. They allow your app to stay performant even when loading data from the web, manipulating large datasets, or performing expensive computations.

#### Cache data
Function decorator to cache functions that return data (e.g. dataframe transforms, database queries, ML inference).
```python
@st.cache_data
def long_function(param1, param2):
    # Perform expensive computation here or
    # fetch data from the web here
    return data
```

#### Cache resource
Function decorator to cache functions that return global resources (e.g. database connections, ML models).
```python
@st.cache_resource
def init_model():
    # Return a global resource here
    return pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
```

### Browser and server state
Streamlit re-executes your script with each user interaction. Widgets have built-in statefulness between reruns, but Session State lets you do more!

#### Context
`st.context` provides a read-only interface to access cookies, headers, locale, and other browser-session information.
```python
st.context.cookies
st.context.headers
```

#### Session State
Save data between reruns and across pages.
```python
st.session_state["foo"] = "bar"
```

#### Query parameters
Get, set, or clear the query parameters that are shown in the browser's URL bar.
```python
st.query_params[key] = value
st.query_params.clear()
```

### Deprecated commands
#### Get query parameters
Get query parameters that are shown in the browser's URL bar.
```python
param_dict = st.experimental_get_query_params()
```

#### Set query parameters
Set query parameters that are shown in the browser's URL bar.
```python
st.experimental_set_query_params({"show_all": True, "selected": ["asia", "america"]})
```

Still have questions? Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.