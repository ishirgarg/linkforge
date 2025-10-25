Here is the clean markdown version of the provided HTML:

# Configuration - Streamlit Docs
## Documentation

### Get started
* [Installation](/get-started/installation)
* [Fundamentals](/get-started/fundamentals)
* [First steps](/get-started/tutorials)

### Develop
* [Concepts](/develop/concepts)
* [API reference](/develop/api-reference)
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
	+ [Authentication and user info](/develop/api-reference/user)
	+ [Navigation and pages](/develop/api-reference/navigation)
	+ [Execution flow](/develop/api-reference/execution-flow)
	+ [Caching and state](/develop/api-reference/caching-and-state)
	+ [Connections and secrets](/develop/api-reference/connections)
	+ [Custom components](/develop/api-reference/custom-components)
	+ [Configuration](/develop/api-reference/configuration)
		- [config.toml](/develop/api-reference/configuration/config.toml)
		- [st.get_option](/develop/api-reference/configuration/st.get_option)
		- [st.set_option](/develop/api-reference/configuration/st.set_option)
		- [st.set_page_config](/develop/api-reference/configuration/st.set_page_config)
	+ [App testing](/develop/api-reference/app-testing)
	+ [Command line](/develop/api-reference/cli)
* [Tutorials](/develop/tutorials)
* [Quick reference](/develop/quick-reference)

### Deploy
* [Concepts](/deploy/concepts)
* [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
* [Snowflake](/deploy/snowflake)
* [Other platforms](/deploy/tutorials)

### Knowledge base
* [FAQ](/knowledge-base/using-streamlit)
* [Installing dependencies](/knowledge-base/dependencies)
* [Deployment issues](/knowledge-base/deploy)

## Configuration
The configuration file configures the default settings for your app.
```markdown
your-project/
├── .streamlit/
│   └── config.toml
└── your_app.py
```
### Configuration file
[config.toml](/develop/api-reference/configuration/config.toml)

### Get config option
`st.get_option("theme.primaryColor")`
[st.get_option](/develop/api-reference/configuration/st.get_option)

### Set config option
`st.set_option("deprecation.showPyplotGlobalUse", False)`
[st.set_option](/develop/api-reference/configuration/st.set_option)

### Set page title, favicon, and more
`st.set_page_config(page_title="My app", page_icon=":shark:", )`
[st.set_page_config](/develop/api-reference/configuration/st.set_page_config)

Still have questions? Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

[Home](/) | [Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20) | [Community](https://discuss.streamlit.io)

[GitHub](https://github.com/streamlit) | [YouTube](https://www.youtube.com/channel/UC3LD42rjj-Owtxsa6PwGU5Q) | [Twitter](https://twitter.com/streamlit) | [LinkedIn](https://www.linkedin.com/company/streamlit) | [Newsletter](https://info.snowflake.com/streamlit-newsletter-sign-up.html)

&copy; 2025 Snowflake Inc. Cookie policy