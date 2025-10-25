```markdown
# st.table

[Original URL](https://docs.streamlit.io/develop/api-reference/data/st.table)

#### Tip

Static tables with `st.table` are the most basic way to display dataframes. For the majority of cases, we recommend using [`st.dataframe`](/develop/api-reference/data/st.dataframe) to display interactive dataframes, and [`st.data_editor`](/develop/api-reference/data/st.data_editor) to let users edit dataframes.

## st.table

Display a static table.

While st.dataframe is geared towards large datasets and interactive data exploration, st.table is useful for displaying small, styled tables without sorting or scrolling. For example, st.table may be the preferred way to display a confusion matrix or leaderboard. Additionally, st.table supports Markdown.

**Function signature**

```python
st.table(data=None, *, border=True)
```

**Parameters**

*   `data` (Anything supported by st.dataframe)

    The table data.

    All cells including the index and column headers can optionally contain GitHub-flavored Markdown. Syntax information can be found at: [https://github.github.com/gfm](https://github.github.com/gfm).

    See the body parameter of [st.markdown](https://docs.streamlit.io/develop/api-reference/text/st.markdown) for additional, supported Markdown directives.

*   `border` (bool or "horizontal")

    Whether to show borders around the table and between cells. This can be one of the following:

    *   `True` (default): Show borders around the table and between cells.
    *   `False`: Don't show any borders.
    *   `"horizontal"`: Show only horizontal borders between rows.

#### Examples

**Example 1: Display a confusion matrix as a static table**

```python
import pandas as pd
import streamlit as st

confusion_matrix = pd.DataFrame(
    {
        "Predicted Cat": [85, 3, 2, 1],
        "Predicted Dog": [2, 78, 4, 0],
        "Predicted Bird": [1, 5, 72, 3],
        "Predicted Fish": [0, 2, 1, 89],
    },
    index=["Actual Cat", "Actual Dog", "Actual Bird", "Actual Fish"],
)
st.table(confusion_matrix)
```

**Example 2: Display a product leaderboard with Markdown and horizontal borders**

```python
import streamlit as st

product_data = {
    "Product": [
        ":material/devices: Widget Pro",
        ":material/smart_toy: Smart Device",
        ":material/inventory: Premium Kit",
    ],
    "Category": [":blue[Electronics]", ":green[IoT]", ":violet[Bundle]"],
    "Stock": ["🟢 Full", "🟡 Low", "🔴 Empty"],
    "Units sold": [1247, 892, 654],
    "Revenue": [125000, 89000, 98000],
}
st.table(product_data, border="horizontal")
```


### `st.add_rows`

Concatenate a dataframe to the bottom of the current one.

#### Function signature

```python
element.add_rows(data=None, **kwargs)
```

#### Parameters

*   **`data`** (`pandas.DataFrame`, `pandas.Styler`, `pyarrow.Table`, `numpy.ndarray`, `pyspark.sql.DataFrame`, `snowflake.snowpark.dataframe.DataFrame`, `Iterable`, `dict`, or `None`)
    Table to concat. Optional.
*   **`**kwargs`** (`pandas.DataFrame`, `numpy.ndarray`, `Iterable`, `dict`, or `None`)
    The named dataset to concat. Optional. You can only pass in 1 dataset (including the one in the `data` parameter).

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

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.