Here is the HTML converted to clean Markdown:

# Streamlit Docs
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
			- BUTTONS
			- [st.button](/develop/api-reference/widgets/st.button)
			- [st.download_button](/develop/api-reference/widgets/st.download_button)
			- [st.form_submit_button](/develop/api-reference/execution-flow/st.form_submit_button)
			- [st.link_button](/develop/api-reference/widgets/st.link_button)
			- [st.page_link](/develop/api-reference/widgets/st.page_link)
			- SELECTIONS
			- [st.checkbox](/develop/api-reference/widgets/st.checkbox)
			- [st.color_picker](/develop/api-reference/widgets/st.color_picker)
			- [st.feedback](/develop/api-reference/widgets/st.feedback)
			- [st.multiselect](/develop/api-reference/widgets/st.multiselect)
			- [st.pills](/develop/api-reference/widgets/st.pills)
			- [st.radio](/develop/api-reference/widgets/st.radio)
			- [st.segmented_control](/develop/api-reference/widgets/st.segmented_control)
			- [st.selectbox](/develop/api-reference/widgets/st.selectbox)
			- [st.select_slider](/develop/api-reference/widgets/st.select_slider)
			- [st.toggle](/develop/api-reference/widgets/st.toggle)
			- NUMERIC
			- [st.number_input](/develop/api-reference/widgets/st.number_input)
			- [st.slider](/develop/api-reference/widgets/st.slider)
			- DATE AND TIME
			- [st.date_input](/develop/api-reference/widgets/st.date_input)
			- [st.time_input](/develop/api-reference/widgets/st.time_input)
			- TEXT
			- [st.chat_input](/develop/api-reference/chat/st.chat_input)
			- [st.text_area](/develop/api-reference/widgets/st.text_area)
			- [st.text_input](/develop/api-reference/widgets/st.text_input)
			- MEDIA AND FILES
			- [st.audio_input](/develop/api-reference/widgets/st.audio_input)
			- [st.camera_input](/develop/api-reference/widgets/st.camera_input)
			- [st.data_editor](/develop/api-reference/data/st.data_editor)
			- [st.file_uploader](/develop/api-reference/widgets/st.file_uploader)
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
* **Deploy**
	+ [Concepts](/deploy/concepts)
	+ [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
	+ [Snowflake](/deploy/snowflake)
	+ [Other platforms](/deploy/tutorials)
* **Knowledge base**
	+ [FAQ](/knowledge-base/using-streamlit)
	+ [Installing dependencies](/knowledge-base/dependencies)
	+ [Deployment issues](/knowledge-base/deploy)

### Tip
Check out our [tutorial](/develop/tutorials/multipage/st.page_link-nav) to learn about building custom, dynamic menus with `st.page_link`.

## st.page_link
Streamlit Version: 
1.50.0
1.49.0
1.48.0
1.47.0
1.46.0
1.45.0
1.44.0
1.43.0
1.42.0
1.41.0
1.40.0
1.39.0
1.38.0
1.37.0
1.36.0
1.35.0
1.34.0
1.33.0
1.32.0
1.31.0
1.30.0
1.29.0
1.28.0
1.27.0
1.26.0
1.25.0
1.24.0
1.23.0
1.22.0

Display a link to another page in a multipage app or to an external page.

If another page in a multipage app is specified, clicking `st.page_link` stops the current page execution and runs the specified page as if the user clicked on it in the sidebar navigation.

If an external page is specified, clicking `st.page_link` opens a new tab to the specified page. The current script run will continue if not complete.

### Function signature
```python
st.page_link(page, *, label=None, icon=None, help=None, disabled=False, use_container_width=None, width="content")
```

### Parameters

* **page** (str, Path, or StreamlitPage): The file path (relative to the main script) or a StreamlitPage indicating the page to switch to. Alternatively, this can be the URL to an external page (must start with "http://" or "https://").
* **label** (str): The label for the page link. Labels are required for external pages. The label can optionally contain GitHub-flavored Markdown of the following types: Bold, Italics, Strikethroughs, Inline Code, Links, and Images. Images display like icons, with a max height equal to the font height.
* **icon** (str or None): An optional emoji or icon to display next to the button label. If icon is None (default), the icon is inferred from the StreamlitPage object or no icon is displayed. If icon is a string, the following options are valid:
	+ A single-character emoji. For example, you can set `icon="🚨"` or `icon="🔥"`. Emoji short codes are not supported.
	+ An icon from the Material Symbols library (rounded style) in the format ":material/icon_name:" where "icon_name" is the name of the icon in snake case.
* **help** (str or None): A tooltip that gets displayed when the link is hovered over. If this is None (default), no tooltip is displayed.
* **disabled** (bool): An optional boolean that disables the page link if set to True. The default is False.
* **use_container_width** (bool): _delete_ (deprecated)
* **width** ("content", "stretch", or int): The width of the page-link button.

### Example
Consider the following example given this file structure:
```
your-repository/
├── pages/
│   ├── page_1.py
│   └── page_2.py
└── your_app.py
```

```python
import streamlit as st

st.page_link("your_app.py", label="Home", icon="🏠")
st.page_link("pages/page_1.py", label="Page 1", icon="1️⃣")
st.page_link("pages/page_2.py", label="Page 2", icon="2️⃣", disabled=True)
st.page_link("http://www.google.com", label="Google", icon="🌎")
```
The default navigation is shown here for comparison, but you can hide the default navigation using the [client.showSidebarNavigation](https://docs.streamlit.io/develop/api-reference/configuration/config.toml#client) configuration option. This allows you to create custom, dynamic navigation menus for your apps!