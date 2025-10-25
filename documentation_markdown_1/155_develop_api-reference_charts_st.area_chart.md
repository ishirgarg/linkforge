```markdown
# st.area_chart

[Original URL](https://docs.streamlit.io/develop/api-reference/charts/st.area_chart)

`st.area_chart` displays an area chart.

Area charts are a way to show the evolution of one or more numeric variables over a second variable (often time). You can use them to visualize changes in data over time, or to compare the values of different categories.

```python
st.area_chart(data=None, *, x=None, y=None, color=None, width=0, height=0, use_container_width=False, **kwargs)
```


Display an area chart.

This is syntax-sugar around `st.altair_chart`. The main difference is this command uses the data's own column and indices to figure out the chart's Altair spec. As a result this is easier to use for many "just plot this" scenarios, while being less customizable.

Function signature ([source](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/elements/vega_charts.py#L840 "View st.area_chart source code on GitHub"))

```python
st.area_chart(data=None, *, x=None, y=None, x_label=None, y_label=None, color=None, stack=None, width=None, height=None, use_container_width=True)
```

Parameters

*   **data** (Anything supported by `st.dataframe`)

    Data to be plotted.
*   **x** (`str` or `None`)

    Column name or key associated to the x-axis data. If `x` is `None` (default), Streamlit uses the data index for the x-axis values.
*   **y** (`str`, `Sequence` of `str`, or `None`)

    Column name(s) or key(s) associated to the y-axis data. If this is `None` (default), Streamlit draws the data of all remaining columns as data series. If this is a `Sequence` of strings, Streamlit draws several series on the same chart by melting your wide-format table into a long-format table behind the scenes.
*   **x_label** (`str` or `None`)

    The label for the x-axis. If this is `None` (default), Streamlit will use the column name specified in `x` if available, or else no label will be displayed.
*   **y_label** (`str` or `None`)

    The label for the y-axis. If this is `None` (default), Streamlit will use the column name(s) specified in `y` if available, or else no label will be displayed.
*   **color** (`str`, `tuple`, `Sequence` of `str`, `Sequence` of `tuple`, or `None`)

    The color to use for different series in this chart.

    For an area chart with just 1 series, this can be:

    *   `None`, to use the default color.
    *   A hex string like `"#ffaa00"` or `"#ffaa0088"`.
    *   An RGB or RGBA tuple with the red, green, blue, and alpha components specified as ints from 0 to 255 or floats from 0.0 to 1.0.

    For an area chart with multiple series, where the dataframe is in long format (that is, `y` is `None` or just one column), this can be:

    *   `None`, to use the default colors.
    *   The name of a column in the dataset. Data points will be grouped into series of the same color based on the value of this column. In addition, if the values in this column match one of the color formats above (hex string or color tuple), then that color will be used.

        For example: if the dataset has 1000 rows, but this column only contains the values `"adult"`, `"child"`, and `"baby"`, then those 1000 datapoints will be grouped into three series whose colors will be automatically selected from the default palette.

        But, if for the same 1000-row dataset, this column contained the values `"#ffaa00"`, `"#f0f"`, `"#0000ff"`, then then those 1000 datapoints would still be grouped into 3 series, but their colors would be `"#ffaa00"`, `"#f0f"`, `"#0000ff"` this time around.

    For an area chart with multiple series, where the dataframe is in wide format (that is, `y` is a `Sequence` of columns), this can be:

    *   `None`, to use the default colors.
    *   A list of string colors or color tuples to be used for each of the series in the chart. This list should have the same length as the number of y values (e.g. `color=["#fd0", "#f0f", "#04f"]` for three lines).

    You can set the default colors in the `theme.chartCategoryColors` configuration option.
*   **stack** (`bool`, `"normalize"`, `"center"`, or `None`)

    Whether to stack the areas. If this is `None` (default), Streamlit uses Vega's default. Other values can be as follows:

    *   `True`: The areas form a non-overlapping, additive stack within the chart.
    *   `False`: The areas overlap each other without stacking.
    *   `"normalize"`: The areas are stacked and the total height is normalized to 100% of the height of the chart.
    *   `"center"`: The areas are stacked and shifted to center their baseline, which creates a steamgraph.
*   **width** (`int` or `None`)

    Desired width of the chart expressed in pixels. If `width` is `None` (default), Streamlit sets the width of the chart to fit its contents according to the plotting library, up to the width of the parent container. If `width` is greater than the width of the parent container, Streamlit sets the chart width to match the width of the parent container.

    To use `width`, you must set `use_container_width=False`.
*   **height** (`int` or `None`)

    Desired height of the chart expressed in pixels. If `height` is `None` (default), Streamlit sets the height of the chart to fit its contents according to the plotting library.
*   **use_container_width** (`bool`)

    Whether to override `width` with the width of the parent container. If `use_container_width` is `True` (default), Streamlit sets the width of the chart to match the width of the parent container. If `use_container_width` is `False`, Streamlit sets the chart's width according to `width`.

#### Examples

**Example 1: Basic area chart from a dataframe**

If you don't use any of the optional parameters, Streamlit plots each column as a separate area, uses the index as the x values, and labels each series with the column name:

```python
import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng

