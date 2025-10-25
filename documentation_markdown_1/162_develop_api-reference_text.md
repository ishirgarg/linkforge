```markdown
# Text elements

[Original URL](https://docs.streamlit.io/develop/api-reference/text)

Streamlit apps usually start with a call to `st.title` to set the app's title. After that, there are 2 heading levels you can use: `st.header` and `st.subheader`.

Pure text is entered with `st.text`, and Markdown with `st.markdown`.

We also offer a "swiss-army knife" command called `st.write`, which accepts multiple arguments, and multiple data types. And as described above, you can also use [magic commands](/develop/api-reference/write-magic/magic) in place of `st.write`.

## Headings and body text

[![screenshot](/images/api/markdown.jpg)

#### Markdown

Display string formatted as Markdown.

`st.markdown("Hello **world**!")`

](/develop/api-reference/text/st.markdown)

[![screenshot](/images/api/title.jpg)

#### Title

Display text in title formatting.

`st.title("The app title")`

](/develop/api-reference/text/st.title)

[![screenshot](/images/api/header.jpg)

#### Header

Display text in header formatting.

`st.header("This is a header")`

](/develop/api-reference/text/st.header)

[![screenshot](/images/api/subheader.jpg)

#### Subheader

Display text in subheader formatting.

`st.subheader("This is a subheader")`

](/develop/api-reference/text/st.subheader)

## Formatted text

[![screenshot](/images/api/badge.jpg)

#### Badge

Display a small, colored badge.

`st.badge("New")`

](/develop/api-reference/text/st.badge)

[![screenshot](/images/api/caption.jpg)

#### Caption

Display text in small font.

`st.caption("This is written small caption text")`

](/develop/api-reference/text/st.caption)

[![screenshot](/images/api/code.jpg)

#### Code block

Display a code block with optional syntax highlighting.

`st.code("a = 1234")`

](/develop/api-reference/text/st.code)

[![screenshot](/images/api/code.jpg)

#### Echo

Display some code on the app, then execute it. Useful for tutorials.

`with st.echo(): st.write('This code will be printed')`

](/develop/api-reference/text/st.echo)

[![screenshot](/images/api/text.jpg)

#### Preformatted text

Write fixed-width and preformatted text.

`st.text("Hello world")`

](/develop/api-reference/text/st.text)

[![screenshot](/images/api/latex.jpg)

#### LaTeX

Display mathematical expressions formatted as LaTeX.

`st.latex("\int a x^2 \,dx")`

](/develop/api-reference/text/st.latex)

[![screenshot](/images/api/divider.jpg)

#### Divider

Display a horizontal rule.

`st.divider()`

](/develop/api-reference/text/st.divider)

## Utilities

[

#### Get help

Display object’s doc string, nicely formatted.

`st.help(st.write) st.help(pd.DataFrame)`

](/develop/api-reference/text/st.help)
```

Renders HTML strings to your app.

```python
st.html("<p>Foo bar.</p>")
```

### Third-party components

These are featured components created by our lovely community. For more examples and inspiration, check out our [Components Gallery](https://streamlit.io/components) and [Streamlit Extras](https://extras.streamlit.app)!

#### Tags

Add tags to your Streamlit apps. Created by [@gagan3012](https://github.com/gagan3012).

```python
st_tags(label='# Enter Keywords:', text='Press enter to add more', value=['Zero', 'One', 'Two'], suggestions=['five', 'six', 'seven', 'eight', 'nine', 'three', 'eleven', 'ten', 'four'], maxtags = 4, key='1')
```

#### NLU

Apply text mining on a dataframe. Created by [@JohnSnowLabs](https://github.com/JohnSnowLabs/).

```python
nlu.load('sentiment').predict('I love NLU! <3')
```

#### Streamlit Extras

A library with useful Streamlit extras. Created by [@arnaudmiribel](https://github.com/arnaudmiribel/).

```python
mention(label="An awesome Streamlit App", icon="streamlit", url="https://extras.streamlit.app",)
```

#### Annotated text

Display annotated text in Streamlit apps. Created by [@tvst](https://github.com/tvst).

```python
annotated_text("This ", ("is", "verb"), " some ", ("annotated", "adj"), ("text", "noun"), " for those of ", ("you", "pronoun"), " who ", ("like", "verb"), " this sort of ", ("thing", "noun"), ".")
```

#### Drawable Canvas

Provides a sketching canvas using [Fabric.js](http://fabricjs.com/). Created by [@andfanilo](https://github.com/andfanilo).

```python
st_canvas(fill_color="rgba(255, 165, 0, 0.3)", stroke_width=stroke_width, stroke_color=stroke_color, background_color=bg_color, background_image=Image.open(bg_image) if bg_image else None, update_streamlit=realtime_update, height=150, drawing_mode=drawing_mode, point_display_radius=point_display_radius if drawing_mode == 'point' else 0, key="canvas",)
```

---

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.