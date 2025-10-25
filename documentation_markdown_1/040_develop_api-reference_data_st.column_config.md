```markdown
# st.column_config - Streamlit Documentation

> **Source:** [https://docs.streamlit.io/develop/api-reference/data/st.column_config](https://docs.streamlit.io/develop/api-reference/data/st.column_config)

## Column configuration

This section provides information on how to configure columns within Streamlit's data display elements, such as `st.dataframe` and `st.data_editor`.
```


When working with data in Streamlit, the `st.column_config` class is a powerful tool for configuring data display and interaction. Specifically designed for the `column_config` parameter in [`st.dataframe`](/develop/api-reference/data/st.dataframe) and [`st.data_editor`](/develop/api-reference/data/st.data_editor), it provides a suite of methods to tailor your columns to various data types - from simple text and numbers to lists, URLs, images, and more.

Whether it's translating temporal data into user-friendly formats or utilizing charts and progress bars for clearer data visualization, column configuration not only provides the user with an enriched data viewing experience but also ensures that you're equipped with the tools to present and interact with your data, just the way you want it.

![screenshot](/images/api/column_config.column.jpg)

### [Column](/develop/api-reference/data/st.column_config/st.column_config.column)

Configure a generic column.

```python
Column("Streamlit Widgets", width="medium", help="Streamlit **widget** commands 🎈")
```

![screenshot](/images/api/column_config.textcolumn.jpg)

### [Text column](/develop/api-reference/data/st.column_config/st.column_config.textcolumn)

Configure a text column.

```python
TextColumn("Widgets", max_chars=50, validate="^st\.[a-z_]+$")
```

![screenshot](/images/api/column_config.numbercolumn.jpg)

### [Number column](/develop/api-reference/data/st.column_config/st.column_config.numbercolumn)

Configure a number column.

```python
NumberColumn("Price (in USD)", min_value=0, format="$%d")
```

![screenshot](/images/api/column_config.checkboxcolumn.jpg)

### [Checkbox column](/develop/api-reference/data/st.column_config/st.column_config.checkboxcolumn)

Configure a checkbox column.

```python
CheckboxColumn("Your favorite?", help="Select your **favorite** widgets")
```

![screenshot](/images/api/column_config.selectboxcolumn.jpg)

### [Selectbox column](/develop/api-reference/data/st.column_config/st.column_config.selectboxcolumn)

Configure a selectbox column.

```python
SelectboxColumn("App Category", options=["🤖 LLM", "📈 Data Viz"])
```

![screenshot](/images/api/column_config.multiselectcolumn.jpg)

### [Multiselect column](/develop/api-reference/data/st.column_config/st.column_config.multiselectcolumn)

Configure a multiselect column.

```python
MultiselectColumn("App Category", options=["LLM", "Visualization"])
```

![screenshot](/images/api/column_config.datetimecolumn.jpg)

### [Datetime column](/develop/api-reference/data/st.column_config/st.column_config.datetimecolumn)

Configure a datetime column.

```python
DatetimeColumn("Appointment", min_value=datetime(2023, 6, 1), format="D MMM YYYY, h:mm a")
```

![screenshot](/images/api/column_config.datecolumn.jpg)

### [Date column](/develop/api-reference/data/st.column_config/st.column_config.datecolumn)

Configure a date column.

```python
DateColumn("Birthday", max_value=date(2005, 1, 1), format="DD.MM.YYYY")
```

![screenshot](/images/api/column_config.timecolumn.jpg)

### [Time column](/develop/api-reference/data/st.column_config/st.column_config.timecolumn)

Configure a time column.

```python
TimeColumn("Appointment", min_value=time(8, 0, 0), format="hh:mm a")
```

![screenshot](/images/api/column_config.jsoncolumn.jpg)

### [JSON column](/develop/api-reference/data/st.column_config/st.column_config.jsoncolumn)

Configure a JSON column.

```python
JSONColumn("Properties", width="medium")
```

![screenshot](/images/api/column_config.listcolumn.jpg)

### [List column](/develop/api-reference/data/st.column_config/st.column_config.listcolumn)

Configure a list column.

```python
ListColumn("Sales (last 6 months)", width="medium")
```

![screenshot](/images/api/column_config.linkcolumn.jpg)

### [Link column](/develop/api-reference/data/st.column_config/st.column_config.linkcolumn)

Configure a link column.

```python
LinkColumn("Trending apps", max_chars=100, validate="^https://.*$")
```

![screenshot](/images/api/column_config.imagecolumn.jpg)

### [Image column](/develop/api-reference/data/st.column_config/st.column_config.imagecolumn)

Configure an image column.

```python
ImageColumn("Preview Image", help="The preview screenshots")
```

![screenshot](/images/api/column_config.areachartcolumn.jpg)

### [Area chart column](/develop/api-reference/data/st.column_config/st.column_config.areachartcolumn)

Configure an area chart column.

```python
AreaChartColumn("Sales (last 6 months)", y_min=0, y_max=100)
```

![screenshot](/images/api/column_config.linechartcolumn.jpg)

### [Line chart column](/develop/api-reference/data/st.column_config/st.column_config.linechartcolumn)

Configure a line chart column.

```python
LineChartColumn("Sales (last 6 months)", y_min=0, y_max=100)
```

![screenshot](/images/api/column_config.barchartcolumn.jpg)

### [Bar chart column](/develop/api-reference/data/st.column_config/st.column_config.barchartcolumn)

Configure a bar chart column.

```python
BarChartColumn("Marketing spend", y_min=0, y_max=100)
```

![screenshot](/images/api/column_config.progresscolumn.jpg)

### [Progress column](/develop/api-reference/data/st.column_config/st.column_config.progresscolumn)

Configure a progress column.

```python
ProgressColumn("Sales volume", min_value=0, max_value=1000, format="$%f")
```

[Previous: st.data_editor](/develop/api-reference/data/st.data_editor) | [Next: Column](/develop/api-reference/data/st.column_config/st.column_config.column)

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.