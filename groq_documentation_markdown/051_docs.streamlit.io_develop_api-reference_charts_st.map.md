Here is the HTML content converted to clean Markdown:

### Streamlit Docs

#### Documentation
##### Get Started
* [Installation](/get-started/installation)
* [Fundamentals](/get-started/fundamentals)
* [First steps](/get-started/tutorials)

##### Develop
* [Concepts](/develop/concepts)
* [API reference](/develop/api-reference)
	+ PAGE ELEMENTS
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
	+ APPLICATION LOGIC
		- [Authentication and user info](/develop/api-reference/user)
		- [Navigation and pages](/develop/api-reference/navigation)
		- [Execution flow](/develop/api-reference/execution-flow)
		- [Caching and state](/develop/api-reference/caching-and-state)
		- [Connections and secrets](/develop/api-reference/connections)
		- [Custom components](/develop/api-reference/custom-components)
		- [Configuration](/develop/api-reference/configuration)
	+ TOOLS
		- [App testing](/develop/api-reference/app-testing)
		- [Command line](/develop/api-reference/cli)
* [Tutorials](/develop/tutorials)
* [Quick reference](/develop/quick-reference)

##### Deploy
* [Concepts](/deploy/concepts)
* [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
* [Snowflake](/deploy/snowflake)
* [Other platforms](/deploy/tutorials)

##### Knowledge base
* [FAQ](/knowledge-base/using-streamlit)
* [Installing dependencies](/knowledge-base/dependencies)
* [Deployment issues](/knowledge-base/deploy)

### Navigation
* [Home](/)
* [Develop](/develop)
* [API reference](/develop/api-reference)
* [Chart elements](/develop/api-reference/charts)
* [st.map](/develop/api-reference/charts/st.map)

Here is the converted text in clean markdown:

## st.map
Streamlit Version: 1.50.0, 1.49.0, 1.48.0, 1.47.0, 1.46.0, 1.45.0, 1.44.0, 1.43.0, 1.42.0, 1.41.0, 1.40.0, 1.39.0, 1.38.0, 1.37.0, 1.36.0, 1.35.0, 1.34.0, 1.33.0, 1.32.0, 1.31.0, 1.30.0, 1.29.0, 1.28.0, 1.27.0, 1.26.0, 1.25.0, 1.24.0, 1.23.0, 1.22.0

Display a map with a scatterplot overlaid onto it.

This is a wrapper around `st.pydeck_chart` to quickly create scatterplot charts on top of a map, with auto-centering and auto-zoom.

When using this command, a service called [Carto](https://carto.com) provides the map tiles to render map content. If you're using advanced PyDeck features, you may need to obtain an API key from Carto first. You can do that as `pydeck.Deck(api_keys={"carto": YOUR_KEY})` or by setting the `CARTO_API_KEY` environment variable. See [PyDeck's documentation](https://deckgl.readthedocs.io/en/latest/deck.html) for more information.

Another common provider for map tiles is [Mapbox](https://mapbox.com). If you prefer to use that, you'll need to create an account at [https://mapbox.com](https://mapbox.com) and specify your Mapbox key when creating the `pydeck.Deck` object. You can do that as `pydeck.Deck(api_keys={"mapbox": YOUR_KEY})` or by setting the `MAPBOX_API_KEY` environment variable.

Carto and Mapbox are third-party products, and Streamlit accepts no responsibility or liability of any kind for Carto or Mapbox, or for any content or information made available by Carto or Mapbox. The use of Carto or Mapbox is governed by their respective Terms of Use.

### Function signature
```python
st.map(data=None, *, latitude=None, longitude=None, color=None, size=None, zoom=None, use_container_width=True, width=None, height=None)
```
### Parameters

* `data`: The data to be plotted. Anything supported by `st.dataframe`.
* `latitude`: The name of the column containing the latitude coordinates of the datapoints in the chart. If `None`, the latitude data will come from any column named 'lat', 'latitude', 'LAT', or 'LATITUDE'.
* `longitude`: The name of the column containing the longitude coordinates of the datapoints in the chart. If `None`, the longitude data will come from any column named 'lon', 'longitude', 'LON', or 'LONGITUDE'.
* `color`: The color of the circles representing each datapoint. Can be:
	+ `None`, to use the default color.
	+ A hex string like "#ffaa00" or "#ffaa0088".
	+ An RGB or RGBA tuple with the red, green, blue, and alpha components specified as ints from 0 to 255 or floats from 0.0 to 1.0.
	+ The name of the column to use for the color. Cells in this column should contain colors represented as a hex string or color tuple, as described above.
* `size`: The size of the circles representing each point, in meters. This can be:
	+ `None`, to use the default size.
	+ A number like 100, to specify a single size to use for all datapoints.
	+ The name of the column to use for the size. This allows each datapoint to be represented by a circle of a different size.
* `zoom`: Zoom level as specified in [https://wiki.openstreetmap.org/wiki/Zoom_levels](https://wiki.openstreetmap.org/wiki/Zoom_levels).
* `use_container_width`: Whether to override the map's native width with the width of the parent container. If `use_container_width` is `True` (default), Streamlit sets the width of the map to match the width of the parent container. If `use_container_width` is `False`, Streamlit sets the width of the chart to fit its contents according to the plotting library, up to the width of the parent container.
* `width`: Desired width of the chart expressed in pixels. If `width` is `None` (default), Streamlit sets the width of the chart to fit its contents according to the plotting library, up to the width of the parent container. If `width` is greater than the width of the parent container, Streamlit sets the chart width to match the width of the parent container. To use `width`, you must set `use_container_width=False`.
* `height`: Desired height of the chart expressed in pixels. If `height` is `None` (default), Streamlit sets the height of the chart to fit its contents according to the plotting library.

### Examples
```python
import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng

df = pd.DataFrame(
    rng(0).standard_normal((1000, 2)) / [50, 50] + [37.76, -122.4],
    columns=["lat", "lon"],
)

st.map(df)

# You can also customize the size and color of the datapoints:
st.map(df, size=20, color="#0044ff")

# And finally, you can choose different columns to use for the latitude and longitude components, as well as set size and color of each datapoint dynamically based on other columns:
df = pd.DataFrame(
    {
        "col1": rng(0).standard_normal(1000) / 50 + 37.76,
        "col2": rng(1).standard_normal(1000) / 50 + -122.4,
        "col3": rng(2).standard_normal(1000) * 100,
        "col4": rng(3).standard_normal((1000, 4)).tolist(),
    }
)

st.map(df, latitude="col1", longitude="col2", size="col3", color="col4")
```

## element.add_rows
Streamlit Version: 1.50.0, 1.49.0, 1.48.0, 1.47.0, 1.46.0, 1.45.0, 1.44.0, 1.43.0, 1.42.0, 1.41.0, 1.40.0, 1.39.0, 1.38.0, 1.37.0, 1.36.0, 1.35.0, 1.34.0, 1.33.0, 1.32.0, 1.31.0, 1.30.0, 1.29.0, 1.28.0, 1.27.0, 1.26.0, 1.25.0, 1.24.0, 1.23.0, 1.22.0

Concatenate a dataframe to the bottom of the current one.

### Function signature
```python
element.add_rows(data=None, **kwargs)
```
### Parameters

* `data`: Table to concat. Optional.
* `**kwargs`: The named dataset to concat. Optional. You can only pass in 1 dataset (including the one in the `data` parameter).

### Example
```python
import time
import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng

df1 = pd.DataFrame(
    rng(0).standard_normal(size=(50, 20)), columns=("col %d" % i for i in range(20))
)

df2 = pd.DataFrame(
    rng(1).standard_normal(size=(50, 20)), columns=("col %d" % i for i in range(20))
)

my_table = st.table(df1)
time.sleep(1)
my_table.add_rows(df2)

# You can do the same thing with plots. For example, if you want to add more data to a line chart:
my_chart = st.line_chart(df1)
time.sleep(1)
my_chart.add_rows(df2)

# And for plots whose datasets are named, you can pass the data with a keyword argument where the key is the name:
my_chart = st.vega_lite_chart(
    {
        "mark": "line",
        "encoding": {"x": "a", "y": "b"},
        "datasets": {
            "some_fancy_name": df1,  # <-- named dataset
        },
        "data": {"name": "some_fancy_name"},
    }
)
my_chart.add_rows(some_fancy_name=df2)  # <-- name used as keyword
```