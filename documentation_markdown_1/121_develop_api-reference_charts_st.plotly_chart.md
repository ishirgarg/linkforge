# st.plotly_chart

[Original URL](https://docs.streamlit.io/develop/api-reference/charts/st.plotly_chart)

`st.plotly_chart` displays an interactive Plotly chart.


You must install `plotly>=4.0.0` to use this command. Your app's performance may be enhanced by installing `orjson` as well. You can install all charting dependencies (except Bokeh) as an extra with Streamlit:

```bash
pip install streamlit[charts]
```

### Function signature

```python
st.plotly_chart(figure_or_data, use_container_width=True, *, theme="streamlit", key=None, on_select="ignore", selection_mode=('points', 'box', 'lasso'), config=None, **kwargs)
```

### Parameters

*   **`figure_or_data`** (`plotly.graph_objs.Figure`, `plotly.graph_objs.Data`, or `dict`/`list` of `plotly.graph_objs.Figure`/`Data`)
    The Plotly Figure or Data object to render. See [https://plot.ly/python/](https://plot.ly/python/) for examples of graph descriptions.

    **Note:** If your chart contains more than 1000 data points, Plotly will use a WebGL renderer to display the chart. Different browsers have different limits on the number of WebGL contexts per page. If you have multiple WebGL contexts on a page, you may need to switch to SVG rendering mode. You can do this by setting `render_mode="svg"` within the figure. For example, the following code defines a Plotly Express line chart that will render in SVG mode when passed to `st.plotly_chart`: `px.line(df, x="x", y="y", render_mode="svg")`.

*   **`use_container_width`** (`bool`)
    Whether to override the figure's native width with the width of the parent container. If `use_container_width` is `True` (default), Streamlit sets the width of the figure to match the width of the parent container. If `use_container_width` is `False`, Streamlit sets the width of the chart to fit its contents according to the plotting library, up to the width of the parent container.

*   **`theme`** (`"streamlit"` or `None`)
    The theme of the chart. If `theme` is `"streamlit"` (default), Streamlit uses its own design default. If `theme` is `None`, Streamlit falls back to the default behavior of the library.

    The `"streamlit"` theme can be partially customized through the configuration options `theme.chartCategoricalColors` and `theme.chartSequentialColors`. Font configuration options are also applied.

*   **`key`** (`str`)
    An optional string to use for giving this element a stable identity. If `key` is `None` (default), this element's identity will be determined based on the values of the other parameters.

    Additionally, if selections are activated and `key` is provided, Streamlit will register the key in Session State to store the selection state. The selection state is read-only.

*   **`on_select`** (`"ignore"` or `"rerun"` or `callable`)
    How the figure should respond to user selection events. This controls whether or not the figure behaves like an input widget. `on_select` can be one of the following:
    *   `"ignore"` (default): Streamlit will not react to any selection events in the chart. The figure will not behave like an input widget.
    *   `"rerun"`: Streamlit will rerun the app when the user selects data in the chart. In this case, `st.plotly_chart` will return the selection data as a dictionary.
    *   A `callable`: Streamlit will rerun the app and execute the callable as a callback function before the rest of the app. In this case, `st.plotly_chart` will return the selection data as a dictionary.

*   **`selection_mode`** (`"points"`, `"box"`, `"lasso"` or an `Iterable` of these)
    The selection mode of the chart. This can be one of the following:
    *   `"points"`: The chart will allow selections based on individual data points.
    *   `"box"`: The chart will allow selections based on rectangular areas.
    *   `"lasso"`: The chart will allow selections based on freeform areas.
    *   An `Iterable` of the above options: The chart will allow selections based on the modes specified.

    All selections modes are activated by default.

*   **`config`** (`dict` or `None`)
    A dictionary of Plotly configuration options. This is passed to Plotly's `show()` function. For more information about Plotly configuration options, see Plotly's documentation on [Configuration in Python](https://plotly.com/python/configuration-options/).

*   **`**kwargs`** (`null`)
    _delete_

    `**kwargs` are deprecated and will be removed in a future release. Use `config` instead.

    Additional arguments accepted by Plotly's `plot()` function.

    This supports `config`, a dictionary of Plotly configuration options. For more information about Plotly configuration options, see Plotly's documentation on [Configuration in Python](https://plotly.com/python/configuration-options/).

### Returns

*   (`element` or `dict`)
    If `on_select` is `"ignore"` (default), this command returns an internal placeholder for the chart element. Otherwise, this command returns a dictionary-like object that supports both key and attribute notation. The attributes are described by the `PlotlyState` dictionary schema.

### Examples

**Example 1: Basic Plotly chart**

The example below comes from the examples at [https://plot.ly/python](https://plot.ly/python). Note that `plotly.figure_factory` requires `scipy` to run.

```python
import plotly.figure_factory as ff
import streamlit as st
from numpy.random import default_rng as rng

hist_data = [
    rng(0).standard_normal(200) - 2,
    rng(1).standard_normal(200),
    rng(2).standard_normal(200) + 2,
]
group_labels = ["Group 1", "Group 2", "Group 3"]

fig = ff.create_distplot(
    hist_data, group_labels, bin_size=[0.1, 0.25, 0.5]
)

st.plotly_chart(fig)
```

**Example 2: Plotly Chart with configuration**

By default, Plotly charts have scroll zoom enabled. If you have a longer page and want to avoid conflicts between page scrolling and zooming, you can use Plotly's configuration options to disable scroll zoom. In the following example, scroll zoom is disabled, but the zoom buttons are still enabled in the modebar.

```python
import plotly.graph_objects as go
import streamlit as st

fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x=[1, 2, 3, 4, 5],
        y=[1, 3, 2, 5, 4]
    )
)

st.plotly_chart(fig, config = {'scrollZoom': False})
```

## Chart selections

### PlotlyState

```markdown
The schema for the Plotly chart event state.

The event state is stored in a dictionary-like object that supports both key and attribute notation. Event states cannot be programmatically changed or set through Session State.

Only selection events are supported at this time.

**Attributes**

*   `selection` (dict)
    The state of the `on_select` event. This attribute returns a dictionary-like object that supports both key and attribute notation. The attributes are described by the `PlotlySelectionState` dictionary schema.

#### Example

Try selecting points by any of the three available methods (direct click, box, or lasso). The current selection state is available through Session State or as the output of the chart function.

```python
import plotly.express as px
import streamlit as st

df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length")

event = st.plotly_chart(fig, key="iris", on_select="rerun")

event
```

### PlotlySelectionState

The schema for the Plotly chart selection state.

The selection state is stored in a dictionary-like object that supports both key and attribute notation. Selection states cannot be programmatically changed or set through Session State.

**Attributes**

*   `points` (list\[dict\[str, Any\]\])
    The selected data points in the chart, including the data points selected by the box and lasso mode. The data includes the values associated to each point and a point index used to populate `point_indices`. If additional information has been assigned to your points, such as size or legend group, this is also included.
*   `point_indices` (list\[int\])
    The numerical indices of all selected data points in the chart. The details of each identified point are included in `points`.
*   `box` (list\[dict\[str, Any\]\])
    The metadata related to the box selection. This includes the coordinates of the selected area.
*   `lasso` (list\[dict\[str, Any\]\])
    The metadata related to the lasso selection. This includes the coordinates of the selected area.

#### Example

When working with more complicated graphs, the `points` attribute displays additional information. Try selecting points in the following example:

```python
import plotly.express as px
import streamlit as st

df = px.data.iris()
fig = px.scatter(
    df,
    x="sepal_width",
    y="sepal_length",
    color="species",
    size="petal_length",
    hover_data=["petal_width"],
)

event = st.plotly_chart(fig, key="iris", on_select="rerun")

event.selection
```

This is an example of the selection state when selecting a single point:

```json
{
  "points": [
    {
      "curve_number": 2,
      "point_number": 9,
      "point_index": 9,
      "x": 3.6,
      "y": 7.2,
      "customdata": [
        2.5
      ],
      "marker_size": 6.1,
      "legendgroup": "virginica"
    }
  ],
  "point_indices": [
    9
  ],
  "box": [],
  "lasso": []
}
```

## Theming

Plotly charts are displayed using the Streamlit theme by default. This theme is sleek, user-friendly, and incorporates Streamlit's color palette. The added benefit is that your charts better integrate with the rest of your app's design.

The Streamlit theme is available from Streamlit 1.16.0 through the `theme="streamlit"` keyword argument. To disable it, and use Plotly's native theme, use `theme=None` instead.

Let's look at an example of charts with the Streamlit theme and the native Plotly theme:

```python
import plotly.express as px
import streamlit as st

df = px.data.gapminder()
fig = px.scatter(
    df.query("year==2007"),
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    hover_name="country",
    log_x=True,
    size_max=60,
)
tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])

with tab1:
    # Use the Streamlit theme.
    # This is the default. So you can also omit the theme argument.
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)

with tab2:
    # Use the native Plotly theme.
    st.plotly_chart(fig, theme=None, use_container_width=True)
```

Click the tabs in the interactive app below to see the charts with the Streamlit theme enabled and disabled.

If you're wondering if your own customizations will still be taken into account, don't worry! You can still make changes to your chart configurations. In other words, although we now enable the Streamlit theme by default, you can overwrite it with custom colors or fonts. For example, if you want a chart line to be green instead of the default red, you can do it!

Here's an example of an Plotly chart where a custom color scale is defined and reflected:

```python
import plotly.express as px
import streamlit as st

st.subheader("Define a custom colorscale")
df = px.data.iris()
fig = px.scatter(
    df,
    x="sepal_width",
    y="sepal_length",
    color="sepal_length",
    color_continuous_scale="reds",
)
tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])

with tab1:
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)

with tab2:
    st.plotly_chart(fig, theme=None, use_container_width=True)
```

Notice how the custom color scale is still reflected in the chart, even when the Streamlit theme is enabled 👇

For many more examples of Plotly charts with and without the Streamlit theme, check out the [plotly.streamlit.app](https://plotly.streamlit.app).

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---
```