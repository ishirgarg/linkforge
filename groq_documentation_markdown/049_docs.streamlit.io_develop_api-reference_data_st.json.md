Here is the HTML content converted to clean Markdown:

### st.json
#### Streamlit Docs
Streamlit Version: 1.50.0

Display an object or string as a pretty-printed, interactive JSON string.

##### Function Signature
```python
st.json(body, *, expanded=True, width="stretch")
```

##### Parameters

* `body` (object or str): The object to print as JSON. All referenced objects should be serializable to JSON as well. If object is a string, we assume it contains serialized JSON.
* `expanded` (bool or int): The initial expansion state of the JSON element.
	+ `True` (default): The element is fully expanded.
	+ `False`: The element is fully collapsed.
	+ An integer: The element is expanded to the depth specified. The integer must be non-negative. `expanded=0` is equivalent to `expanded=False`.
* `width` ("stretch" or int): The width of the JSON element.
	+ "stretch" (default): The width of the element matches the width of the parent container.
	+ An integer specifying the width in pixels: The element has a fixed width. If the specified width is greater than the width of the parent container, the width of the element matches the width of the parent container.

##### Example
```python
import streamlit as st

st.json({
    "foo": "bar",
    "stuff": [
        "stuff 1",
        "stuff 2",
        "stuff 3",
    ],
    "level1": {"level2": {"level3": {"a": "b"}}},
}, expanded=2)
```

### Navigation

* [Get Started](/get-started)
* [Develop](/develop)
* [API Reference](/develop/api-reference)
* [Data Elements](/develop/api-reference/data)
* [st.json](/develop/api-reference/data/st.json)

### Still Have Questions?
Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

### Contact Us
[Home](/) | [Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20) | [Community](https://discuss.streamlit.io)

### Follow Us
[GitHub](https://github.com/streamlit) | [YouTube](https://www.youtube.com/channel/UC3LD42rjj-Owtxsa6PwGU5Q) | [Twitter](https://twitter.com/streamlit) | [LinkedIn](https://www.linkedin.com/company/streamlit) | [Newsletter](https://info.snowflake.com/streamlit-newsletter-sign-up.html)

&copy; 2025 Snowflake Inc. [Cookie policy](https://www.streamlit.io/cookie-policy)