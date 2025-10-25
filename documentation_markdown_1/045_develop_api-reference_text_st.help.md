# st.help

[Original URL](https://docs.streamlit.io/develop/api-reference/text/st.help)

Display help and other information for a given object.

Depending on the type of object that is passed in, this displays the object's name, type, value, signature, docstring, and member variables, methods — as well as the values/docstring of members and methods.

## Function signature

[\[source\]](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/elements/doc_string.py#L47 "View st.help source code on GitHub")

`st.help(obj=, *, width="stretch")`

## Parameters

### obj (any)

The object whose information should be displayed. If left unspecified, this call will display help for Streamlit itself.

### width ("stretch" or int)

The width of the help element. This can be one of the following:

*   `"stretch"` (default): The width of the element matches the width of the parent container.
*   An integer specifying the width in pixels: The element has a fixed width. If the specified width is greater than the width of the parent container, the width of the element matches the width of the parent container.

## Example

Don't remember how to initialize a dataframe? Try this:

```python
import streamlit as st
import pandas

st.help(pandas.DataFrame)
```

Want to quickly check what data type is output by a certain function? Try:

```python
import streamlit as st

x = my_poorly_documented_function()
st.help(x)
```

Want to quickly inspect an object? No sweat:

```python
class Dog:
  '''A typical dog.'''

  def __init__(self, breed, color):
    self.breed = breed
    self.color = color

  def bark(self):
    return 'Woof!'


fido = Dog("poodle", "white")

st.help(fido)
```

And if you're using Magic, you can get help for functions, classes, and modules without even typing `st.help`:

```python
import streamlit as st
import pandas

# Get help for Pandas read_csv:
pandas.read_csv

# Get help for Streamlit itself:
```


### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

[GitHub](https://github.com/streamlit) [YouTube](https://www.youtube.com/channel/UC3LD42rjj-Owtxsa6PwGU5Q) [Twitter](https://twitter.com/streamlit) [LinkedIn](https://www.linkedin.com/company/streamlit) [Newsletter](https://info.snowflake.com/streamlit-newsletter-sign-up.html)

© 2025 Snowflake Inc. Cookie policy
