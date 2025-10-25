Here is the clean Markdown version:

# Chart elements - Streamlit Docs
## Documentation
### Search
#### Getting Started
* [Get started](/get-started)
	+ [Installation](/get-started/installation)
	+ [Fundamentals](/get-started/fundamentals)
	+ [First steps](/get-started/tutorials)
#### Develop
* [Develop](/develop)
	+ [Concepts](/develop/concepts)
	+ [API reference](/develop/api-reference)
		- [Page Elements](#)
		- [Write and magic](/develop/api-reference/write-magic)
		- [Text elements](/develop/api-reference/text)
		- [Data elements](/develop/api-reference/data)
		- [Chart elements](/develop/api-reference/charts)
			- Simple
				- [st.area_chart](/develop/api-reference/charts/st.area_chart)
				- [st.bar_chart](/develop/api-reference/charts/st.bar_chart)
				- [st.line_chart](/develop/api-reference/charts/st.line_chart)
				- [st.map](/develop/api-reference/charts/st.map)
				- [st.scatter_chart](/develop/api-reference/charts/st.scatter_chart)
			- Advanced
				- [st.altair_chart](/develop/api-reference/charts/st.altair_chart)
				- [st.bokeh_chart](/develop/api-reference/charts/st.bokeh_chart)
				- [st.graphviz_chart](/develop/api-reference/charts/st.graphviz_chart)
				- [st.plotly_chart](/develop/api-reference/charts/st.plotly_chart)
				- [st.pydeck_chart](/develop/api-reference/charts/st.pydeck_chart)
				- [st.pyplot](/develop/api-reference/charts/st.pyplot)
				- [st.vega_lite_chart](/develop/api-reference/charts/st.vega_lite_chart)
		- [Input widgets](/develop/api-reference/widgets)
		- [Media elements](/develop/api-reference/media)
		- [Layouts and containers](/develop/api-reference/layout)
		- [Chat elements](/develop/api-reference/chat)
		- [Status elements](/develop/api-reference/status)
		- [Third-party components](https://streamlit.io/components)
		- Application Logic
			- [Authentication and user info](/develop/api-reference/user)
			- [Navigation and pages](/develop/api-reference/navigation)
			- [Execution flow](/develop/api-reference/execution-flow)
			- [Caching and state](/develop/api-reference/caching-and-state)
			- [Connections and secrets](/develop/api-reference/connections)
			- [Custom components](/develop/api-reference/custom-components)
			- [Configuration](/develop/api-reference/configuration)
		- Tools
			- [App testing](/develop/api-reference/app-testing)
			- [Command line](/develop/api-reference/cli)
	+ [Tutorials](/develop/tutorials)
	+ [Quick reference](/develop/quick-reference)
#### Deploy
* [Deploy](/deploy)
	+ [Concepts](/deploy/concepts)
	+ [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
	+ [Snowflake](/deploy/snowflake)
	+ [Other platforms](/deploy/tutorials)
#### Knowledge base
* [Knowledge base](/knowledge-base)
	+ [FAQ](/knowledge-base/using-streamlit)
	+ [Installing dependencies](/knowledge-base/dependencies)
	+ [Deployment issues](/knowledge-base/deploy)

### Links
* [Home](/)
* [Develop](/develop)
* [API reference](/develop/api-reference)
* [Chart elements](/develop/api-reference/charts)

# Chart elements
Streamlit supports several different charting libraries, and our goal is to continually add support for more. Right now, the most basic library in our arsenal is [Matplotlib](https://matplotlib.org/). Then there are also interactive charting libraries like [Vega Lite](https://vega.github.io/vega-lite/) (2D charts) and [deck.gl](https://github.com/uber/deck.gl) (maps and 3D charts). And finally we also provide a few chart types that are "native" to Streamlit, like `st.line_chart` and `st.area_chart`.

## Simple chart elements
### Simple area charts
Display an area chart.
```python
st.area_chart(my_data_frame)
```
### Simple bar charts
Display a bar chart.
```python
st.bar_chart(my_data_frame)
```
### Simple line charts
Display a line chart.
```python
st.line_chart(my_data_frame)
```
### Simple scatter charts
Display a line chart.
```python
st.scatter_chart(my_data_frame)
```
### Scatterplots on maps
Display a map with points on it.
```python
st.map(my_data_frame)
```

## Advanced chart elements
### Matplotlib
Display a matplotlib.pyplot figure.
```python
st.pyplot(my_mpl_figure)
```
### Altair
Display a chart using the Altair library.
```python
st.altair_chart(my_altair_chart)
```
### Vega-Lite
Display a chart using the Vega-Lite library.
```python
st.vega_lite_chart(my_vega_lite_chart)
```
### Plotly
Display an interactive Plotly chart.
```python
st.plotly_chart(my_plotly_chart)
```
### Bokeh
Display an interactive Bokeh chart.
```python
st.bokeh_chart(my_bokeh_chart)
```
### PyDeck
Display a chart using the PyDeck library.
```python
st.pydeck_chart(my_pydeck_chart)
```
### GraphViz
Display a graph using the dagre-d3 library.
```python
st.graphviz_chart(my_graphviz_spec)
```

Third-party components
These are featured components created by our lovely community. For more examples and inspiration, check out our [Components Gallery](https://streamlit.io/components) and [Streamlit Extras](https://extras.streamlit.app)!

### Streamlit Lottie
Integrate [Lottie](https://lottiefiles.com/) animations inside your Streamlit app.
```python
lottie_hello = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_V9t630.json")
st_lottie(lottie_hello, key="hello")
```
### Plotly Events
Make Plotly charts interactive!
```python
fig = px.line(x=[1], y=[1])
selected_points = plotly_events(fig)
```
### Streamlit Extras
A library with useful Streamlit extras.
```python
chart += get_annotations_chart(annotations=[("Mar 01, 2008", "Pretty good day for GOOG"), ("Dec 01, 2007", "Something's going wrong for GOOG & AAPL"), ("Nov 01, 2008", "Market starts again thanks to..."), ("Dec 01, 2009", "Small crash for GOOG after..."),],)
st.altair_chart(chart, use_container_width=True)
```
### Plost
A deceptively simple plotting library for Streamlit.
```python
import plost
plost.line_chart(my_dataframe, x='time', y='stock_value', color='stock_name',)
```
### HiPlot
High dimensional Interactive Plotting.
```python
data = [{'dropout':0.1, 'lr': 0.001, 'loss': 10.0, 'optimizer': 'SGD'}, {'dropout':0.15, 'lr': 0.01, 'loss': 3.5, 'optimizer': 'Adam'}, {'dropout':0.3, 'lr': 0.1, 'loss': 4.5, 'optimizer': 'Adam'}]
hip.Experiment.from_iterable(data).display()
```
### ECharts
High dimensional Interactive Plotting.
```python
from streamlit_echarts import st_echarts
st_echarts(options=options)
```
### Streamlit Folium
Streamlit Component for rendering Folium maps.
```python
m = folium.Map(location=[39.949610, -75.150282], zoom_start=16)
st_data = st_folium(m, width=725)
```
### Spacy-Streamlit
spaCy building blocks and visualizers for Streamlit apps.
```python
models = ["en_core_web_sm", "en_core_web_md"]
spacy_streamlit.visualize(models, "Sundar Pichai is the CEO of Google.")
```
### Streamlit Agraph
A Streamlit Graph Vis, based on [react-grah-vis](https://github.com/crubier/react-graph-vis).
```python
from streamlit_agraph import agraph, Node, Edge, Config
agraph(nodes=nodes, edges=edges, config=config)
```