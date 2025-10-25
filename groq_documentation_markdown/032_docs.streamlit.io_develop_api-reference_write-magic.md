Here is the converted markdown:

# st.write and magic commands - Streamlit Docs
## Documentation

### Search
Search

### Navigation
* [Get started](/get-started)
	+ [Installation](/get-started/installation)
	+ [Fundamentals](/get-started/fundamentals)
	+ [First steps](/get-started/tutorials)
* [Develop](/develop)
	+ [Concepts](/develop/concepts)
	+ [API reference](/develop/api-reference)
		- [Write and magic](/develop/api-reference/write-magic)
			- [st.write](/develop/api-reference/write-magic/st.write)
			- [st.write_stream](/develop/api-reference/write-magic/st.write_stream)
			- [Magic](/develop/api-reference/write-magic/magic)
		- [Text elements](/develop/api-reference/text)
		- [Data elements](/develop/api-reference/data)
		- [Chart elements](/develop/api-reference/charts)
		- [Input widgets](/develop/api-reference/widgets)
		- [Media elements](/develop/api-reference/media)
		- [Layouts and containers](/develop/api-reference/layout)
		- [Chat elements](/develop/api-reference/chat)
		- [Status elements](/develop/api-reference/status)
		- [Third-party components](https://streamlit.io/components)
		- [Application logic](/develop/api-reference/user)
		- [Navigation and pages](/develop/api-reference/navigation)
		- [Execution flow](/develop/api-reference/execution-flow)
		- [Caching and state](/develop/api-reference/caching-and-state)
		- [Connections and secrets](/develop/api-reference/connections)
		- [Custom components](/develop/api-reference/custom-components)
		- [Configuration](/develop/api-reference/configuration)
		- [Tools](/develop/api-reference/app-testing)
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

## st.write and magic commands
Streamlit has two easy ways to display information into your app, which should typically be the first thing you try: `st.write` and magic.

### st.write
Write arguments to the app.
```python
st.write("Hello **world**!")
st.write(my_data_frame)
st.write(my_mpl_figure)
```

### st.write_stream
Write generators or streams to the app with a typewriter effect.
```python
st.write_stream(my_generator)
st.write_stream(my_llm_stream)
```

### Magic
Any time Streamlit sees either a variable or literal value on its own line, it automatically writes that to your app using `st.write`
```python
"Hello **world**!"
my_data_frame
my_mpl_figure
```

## Still have questions?
Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

## Contact and community
* [Home](/)
* [Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)
* [Community](https://discuss.streamlit.io)
* [GitHub](https://github.com/streamlit)
* [YouTube](https://www.youtube.com/channel/UC3LD42rjj-Owtxsa6PwGU5Q)
* [Twitter](https://twitter.com/streamlit)
* [LinkedIn](https://www.linkedin.com/company/streamlit)
* [Newsletter](https://info.snowflake.com/streamlit-newsletter-sign-up.html)

&copy; 2025 Snowflake Inc.
[Cookie policy](https://www.streamlit.io/cookie-policy)