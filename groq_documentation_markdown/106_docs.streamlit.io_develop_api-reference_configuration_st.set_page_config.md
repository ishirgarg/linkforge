Here is the HTML content converted to clean markdown:

# st.set_page_config - Streamlit Docs

## Documentation

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
			- [config.toml](/develop/api-reference/configuration/config.toml)
			- [st.get_option](/develop/api-reference/configuration/st.get_option)
			- [st.set_option](/develop/api-reference/configuration/st.set_option)
			- [st.set_page_config](/develop/api-reference/configuration/st.set_page_config)
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
* [Configuration](/develop/api-reference/configuration)
* [st.set_page_config](/develop/api-reference/configuration/st.set_page_config)

## st.set_page_config
Configure the default settings of the page.

This command can be called multiple times in a script run to dynamically change the page configuration. The calls are additive, with each successive call overriding only the parameters that are specified.

### Function Signature
```python
st.set_page_config(
    page_title=None, 
    page_icon=None, 
    layout=None, 
    initial_sidebar_state=None, 
    menu_items=None
)
```

### Parameters

* **page_title** (str or None): The page title, shown in the browser tab. If this is None (default), the page title is inherited from the previous call of `st.set_page_config`. If this is None and no previous call exists, the page title is inferred from the page source.
* **page_icon** (Anything supported by `st.image` (except list), str, or None): The page favicon. If `page_icon` is None (default), the page icon is inherited from the previous call of `st.set_page_config`. If this is None and no previous call exists, the favicon is a monochrome Streamlit logo.
	+ Valid strings:
		- A single-character emoji (e.g. "🦈")
		- An emoji short code (e.g. ":shark:")
		- The string literal "random"
		- An icon from the Material Symbols library (rounded style) in the format ":material/icon_name:" (e.g. ":material/thumb_up:")
* **layout** ("centered", "wide", or None): How the page content should be laid out. If this is None (default), the page layout is inherited from the previous call of `st.set_page_config`. If this is None and no previous call exists, the page layout is "centered".
* **initial_sidebar_state** ("auto", "expanded", "collapsed", or None): How the sidebar should start out. If this is None (default), the sidebar state is inherited from the previous call of `st.set_page_config`. If no previous call exists, the sidebar state is "auto".
	+ Supported states:
		- "auto": The sidebar is hidden on small devices and shown otherwise.
		- "expanded": The sidebar is shown initially.
		- "collapsed": The sidebar is hidden initially.
* **menu_items** (dict): Configure the menu that appears on the top-right side of this app. The keys in this dict denote the menu item to configure. The following keys can have string or None values:
	+ "Get help": The URL this menu item should point to.
	+ "Report a Bug": The URL this menu item should point to.
	+ "About": A markdown string to show in the About dialog.

### Example
```python
import streamlit as st

st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)
```