```markdown
# st.map

[Original URL](https://docs.streamlit.io/develop/api-reference/charts/st.map)

`st.map` displays a map with points based on geographic data.
```

This is a wrapper around `st.pydeck_chart` to quickly create scatterplot charts on top of a map, with auto-centering and auto-zoom.

When using this command, a service called [Carto](https://carto.com) provides the map tiles to render map content. If you're using advanced PyDeck features you may need to obtain an API key from Carto first. You can do that as `pydeck.Deck(api_keys={"carto": YOUR_KEY})` or by setting the `CARTO_API_KEY` environment variable. See [PyDeck's documentation](https://deckgl.readthedocs.io/en/latest/deck.html) for more information.

Another common provider for map tiles is [Mapbox](https://mapbox.com). If you prefer to use that, you'll need to create an account at [https://mapbox.com](https://mapbox.com) and specify your Mapbox key when creating the `pydeck.Deck` object. You can do that as `pydeck.Deck(api_keys={"mapbox": YOUR_KEY})` or by setting the `MAPBOX_API_KEY` environment variable.

Carto and Mapbox are third-party products and Streamlit accepts no responsibility or liability of any kind for Carto or Mapbox, or for any content or information made available by Carto or Mapbox. The use of Carto or Mapbox is governed by their respective Terms of Use.

### Function signature

[\[source\]](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/elements/map.py#L78 "View st.map source code on GitHub")

```python
st.map(data=None, *, latitude=None, longitude=None, color=None, size=None, zoom=None, use_container_width=True, width=None, height=None)
```

### Parameters

*   **data** (`Anything supported by st.dataframe`)
    The data to be plotted.

*   **latitude** (`str` or `None`)
    The name of the column containing the latitude coordinates of the datapoints in the chart.
    If `None`, the latitude data will come from any column named 'lat', 'latitude', 'LAT', or 'LATITUDE'.

*   **longitude** (`str` or `None`)
    The name of the column containing the longitude coordinates of the datapoints in the chart.
    If `None`, the longitude data will come from any column named 'lon', 'longitude', 'LON', or 'LONGITUDE'.

*   **color** (`str` or `tuple` or `None`)
    The color of the circles representing each datapoint.
    Can be:
    *   `None`, to use the default color.
    *   A hex string like `"#ffaa00"` or `"#ffaa0088"`.
    *   An RGB or RGBA tuple with the red, green, blue, and alpha components specified as ints from 0 to 255 or floats from 0.0 to 1.0.
    *   The name of the column to use for the color. Cells in this column should contain colors represented as a hex string or color tuple, as described above.

*   **size** (`str` or `float` or `None`)
    The size of the circles representing each point, in meters.
    This can be:
    *   `None`, to use the default size.
    *   A number like `100`, to specify a single size to use for all datapoints.
    *   The name of the column to use for the size. This allows each datapoint to be represented by a circle of a different size.

*   **zoom** (`int`)
    Zoom level as specified in [https://wiki.openstreetmap.org/wiki/Zoom_levels](https://wiki.openstreetmap.org/wiki/Zoom_levels).

*   **use_container_width** (`bool`)
    Whether to override the map's native width with the width of the parent container. If `use_container_width` is `True` (default), Streamlit sets the width of the map to match the width of the parent container. If `use_container_width` is `False`, Streamlit sets the width of the chart to fit its contents according to the plotting library, up to the width of the parent container.

*   **width** (`int` or `None`)
    Desired width of the chart expressed in pixels. If `width` is `None` (default), Streamlit sets the width of the chart to fit its contents according to the plotting library, up to the width of the parent container. If `width` is greater than the width of the parent container, Streamlit sets the chart width to match the width of the parent container.
    To use `width`, you must set `use_container_width=False`.

*   **height** (`int` or `None`)
    Desired height of the chart expressed in pixels. If `height` is `None` (default), Streamlit sets the height of the chart to fit its contents according to the plotting library.

#### Examples

```python
import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng

df = pd.DataFrame(
    rng(0).standard_normal((1000, 2)) / [50, 50] + [37.76, -122.4],
    columns=["lat", "lon"],
)

st.map(df)
```

You can also customize the size and color of the datapoints:

```python
st.map(df, size=20, color="#0044ff")
```

And finally, you can choose different columns to use for the latitude and longitude components, as well as set size and color of each datapoint dynamically based on other columns:

```python
import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng

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

### `st.add_rows`

Concatenate a dataframe to the bottom of the current one.

**Function signature**

[\[source\]](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/elements/arrow.py#L866 "View st.add_rows source code on GitHub")

```python
element.add_rows(data=None, **kwargs)
```

**Parameters**

*   `data` (pandas.DataFrame, pandas.Styler, pyarrow.Table, numpy.ndarray, pyspark.sql.DataFrame, snowflake.snowpark.dataframe.DataFrame, Iterable, dict, or None): Table to concat. Optional.
*   `**kwargs` (pandas.DataFrame, numpy.ndarray, Iterable, dict, or None): The named dataset to concat. Optional. You can only pass in 1 dataset (including the one in the `data` parameter).

#### Example

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
```

You can do the same thing with plots. For example, if you want to add more data to a line chart:

```python
# Assuming df1 and df2 from the example above still exist...
my_chart = st.line_chart(df1)
time.sleep(1)
my_chart.add_rows(df2)
```

And for plots whose datasets are named, you can pass the data with a keyword argument where the key is the name:

```python
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

---

[_arrow\_back\_Previous: st.line\_chart](/develop/api-reference/charts/st.line_chart)
[_arrow\_forward\_Next: st.scatter\_chart](/develop/api-reference/charts/st.scatter_chart)

---

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)