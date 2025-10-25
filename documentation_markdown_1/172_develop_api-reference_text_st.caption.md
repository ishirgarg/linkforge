```markdown
# st.caption - Streamlit

> Source URL: [https://docs.streamlit.io/develop/api-reference/text/st.caption](https://docs.streamlit.io/develop/api-reference/text/st.caption)

## st.caption

Display text in small font.

This should be used for captions, asides, footnotes, sidenotes, and other explanatory text.

### Function signature

`st.caption(body, unsafe_allow_html=False, *, help=None, width="stretch")`

### Parameters

*   **body (str)**

    The text to display as GitHub-flavored Markdown. Syntax information can be found at: [https://github.github.com/gfm](https://github.github.com/gfm).

    See the body parameter of [st.markdown](https://docs.streamlit.io/develop/api-reference/text/st.markdown) for additional, supported Markdown directives.

*   **unsafe\_allow\_html (bool)**

    Whether to render HTML within body. If this is False (default), any HTML tags found in body will be escaped and therefore treated as raw text. If this is True, any HTML expressions within body will be rendered.

    Adding custom HTML to your app impacts safety, styling, and maintainability.

    **Note:** If you only want to insert HTML or CSS without Markdown text, we recommend using st.html instead.

*   **help (str or None)**

    A tooltip that gets displayed next to the caption. If this is None (default), no tooltip is displayed.

    The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of st.markdown.

*   **width ("stretch", "content", or int)**

    The width of the caption element. This can be one of the following:

    *   "stretch" (default): The width of the element matches the width of the parent container.
    *   "content": The width of the element matches the width of its content, but doesn't exceed the width of the parent container.
    *   An integer specifying the width in pixels: The element has a fixed width. If the specified width is greater than the width of the parent container, the width of the element matches the width of the parent container.

### Examples

```python
import streamlit as st

st.caption("This is a string that explains something above.")
st.caption("A caption with _italics_ :blue[colors] and emojis :sunglasses:")
```

![](/images/api/st.caption.png)
```


### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

*   [GitHub](https://github.com/streamlit)
*   [YouTube](https://www.youtube.com/channel/UC3LD42rjj-Owtxsa6PwGU5Q)
*   [Twitter](https://twitter.com/streamlit)
*   [LinkedIn](https://www.linkedin.com/company/streamlit)
*   [Newsletter](https://info.snowflake.com/streamlit-newsletter-sign-up.html)

© 2025 Snowflake Inc.
[Cookie policy](/)

_forum_ Ask A