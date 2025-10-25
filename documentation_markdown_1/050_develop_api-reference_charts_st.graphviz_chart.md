# st.graphviz_chart

**URL:** https://docs.streamlit.io/develop/api-reference/charts/st.graphviz_chart

This document describes the `st.graphviz_chart` function in Streamlit, which allows you to display Graphviz charts within your Streamlit applications.

---

**Note:** This is the first part of the conversion. The full content will be provided in subsequent parts.

### Important

You must install `graphviz>=0.19.0` to use this command. You can install all charting dependencies (except Bokeh) as an extra with Streamlit:

```bash
pip install streamlit[charts]
```

### Function signature

[`source`](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/elements/graphviz_chart.py#L51)

```python
st.graphviz_chart(figure_or_dot, use_container_width=None, *, width="content", height="content")
```

### Parameters

*   **`figure_or_dot`** (`graphviz.dot.Graph`, `graphviz.dot.Digraph`, `graphviz.sources.Source`, `str`)
    The Graphlib graph object or dot string to display.

*   **`use_container_width`** (`bool`)
    _Deprecated_: `use_container_width` is deprecated and will be removed in a future release. For `use_container_width=True`, use `width="stretch"`. For `use_container_width=False`, use `width="content"`.

    Whether to override the figure's native width with the width of the parent container. If `use_container_width` is `False` (default), Streamlit sets the width of the chart to fit its contents according to the plotting library, up to the width of the parent container. If `use_container_width` is `True`, Streamlit sets the width of the figure to match the width of the parent container.

*   **`width`** (`"content"`, `"stretch"`, or `int`)
    The width of the chart element. This can be one of the following:
    *   `"content"` (default): The width of the element matches the width of its content, but doesn't exceed the width of the parent container.
    *   `"stretch"`: The width of the element matches the width of the parent container.
    *   An integer specifying the width in pixels: The element has a fixed width. If the specified width is greater than the width of the parent container, the width of the element matches the width of the parent container.

*   **`height`** (`"content"`, `"stretch"`, or `int`)
    The height of the chart element. This can be one of the following:
    *   `"content"` (default): The height of the element matches the height of its content.
    *   `"stretch"`: The height of the element matches the height of its content or the height of the parent container, whichever is larger. If the element is not in a parent container, the height of the element matches the height of its content.
    *   An integer specifying the height in pixels: The element has a fixed height. If the content is larger than the specified height, scrolling is enabled.

### Example

```python
import streamlit as st
import graphviz

# Create a graphlib graph object
graph = graphviz.Digraph()
graph.edge("run", "intr")
graph.edge("intr", "runbl")
graph.edge("runbl", "run")
graph.edge("run", "kernel")
graph.edge("kernel", "zombie")
graph.edge("kernel", "sleep")
graph.edge("kernel", "runmem")
graph.edge("sleep", "swap")
graph.edge("swap", "runswap")
graph.edge("runswap", "new")
graph.edge("runswap", "runmem")
graph.edge("new", "runmem")
graph.edge("sleep", "runmem")

st.graphviz_chart(graph)
```

Or you can render the chart from the graph using GraphViz's Dot language:

```python
st.graphviz_chart('''
    digraph {
        run -> intr
        intr -> runbl
        runbl -> run
        run -> kernel
        kernel -> zombie
        kernel -> sleep
        kernel -> runmem
        sleep -> swap
        swap -> runswap
        runswap -> new
        runswap -> runmem
        new -> runmem
        sleep -> runmem
    }
''')
```

---

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.