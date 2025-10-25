Here is the HTML content converted to clean Markdown:

### Text elements
Streamlit apps usually start with a call to `st.title` to set the app's title. After that, there are 2 heading levels you can use: `st.header` and `st.subheader`.

Pure text is entered with `st.text`, and Markdown with `st.markdown`.

We also offer a "swiss-army knife" command called `st.write`, which accepts multiple arguments, and multiple data types. And as described above, you can also use [magic commands](/develop/api-reference/write-magic/magic) in place of `st.write`.

#### Headings and body text
Display string formatted as Markdown.
```python
st.markdown("Hello **world**!")
```
Display text in title formatting.
```python
st.title("The app title")
```
Display text in header formatting.
```python
st.header("This is a header")
```
Display text in subheader formatting.
```python
st.subheader("This is a subheader")
```

#### Formatted text
Display a small, colored badge.
```python
st.badge("New")
```
Display text in small font.
```python
st.caption("This is written small caption text")
```
Display a code block with optional syntax highlighting.
```python
st.code("a = 1234")
```
Display some code on the app, then execute it. Useful for tutorials.
```python
with st.echo(): st.write('This code will be printed')
```
Write fixed-width and preformatted text.
```python
st.text("Hello world")
```
Display mathematical expressions formatted as LaTeX.
```python
st.latex("\int a x^2 \,dx")
```
Display a horizontal rule.
```python
st.divider()
```

#### Utilities
Display object’s doc string, nicely formatted.
```python
st.help(st.write)
st.help(pd.DataFrame)
```
Renders HTML strings to your app.
```python
st.html("<p>Foo bar.</p>")
```

### Third-party components
These are featured components created by our lovely community. For more examples and inspiration, check out our [Components Gallery](https://streamlit.io/components) and [Streamlit Extras](https://extras.streamlit.app)!

*   **Tags**: Add tags to your Streamlit apps. Created by [@gagan3012](https://github.com/gagan3012).
    ```python
st_tags(label='# Enter Keywords:', text='Press enter to add more', value=['Zero', 'One', 'Two'], suggestions=['five', 'six', 'seven', 'eight', 'nine', 'three', 'eleven', 'ten', 'four'], maxtags = 4, key='1')
```
*   **NLU**: Apply text mining on a dataframe. Created by [@JohnSnowLabs](https://github.com/JohnSnowLabs/).
    ```python
nlu.load('sentiment').predict('I love NLU! <3')
```
*   **Streamlit Extras**: A library with useful Streamlit extras. Created by [@arnaudmiribel](https://github.com/arnaudmiribel/).
    ```python
mention(label="An awesome Streamlit App", icon="streamlit", url="https://extras.streamlit.app",)
```
*   **Annotated text**: Display annotated text in Streamlit apps. Created by [@tvst](https://github.com/tvst).
    ```python
annotated_text("This ", ("is", "verb"), " some ", ("annotated", "adj"), ("text", "noun"), " for those of ", ("you", "pronoun"), " who ", ("like", "verb"), " this sort of ", ("thing", "noun"), ".")
```
*   **Drawable Canvas**: Provides a sketching canvas using [Fabric.js](http://fabricjs.com/). Created by [@andfanilo](https://github.com/andfanilo).
    ```python
st_canvas(fill_color="rgba(255, 165, 0, 0.3)", stroke_width=stroke_width, stroke_color=stroke_color, background_color=bg_color, background_image=Image.open(bg_image) if bg_image else None, update_streamlit=realtime_update, height=150, drawing_mode=drawing_mode, point_display_radius=point_display_radius if drawing_mode == 'point' else 0, key="canvas",)
```

### Still have questions?
Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

### Navigation
*   [Home](/)
*   [Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)
*   [Community](https://discuss.streamlit.io)

### Social Media
*   [GitHub](https://github.com/streamlit)
*   [YouTube](https://www.youtube.com/channel/UC3LD42rjj-Owtxsa6PwGU5Q)
*   [Twitter](https://twitter.com/streamlit)
*   [LinkedIn](https://www.linkedin.com/company/streamlit)
*   [Newsletter](https://info.snowflake.com/streamlit-newsletter-sign-up.html)

&copy; 2025 Snowflake Inc.
[Cookie policy](https://www.streamlit.io/cookie-policy)