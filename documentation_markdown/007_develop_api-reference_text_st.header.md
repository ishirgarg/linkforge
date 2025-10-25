# st.header - Streamlit Docs

**URL:** https://docs.streamlit.io/develop/api-reference/text/st.header

This document provides information about the `st.header` function in Streamlit, which is used to display a large, prominent header in your application.

---

**Note:** This is the first part of the content. The full documentation would typically include more sections like "Usage," "Parameters," "Examples," and "Return Value."

Display text in header formatting.

Function signature ([source](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/elements/heading.py#L45 "View st.header source code on GitHub"))

```python
st.header(body, anchor=None, *, help=None, divider=False, width="stretch")
```

Parameters

*   **body** (*str*)

    The text to display as GitHub-flavored Markdown. Syntax information can be found at: [https://github.github.com/gfm](https://github.github.com/gfm).

    See the `body` parameter of [st.markdown](https://docs.streamlit.io/develop/api-reference/text/st.markdown) for additional, supported Markdown directives.
*   **anchor** (*str or False*)

    The anchor name of the header that can be accessed with `#anchor` in the URL. If omitted, it generates an anchor using the body. If `False`, the anchor is not shown in the UI.
*   **help** (*str or None*)

    A tooltip that gets displayed next to the header. If this is `None` (default), no tooltip is displayed.

    The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the `body` parameter of `st.markdown`.
*   **divider** (*bool, "blue", "green", "orange", "red", "violet", "yellow", "gray"/"grey", or "rainbow"*)

    Shows a colored divider below the header. If this is `True`, successive headers will cycle through divider colors, except gray and rainbow. That is, the first header will have a blue line, the second header will have a green line, and so on. If this is a string, the color can be set to one of the following: blue, green, orange, red, violet, yellow, gray/grey, or rainbow.
*   **width** (*"stretch", "content", or int*)

    The width of the header element. This can be one of the following:

    *   `"stretch"` (default): The width of the element matches the width of the parent container.
    *   `"content"`: The width of the element matches the width of its content, but doesn't exceed the width of the parent container.
    *   An integer specifying the width in pixels: The element has a fixed width. If the specified width is greater than the width of the parent container, the width of the element matches the width of the parent container.

#### Examples

```python
import streamlit as st

st.header("_Streamlit_ is :blue[cool] :sunglasses:")
st.header("This is a header with a divider", divider="gray")
st.header("These headers have rotating dividers", divider=True)
st.header("One", divider=True)
st.header("Two", divider=True)
st.header("Three", divider=True)
st.header("Four", divider=True)
```

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen _open\_in\_new_](https://doc-header.streamlit.app//?utm_medium=oembed&)

[_arrow\_back_Previous: st.title](/develop/api-reference/text/st.title) [_arrow\_forward_Next: st.subheader](/develop/api-reference/text/st.subheader)

_forum_

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

* * *

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

[](https://github.com/streamlit "GitHub")[](https://www.youtube.com/channel/UC3LD42rjj-Owtxsa6PwGU5Q "YouTube")[](https://twitter.com/streamlit "Twitter")[](https://www.linkedin.com/company/streamlit "LinkedIn")[](https://info.snowflake.com/streamlit-newsletter-sign-up.html "Newsletter")

© 2025 Snowflake Inc.Cookie policy

_forum_ Ask
