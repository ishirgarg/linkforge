Here is the clean Markdown version of the provided HTML:
### st.pyplot - Streamlit Docs

#### Documentation

[![Logo](/logo.svg)](/)

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
			- SIMPLE
			- [st.area_chart](/develop/api-reference/charts/st.area_chart)
			- [st.bar_chart](/develop/api-reference/charts/st.bar_chart)
			- [st.line_chart](/develop/api-reference/charts/st.line_chart)
			- [st.map](/develop/api-reference/charts/st.map)
			- [st.scatter_chart](/develop/api-reference/charts/st.scatter_chart)
			- ADVANCED
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

### Navigation
* [Home](/)
* [Develop](/develop)
* [API reference](/develop/api-reference)
* [Chart elements](/develop/api-reference/charts)
* [st.pyplot](/develop/api-reference/charts/st.pyplot)

Here is the HTML converted to clean Markdown:

### st.pyplot
#### Streamlit Version
Version 1.50.0, Version 1.49.0, Version 1.48.0, Version 1.47.0, Version 1.46.0, Version 1.45.0, Version 1.44.0, Version 1.43.0, Version 1.42.0, Version 1.41.0, Version 1.40.0, Version 1.39.0, Version 1.38.0, Version 1.37.0, Version 1.36.0, Version 1.35.0, Version 1.34.0, Version 1.33.0, Version 1.32.0, Version 1.31.0, Version 1.30.0, Version 1.29.0, Version 1.28.0, Version 1.27.0, Version 1.26.0, Version 1.25.0, Version 1.24.0, Version 1.23.0, Version 1.22.0

Display a matplotlib.pyplot figure.

**Important**: You must install matplotlib>=3.0.0 to use this command. You can install all charting dependencies (except Bokeh) as an extra with Streamlit:
```bash
pip install streamlit[charts]
```
#### Function signature
```python
st.pyplot(fig=None, clear_figure=None, *, width="stretch", use_container_width=None, **kwargs)
```
#### Parameters

* `fig` (Matplotlib Figure): The Matplotlib Figure object to render. See [matplotlib.org](https://matplotlib.org/stable/gallery/index.html) for examples.
* `clear_figure` (bool): If True, the figure will be cleared after being rendered. If False, the figure will not be cleared after being rendered.
* `width` ("stretch", "content", or int): The width of the chart element.
* `use_container_width` (bool): **Deprecated**. Use `width="stretch"` instead.
* `**kwargs` (any): Arguments to pass to Matplotlib's savefig function.

#### Example
```python
import matplotlib.pyplot as plt
import streamlit as st
from numpy.random import default_rng as rng

arr = rng(0).normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)
```
#### Warning
Matplotlib doesn't work well with threads. Wrap your code with locks to avoid issues.

```python
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from threading import RLock

_lock = RLock()
x = np.random.normal(1, 1, 100)
y = np.random.normal(1, 1, 100)

with _lock:
    fig, ax = plt.subplots()
    ax.scatter(x, y)
    st.pyplot(fig)
```
### Still have questions?
Check out our [forums](https://discuss.streamlit.io) for helpful information and Streamlit experts.