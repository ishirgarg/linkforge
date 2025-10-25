Here is the HTML converted to clean Markdown:

# st.write - Streamlit Docs
## Documentation
Search

### Get started
* [Installation](/get-started/installation)
* [Fundamentals](/get-started/fundamentals)
* [First steps](/get-started/tutorials)

### Develop
* [Concepts](/develop/concepts)
* [API reference](/develop/api-reference)
	+ PAGE ELEMENTS
	+ [Write and magic](/develop/api-reference/write-magic)
		- [st.write](/develop/api-reference/write-magic/st.write)
		- [st.write_stream](/develop/api-reference/write-magic/st.write_stream)
		- [magic](/develop/api-reference/write-magic/magic)
	+ [Text elements](/develop/api-reference/text)
	+ [Data elements](/develop/api-reference/data)
	+ [Chart elements](/develop/api-reference/charts)
	+ [Input widgets](/develop/api-reference/widgets)
	+ [Media elements](/develop/api-reference/media)
	+ [Layouts and containers](/develop/api-reference/layout)
	+ [Chat elements](/develop/api-reference/chat)
	+ [Status elements](/develop/api-reference/status)
	+ [Third-party components](https://streamlit.io/components)
	+ APPLICATION LOGIC
	+ [Authentication and user info](/develop/api-reference/user)
	+ [Navigation and pages](/develop/api-reference/navigation)
	+ [Execution flow](/develop/api-reference/execution-flow)
	+ [Caching and state](/develop/api-reference/caching-and-state)
	+ [Connections and secrets](/develop/api-reference/connections)
	+ [Custom components](/develop/api-reference/custom-components)
	+ [Configuration](/develop/api-reference/configuration)
	+ TOOLS
	+ [App testing](/develop/api-reference/app-testing)
	+ [Command line](/develop/api-reference/cli)
* [Tutorials](/develop/tutorials)
* [Quick reference](/develop/quick-reference)

### Deploy
* [Concepts](/deploy/concepts)
* [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
* [Snowflake](/deploy/snowflake)
* [Other platforms](/deploy/tutorials)

### Knowledge base
* [FAQ](/knowledge-base/using-streamlit)
* [Installing dependencies](/knowledge-base/dependencies)
* [Deployment issues](/knowledge-base/deploy)

[Home](/) | [Develop](/develop) | [API reference](/develop/api-reference) | [Write and magic](/develop/api-reference/write-magic) | [st.write](/develop/api-reference/write-magic/st.write)

Here is the converted text in clean Markdown:
### st.write
#### Streamlit Version
Version 1.50.0
Version 1.49.0
Version 1.48.0
Version 1.47.0
Version 1.46.0
Version 1.45.0
Version 1.44.0
Version 1.43.0
Version 1.42.0
Version 1.41.0
Version 1.40.0
Version 1.39.0
Version 1.38.0
Version 1.37.0
Version 1.36.0
Version 1.35.0
Version 1.34.0
Version 1.33.0
Version 1.32.0
Version 1.31.0
Version 1.30.0
Version 1.29.0
Version 1.28.0
Version 1.27.0
Version 1.26.0
Version 1.25.0
Version 1.24.0
Version 1.23.0
Version 1.22.0

Displays arguments in the app.

This is the Swiss Army knife of Streamlit commands: it does different things depending on what you throw at it. Unlike other Streamlit commands, `st.write()` has some unique properties:
* You can pass in multiple arguments, all of which will be displayed.
* Its behavior depends on the input type(s).

#### Function signature
```python
st.write(*args, unsafe_allow_html=False)
```
#### Parameters
* `*args` (any): One or many objects to display in the app.
* `unsafe_allow_html` (bool): Whether to render HTML within `*args`.

Each type of argument is handled as follows:

| Type | Handling |
| --- | --- |
| str | Uses `st.markdown()`. |
| dataframe-like, dict, or list | Uses `st.dataframe()`. |
| Exception | Uses `st.exception()`. |
| function, module, or class | Uses `st.help()`. |
| DeltaGenerator | Uses `st.help()`. |
| Altair chart | Uses `st.altair_chart()`. |
| Bokeh figure | Uses `st.bokeh_chart()`. |
| Graphviz graph | Uses `st.graphviz_chart()`. |
| Keras model | Converts model and uses `st.graphviz_chart()`. |
| Matplotlib figure | Uses `st.pyplot()`. |
| Plotly figure | Uses `st.plotly_chart()`. |
| PIL.Image | Uses `st.image()`. |
| generator or stream (like openai.Stream) | Uses `st.write_stream()`. |
| SymPy expression | Uses `st.latex()`. |
| An object with `._repr_html()` | Uses `st.html()`. |
| Database cursor | Displays DB API 2.0 cursor results in a table. |
| Any | Displays `str(arg)` as inline code. |

#### Returns
None

#### Examples

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
st.write(pd.DataFrame({"first column": [1, 2, 3, 4], "second column": [10, 20, 30, 40]}))
```
Finally, you can pass in multiple arguments to do things like:
```python
import streamlit as st

st.write("1 + 1 = ", 2)
st.write("Below is a DataFrame:", pd.DataFrame({"A": [1, 2], "B": [3, 4]}), "Above is a dataframe.")
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
### Featured video

Learn what the [`st.write`](/develop/api-reference/write-magic/st.write) and [magic](/develop/api-reference/write-magic/magic) commands are and how to use them.

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.