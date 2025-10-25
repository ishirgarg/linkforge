Here is the converted markdown:

# Data elements - Streamlit Docs

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
				- [st.dataframe](/develop/api-reference/data/st.dataframe)
				- [st.data_editor](/develop/api-reference/data/st.data_editor)
				- [st.column_config](/develop/api-reference/data/st.column_config)
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

### Links
* [Home](/)
* [Develop](/develop)
* [API reference](/develop/api-reference)
* [Data elements](/develop/api-reference/data)

# Data elements
When you're working with data, it is extremely valuable to visualize that data quickly, interactively, and from multiple different angles. That's what Streamlit is actually built and optimized for.

You can display data via [charts](/develop/api-reference/data#display-charts), and you can display it in raw form. These are the Streamlit commands you can use to display and interact with raw data.

## Dataframes
Display a dataframe as an interactive table.
```python
st.dataframe(my_data_frame)
```

## Data editor
Display a data editor widget.
```python
edited = st.data_editor(df, num_rows="dynamic")
```

## Column configuration
Configure the display and editing behavior of dataframes and data editors.
```python
st.column_config.NumberColumn("Price (in USD)", min_value=0, format="$%d")
```

## Static tables
Display a static table.
```python
st.table(my_data_frame)
```

## Metrics
Display a metric in big bold font, with an optional indicator of how the metric changed.
```python
st.metric("My metric", 42, 2)
```

## Dicts and JSON
Display object or string as a pretty-printed JSON string.
```python
st.json(my_dict)
```

### Third-party components
These are featured components created by our lovely community. For more examples and inspiration, check out our [Components Gallery](https://streamlit.io/components) and [Streamlit Extras](https://extras.streamlit.app)!

#### Image Coordinates
Get the coordinates of clicks on an image. Created by [@blackary](https://github.com/blackary/).
```python
from streamlit_image_coordinates import streamlit_image_coordinates
value = streamlit_image_coordinates("https://placekitten.com/200/300")
st.write(value)
```

#### Plotly Events
Make Plotly charts interactive!. Created by [@null-jones](https://github.com/null-jones/).
```python
from streamlit_plotly_events import plotly_events
fig = px.line(x=[1], y=[1])
selected_points = plotly_events(fig)
```

#### Streamlit Extras
A library with useful Streamlit extras. Created by [@arnaudmiribel](https://github.com/arnaudmiribel/).
```python
from streamlit_extras.metric_cards import style_metric_cards
col3.metric(label="No Change", value=5000, delta=0)
style_metric_cards()
```

#### Streamlit Aggrid
Implementation of Ag-Grid component for Streamlit. Created by [@PablocFonseca](https://github.com/PablocFonseca).
```python
df = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6]})
grid_return = AgGrid(df, editable=True)
new_df = grid_return['data']
```

#### Streamlit Folium
Streamlit Component for rendering Folium maps. Created by [@randyzwitch](https://github.com/randyzwitch).
```python
m = folium.Map(location=[39.949610, -75.150282], zoom_start=16)
folium.Marker([39.949610, -75.150282], popup="Liberty Bell", tooltip="Liberty Bell").add_to(m)
st_data = st_folium(m, width=725)
```

#### Pandas Profiling
Pandas profiling component for Streamlit. Created by [@okld](https://github.com/okld/).
```python
df = pd.read_csv("https://storage.googleapis.com/tf-datasets/titanic/train.csv")
pr = df.profile_report()
st_profile_report(pr)
```