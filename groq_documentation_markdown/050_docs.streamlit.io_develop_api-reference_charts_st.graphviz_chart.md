Here is the content converted to clean markdown:

# st.graphviz_chart - Streamlit Docs
![Logo](/logo.svg)

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
		- [Text elements](/develop/api-reference/text)
		- [Data elements](/develop/api-reference/data)
		- [Chart elements](/develop/api-reference/charts)
			- [st.area_chart](/develop/api-reference/charts/st.area_chart)
			- [st.bar_chart](/develop/api-reference/charts/st.bar_chart)
			- [st.line_chart](/develop/api-reference/charts/st.line_chart)
			- [st.map](/develop/api-reference/charts/st.map)
			- [st.scatter_chart](/develop/api-reference/charts/st.scatter_chart)
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
		- [Authentication and user info](/develop/api-reference/user)
		- [Navigation and pages](/develop/api-reference/navigation)
		- [Execution flow](/develop/api-reference/execution-flow)
		- [Caching and state](/develop/api-reference/caching-and-state)
		- [Connections and secrets](/develop/api-reference/connections)
		- [Custom components](/develop/api-reference/custom-components)
		- [Configuration](/develop/api-reference/configuration)
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

### Breadcrumbs
* [Home](/)
* [Develop](/develop)
* [API reference](/develop/api-reference)
* [Chart elements](/develop/api-reference/charts)
* [st.graphviz_chart](/develop/api-reference/charts/st.graphviz_chart)

## st.graphviz_chart
### Description
Display a graph using the dagre-d3 library.

**Important**: You must install graphviz>=0.19.0 to use this command. You can install all charting dependencies (except Bokeh) as an extra with Streamlit:
```bash
pip install streamlit[charts]
```
### Function signature
```python
st.graphviz_chart(figure_or_dot, use_container_width=None, *, width="content", height="content")
```
### Parameters

* `figure_or_dot`: The Graphlib graph object or dot string to display
* `use_container_width`: *Deprecated*. Use `width="stretch"` instead of `use_container_width=True` and `width="content"` instead of `use_container_width=False`.
* `width`: The width of the chart element. Can be "content", "stretch", or an integer specifying the width in pixels.
* `height`: The height of the chart element. Can be "content", "stretch", or an integer specifying the height in pixels.

### Example
```python
import streamlit as st
import graphviz

# Create a graphlib graph object
graph = graphviz.Digraph()
graph.edge("run", "intr")
graph.edge("intr", "runbl")
graph.edge("runbl", "run")
graph.edge("run", "kernel")
graph.edge("kernel", "zombie")
graph.edge("kernel", "sleep")
graph.edge("kernel", "runmem")
graph.edge("sleep", "swap")
graph.edge("swap", "runswap")
graph.edge("runswap", "new")
graph.edge("runswap", "runmem")
graph.edge("new", "runmem")
graph.edge("sleep", "runmem")

st.graphviz_chart(graph)
```
Or you can render the chart from the graph using GraphViz's Dot language:
```python
st.graphviz_chart('''
    digraph {
        run -> intr
        intr -> runbl
        runbl -> run
        run -> kernel
        kernel -> zombie
        kernel -> sleep
        kernel -> runmem
        sleep -> swap
        swap -> runswap
        runswap -> new
        runswap -> runmem
        new -> runmem
        sleep -> runmem
    }
''')
```