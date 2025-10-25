# st.line_chart

This document provides an overview of the `st.line_chart` function in Streamlit, a tool for creating interactive data visualizations.

**URL:** https://docs.streamlit.io/develop/api-reference/charts/st.line_chart

---

This is the first part of the documentation for `st.line_chart`. It covers the basic introduction and usage of the function.

**Note:** The provided HTML content includes navigation elements, sidebars, and other non-content related information. This markdown conversion focuses solely on the main content of the `st.line_chart` documentation page.

Display a line chart.

This is syntax-sugar around `st.altair_chart`. The main difference is this command uses the data's own column and indices to figure out the chart's Altair spec. As a result this is easier to use for many "just plot this" scenarios, while being less customizable.

### Function signature
[source](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/elements/vega_charts.py#L591 "View st.line_chart source code on GitHub")

```python
st.line_chart(data=None, *, x=None, y=None, x_label=None, y_label=None, color=None, width="stretch", height="content", use_container_width=None)
```

### Parameters

*   **data** (`Anything supported by st.dataframe`)
    Data to be plotted.
*   **x** (`str or None`)
    Column name or key associated to the x-axis data. If `x` is `None` (default), Streamlit uses the data index for the x-axis values.
*   **y** (`str, Sequence of str, or None`)
    Column name(s) or key(s) associated to the y-axis data. If this is `None` (default), Streamlit draws the data of all remaining columns as data series. If this is a `Sequence` of strings, Streamlit draws several series on the same chart by melting your wide-format table into a long-format table behind the scenes.
*   **x_label** (`str or None`)
    The label for the x-axis. If this is `None` (default), Streamlit will use the column name specified in `x` if available, or else no label will be displayed.
*   **y_label** (`str or None`)
    The label for the y-axis. If this is `None` (default), Streamlit will use the column name(s) specified in `y` if available, or else no label will be displayed.
*   **color** (`str, tuple, Sequence of str, Sequence of tuple, or None`)
    The color to use for different lines in this chart.

    For a line chart with just one line, this can be:
    *   `None`, to use the default color.
    *   A hex string like `"#ffaa00"` or `"#ffaa0088"`.
    *   An RGB or RGBA tuple with the red, green, blue, and alpha components specified as ints from 0 to 255 or floats from 0.0 to 1.0.

    For a line chart with multiple lines, where the dataframe is in long format (that is, `y` is `None` or just one column), this can be:
    *   `None`, to use the default colors.
    *   The name of a column in the dataset. Data points will be grouped into lines of the same color based on the value of this column. In addition, if the values in this column match one of the color formats above (hex string or color tuple), then that color will be used.

        For example: if the dataset has 1000 rows, but this column only contains the values "adult", "child", and "baby", then those 1000 datapoints will be grouped into three lines whose colors will be automatically selected from the default palette.

        But, if for the same 1000-row dataset, this column contained the values "#ffaa00", "#f0f", "#0000ff", then then those 1000 datapoints would still be grouped into three lines, but their colors would be "#ffaa00", "#f0f", "#0000ff" this time around.

    For a line chart with multiple lines, where the dataframe is in wide format (that is, `y` is a `Sequence` of columns), this can be:
    *   `None`, to use the default colors.
    *   A list of string colors or color tuples to be used for each of the lines in the chart. This list should have the same length as the number of `y` values (e.g. `color=["#fd0", "#f0f", "#04f"]` for three lines).

    You can set the default colors in the `theme.chartCategoryColors` configuration option.
*   **width** (`"stretch"`, `"content"`, or `int`)
    The width of the chart element. This can be one of the following:
    *   `"stretch"` (default): The width of the element matches the width of the parent container.
    *   `"content"`: The width of the element matches the width of its content, but doesn't exceed the width of the parent container.
    *   An integer specifying the width in pixels: The element has a fixed width. If the specified width is greater than the width of the parent container, the width of the element matches the width of the parent container.
*   **height** (`"content"`, `"stretch"`, or `int`)
    The height of the chart element. This can be one of the following:
    *   `"content"` (default): The height of the element matches the height of its content.
    *   `"stretch"`: The height of the element matches the height of its content or the height of the parent container, whichever is larger. If the element is not in a parent container, the height of the element matches the height of its content.
    *   An integer specifying the height in pixels: The element has a fixed height. If the content is larger than the specified height, scrolling is enabled.
*   **use_container_width** (`bool`)
    _The `use_container_width` parameter is deprecated and will be removed in a future version. Use the `width` parameter with `width="stretch"` instead._

    Whether to override `width` with the width of the parent container. If `use_container_width` is `True` (default), Streamlit sets the width of the chart to match the width of the parent container. If `use_container_width` is `False`, Streamlit sets the chart's width according to `width`.

#### Examples

**Example 1: Basic line chart from a dataframe**

If you don't use any of the optional parameters, Streamlit plots each column as a separate line, uses the index as the x values, and labels each series with the column name:

```python
import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng

df = pd.DataFrame(rng(0).standard_normal((20, 3)), columns=["a", "b", "c"])

st.line_chart(df)
```

**Example 2: Line chart from specific dataframe columns**

You can choose different columns to use for the x and y values. If your dataframe is in long format (all y-values in one column), you can set the line colors from another column.

If the column contains color strings, the colors will be applied directly and the series will be unlabeled. If the column contains other values, those values will label each line, and the line colors will be selected from the default color palette. You can configure this color palette in the `theme.chartCategoryColors` configuration option.

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

st.line_chart(df, x="col1", y="col2", color="col3")
```

**Example 3: Line chart from wide-format dataframe**

If your dataframe is in wide format (y-values are in multiple columns), you can pass a list of columns to the `y` parameter. Each column name becomes a series label. To override the default colors, pass a list of colors to the `color` parameter, one for each series:

```python
import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng

df = pd.DataFrame(rng(0).standard_normal((20, 3)), columns=["a", "b", "c"])

st.line_chart(
    df,
    x="a",
    y=["b", "c"],
    color=["#FF0000", "#0000FF"],
)
```

## element.add_rows

Concatenate a dataframe to the bottom of the current one.

## Function signature

```python
element.add_rows(data=None, **kwargs)
```

[\[source\]](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/elements/arrow.py#L866 "View st.add_rows source code on GitHub")

## Parameters

*   **data** (`pandas.DataFrame`, `pandas.Styler`, `pyarrow.Table`, `numpy.ndarray`, `pyspark.sql.DataFrame`, `snowflake.snowpark.dataframe.DataFrame`, `Iterable`, `dict`, or `None`)

    Table to concat. Optional.
*   **\*\*kwargs** (`pandas.DataFrame`, `numpy.ndarray`, `Iterable`, `dict`, or `None`)

    The named dataset to concat. Optional. You can only pass in 1 dataset (including the one in the data parameter).

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

[Previous: st.bar\_chart](/develop/api-reference/charts/st.bar_chart) | [Next: st.map](/develop/api-reference/charts/st.map)

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.
