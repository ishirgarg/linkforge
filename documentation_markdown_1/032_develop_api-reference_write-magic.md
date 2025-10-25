```markdown
# st.write and magic commands

[Original URL](https://docs.streamlit.io/develop/api-reference/write-magic)

Streamlit has two easy ways to display information into your app, which should typically be the first thing you try: `st.write` and magic.

## st.write

Write arguments to the app.

```python
st.write("Hello **world**!")
st.write(my_data_frame)
st.write(my_mpl_figure)
```

## st.write_stream

Write generators or streams to the app with a typewriter effect.

```python
st.write_stream(my_generator)
st.write_stream(my_llm_stream)
```

## Magic

Any time Streamlit sees either a variable or literal value on its own line, it automatically writes that to your app using `st.write`

```python
"Hello **world**!"
my_data_frame
my_mpl_figure
```
```