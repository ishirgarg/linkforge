Here is the HTML content converted to clean Markdown:
### st.markdown
Display string formatted as Markdown.

#### Function signature
```python
st.markdown(body, unsafe_allow_html=False, *, help=None, width="stretch")
```
#### Parameters
* **body** (any): The text to display as GitHub-flavored Markdown. Syntax information can be found at: [https://github.github.com/gfm](https://github.github.com/gfm). If anything other than a string is passed, it will be converted into a string behind the scenes using `str(body)`. This also supports:
	+ Emoji shortcodes, such as :+1: and :sunglasses:. For a list of all supported codes, see [https://share.streamlit.io/streamlit/emoji-shortcodes](https://share.streamlit.io/streamlit/emoji-shortcodes).
	+ Streamlit logo shortcode. Use :streamlit: to add a little Streamlit flair to your text.
	+ A limited set of typographical symbols. "<- \-> <-> \-- >= <= ~=" becomes "← → ↔ — ≥ ≤ ≈" when parsed as Markdown.
	+ Google Material Symbols (rounded style), using the syntax :material/icon_name:, where "icon_name" is the name of the icon in snake case. For a complete list of icons, see Google's [Material Symbols](https://fonts.google.com/icons?icon.set=Material+Symbols&icon.style=Rounded) font library.
	+ LaTeX expressions, by wrapping them in "$" or "$$" (the "$$" must be on their own lines). Supported LaTeX functions are listed at [https://katex.org/docs/supported.html](https://katex.org/docs/supported.html).
	+ Colored text and background colors for text, using the syntax :color[text to be colored] and :color-background[text to be colored], respectively. color must be replaced with any of the following supported colors: red, orange, yellow, green, blue, violet, gray/grey, rainbow, or primary. For example, you can use :orange[text to be colored] or :blue-background[text to be colored]. If you use "primary" for color, Streamlit will use the default primary accent color unless you set the theme.primaryColor configuration option.
	+ Colored badges, using the syntax :color-badge[text in the badge]. color must be replaced with any of the following supported colors: red, orange, yellow, green, blue, violet, gray/grey, or primary. For example, you can use :orange-badge[text to be colored] or :blue-badge[text to be colored].
	+ Small text, using the syntax :small[text to show small].
* **unsafe_allow_html** (bool): Whether to render HTML within body. If this is False (default), any HTML tags found in body will be escaped and therefore treated as raw text. If this is True, any HTML expressions within body will be rendered.
* **help** (str or None): A tooltip that gets displayed next to the Markdown. If this is None (default), no tooltip is displayed. The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of `st.markdown`.
* **width** ("stretch", "content", or int): The width of the Markdown element. This can be one of the following:
	+ "stretch" (default): The width of the element matches the width of the parent container.
	+ "content": The width of the element matches the width of its content, but doesn't exceed the width of the parent container.
	+ An integer specifying the width in pixels: The element has a fixed width. If the specified width is greater than the width of the parent container, the width of the element matches the width of the parent container.

#### Examples
```python
import streamlit as st

st.markdown("*Streamlit* is **really** ***cool***.")
st.markdown('''
    :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[color] and :blue-background[highlight] text.
''')
st.markdown("Here's a bouquet &mdash; \
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")
```
Note: This conversion removed the unnecessary HTML elements and reformatted the content to follow Markdown guidelines.