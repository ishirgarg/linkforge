# st.latex

[Original URL](https://docs.streamlit.io/develop/api-reference/text/st.latex)

Display mathematical expressions formatted as LaTeX.

Supported LaTeX functions are listed at [https://katex.org/docs/supported.html](https://katex.org/docs/supported.html).

## Function signature

`st.latex(body, *, help=None, width="stretch")`

## Parameters

### body (str or SymPy expression)

The string or SymPy expression to display as LaTeX. If str, it's a good idea to use raw Python strings since LaTeX uses backslashes a lot.

### help (str or None)

A tooltip that gets displayed next to the LaTeX expression. If this is None (default), no tooltip is displayed.

The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of st.markdown.

### width ("stretch", "content", or int)

The width of the LaTeX element. This can be one of the following:

*   "stretch" (default): The width of the element matches the width of the parent container.
*   "content": The width of the element matches the width of its content, but doesn't exceed the width of the parent container.
*   An integer specifying the width in pixels: The element has a fixed width. If the specified width is greater than the width of the parent container, the width of the element matches the width of the parent container.

## Example

```python
import streamlit as st

st.latex(r'''
    a + ar + a r^2 + a r^3 + \\cdots + a r^{n-1} =
    \\sum\_{k=0}^{n-1} ar^k =
    a \\left(\\frac{1-r^{n}}{1-r}\\right)
    ''')
```


Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.