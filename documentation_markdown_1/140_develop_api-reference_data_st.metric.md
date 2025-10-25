```markdown
# st.metric

[Original URL](https://docs.streamlit.io/develop/api-reference/data/st.metric)

`st.metric` displays a single, important value, which can be optionally compared to a previous value.

```python
streamlit.metric(label, value, delta=None, delta_color="normal", help=None, *, inverse_delta=None)
```


Display a metric in big bold font, with an optional indicator of how the metric changed.

Tip: If you want to display a large number, it may be a good idea to shorten it using packages like [millify](https://github.com/azaitsev/millify) or [numerize](https://github.com/davidsa03/numerize). E.g. 1234 can be displayed as 1.2k using `st.metric("Short number", millify(1234))`.

### Function signature

[\[source\]](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/elements/metric.py#L57 "View st.metric source code on GitHub")

```python
st.metric(
    label,
    value,
    delta=None,
    delta_color="normal",
    *,
    help=None,
    label_visibility="visible",
    border=False,
    width="stretch",
    height="content",
    chart_data=None,
    chart_type="line"
)
```

### Parameters

*   **label** (`str`)
    The header or title for the metric. The label can optionally contain GitHub-flavored Markdown of the following types: Bold, Italics, Strikethroughs, Inline Code, Links, and Images. Images display like icons, with a max height equal to the font height.

    Unsupported Markdown elements are unwrapped so only their children (text contents) render. Display unsupported elements as literal characters by backslash-escaping them. E.g., "1\. Not an ordered list".

    See the body parameter of [st.markdown](https://docs.streamlit.io/develop/api-reference/text/st.markdown) for additional, supported Markdown directives.

*   **value** (`int`, `float`, `decimal.Decimal`, `str`, or `None`)
    Value of the metric. `None` is rendered as a long dash.

*   **delta** (`int`, `float`, `decimal.Decimal`, `str`, or `None`)
    Indicator of how the metric changed, rendered with an arrow below the metric. If `delta` is negative (`int`/`float`) or starts with a minus sign (`str`), the arrow points down and the text is red; else the arrow points up and the text is green. If `None` (default), no delta indicator is shown.

*   **delta\_color** (`"normal"`, `"inverse"`, or `"off"`)
    If `"normal"` (default), the delta indicator is shown as described above. If `"inverse"`, it is red when positive and green when negative. This is useful when a negative change is considered good, e.g. if cost decreased. If `"off"`, delta is shown in gray regardless of its value.

*   **help** (`str` or `None`)
    A tooltip that gets displayed next to the metric label. Streamlit only displays the tooltip when `label_visibility="visible"`. If this is `None` (default), no tooltip is displayed.

    The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of `st.markdown`.

*   **label\_visibility** (`"visible"`, `"hidden"`, or `"collapsed"`)
    The visibility of the label. The default is `"visible"`. If this is `"hidden"`, Streamlit displays an empty spacer instead of the label, which can help keep the widget aligned with other widgets. If this is `"collapsed"`, Streamlit displays no label or spacer.

*   **border** (`bool`)
    Whether to show a border around the metric container. If this is `False` (default), no border is shown. If this is `True`, a border is shown.

*   **width** (`"stretch"`, `"content"`, or `int`)
    The width of the metric element. This can be one of the following:
    *   `"stretch"` (default): The width of the element matches the width of the parent container.
    *   `"content"`: The width of the element matches the width of its content, but doesn't exceed the width of the parent container.
    *   An integer specifying the width in pixels: The element has a fixed width. If the specified width is greater than the width of the parent container, the width of the element matches the width of the parent container.

*   **height** (`"content"`, `"stretch"`, or `int`)
    The height of the metric element. This can be one of the following:
    *   `"content"` (default): The height of the element matches the height of its content.
    *   `"stretch"`: The height of the element matches the height of its content or the height of the parent container, whichever is larger. If the element is not in a parent container, the height of the element matches the height of its content.
    *   An integer specifying the height in pixels: The element has a fixed height. If the content is larger than the specified height, scrolling is enabled.

*   **chart\_data** (`Iterable` or `None`)
    A sequence of numeric values to display as a sparkline chart. If this is `None` (default), no chart is displayed. The sequence can be anything supported by `st.dataframe`, including a list or set. If the sequence is dataframe-like, the first column will be used. Each value will be cast to `float` internally by default.

*   **chart\_type** (`"line"`, `"bar"`, or `"area"`)
    The type of sparkline chart to display. This can be one of the following:
    *   `"line"` (default): A simple sparkline.
    *   `"area"`: A sparkline with area shading.
    *   `"bar"`: A bar chart.

### Examples

**Example 1: Show a metric**

```python
import streamlit as st

st.metric(label="Temperature", value="70 °F", delta="1.2 °F")
```

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen _open\_in\_new_](https://doc-metric-example1.streamlit.app//?utm_medium=oembed&)

**Example 2: Create a row of metrics**

`st.metric` looks especially nice in combination with `st.columns`.

```python
import streamlit as st

col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")
```

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen _open\_in\_new_](https://doc-metric-example2.streamlit.app//?utm_medium=oembed&)

**Example 3: Modify the delta indicator**

The delta indicator color can also be inverted or turned off.

```python
import streamlit as st

st.metric(label="Gas price", value=4, delta=-0.5, delta_color="inverse")

st.metric(
    label="Active developers",
    value=123,
    delta=123,
    delta_color="off",
)
```

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen _open\_in\_new_](https://doc-metric-example3.streamlit.app//?utm_medium=oembed&)

**Example 4: Create a grid of metric cards**

Add borders to your metrics to create a dashboard look.

```python
import streamlit as st

a, b = st.columns(2)
c, d = st.columns(2)

a.metric("Temperature", "30°F", "-9°F", border=True)
b.metric("Wind", "4 mph", "2 mph", border=True)

c.metric("Humidity", "77%", "5%", border=True)
d.metric("Pressure", "30.34 inHg", "-2 inHg", border=True)
```

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen _open\_in\_new_](https://doc-metric-example4.streamlit.app//?utm_medium=oembed&)

**Example 5: Show sparklines**

To show trends over time, add sparklines.

```python
import streamlit as st
from numpy.random import default_rng as rng

changes = list(rng(4).standard_normal(20))
data = [sum(changes[:i]) for i in range(20)]
delta = round(data[-1], 2)

row = st.container(horizontal=True)
with row:
    st.metric(
        "Line", 10, delta, chart_data=data, chart_type="line", border=True
    )
    st.metric(
        "Area", 10, delta, chart_data=data, chart_type="area", border=True
    )
    st.metric(
        "Bar", 10, delta, chart_data=data, chart_type="bar", border=True
    )
```

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen _open\_in\_new_](https://doc-metric-example5.streamlit.app//?utm_medium=oembed&)

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.
