Here is the HTML content converted to clean Markdown:

### Streamlit Documentation
#### Navigation
* [Get Started](/get-started)
	+ [Installation](/get-started/installation)
	+ [Fundamentals](/get-started/fundamentals)
	+ [First Steps](/get-started/tutorials)
* [Develop](/develop)
	+ [Concepts](/develop/concepts)
	+ [API Reference](/develop/api-reference)
		- [Page Elements](#)
			- [Write and Magic](/develop/api-reference/write-magic)
			- [Text Elements](/develop/api-reference/text)
			- [Data Elements](/develop/api-reference/data)
			- [Chart Elements](/develop/api-reference/charts)
			- [Input Widgets](/develop/api-reference/widgets)
			- [Media Elements](/develop/api-reference/media)
			- [Layouts and Containers](/develop/api-reference/layout)
			- [Chat Elements](/develop/api-reference/chat)
			- [Status Elements](/develop/api-reference/status)
			- [Third-Party Components](https://streamlit.io/components)
		- [Application Logic](#)
			- [Authentication and User Info](/develop/api-reference/user)
			- [Navigation and Pages](/develop/api-reference/navigation)
			- [Execution Flow](/develop/api-reference/execution-flow)
			- [Caching and State](/develop/api-reference/caching-and-state)
				- [Server](#)
					- [st.cache_data](/develop/api-reference/caching-and-state/st.cache_data)
					- [st.cache_resource](/develop/api-reference/caching-and-state/st.cache_resource)
					- [st.session_state](/develop/api-reference/caching-and-state/st.session_state)
				- [Browser](#)
					- [st.context](/develop/api-reference/caching-and-state/st.context)
					- [st.query_params](/develop/api-reference/caching-and-state/st.query_params)
					- [st.experimental_get_query_params](/develop/api-reference/caching-and-state/st.experimental_get_query_params)
					- [st.experimental_set_query_params](/develop/api-reference/caching-and-state/st.experimental_set_query_params)
			- [Connections and Secrets](/develop/api-reference/connections)
			- [Custom Components](/develop/api-reference/custom-components)
			- [Configuration](/develop/api-reference/configuration)
			- [Tools](#)
				- [App Testing](/develop/api-reference/app-testing)
				- [Command Line](/develop/api-reference/cli)
	+ [Tutorials](/develop/tutorials)
	+ [Quick Reference](/develop/quick-reference)
* [Deploy](/deploy)
	+ [Concepts](/deploy/concepts)
	+ [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
	+ [Snowflake](/deploy/snowflake)
	+ [Other Platforms](/deploy/tutorials)
* [Knowledge Base](/knowledge-base)
	+ [FAQ](/knowledge-base/using-streamlit)
	+ [Installing Dependencies](/knowledge-base/dependencies)
	+ [Deployment Issues](/knowledge-base/deploy)

### Current Page
* [Home](/)
* [Develop](/develop)
* [API Reference](/develop/api-reference)
* [Caching and State](/develop/api-reference/caching-and-state)
* [st.query_params](/develop/api-reference/caching-and-state/st.query_params)

Here is the HTML converted to clean Markdown:

## st.query_params
`st.query_params` provides a dictionary-like interface to access query parameters in your app's URL and is available as of Streamlit 1.30.0. It behaves similarly to `st.session_state` with the notable exception that keys may be repeated in an app's URL. Handling of repeated keys requires special consideration as explained below.

`st.query_params` can be used with both key and attribute notation. For example, `st.query_params.my_key` and `st.query_params["my_key"]`. All keys and values will be set and returned as strings. When you write to `st.query_params`, a key-value pair prefixed with `?` is added to the end of your app's URL. Each additional pair is prefixed with `&` instead of `?`. Query parameters are cleared when navigating between pages in a multipage app.

For example, consider the following URL:
```
https://your_app.streamlit.app/?first_key=1&second_key=two&third_key=true
```
The parameters in the URL above will be accessible in `st.query_params` as:
```json
{
  "first_key": "1",
  "second_key": "two",
  "third_key": "true"
}
```
This means you can use those parameters in your app like this:
```python
# You can read query params using key notation
if st.query_params["first_key"] == "1":
  do_something()

# ...or using attribute notation
if st.query_params.second_key == "two":
  do_something_else()

# And you can change a param by just writing to it
st.query_params.first_key = 2  # This gets converted to str automatically
```

### Repeated keys
When a key is repeated in your app's URL (`?a=1&a=2&a=3`), dict-like methods will return only the last value. In this example, `st.query_params["a"]` returns `"3"`. To get all keys as a list, use the `.get_all()` method shown below. To set the value of a repeated key, assign the values as a list. For example, `st.query_params.a = ["1", "2", "3"]` produces the repeated key given at the beginning of this paragraph.

### Limitation
`st.query_params` can't get or set embedding settings as described in [Embed your app](https://docs.streamlit.io/deploy/streamlit-community-cloud/share-your-app/embed-your-app#embed-options). `st.query_params.embed` and `st.query_params.embed_options` will raise an `AttributeError` or `StreamlitAPIException` when trying to get or set their values, respectively.

## st.query_params.clear
Clear all query parameters from the URL of the app.
```python
st.query_params.clear()
```
Returns: `None`

## st.query_params.from_dict
Set all of the query parameters from a dictionary or dictionary-like object.
```python
st.query_params.from_dict(params)
```
Parameters:

* `params` (dict): A dictionary used to replace the current query parameters.

Example:
```python
import streamlit as st
st.query_params.from_dict({"foo": "bar", "baz": [1, "two"]})
```

## st.query_params.get_all
Get a list of all query parameter values associated to a given key.
```python
st.query_params.get_all(key)
```
Parameters:

* `key` (str): The label of the query parameter in the URL.

Returns: A list of values associated to the given key. May return zero, one, or multiple values.

## st.query_params.to_dict
Get all query parameters as a dictionary.
```python
st.query_params.to_dict()
```
Returns: A dictionary of the current query parameters in the app's URL.