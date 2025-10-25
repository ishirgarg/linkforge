Here is the converted text in clean markdown:

# st.empty - Streamlit Docs
#### Documentation

## Search
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

## st.empty
### Description
Insert a single-element container.

Inserts a container into your app that can be used to hold a single element. This allows you to, for example, remove elements at any point, or replace several elements at once (using a child multi-element container).

To insert/replace/clear an element on the returned container, you can use with notation or just call methods directly on the returned object. See examples below.

### Function signature
```python
st.empty()
```

### Examples
#### Example 1
Inside a with st.empty(): block, each displayed element will replace the previous one.
```python
import streamlit as st
import time

with st.empty():
    for seconds in range(10):
        st.write(f"⏳ {seconds} seconds have passed")
        time.sleep(1)
    st.write(":material/check: 10 seconds over!")
st.button("Rerun")
```

#### Example 2
You can use an st.empty to replace multiple elements in succession. Use st.container inside st.empty to display (and later replace) a group of elements.
```python
import streamlit as st
import time

st.button("Start over")

placeholder = st.empty()
placeholder.markdown("Hello")
time.sleep(1)

placeholder.progress(0, "Wait for it...")
time.sleep(1)
placeholder.progress(50, "Wait for it...")
time.sleep(1)
placeholder.progress(100, "Wait for it...")
time.sleep(1)

with placeholder.container():
    st.line_chart({"data": [1, 5, 2, 6]})
    time.sleep(1)
    st.markdown("3...")
    time.sleep(1)
    st.markdown("2...")
    time.sleep(1)
    st.markdown("1...")
    time.sleep(1)

placeholder.markdown("Poof!")
time.sleep(1)

placeholder.empty()
```

### Version History
* Version 1.50.0
* Version 1.49.0
* Version 1.48.0
* Version 1.47.0
* Version 1.46.0
* Version 1.45.0
* Version 1.44.0
* Version 1.43.0
* Version 1.42.0
* Version 1.41.0
* Version 1.40.0
* Version 1.39.0
* Version 1.38.0
* Version 1.37.0
* Version 1.36.0
* Version 1.35.0
* Version 1.34.0
* Version 1.33.0
* Version 1.32.0
* Version 1.31.0
* Version 1.30.0
* Version 1.29.0
* Version 1.28.0
* Version 1.27.0
* Version 1.26.0
* Version 1.25.0
* Version 1.24.0
* Version 1.23.0
* Version 1.22.0

### Need Help?
Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

### Contact Us
[Home](/) | [Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20) | [Community](https://discuss.streamlit.io)

### Social Media
[GitHub](https://github.com/streamlit) | [YouTube](https://www.youtube.com/channel/UC3LD42rjj-Owtxsa6PwGU5Q) | [Twitter](https://twitter.com/streamlit) | [LinkedIn](https://www.linkedin.com/company/streamlit) | [Newsletter](https://info.snowflake.com/streamlit-newsletter-sign-up.html)

### Copyright
&copy; 2025 Snowflake Inc. [Cookie policy](https://www.streamlit.io/cookie-policy)