```markdown
# st.pydeck_chart

[Original URL](https://docs.streamlit.io/develop/api-reference/charts/st.pydeck_chart)

## st.pydeck_chart
```

This command draws a chart using the PyDeck library, supporting 3D maps, point clouds, and more. You can find more information about PyDeck at [https://deckgl.readthedocs.io/en/latest/](https://deckgl.readthedocs.io/en/latest/).

Additional useful documentation:

*   DeckGL docs: [https://github.com/uber/deck.gl/tree/master/docs](https://github.com/uber/deck.gl/tree/master/docs)
*   DeckGL JSON docs: [https://github.com/uber/deck.gl/tree/master/modules/json](https://github.com/uber/deck.gl/tree/master/modules/json)

When using this command, the service [Carto](https://carto.com) provides the map tiles for rendering map content. If you utilize advanced PyDeck features, you might need to obtain an API key from Carto. This can be done via `pydeck.Deck(api_keys={"carto": YOUR_KEY})` or by setting the `CARTO_API_KEY` environment variable. Refer to [PyDeck's documentation](https://deckgl.readthedocs.io/en/latest/deck.html) for more details.

Another common provider for map tiles is [Mapbox](https://mapbox.com). If you prefer to use Mapbox, you'll need to create an account at [https://mapbox.com](https://mapbox.com) and specify your Mapbox key when creating the `pydeck.Deck` object. This can be done using `pydeck.Deck(api_keys={"mapbox": YOUR_KEY})` or by setting the `MAPBOX_API_KEY` environment variable.

Carto and Mapbox are third-party products, and Streamlit assumes no responsibility or liability for them or any content or information they provide. Your use of Carto or Mapbox is governed by their respective Terms of Use.

**Note**

Pydeck utilizes two WebGL contexts per chart. Different browsers have varying limits on the number of WebGL contexts per page. Exceeding this limit will cause the oldest contexts to be dropped to accommodate new ones. To mitigate this in most browsers, avoid displaying more than eight Pydeck charts on a single page.

### Function signature

[View `st.pydeck_chart` source code on GitHub](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/elements/deck_gl_json_chart.py#L290)

```python
st.pydeck_chart(pydeck_obj=None, *, use_container_width=True, width=None, height=None, selection_mode="single-object", on_select="ignore", key=None)
```

### Parameters

*   **`pydeck_obj`** (`pydeck.Deck` or `None`):
    Object specifying the PyDeck chart to draw.

*   **`use_container_width`** (`bool`):
    Whether to override the figure's native width with the width of the parent container. If `True` (default), Streamlit sets the figure's width to match the parent container. If `False`, Streamlit sets the chart's width to fit its contents according to the plotting library, up to the parent container's width.

*   **`width`** (`int` or `None`):
    Desired width of the chart in pixels. If `None` (default), Streamlit sets the chart's width to fit its contents according to the plotting library, up to the parent container's width. If `width` exceeds the parent container's width, Streamlit will match the chart width to the parent container's width.
    To use `width`, you must set `use_container_width=False`.

*   **`height`** (`int` or `None`):
    Desired height of the chart in pixels. If `None` (default), Streamlit sets the chart's height to fit its contents according to the plotting library.

*   **`on_select`** (`"ignore"` or `"rerun"` or `callable`):
    Determines how the figure responds to user selection events, controlling whether the chart behaves as an input widget. `on_select` can be one of the following:
    *   `"ignore"` (default): Streamlit will not react to any selection events in the chart. The figure will not function as an input widget.
    *   `"rerun"`: Streamlit will rerun the app when the user selects data in the chart. In this case, `st.pydeck_chart` will return the selection data as a dictionary.
    *   A `callable`: Streamlit will rerun the app and execute the callable as a callback function before the rest of the app. In this case, `st.pydeck_chart` will return the selection data as a dictionary.

    If `on_select` is not `"ignore"`, all layers must have a declared `id` to maintain chart state across reruns.

*   **`selection_mode`** (`"single-object"` or `"multi-object"`):
    The selection mode of the chart. This can be one of the following:
    *   `"single-object"` (default): Only one object can be selected at a time.
    *   `"multi-object"`: Multiple objects can be selected at a time.

*   **`key`** (`str`):
    An optional string to provide a stable identity for this element. If `None` (default), the element's identity is determined by its parameters.
    Additionally, if selections are activated and a `key` is provided, Streamlit will register the key in Session State to store the selection state. This selection state is read-only.

### Returns

*   (`element` or `dict`):
    If `on_select` is `"ignore"` (default), this command returns an internal placeholder for the chart element. Otherwise, this method returns a dictionary-like object that supports both key and attribute notation. The attributes are described by the PydeckState dictionary schema.

#### Example

Here's a chart using a `HexagonLayer` and a `ScatterplotLayer`. It dynamically adopts either a light or dark map style based on the currently active Streamlit theme:

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

**Note**

To ensure the PyDeck chart's style aligns with Streamlit's theme, set `map_style=None` within the `pydeck.Deck` object.

## Chart selections

### PydeckState

### PyDeck Event State

The event state is stored in a dictionary-like object that supports both key and attribute notation. Event states cannot be programmatically changed or set through Session State.

Only selection events are supported at this time.

#### Attributes

*   **selection** (`dict`): The state of the `on_select` event. This attribute returns a dictionary-like object that supports both key and attribute notation. The attributes are described by the `PydeckSelectionState` dictionary schema.

### PydeckSelectionState

The schema for the PyDeck chart selection state.

The selection state is stored in a dictionary-like object that supports both key and attribute notation. Selection states cannot be programmatically changed or set through Session State.

You must define `id` in `pydeck.Layer` to ensure statefulness when using selections with `st.pydeck_chart`.

#### Attributes

*   **indices** (`dict[str, list[int]]`): A dictionary of selected objects by layer. Each key in the dictionary is a layer id, and each value is a list of object indices within that layer.
*   **objects** (`dict[str, list[dict[str, Any]]]`): A dictionary of object attributes by layer. Each key in the dictionary is a layer id, and each value is a list of metadata dictionaries for the selected objects in that layer.

#### Examples

The following example has multi-object selection enabled. The chart displays US state capitals by population (2023 US Census estimate). You can access this [data](https://github.com/streamlit/docs/blob/main/python/api-examples-source/data/capitals.csv) from GitHub.

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

This is an example of the selection state when selecting a single object from a layer with id, "captial-cities":

```json
{
  "indices":{
    "capital-cities":[
      2
    ]
  },
  "objects":{
    "capital-cities":[
      {
        "Abbreviation":" AZ"
        "Capital":"Phoenix"
        "Latitude":33.448457
        "Longitude":-112.073844
        "Population":1650070
        "State":" Arizona"
        "size":165007.0
      }
    ]
  }
}
```