Here is the HTML content converted to clean Markdown:

### st.echo - Streamlit Docs
![Logo](/logo.svg)

#### Documentation

### Search
Search

### Menu
* **Get started**
	+ [Installation](/get-started/installation)
	+ [Fundamentals](/get-started/fundamentals)
	+ [First steps](/get-started/tutorials)
* **Develop**
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
		- [Tutorials](/develop/tutorials)
		- [Quick reference](/develop/quick-reference)
* **Deploy**
	+ [Concepts](/deploy/concepts)
	+ [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
	+ [Snowflake](/deploy/snowflake)
	+ [Other platforms](/deploy/tutorials)
* **Knowledge base**
	+ [FAQ](/knowledge-base/using-streamlit)
	+ [Installing dependencies](/knowledge-base/dependencies)
	+ [Deployment issues](/knowledge-base/deploy)

### Links
* [Home](/)
* [Develop](/develop)
* [API reference](/develop/api-reference)
* [Text elements](/develop/api-reference/text)
* [st.echo](/develop/api-reference/text/st.echo)

## st.echo
### Streamlit Version
1.50.0, 1.49.0, 1.48.0, 1.47.0, 1.46.0, 1.45.0, 1.44.0, 1.43.0, 1.42.0, 1.41.0, 1.40.0, 1.39.0, 1.38.0, 1.37.0, 1.36.0, 1.35.0, 1.34.0, 1.33.0, 1.32.0, 1.31.0, 1.30.0, 1.29.0, 1.28.0, 1.27.0, 1.26.0, 1.25.0, 1.24.0, 1.23.0, 1.22.0

Use in a `with` block to draw some code on the app, then execute it.

### Function signature
[Source](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/commands/echo.py#L33)

`st.echo(code_location="above")`

### Parameters
* `code_location`: ("above" or "below") - Whether to show the echoed code before or after the results of the executed code block.

### Example
```python
import streamlit as st

with st.echo():
    st.write('This code will be printed')
```

### Display code
Sometimes you want your Streamlit app to contain both your usual Streamlit graphic elements and the code that generated those elements. That's where `st.echo()` comes in.

Let's say you have the following file, and you want to make its app a little bit more self-explanatory by making that middle section visible in the Streamlit app:
```python
import streamlit as st

def get_user_name():
    return 'John'

# Want people to see this part of the code...
def get_punctuation():
    return '!!!'

greeting = "Hi there, "
user_name = get_user_name()
punctuation = get_punctuation()
st.write(greeting, user_name, punctuation)
# ...up to here

foo = 'bar'
st.write('Done!')
```
The file above creates a Streamlit app containing the words "Hi there, John", and then "Done!".

Now let's use `st.echo()` to make that middle section of the code visible in the app:
```python
import streamlit as st

def get_user_name():
    return 'John'

with st.echo():
    # Everything inside this block will be both printed to the screen
    # and executed.
    def get_punctuation():
        return '!!!'

    greeting = "Hi there, "
    value = get_user_name()
    punctuation = get_punctuation()
    st.write(greeting, value, punctuation)

# And now we're back to _not_ printing to the screen
foo = 'bar'
st.write('Done!')
```
It's that simple!

### Note
You can have multiple `st.echo()` blocks in the same file. Use it as often as you wish!