df = pd.DataFrame(rng(0).standard_normal((20, 3)), columns=["a", "b", "c"])

st.area_chart(df)
```

**Example 2: Area chart from specific dataframe columns**

You can choose different columns to use for the x and y values. If your dataframe is in long format (all y-values in one column), you can set the area colors from another column.

If the column contains color strings, the colors will be applied directly and the series will be unlabeled. If the column contains other values, those values will label each area, and the area colors will be selected from the default color palette. You can configure this color palette in the `theme.chartCategoryColors` configuration option.

```python
import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng

df = pd.DataFrame(
    {
        "col1": list(range(20)) * 3,
        "col2": rng(0).standard_normal(60),
        "col3": ["a"] * 20 + ["b"] * 20 + ["c"] * 20,
    }
)

st.area_chart(df, x="col1", y="col2", color="col3")
```

**Example 3: Area chart from wide-format dataframe**

If your dataframe is in wide format (y-values are in multiple columns), you can pass a list of columns to the y parameter. Each column name becomes a series label. To override the default colors, pass a list of colors to the color parameter, one for each series. If your areas are overlapping, use colors with some transparency (alpha channel) for the best results.

```python
import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng

df = pd.DataFrame(
    {
        "col1": list(range(20)),
        "col2": rng(0).standard_normal(20),
        "col3": rng(1).standard_normal(20),
    }
)

st.area_chart(
    df,
    x="col1",
    y=["col2", "col3"],
    color=["#FF000080", "#0000FF80"],
)
```

**Example 4: Area chart with different stacking**

You can adjust the stacking behavior by setting `stack`. You can create a streamgraph by setting `stack="center"`:

```python
import streamlit as st
from vega_datasets import data
```

```python
df = data.unemployment_across_industries()

st.area_chart(df, x="date", y="count", color="series", stack="center")
```
[<ins>Fullscreen</ins>](https://doc-area-chart-steamgraph.streamlit.app/)

## element.add_rows

Concatenate a dataframe to the bottom of the current one.

**Function signature:**

```python
element.add_rows(data=None, **kwargs)
```

**Parameters:**

*   **data** (`pandas.DataFrame`, `pandas.Styler`, `pyarrow.Table`, `numpy.ndarray`, `pyspark.sql.DataFrame`, `snowflake.snowpark.dataframe.DataFrame`, `Iterable`, `dict`, or `None`)

    Table to concat. Optional.

*   **\*\*kwargs** (`pandas.DataFrame`, `numpy.ndarray`, `Iterable`, `dict`, or `None`)

    The named dataset to concat. Optional. You can only pass in 1 dataset (including the one in the data parameter).

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

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.
