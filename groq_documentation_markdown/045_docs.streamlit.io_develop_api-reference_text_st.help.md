Here is the converted markdown text:
### st.help - Streamlit Docs

![logo](/logo.svg)

#### Documentation

### Search

### Table of Contents
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
				- HEADINGS AND BODY
					- [st.title](/develop/api-reference/text/st.title)
					- [st.header](/develop/api-reference/text/st.header)
					- [st.subheader](/develop/api-reference/text/st.subheader)
					- [st.markdown](/develop/api-reference/text/st.markdown)
				- FORMATTED TEXT
					- [st.badge](/develop/api-reference/text/st.badge)
					- [st.caption](/develop/api-reference/text/st.caption)
					- [st.code](/develop/api-reference/text/st.code)
					- [st.divider](/develop/api-reference/text/st.divider)
					- [st.echo](/develop/api-reference/text/st.echo)
					- [st.latex](/develop/api-reference/text/st.latex)
					- [st.text](/develop/api-reference/text/st.text)
				- UTILITIES
					- [st.help](/develop/api-reference/text/st.help)
					- [st.html](/develop/api-reference/text/st.html)
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
[Text elements](/develop/api-reference/text)/ 
[st.help](/develop/api-reference/text/st.help)

## st.help
### Display help and other information for a given object

The `st.help` function displays the object's name, type, value, signature, docstring, and member variables, methods — as well as the values/docstring of members and methods.

#### Function signature
```python
st.help(obj=None, *, width="stretch")
```
#### Parameters

* `obj` (any): The object whose information should be displayed. If left unspecified, this call will display help for Streamlit itself.
* `width` ("stretch" or int): The width of the help element. This can be one of the following:
	+ "stretch" (default): The width of the element matches the width of the parent container.
	+ An integer specifying the width in pixels: The element has a fixed width. If the specified width is greater than the width of the parent container, the width of the element matches the width of the parent container.

#### Example

Don't remember how to initialize a dataframe? Try this:
```python
import streamlit as st
import pandas

st.help(pandas.DataFrame)
```
Want to quickly check what data type is output by a certain function? Try:
```python
import streamlit as st

x = my_poorly_documented_function()
st.help(x)
```
Want to quickly inspect an object? No sweat:
```python
class Dog:
    '''A typical dog.'''

    def __init__(self, breed, color):
        self.breed = breed
        self.color = color

    def bark(self):
        return 'Woof!'

fido = Dog("poodle", "white")

st.help(fido)
```
And if you're using Magic, you can get help for functions, classes, and modules without even typing `st.help`:
```python
import streamlit as st
import pandas

# Get help for Pandas read_csv:
pandas.read_csv

# Get help for Streamlit itself:
st
```