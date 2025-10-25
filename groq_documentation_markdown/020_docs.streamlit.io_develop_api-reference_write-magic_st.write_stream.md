Here is the HTML content converted to clean Markdown:
### Streamlit Docs
#### Documentation

* [Get started](/get-started)
	+ [Installation](/get-started/installation)
	+ [Fundamentals](/get-started/fundamentals)
	+ [First steps](/get-started/tutorials)
* [Develop](/develop)
	+ [Concepts](/develop/concepts)
	+ [API reference](/develop/api-reference)
		- [Write and magic](/develop/api-reference/write-magic)
			- [st.write](/develop/api-reference/write-magic/st.write)
			- [st.write_stream](/develop/api-reference/write-magic/st.write_stream)
			- [magic](/develop/api-reference/write-magic/magic)
		- [Text elements](/develop/api-reference/text)
		- [Data elements](/develop/api-reference/data)
		- [Chart elements](/develop/api-reference/charts)
		- [Input widgets](/develop/api-reference/widgets)
		- [Media elements](/develop/api-reference/media)
		- [Layouts and containers](/develop/api-reference/layout)
		- [Chat elements](/develop/api-reference/chat)
		- [Status elements](/develop/api-reference/status)
		- [Third-party components](https://streamlit.io/components)
		- [Authentication and user info](/develop/api-reference/user)
		- [Navigation and pages](/develop/api-reference/navigation)
		- [Execution flow](/develop/api-reference/execution-flow)
		- [Caching and state](/develop/api-reference/caching-and-state)
		- [Connections and secrets](/develop/api-reference/connections)
		- [Custom components](/develop/api-reference/custom-components)
		- [Configuration](/develop/api-reference/configuration)
		- [App testing](/develop/api-reference/app-testing)
		- [Command line](/develop/api-reference/cli)
	+ [Tutorials](/develop/tutorials)
	+ [Quick reference](/develop/quick-reference)
* [Deploy](/deploy)
	+ [Concepts](/deploy/concepts)
	+ [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
	+ [Snowflake](/deploy/snowflake)
	+ [Other platforms](/deploy/tutorials)
* [Knowledge base](/knowledge-base)
	+ [FAQ](/knowledge-base/using-streamlit)
	+ [Installing dependencies](/knowledge-base/dependencies)
	+ [Deployment issues](/knowledge-base/deploy)

[Breadcrumbs]
* [Home](/)
* [Develop](/develop)
* [API reference](/develop/api-reference)
* [Write and magic](/develop/api-reference/write-magic)
* [st.write_stream](/develop/api-reference/write-magic/st.write_stream)

## st.write_stream
Streamlit Version: 1.50.0, 1.49.0, 1.48.0, 1.47.0, 1.46.0, 1.45.0, 1.44.0, 1.43.0, 1.42.0, 1.41.0, 1.40.0, 1.39.0, 1.38.0, 1.37.0, 1.36.0, 1.35.0, 1.34.0, 1.33.0, 1.32.0, 1.31.0, 1.30.0, 1.29.0, 1.28.0, 1.27.0, 1.26.0, 1.25.0, 1.24.0, 1.23.0, 1.22.0

Stream a generator, iterable, or stream-like sequence to the app.

`st.write_stream` iterates through the given sequences and writes all chunks to the app. String chunks will be written using a typewriter effect. Other data types will be written using `st.write`.

### Function signature
```python
st.write_stream(stream)
```
### Parameters

* `stream`: The generator or iterable to stream. Can be a Callable, Generator, Iterable, OpenAI Stream, or LangChain Stream.

Note: If you pass an async generator, Streamlit will internally convert it to a sync generator. If the generator depends on a cached object with async references, this can raise an error.

### Returns

* `(str or list)`: The full response. If the streamed output only contains text, this is a string. Otherwise, this is a list of all the streamed objects. The return value is fully compatible as input for `st.write`.

### Example
You can pass an OpenAI stream as shown in our tutorial, [Build a basic LLM chat app](https://docs.streamlit.io/develop/tutorials/llms/build-conversational-apps#build-a-chatgpt-like-app). Alternatively, you can pass a generic generator function as input:
```python
import time
import numpy as np
import pandas as pd
import streamlit as st

LOREM_IPSUM = """
Lorem ipsum dolor sit amet, **consectetur adipiscing** elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
"""

def stream_data():
    for word in LOREM_IPSUM.split(" "):
        yield word + " "
        time.sleep(0.02)

    yield pd.DataFrame(
        np.random.randn(5, 10),
        columns=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"],
    )

    for word in LOREM_IPSUM.split(" "):
        yield word + " "
        time.sleep(0.02)

if st.button("Stream data"):
    st.write_stream(stream_data)
```
### Tip
If your stream object is not compatible with `st.write_stream`, define a wrapper around your stream object to create a compatible generator function.
```python
for chunk in unsupported_stream:
    yield preprocess(chunk)
```
For an example, see how we use [Replicate](https://replicate.com/docs/get-started/python) with [Snowflake Arctic](https://www.snowflake.com/en/data-cloud/arctic/) in [this code](https://github.com/streamlit/snowflake-arctic-st-demo/blob/0f0d8b49f328f72ae58ced2e9000790fb5e56e6f/simple_app.py#L58).