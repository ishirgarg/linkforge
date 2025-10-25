Here is the clean markdown version of the provided HTML:

# st.components.v1.iframe - Streamlit Docs

## Documentation

### Search
Search

### Get Started
* [Installation](/get-started/installation)
* [Fundamentals](/get-started/fundamentals)
* [First steps](/get-started/tutorials)

### Develop
* [Concepts](/develop/concepts)
* [API reference](/develop/api-reference)
	+ PAGE ELEMENTS
	+ [Write and magic](/develop/api-reference/write-magic)
	+ [Text elements](/develop/api-reference/text)
	+ [Data elements](/develop/api-reference/data)
	+ [Chart elements](/develop/api-reference/charts)
	+ [Input widgets](/develop/api-reference/widgets)
	+ [Media elements](/develop/api-reference/media)
	+ [Layouts and containers](/develop/api-reference/layout)
	+ [Chat elements](/develop/api-reference/chat)
	+ [Status elements](/develop/api-reference/status)
	+ [Third-party components](https://streamlit.io/components)
	+ APPLICATION LOGIC
	+ [Authentication and user info](/develop/api-reference/user)
	+ [Navigation and pages](/develop/api-reference/navigation)
	+ [Execution flow](/develop/api-reference/execution-flow)
	+ [Caching and state](/develop/api-reference/caching-and-state)
	+ [Connections and secrets](/develop/api-reference/connections)
	+ [Custom components](/develop/api-reference/custom-components)
		- [st.components.v1.declare_component](/develop/api-reference/custom-components/st.components.v1.declare_component)
		- [st.components.v1.html](/develop/api-reference/custom-components/st.components.v1.html)
		- [st.components.v1.iframe](/develop/api-reference/custom-components/st.components.v1.iframe)
	+ [Configuration](/develop/api-reference/configuration)
	+ TOOLS
	+ [App testing](/develop/api-reference/app-testing)
	+ [Command line](/develop/api-reference/cli)
* [Tutorials](/develop/tutorials)
* [Quick reference](/develop/quick-reference)

### Deploy
* [Concepts](/deploy/concepts)
* [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
* [Snowflake](/deploy/snowflake)
* [Other platforms](/deploy/tutorials)

### Knowledge Base
* [FAQ](/knowledge-base/using-streamlit)
* [Installing dependencies](/knowledge-base/dependencies)
* [Deployment issues](/knowledge-base/deploy)

## st.components.v1.iframe

### Description
Load a remote URL in an iframe.

### Function Signature
```python
st.components.v1.iframe(src, width=None, height=None, scrolling=False, *, tab_index=None)
```

### Parameters
* `src` (str): The URL of the page to embed.
* `width` (int): The width of the iframe in CSS pixels. By default, this is the app's default element width.
* `height` (int): The height of the frame in CSS pixels. By default, this is 150.
* `scrolling` (bool): Whether to allow scrolling in the iframe. If this False (default), Streamlit crops any content larger than the iframe and does not show a scrollbar. If this is True, Streamlit shows a scrollbar when the content is larger than the iframe.
* `tab_index` (int or None): Specifies how and if the iframe is sequentially focusable.

### Example
```python
import streamlit.components.v1 as components

components.iframe("https://example.com", height=500)
```

### Still have questions?
Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

### Contact Us
[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

### Social Media
[GitHub](https://github.com/streamlit)[YouTube](https://www.youtube.com/channel/UC3LD42rjj-Owtxsa6PwGU5Q)[Twitter](https://twitter.com/streamlit)[LinkedIn](https://www.linkedin.com/company/streamlit)[Newsletter](https://info.snowflake.com/streamlit-newsletter-sign-up.html)

&copy; 2025 Snowflake Inc.
[Cookie policy](https://www.streamlit.io/cookie-policy)