# st.pyplot

**URL:** https://docs.streamlit.io/develop/api-reference/charts/st.pyplot

This document provides information on the `st.pyplot` function in Streamlit, which is used to display Matplotlib plots.

---

**Note:** This is the first part of the conversion. The full content will be provided in subsequent responses.

Display a matplotlib.pyplot figure.

> **Important**
> You must install matplotlib>=3.0.0 to use this command. You can install all charting dependencies (except Bokeh) as an extra with Streamlit:
>
> ```bash
> pip install streamlit[charts]
> ```

### Function signature
[`[source]`](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/elements/pyplot.py#L38 "View st.pyplot source code on GitHub")

```python
st.pyplot(fig=None, clear_figure=None, *, width="stretch", use_container_width=None, **kwargs)
```

### Parameters

*   `fig` (Matplotlib Figure)
    The Matplotlib Figure object to render. See [https://matplotlib.org/stable/gallery/index.html](https://matplotlib.org/stable/gallery/index.html) for examples.

    > **Note**
    > When this argument isn't specified, this function will render the global Matplotlib figure object. However, this feature is deprecated and will be removed in a later version.

*   `clear_figure` (bool)
    If `True`, the figure will be cleared after being rendered. If `False`, the figure will not be cleared after being rendered. If left unspecified, we pick a default based on the value of `fig`.
    *   If `fig` is set, defaults to `False`.
    *   If `fig` is not set, defaults to `True`. This simulates Jupyter's approach to matplotlib rendering.

*   `width` ("stretch", "content", or int)
    The width of the chart element. This can be one of the following:
    *   `"stretch"` (default): The width of the element matches the width of the parent container.
    *   `"content"`: The width of the element matches the width of its content, but doesn't exceed the width of the parent container.
    *   An integer specifying the width in pixels: The element has a fixed width. If the specified width is greater than the width of the parent container, the width of the element matches the width of the parent container.

*   `use_container_width` (bool)
    > **Deprecated**
    > `use_container_width` is deprecated and will be removed in a future release. For `use_container_width=True`, use `width="stretch"`. For `use_container_width=False`, use `width="content"`.
    >
    > Whether to override the figure's native width with the width of the parent container. If `use_container_width` is `True` (default), Streamlit sets the width of the figure to match the width of the parent container. If `use_container_width` is `False`, Streamlit sets the width of the chart to fit its contents according to the plotting library, up to the width of the parent container.

*   `**kwargs` (any)
    Arguments to pass to Matplotlib's `savefig` function.

#### Example

```python
import matplotlib.pyplot as plt
import streamlit as st
from numpy.random import default_rng as rng

arr = rng(0).normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)
```

Matplotlib supports several types of "backends". If you're getting an error using Matplotlib with Streamlit, try setting your backend to "TkAgg":

```bash
echo "backend: TkAgg" >> ~/.matplotlib/matplotlibrc
```

For more information, see [https://matplotlib.org/faq/usage_faq.html](https://matplotlib.org/faq/usage_faq.html).

#### Warning

> **Warning**
> Matplotlib [doesn't work well with threads](https://matplotlib.org/3.3.2/faq/howto_faq.html#working-with-threads). So if you're using Matplotlib you should wrap your code with locks. This Matplotlib bug is more prominent when you deploy and share your apps because you're more likely to get concurrent users then. The following example uses [`Rlock`](https://docs.python.org/3/library/threading.html#rlock-objects) from the `threading` module.

```python
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from threading import RLock

_lock = RLock()

x = np.random.normal(1, 1, 100)
y = np.random.normal(1, 1, 100)

with _lock:
    fig, ax = plt.subplots()
    ax.scatter(x, y)
    st.pyplot(fig)
```

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.