Here is the converted HTML to clean markdown:
### Streamlit Docs
#### Documentation
[Get Started](/get-started)
* [Installation](/get-started/installation)
* [Fundamentals](/get-started/fundamentals)
* [First steps](/get-started/tutorials)

[Develop](/develop)
* [Concepts](/develop/concepts)
* [API reference](/develop/api-reference)
	+ [PAGE ELEMENTS](#)
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
	+ [APPLICATION LOGIC](#)
		- [Authentication and user info](/develop/api-reference/user)
		- [Navigation and pages](/develop/api-reference/navigation)
			- [st.navigation](/develop/api-reference/navigation/st.navigation)
			- [st.Page](/develop/api-reference/navigation/st.page)
			- [st.page_link](/develop/api-reference/widgets/st.page_link)
			- [st.switch_page](/develop/api-reference/navigation/st.switch_page)
		- [Execution flow](/develop/api-reference/execution-flow)
		- [Caching and state](/develop/api-reference/caching-and-state)
		- [Connections and secrets](/develop/api-reference/connections)
		- [Custom components](/develop/api-reference/custom-components)
		- [Configuration](/develop/api-reference/configuration)
	+ [TOOLS](#)
		- [App testing](/develop/api-reference/app-testing)
		- [Command line](/develop/api-reference/cli)
* [Tutorials](/develop/tutorials)
* [Quick reference](/develop/quick-reference)

[Deploy](/deploy)
* [Concepts](/deploy/concepts)
* [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
* [Snowflake](/deploy/snowflake)
* [Other platforms](/deploy/tutorials)

[Knowledge base](/knowledge-base)
* [FAQ](/knowledge-base/using-streamlit)
* [Installing dependencies](/knowledge-base/dependencies)
* [Deployment issues](/knowledge-base/deploy)

### Links
* [Home](/)
* [Develop](/develop)
* [API reference](/develop/api-reference)
* [Navigation and pages](/develop/api-reference/navigation)
* [st.Page](/develop/api-reference/navigation/st.page)

## st.Page
Configure a page for st.navigation in a multipage app.

Call st.Page to initialize a StreamlitPage object, and pass it to st.navigation to declare a page in your app.

When a user navigates to a page, st.navigation returns the selected StreamlitPage object. Call .run() on the returned StreamlitPage object to execute the page. You can only run the page returned by st.navigation, and you can only run it once per app rerun.

A page can be defined by a Python file or Callable.

### Function Signature
```python
st.Page(page, *, title=None, icon=None, url_path=None, default=False)
```

### Parameters

* `page` (str, Path, or callable): The page source as a Callable or path to a Python file.
* `title` (str or None): The title of the page. If this is None (default), the page title will be inferred from the filename or callable name in page.
* `icon` (str or None): An optional emoji or icon to display next to the page title and label.
* `url_path` (str or None): The page's URL pathname, which is the path relative to the app's root URL.
* `default` (bool): Whether this page is the default page to be shown when the app is loaded.

### Returns
The page object associated to the given script.

### Example
```python
import streamlit as st

def page2():
    st.title("Second page")

pg = st.navigation([
    st.Page("page1.py", title="First page", icon=""),
    st.Page(page2, title="Second page", icon=":material/favorite:"),
])
pg.run()
```

## StreamlitPage
A page within a multipage Streamlit app.

Use st.Page to initialize a StreamlitPage object.

### Class Description
```python
StreamlitPage(page, *, title=None, icon=None, url_path=None, default=False)
```

### Methods

* `run()`: Execute the page.

### Attributes

* `icon` (str): The icon of the page.
* `title` (str): The title of the page.
* `url_path` (str): The page's URL pathname, which is the path relative to the app's root URL.

## StreamlitPage.run
Execute the page.

When a page is returned by st.navigation, use the .run() method within your entrypoint file to render the page. You can only call this method on the page returned by st.navigation. You can only call this method once per run of your entrypoint file.

### Function Signature
```python
StreamlitPage.run()
```