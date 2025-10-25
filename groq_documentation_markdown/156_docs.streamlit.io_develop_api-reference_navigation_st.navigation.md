Here is the converted HTML to clean Markdown:

# Streamlit Docs

## Documentation

### Search
Search

### Navigation

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
				- [st.navigation](/develop/api-reference/navigation/st.navigation)
				- [st.Page](/develop/api-reference/navigation/st.page)
				- [st.page_link](/develop/api-reference/widgets/st.page_link)
				- [st.switch_page](/develop/api-reference/navigation/st.switch_page)
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
* [Navigation and pages](/develop/api-reference/navigation)
* [st.navigation](/develop/api-reference/navigation/st.navigation)

## st.navigation
### Description

Configure the available pages in a multipage app. Call `st.navigation` in your entrypoint file to define the available pages for your app. `st.navigation` returns the current page, which can be executed using the `.run()` method.

### Parameters

* `pages`: The available pages for the app. This can be a list of page-like objects or a dictionary with labeled sections.
* `position`: The position of the navigation menu. Can be "sidebar", "top", or "hidden". Defaults to "sidebar".
* `expanded`: Whether the navigation menu should be expanded. Defaults to False.

### Returns

The current page selected by the user. To run the page, you must use the `.run()` method on it.

### Examples

#### Example 1: Use a callable or Python file as a page

You can declare pages from callables or file paths. If you pass callables or paths to `st.navigation` as page-like objects, they are internally converted to `StreamlitPage` objects using `st.Page`.

```python
# page_1.py
import streamlit as st

st.title("Page 1")

# streamlit_app.py
import streamlit as st

def page_2():
    st.title("Page 2")

pg = st.navigation(["page_1.py", page_2])
pg.run()
```

#### Example 2: Group pages into sections and customize them with `st.Page`

You can use a dictionary to create sections within your navigation menu. In the following example, each page is similar to Page 1 in Example 1, and all pages are in the same directory.

```python
# streamlit_app.py
import streamlit as st

pages = {
    "Your account": [
        st.Page("create_account.py", title="Create your account"),
        st.Page("manage_account.py", title="Manage your account"),
    ],
    "Resources": [
        st.Page("learn.py", title="Learn about us"),
        st.Page("trial.py", title="Try it out"),
    ],
}

pg = st.navigation(pages)
pg.run()
```

#### Example 3: Use top navigation

You can use the `position` parameter to place the navigation at the top of the app. This is useful for apps with a lot of pages because it allows you to create collapsible sections for each group of pages.

```python
# streamlit_app.py
import streamlit as st

pages = {
    "Your account": [
        st.Page("create_account.py", title="Create your account"),
        st.Page("manage_account.py", title="Manage your account"),
    ],
    "Resources": [
        st.Page("learn.py", title="Learn about us"),
        st.Page("trial.py", title="Try it out"),
    ],
}

pg = st.navigation(pages, position="top")
pg.run()
```

#### Example 4: Stateful widgets across multiple pages

Call widget functions in your entrypoint file when you want a widget to be stateful across pages. Assign keys to your common widgets and access their values through Session State within your pages.

```python
# streamlit_app.py
import streamlit as st

def page1():
    st.write(st.session_state.foo)

def page2():
    st.write(st.session_state.bar)

# Widgets shared by all the pages
st.sidebar.selectbox("Foo", ["A", "B", "C"], key="foo")
st.sidebar.checkbox("Bar", key="bar")

pg = st.navigation([page1, page2])
pg.run()
```