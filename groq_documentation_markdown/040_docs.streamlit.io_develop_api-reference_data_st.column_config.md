Here is the clean markdown version of the provided HTML:

# st.column_config - Streamlit Docs
## Documentation

### Search
Search

### Menu
* [Get started](/get-started)
	+ [Installation](/get-started/installation)
	+ [Fundamentals](/get-started/fundamentals)
	+ [First steps](/get-started/tutorials)
* [Develop](/develop)
	+ [Concepts](/develop/concepts)
	+ [API reference](/develop/api-reference)
		- [Write and magic](/develop/api-reference/write-magic)
		- [Text elements](/develop/api-reference/text)
		- [Data elements](/develop/api-reference/data)
			- [st.dataframe](/develop/api-reference/data/st.dataframe)
			- [st.data_editor](/develop/api-reference/data/st.data_editor)
			- [st.column_config](/develop/api-reference/data/st.column_config)
				- [Column](/develop/api-reference/data/st.column_config/st.column_config.column)
				- [Text column](/develop/api-reference/data/st.column_config/st.column_config.textcolumn)
				- [Number column](/develop/api-reference/data/st.column_config/st.column_config.numbercolumn)
				- [Checkbox column](/develop/api-reference/data/st.column_config/st.column_config.checkboxcolumn)
				- [Selectbox column](/develop/api-reference/data/st.column_config/st.column_config.selectboxcolumn)
				- [Multiselect column](/develop/api-reference/data/st.column_config/st.column_config.multiselectcolumn)
				- [Datetime column](/develop/api-reference/data/st.column_config/st.column_config.datetimecolumn)
				- [Date column](/develop/api-reference/data/st.column_config/st.column_config.datecolumn)
				- [Time column](/develop/api-reference/data/st.column_config/st.column_config.timecolumn)
				- [JSON column](/develop/api-reference/data/st.column_config/st.column_config.jsoncolumn)
				- [List column](/develop/api-reference/data/st.column_config/st.column_config.listcolumn)
				- [Link column](/develop/api-reference/data/st.column_config/st.column_config.linkcolumn)
				- [Image column](/develop/api-reference/data/st.column_config/st.column_config.imagecolumn)
				- [Area chart column](/develop/api-reference/data/st.column_config/st.column_config.areachartcolumn)
				- [Line chart column](/develop/api-reference/data/st.column_config/st.column_config.linechartcolumn)
				- [Bar chart column](/develop/api-reference/data/st.column_config/st.column_config.barchartcolumn)
				- [Progress column](/develop/api-reference/data/st.column_config/st.column_config.progresscolumn)
			- [st.table](/develop/api-reference/data/st.table)
			- [st.metric](/develop/api-reference/data/st.metric)
			- [st.json](/develop/api-reference/data/st.json)
		- [Chart elements](/develop/api-reference/charts)
		- [Input widgets](/develop/api-reference/widgets)
		- [Media elements](/develop/api-reference/media)
		- [Layouts and containers](/develop/api-reference/layout)
		- [Chat elements](/develop/api-reference/chat)
		- [Status elements](/develop/api-reference/status)
		- [Third-party components](https://streamlit.io/components)
		- [Application logic](/develop/api-reference/user)
			- [Authentication and user info](/develop/api-reference/user)
			- [Navigation and pages](/develop/api-reference/navigation)
			- [Execution flow](/develop/api-reference/execution-flow)
			- [Caching and state](/develop/api-reference/caching-and-state)
			- [Connections and secrets](/develop/api-reference/connections)
			- [Custom components](/develop/api-reference/custom-components)
			- [Configuration](/develop/api-reference/configuration)
		- [Tools](/develop/api-reference/app-testing)
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

### Links
* [Home](/)
* [Develop](/develop)
* [API reference](/develop/api-reference)
* [Data elements](/develop/api-reference/data)
* [st.column_config](/develop/api-reference/data/st.column_config)

Here's the HTML content converted to clean Markdown:

# Column Configuration
When working with data in Streamlit, the `st.column_config` class is a powerful tool for configuring data display and interaction. Specifically designed for the `column_config` parameter in [`st.dataframe`](/develop/api-reference/data/st.dataframe) and [`st.data_editor`](/develop/api-reference/data/st.data_editor), it provides a suite of methods to tailor your columns to various data types - from simple text and numbers to lists, URLs, images, and more.

Whether it's translating temporal data into user-friendly formats or utilizing charts and progress bars for clearer data visualization, column configuration not only provides the user with an enriched data viewing experience but also ensures that you're equipped with the tools to present and interact with your data, just the way you want it.

### Column
Configure a generic column.
```python
Column("Streamlit Widgets", width="medium", help="Streamlit **widget** commands ")
```

### Text Column
Configure a text column.
```python
TextColumn("Widgets", max_chars=50, validate="^st\.[a-z_]+$")
```

### Number Column
Configure a number column.
```python
NumberColumn("Price (in USD)", min_value=0, format="$%d")
```

### Checkbox Column
Configure a checkbox column.
```python
CheckboxColumn("Your favorite?", help="Select your **favorite** widgets")
```

### Selectbox Column
Configure a selectbox column.
```python
SelectboxColumn("App Category", options=[" LLM", " Data Viz"])
```

### Multiselect Column
Configure a multiselect column.
```python
MultiselectColumn("App Category", options=["LLM", "Visualization"])
```

### Datetime Column
Configure a datetime column.
```python
DatetimeColumn("Appointment", min_value=datetime(2023, 6, 1), format="D MMM YYYY, h:mm a")
```

### Date Column
Configure a date column.
```python
DateColumn("Birthday", max_value=date(2005, 1, 1), format="DD.MM.YYYY")
```

### Time Column
Configure a time column.
```python
TimeColumn("Appointment", min_value=time(8, 0, 0), format="hh:mm a")
```

### JSON Column
Configure a JSON column.
```python
JSONColumn("Properties", width="medium")
```

### List Column
Configure a list column.
```python
ListColumn("Sales (last 6 months)", width="medium")
```

### Link Column
Configure a link column.
```python
LinkColumn("Trending apps", max_chars=100, validate="^https://.*$")
```

### Image Column
Configure an image column.
```python
ImageColumn("Preview Image", help="The preview screenshots")
```

### Area Chart Column
Configure an area chart column.
```python
AreaChartColumn("Sales (last 6 months)", y_min=0, y_max=100)
```

### Line Chart Column
Configure a line chart column.
```python
LineChartColumn("Sales (last 6 months)", y_min=0, y_max=100)
```

### Bar Chart Column
Configure a bar chart column.
```python
BarChartColumn("Marketing spend", y_min=0, y_max=100)
```

### Progress Column
Configure a progress column.
```python
ProgressColumn("Sales volume", min_value=0, max_value=1000, format="$%f")
```

Still have questions? Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts. 

### Useful Links
* [Home](/)
* [Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)
* [Community](https://discuss.streamlit.io)
* [GitHub](https://github.com/streamlit)
* [YouTube](https://www.youtube.com/channel/UC3LD42rjj-Owtxsa6PwGU5Q)
* [Twitter](https://twitter.com/streamlit)
* [LinkedIn](https://www.linkedin.com/company/streamlit)
* [Newsletter](https://info.snowflake.com/streamlit-newsletter-sign-up.html) 

 2025 Snowflake Inc. [Cookie policy](/)