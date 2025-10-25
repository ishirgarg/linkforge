```markdown
# st.write

[Original URL](https://docs.streamlit.io/develop/api-reference/write-magic/st.write)

`st.write` is Streamlit's "magic" command that can be used to write almost anything to your app.

You can pass a single argument to `st.write`:

```python
st.write('Hello, world!')
```

Or pass multiple arguments:

```python
st.write('Hello,', 'world!')
```

`st.write` also supports a surprising amount of Markdown!
```


Displays arguments in the app.

This is the Swiss Army knife of Streamlit commands: it does different things depending on what you throw at it. Unlike other Streamlit commands, `st.write()` has some unique properties:

*   You can pass in multiple arguments, all of which will be displayed.
*   Its behavior depends on the input type(s).

## Function signature

```python
st.write(*args, unsafe_allow_html=False)
```

## Parameters

`*args` (any)

: One or many objects to display in the app.

Each type of argument is handled as follows:

| Type                         | Handling                                     |
| ---------------------------- | -------------------------------------------- |
| `str`                        | Uses `st.markdown()`.                        |
| dataframe-like, `dict`, or `list` | Uses `st.dataframe()`.                       |
| `Exception`                  | Uses `st.exception()`.                       |
| `function`, `module`, or `class` | Uses `st.help()`.                            |
| `DeltaGenerator`             | Uses `st.help()`.                            |
| Altair chart                 | Uses `st.altair_chart()`.                    |
| Bokeh figure                 | Uses `st.bokeh_chart()`.                     |
| Graphviz graph               | Uses `st.graphviz_chart()`.                  |
| Keras model                  | Converts model and uses `st.graphviz_chart()`. |
| Matplotlib figure            | Uses `st.pyplot()`.                          |
| Plotly figure                | Uses `st.plotly_chart()`.                    |
| `PIL.Image`                  | Uses `st.image()`.                           |
| generator or stream (like openai.Stream) | Uses `st.write_stream()`. |
| SymPy expression             | Uses `st.latex()`.                           |
| An object with `._repr_html()` | Uses `st.html()`.                            |
| Database cursor              | Displays DB API 2.0 cursor results in a table. |
| Any                          | Displays `str(arg)` as inline code.          |

`unsafe_allow_html` (bool)

: Whether to render HTML within `*args`. This only applies to strings or objects falling back on `_repr_html_()`. If this is `False` (default), any HTML tags found in body will be escaped and therefore treated as raw text. If this is `True`, any HTML expressions within body will be rendered.

    Adding custom HTML to your app impacts safety, styling, and maintainability.

!!! note
    If you only want to insert HTML or CSS without Markdown text, we recommend using `st.html` instead.

## Returns

(None)

: No description

## Examples

Its basic use case is to draw Markdown-formatted text, whenever the input is a string:

```python
import streamlit as st

st.write("Hello, *World!* :sunglasses:")
```

As mentioned earlier, `st.write()` also accepts other data formats, such as numbers, data frames, styled data frames, and assorted objects:

```python
import streamlit as st
import pandas as pd

st.write(1234)
st.write(
    pd.DataFrame(
        {
            "first column": [1, 2, 3, 4],
            "second column": [10, 20, 30, 40],
        }
    )
)
```

Finally, you can pass in multiple arguments to do things like:

```python
import streamlit as st

st.write("1 + 1 = ", 2)
st.write("Below is a DataFrame:", data_frame, "Above is a dataframe.")
```

Oh, one more thing: `st.write` accepts chart objects too! For example:

```python
import altair as alt
import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng

df = pd.DataFrame(rng(0).standard_normal((200, 3)), columns=["a", "b", "c"])
chart = (
    alt.Chart(df)
    .mark_circle()
    .encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
)

st.write(chart)
```

## Featured video

Learn what the [`st.write`](/develop/api-reference/write-magic/st.write) and [magic](/develop/api-reference/write-magic/magic) commands are and how to use them.

## Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.
