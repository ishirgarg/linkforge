Here is the HTML converted to clean Markdown:

# st.pydeck_chart - Streamlit Docs
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

### Breadcrumbs
* [Home](/)
* [Develop](/develop)
* [API reference](/develop/api-reference)
* [Chart elements](/develop/api-reference/charts)
* [st.pydeck_chart](/develop/api-reference/charts/st.pydeck_chart)

Here is the document converted to clean Markdown:
### st.pydeck_chart

Draw a chart using the PyDeck library.

This supports 3D maps, point clouds, and more! More info about PyDeck at [https://deckgl.readthedocs.io/en/latest/](https://deckgl.readthedocs.io/en/latest/).

These docs are also quite useful:

* DeckGL docs: [https://github.com/uber/deck.gl/tree/master/docs](https://github.com/uber/deck.gl/tree/master/docs)
* DeckGL JSON docs: [https://github.com/uber/deck.gl/tree/master/modules/json](https://github.com/uber/deck.gl/tree/master/modules/json)

When using this command, a service called [Carto](https://carto.com) provides the map tiles to render map content. If you're using advanced PyDeck features, you may need to obtain an API key from Carto first. You can do that as `pydeck.Deck(api_keys={"carto": YOUR_KEY})` or by setting the `CARTO_API_KEY` environment variable. See [PyDeck's documentation](https://deckgl.readthedocs.io/en/latest/deck.html) for more information.

Another common provider for map tiles is [Mapbox](https://mapbox.com). If you prefer to use that, you'll need to create an account at [https://mapbox.com](https://mapbox.com) and specify your Mapbox key when creating the `pydeck.Deck` object. You can do that as `pydeck.Deck(api_keys={"mapbox": YOUR_KEY})` or by setting the `MAPBOX_API_KEY` environment variable.

Carto and Mapbox are third-party products and Streamlit accepts no responsibility or liability of any kind for Carto or Mapbox, or for any content or information made available by Carto or Mapbox. The use of Carto or Mapbox is governed by their respective Terms of Use.

#### Note

Pydeck uses two WebGL contexts per chart, and different browsers have different limits on the number of WebGL contexts per page. If you exceed this limit, the oldest contexts will be dropped to make room for the new ones. To avoid this limitation in most browsers, don't display more than eight Pydeck charts on a single page.

#### Function signature

```python
st.pydeck_chart(
    pydeck_obj=None, 
    *, 
    use_container_width=True, 
    width=None, 
    height=None, 
    selection_mode="single-object", 
    on_select="ignore", 
    key=None
)
```

#### Parameters

* `pydeck_obj`: Object specifying the PyDeck chart to draw.
* `use_container_width`: Whether to override the figure's native width with the width of the parent container.
* `width`: Desired width of the chart expressed in pixels.
* `height`: Desired height of the chart expressed in pixels.
* `on_select`: How the figure should respond to user selection events.
* `selection_mode`: The selection mode of the chart.
* `key`: An optional string to use for giving this element a stable identity.

#### Returns

If `on_select` is "ignore" (default), this command returns an internal placeholder for the chart element. Otherwise, this method returns a dictionary-like object that supports both key and attribute notation.

#### Example

Here's a chart using a HexagonLayer and a ScatterplotLayer. It uses either the light or dark map style, based on which Streamlit theme is currently active:
```python
import pandas as pd
import pydeck as pdk
import streamlit as st
from numpy.random import default_rng as rng

df = pd.DataFrame(
    rng(0).standard_normal((1000, 2)) / [50, 50] + [37.76, -122.4],
    columns=["lat", "lon"],
)

st.pydeck_chart(
    pdk.Deck(
        map_style=None,  # Use Streamlit theme to pick map style
        initial_view_state=pdk.ViewState(
            latitude=37.76,
            longitude=-122.4,
            zoom=11,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
                "HexagonLayer",
                data=df,
                get_position="[lon, lat]",
                radius=200,
                elevation_scale=4,
                elevation_range=[0, 1000],
                pickable=True,
                extruded=True,
            ),
            pdk.Layer(
                "ScatterplotLayer",
                data=df,
                get_position="[lon, lat]",
                get_color="[200, 30, 0, 160]",
                get_radius=200,
            ),
        ],
    )
)
```

### Chart selections

#### PydeckState

The schema for the PyDeck event state.

* `selection`: The state of the on_select event.

#### PydeckSelectionState

The schema for the PyDeck chart selection state.

* `indices`: A dictionary of selected objects by layer.
* `objects`: A dictionary of object attributes by layer.

#### Examples

The following example has multi-object selection enabled. The chart displays US state capitals by population (2023 US Census estimate).
```python
import streamlit as st
import pydeck
import pandas as pd

capitals = pd.read_csv(
    "capitals.csv",
    header=0,
    names=[
        "Capital",
        "State",
        "Abbreviation",
        "Latitude",
        "Longitude",
        "Population",
    ],
)
capitals["size"] = capitals.Population / 10

point_layer = pydeck.Layer(
    "ScatterplotLayer",
    data=capitals,
    id="capital-cities",
    get_position=["Longitude", "Latitude"],
    get_color="[255, 75, 75]",
    pickable=True,
    auto_highlight=True,
    get_radius="size",
)

view_state = pydeck.ViewState(
    latitude=40, longitude=-117, controller=True, zoom=2.4, pitch=30
)

chart = pydeck.Deck(
    point_layer,
    initial_view_state=view_state,
    tooltip={"text": "{Capital}, {Abbreviation}\nPopulation: {Population}"},
)

event = st.pydeck_chart(chart, on_select="rerun", selection_mode="multi-object")

event.selection
```
This is an example of the selection state when selecting a single object from a layer with id, "capital-cities":
```json
{
  "indices": {
    "capital-cities": [
      2
    ]
  },
  "objects": {
    "capital-cities": [
      {
        "Abbreviation": "AZ",
        "Capital": "Phoenix",
        "Latitude": 33.448457,
        "Longitude": -112.073844,
        "Population": 1650070,
        "State": "Arizona",
        "size": 165007.0
      }
    ]
  }
}
```