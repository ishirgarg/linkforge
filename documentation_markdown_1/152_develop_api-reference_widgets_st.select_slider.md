# st.select_slider

**URL:** https://docs.streamlit.io/develop/api-reference/widgets/st.select_slider

This document describes the `st.select_slider` function in Streamlit, which allows users to select a value or a range of values from a slider.

## Overview

The `st.select_slider` widget displays a slider that enables users to choose a single value or a range of values from a predefined set of options. This is particularly useful for scenarios where you want users to make a selection from a continuous or discrete range.

---
**(This is the first part of the content. The next part will continue with the function signature, parameters, and examples.)**

#### Examples

```python
import streamlit as st

color = st.select_slider(
    "Select a color of the rainbow",
    options=[
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "indigo",
        "violet",
    ],
)
st.write("My favorite color is", color)
```

And here's an example of a range select slider:

```python
import streamlit as st

start_color, end_color = st.select_slider(
    "Select a range of color wavelength",
    options=[
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "indigo",
        "violet",
    ],
    value=("red", "blue"),
)
st.write("You selected wavelengths between", start_color, "and", end_color)
```

### Featured videos

Check out our video on how to use one of Streamlit's core functions, the select slider! 🎈

In the video below, we'll take it a step further and make a double-ended slider.

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.