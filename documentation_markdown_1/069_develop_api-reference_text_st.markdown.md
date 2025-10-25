# st.markdown - Streamlit

> **Source:** [https://docs.streamlit.io/develop/api-reference/text/st.markdown](https://docs.streamlit.io/develop/api-reference/text/st.markdown)

## st.markdown

Display string formatted as Markdown.

**Function signature** [\[source\]](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/elements/markdown.py#L39 "View st.markdown source code on GitHub")

```python
st.markdown(body, unsafe_allow_html=False, *, help=None, width="stretch")
```

**Parameters**

*   **body (any)**

    The text to display as GitHub-flavored Markdown. Syntax information can be found at: [https://github.github.com/gfm](https://github.github.com/gfm). If anything other than a string is passed, it will be converted into a string behind the scenes using `str(body)`.

    This also supports:


*   Emoji shortcodes, such as `: +1:` and `:sunglasses:`. For a list of all supported codes, see [https://share.streamlit.io/streamlit/emoji-shortcodes](https://share.streamlit.io/streamlit/emoji-shortcodes).
*   Streamlit logo shortcode. Use `:streamlit:` to add a little Streamlit flair to your text.
*   A limited set of typographical symbols. "<- \-> <-> \-- >= <= ~=" becomes "← → ↔ — ≥ ≤ ≈" when parsed as Markdown.
*   Google Material Symbols (rounded style), using the syntax `:material/icon_name:`, where "icon_name" is the name of the icon in snake case. For a complete list of icons, see Google's [Material Symbols](https://fonts.google.com/icons?icon.set=Material+Symbols&icon.style=Rounded) font library.
*   LaTeX expressions, by wrapping them in "$" or "$$" (the "$$" must be on their own lines). Supported LaTeX functions are listed at [https://katex.org/docs/supported.html](https://katex.org/docs/supported.html).
*   Colored text and background colors for text, using the syntax `:color[text to be colored]` and `:color-background[text to be colored]`, respectively. color must be replaced with any of the following supported colors: red, orange, yellow, green, blue, violet, gray/grey, rainbow, or primary. For example, you can use `:orange[your text here]` or `:blue-background[your text here]`. If you use "primary" for color, Streamlit will use the default primary accent color unless you set the theme.primaryColor configuration option.
*   Colored badges, using the syntax `:color-badge[text in the badge]`. color must be replaced with any of the following supported colors: red, orange, yellow, green, blue, violet, gray/grey, or primary. For example, you can use `:orange-badge[your text here]` or `:blue-badge[your text here]`.
*   Small text, using the syntax `:small[text to show small]`.

`unsafe_allow_html` (bool)

Whether to render HTML within body. If this is `False` (default), any HTML tags found in body will be escaped and therefore treated as raw text. If this is `True`, any HTML expressions within body will be rendered.

Adding custom HTML to your app impacts safety, styling, and maintainability.

**Note**

If you only want to insert HTML or CSS without Markdown text, we recommend using `st.html` instead.

`help` (str or None)

A tooltip that gets displayed next to the Markdown. If this is `None` (default), no tooltip is displayed.

The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of `st.markdown`.

`width` ("stretch", "content", or int)

The width of the Markdown element. This can be one of the following:

*   "stretch" (default): The width of the element matches the width of the parent container.
*   "content": The width of the element matches the width of its content, but doesn't exceed the width of the parent container.
*   An integer specifying the width in pixels: The element has a fixed width. If the specified width is greater than the width of the parent container, the width of the element matches the width of the parent container.

#### Examples

```python
import streamlit as st

st.markdown("*Streamlit* is **really** ***cool***.")
st.markdown('''
    :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors] and :blue-background[highlight] text.''')
st.markdown("Here's a bouquet &mdash;\\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

multi = '''If you end a line with two spaces,
a soft return is used for the next line.

Two (or more) newline characters in a row will result in a hard return.
'''
st.markdown(multi)
```

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen _open_in_new_](https://doc-markdown.streamlit.app//?utm_medium=oembed&)

````python
import streamlit as st
md = st.text_area('Type in your markdown string (without outer quotes)', "Happy Streamlit-ing! :balloon:")
st.code(f"""
import streamlit as st
st.markdown('''{md}''')
""")
st.markdown(md)
````

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen _open_in_new_](https://doc-markdown1.streamlit.app/?utm_medium=oembed)

[_arrow_back_Previous: st.subheader](/develop/api-reference/text/st.subheader)[_arrow_forward_Next: st.badge](/develop/api-reference/text/st.badge)

_forum_

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.
