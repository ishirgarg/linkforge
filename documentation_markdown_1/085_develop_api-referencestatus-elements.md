```markdown
# API Reference - Streamlit Docs

> **Source:** [https://docs.streamlit.io/develop/api-reference#status-elements](https://docs.streamlit.io/develop/api-reference#status-elements)

Streamlit makes it easy for you to visualize, mutate, and share data. The API reference is organized by activity type, like displaying data or optimizing performance. Each section includes methods associated with the activity type, including examples.

Browse our API below and click to learn more about any of our available commands! 🎈

## Display almost anything

### Write and magic

#### st.write

Write arguments to the app.

```python
st.write("Hello **world**!")
st.write(my_data_frame)
st.write(my_mpl_figure)
```

#### st.write_stream

Write generators or streams to the app with a typewriter effect.

```python
st.write_stream(my_generator)
st.write_stream(my_llm_stream)
```

#### Magic

Any time Streamlit sees either a variable or literal value on its own line, it automatically writes that to your app using `st.write`

```python
"Hello **world**!"
my_data_frame
my_mpl_figure
```

### Text elements

#### Markdown

Display string formatted as Markdown.

```python
st.markdown("Hello **world**!")
```

#### Title

Display text in title formatting.

```python
st.title("The app title")
```

#### Header

Display text in header formatting.

```python
st.header("This is a header")
```

#### Subheader

Display text in subheader formatting.

```python
st.subheader("This is a subheader")
```

#### Badge

Display a small, colored badge.

```python
st.badge("New")
```

#### Caption

Display text in small font.

```python
st.caption("This is written small caption text")
```

#### Code block

Display a code block with optional syntax highlighting.

```python
st.code("a = 1234")
```

#### Echo

Display some code in the app, then execute it. Useful for tutorials.

```python
with st.echo():
    st.write('This code will be printed')
```

#### LaTeX

Display mathematical expressions formatted as LaTeX.

```python
st.latex("\int a x^2 \,dx")
```

#### Preformatted text

Write fixed-width and preformatted text.

```python
st.text("Hello world")
```

#### Divider

Display a horizontal rule.

```python
st.divider()
```

#### Get help

Display object’s doc string, nicely formatted.

```python
st.help(st.write)
st.help(pd.DataFrame)
```

#### Render HTML

Renders HTML strings to your app.

```python
st.html("<p>Foo bar.</p>")
```

Third-party components

These are featured components created by our lovely community. For more examples and inspiration, check out our [Components Gallery](https://streamlit.io/components) and [Streamlit Extras](https://extras.streamlit.app)!

Previous

#### Tags

[Add tags to your Streamlit apps. Created by](https://github.com/gagan3012/streamlit-tags) [@gagan3012](https://github.com/gagan3012).

```python
st_tags(label='# Enter Keywords:', text='Press enter to add more', value=['Zero', 'One', 'Two'], suggestions=['five', 'six', 'seven', 'eight', 'nine', 'three', 'eleven', 'ten', 'four'], maxtags = 4, key='1')
```

#### NLU
```
```


### Data elements

#### Dataframes

Display a dataframe as an interactive table.

```python
st.dataframe(my_data_frame)
```

#### Data editor

Display a data editor widget.

```python
edited = st.data_editor(df, num_rows="dynamic")
```

#### Column configuration

Configure the display and editing behavior of dataframes and data editors.

```python
st.column_config.NumberColumn("Price (in USD)", min_value=0, format="$%d")
```

#### Static tables

Display a static table.

```python
st.table(my_data_frame)
```

#### Metrics

Display a metric in big bold font, with an optional indicator of how the metric changed.

```python
st.metric("My metric", 42, 2)
```

#### Dicts and JSON

Display object or string as a pretty-printed JSON string.

```python
st.json(my_dict)
```

### Third-party components

These are featured components created by our lovely community. For more examples and inspiration, check out our [Components Gallery](https://streamlit.io/components) and [Streamlit Extras](https://extras.streamlit.app)!

#### Image Coordinates

Get the coordinates of clicks on an image. Created by [@blackary](https://github.com/blackary/).

```python
from streamlit_image_coordinates import streamlit_image_coordinates
value = streamlit_image_coordinates("https://placekitten.com/200/300")
st.write(value)
```

#### Plotly Events

Make Plotly charts interactive! Created by [@null-jones](https://github.com/null-jones/).

```python
from streamlit_plotly_events import plotly_events
fig = px.line(x=[1], y=[1])
selected_points = plotly_events(fig)
```

#### Streamlit Extras

A library with useful Streamlit extras. Created by [@arnaudmiribel](https://github.com/arnaudmiribel/).

```python
from streamlit_extras.metric_cards import style_metric_cards
col3.metric(label="No Change", value=5000, delta=0)
style_metric_cards()
```

#### Streamlit Aggrid

[Link to Streamlit Aggrid](https://github.com/PablocFonseca/streamlit-aggrid)

#### NLU

Apply text mining on a dataframe. Created by [@JohnSnowLabs](https://github.com/JohnSnowLabs/).

```python
nlu.load("sentiment").predict("I love NLU! <3")
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

#### Tags

Add tags to your Streamlit apps. Created by [@gagan3012](https://github.com/gagan3012).

```python
st_tags(label='# Enter Keywords:', text='Press enter to add more', value=['Zero', 'One', 'Two'], suggestions=['five', 'six', 'seven', 'eight', 'nine', 'three', 'eleven', 'ten', 'four'], maxtags = 4, key='1')
```

[Implementation of Ag-Grid component for Streamlit. Created by](https://github.com/PablocFonseca/streamlit-aggrid) [@PablocFonseca](https://github.com/PablocFonseca).

```python
df = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6]})
grid_return = AgGrid(df, editable=True)
new_df = grid_return['data']
```

#### [Streamlit Folium](https://github.com/randyzwitch/streamlit-folium)

[Streamlit Component for rendering Folium maps. Created by](https://github.com/randyzwitch/streamlit-folium) [@randyzwitch](https://github.com/randyzwitch).

```python
m = folium.Map(location=[39.949610, -75.150282], zoom_start=16)
folium.Marker([39.949610, -75.150282], popup="Liberty Bell", tooltip="Liberty Bell").add_to(m)
st_data = st_folium(m, width=725)
```

#### [Pandas Profiling](https://github.com/okld/streamlit-pandas-profiling)

[Pandas profiling component for Streamlit. Created by](https://github.com/okld/streamlit-pandas-profiling) [@okld](https://github.com/okld/).

```python
df = pd.read_csv("https://storage.googleapis.com/tf-datasets/titanic/train.csv")
pr = df.profile_report()
st_profile_report(pr)
```

#### [Image Coordinates](https://github.com/blackary/streamlit-image-coordinates)

[Get the coordinates of clicks on an image. Created by](https://github.com/blackary/streamlit-image-coordinates) [@blackary](https://github.com/blackary/).

```python
from streamlit_image_coordinates import streamlit_image_coordinates
value = streamlit_image_coordinates("https://placekitten.com/200/300")
st.write(value)
```

#### [Plotly Events](https://github.com/null-jones/streamlit-plotly-events)

[Make Plotly charts interactive!. Created by](https://github.com/null-jones/streamlit-plotly-events) [@null-jones](https://github.com/null-jones/).

```python
from streamlit_plotly_events import plotly_events
fig = px.line(x=[1], y=[1])
selected_points = plotly_events(fig)
```

#### [Streamlit Extras](https://extras.streamlit.app/)

[A library with useful Streamlit extras. Created by](https://extras.streamlit.app/) [@arnaudmiribel](https://github.com/arnaudmiribel/).

```python
from streamlit_extras.metric_cards import style_metric_cards
col3.metric(label="No Change", value=5000, delta=0)
style_metric_cards()
```

### Chart elements

#### [Simple area charts](/develop/api-reference/charts/st.area_chart)

Display an area chart.

```python
st.area_chart(my_data_frame)
```

#### [Simple bar charts](/develop/api-reference/charts/st.bar_chart)

Display a bar chart.

```python
st.bar_chart(my_data_frame)
```

#### [Simple line charts](/develop/api-reference/charts/st.line_chart)

Display a line chart.

```python
st.line_chart(my_data_frame)
```

#### [Simple scatter charts](/develop/api-reference/charts/st.scatter_chart)

Display a scatter chart.

```python
st.scatter_chart(my_data_frame)
```

#### [Scatterplots on maps](/develop/api-reference/charts/st.map)

Display a map with points on it.

```python
st.map(my_data_frame)
```

#### [Matplotlib](/develop/api-reference/charts/st.pyplot)

Display a matplotlib.pyplot figure.

```python
st.pyplot(my_mpl_figure)
```

#### [Altair](/develop/api-reference/charts/st.altair_chart)

Display a chart using the Altair library.

```python
st.altair_chart(my_altair_chart)
```

#### [Vega-Lite](/develop/api-reference/charts/st.vega_lite_chart)

Display a chart using the Vega-Lite library.

```python
st.vega_lite_chart(my_vega_lite_chart)
```

#### [Plotly](/develop/api-reference/charts/st.plotly_chart)

Display an interactive Plotly chart.

```python
st.plotly_chart(my_plotly_chart)
```

#### [Bokeh](/develop/api-reference/charts/st.bokeh_chart)

Display an interactive Bokeh chart.

```python
st.bokeh_chart(my_bokeh_chart)
```

#### [PyDeck](/develop/api-reference/charts/st.pydeck_chart)

Display a chart using the PyDeck library.

```python
st.pydeck_chart(my_pydeck_chart)
```

#### [GraphViz](/develop/api-reference/charts/st.graphviz_chart)

Display a graph using the dagre-d3 library.

```python
st.graphviz_chart(my_graphviz_spec)
```

### Third-party components

These are featured components created by our lovely community. For more examples and inspiration, check out our [Components Gallery](https://streamlit.io/components) and [Streamlit Extras](https://extras.streamlit.app)!

#### [Streamlit Lottie](https://github.com/andfanilo/streamlit-lottie)

[Integrate](https://github.com/andfanilo/streamlit-lottie) [Lottie](https://lottiefiles.com/) animations inside your Streamlit app. Created by [@andfanilo](https://github.com/andfanilo).

```python
lottie_hello = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_V9t630.json")
st_lottie(lottie_hello, key="hello")
```

[![screenshot](/images/api/components/plotly-events.jpg)](https://github.com/null-jones/streamlit-plotly-events)

#### [Plotly Events](https://github.com/null-jones/streamlit-plotly-events)

[Make Plotly charts interactive!](https://github.com/null-jones/streamlit-plotly-events). Created by [@null-jones](https://github.com/null-jones/).

```python
fig = px.line(x=[1], y=[1])
selected_points = plotly_events(fig)
```

[![screenshot](/images/api/components/extras-chart-annotations.jpg)](https://extras.streamlit.app/)

#### [Streamlit Extras](https://extras.streamlit.app/)

[A library with useful Streamlit extras.](https://extras.streamlit.app/) Created by [@arnaudmiribel](https://github.com/arnaudmiribel/).

```python
chart += get_annotations_chart(annotations=[("Mar 01, 2008", "Pretty good day for GOOG"), ("Dec 01, 2007", "Something's going wrong for GOOG & AAPL"), ("Nov 01, 2008", "Market starts again thanks to..."), ("Dec 01, 2009", "Small crash for GOOG after..."),],)
st.altair_chart(chart, use_container_width=True)
```

[![screenshot](/images/api/components/plost.jpg)](https://github.com/tvst/plost)

#### [Plost](https://github.com/tvst/plost)

[A deceptively simple plotting library for Streamlit.](https://github.com/tvst/plost) Created by [@tvst](https://github.com/tvst).

```python
import plost
plost.line_chart(my_dataframe, x='time', y='stock_value', color='stock_name',)
```

[![screenshot](/images/api/components/hiplot.jpg)](https://github.com/facebookresearch/hiplot)

#### [HiPlot](https://github.com/facebookresearch/hiplot)

[High dimensional Interactive Plotting.](https://github.com/facebookresearch/hiplot) Created by [@facebookresearch](https://github.com/facebookresearch).

```python
data = [{'dropout':0.1, 'lr': 0.001, 'loss': 10.0, 'optimizer': 'SGD'}, {'dropout':0.15, 'lr': 0.01, 'loss': 3.5, 'optimizer': 'Adam'}, {'dropout':0.3, 'lr': 0.1, 'loss': 4.5, 'optimizer': 'Adam'}]
hip.Experiment.from_iterable(data).display()
```

[![screenshot](/images/api/components/echarts.jpg)](https://github.com/andfanilo/streamlit-echarts)

#### [ECharts](https://github.com/andfanilo/streamlit-echarts)

[High dimensional Interactive Plotting.](https://github.com/andfanilo/streamlit-echarts) Created by [@andfanilo](https://github.com/andfanilo).

```python
from streamlit_echarts import st_echarts
st_echarts(options=options)
```

[![screenshot](/images/api/components/folium.jpg)](https://github.com/randyzwitch/streamlit-folium)

#### [Streamlit Folium](https://github.com/randyzwitch/streamlit-folium)

[Streamlit Component for rendering Folium maps.](https://github.com/randyzwitch/streamlit-folium) Created by [@randyzwitch](https://github.com/randyzwitch).

```python
m = folium.Map(location=[39.949610, -75.150282], zoom_start=16)
st_data = st_folium(m, width=725)
```

[![screenshot](/images/api/components/spacy.jpg)](https://github.com/explosion/spacy-streamlit)

#### [Spacy-Streamlit](https://github.com/explosion/spacy-streamlit)

[spaCy building blocks and visualizers for Streamlit apps.](https://github.com/explosion/spacy-streamlit) Created by [@explosion](https://github.com/explosion).

```python
models = ["en_core_web_sm", "en_core_web_md"]
spacy_streamlit.visualize(models, "Sundar Pichai is the CEO of Google.")
```

[![screenshot](/images/api/components/agraph.jpg)](https://github.com/ChrisDelClea/streamlit-agraph)

#### [Streamlit Agraph](https://github.com/ChrisDelClea/streamlit-agraph)

[A Streamlit Graph Vis, based on](https://github.com/ChrisDelClea/streamlit-agraph) [react-grah-vis](https://github.com/crubier/react-graph-vis). Created by [@ChrisDelClea](https://github.DelClea).

```python
from streamlit_agraph import agraph, Node, Edge, Config
agraph(nodes=nodes, edges=edges, config=config)
```

[![screenshot](/images/api/components/lottie.jpg)](https://github.com/andfanilo/streamlit-lottie)

#### [Streamlit Lottie](https://github.com/andfanilo/streamlit-lottie)

[Integrate](https://github.com/andfanilo/streamlit-lottie) [Lottie](https://lottiefiles.com/) animations inside your Streamlit app. Created by [@andfanilo](https://github.com/andfanilo).

```python
lottie_hello = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_V9t630.json")
st_lottie(lottie_hello, key="hello")
```

[![screenshot](/images/api/components/plotly-events.jpg)](https://github.com/null-jones/streamlit-plotly-events)

#### [Plotly Events](https://github.com/null-jones/streamlit-plotly-events)

[Make Plotly charts interactive!](https://github.com/null-jones/streamlit-plotly-events). Created by [@null-jones](https://github.com/null-jones/).

```python
fig = px.line(x=[1], y=[1])
selected_points = plotly_events(fig)
```

[![screenshot](/images/api/components/extras-chart-annotations.jpg)](https://extras.streamlit.app/)

#### [Streamlit Extras](https://extras.streamlit.app/)

[A library with useful Streamlit extras.](https://extras.streamlit.app/) Created by [@arnaudmiribel](https://github.com/arnaudmiribel/).

```python
chart += get_annotations_chart(annotations=[("Mar 01, 2008", "Pretty good day for GOOG"), ("Dec 01, 2007", "Something's going wrong for GOOG & AAPL"), ("Nov 01, 2008", "Market starts again thanks to..."), ("Dec 01, 2009", "Small crash for GOOG after..."),],)
st.altair_chart(chart, use_container_width=True)
```

[![screenshot](/images/api/components/plost.jpg)](https://github.com/tvst/plost)

#### [Plost](https://github.com/tvst/plost)

[A deceptively simple plotting library for Streamlit.](https://github.com/tvst/plost) Created by [@tvst](https://github.com/tvst).

```python
import plost
plost.line_chart(my_dataframe, x='time', y='stock_value', color='stock_name',)
```

[![screenshot](/images/api/components/hiplot.jpg)](https://github.com/facebookresearch/hiplot)

#### [HiPlot](https://github.com/facebookresearch/hiplot)

[High dimensional Interactive Plotting.](https://github.com/facebookresearch/hiplot) Created by [@facebookresearch](https://github.com/facebookresearch).

```python
data = [{'dropout':0.1, 'lr': 0.001, 'loss': 10.0, 'optimizer': 'SGD'}, {'dropout':0.15, 'lr': 0.01, 'loss': 3.5, 'optimizer': 'Adam'}, {'dropout':0.3, 'lr': 0.1, 'loss': 4.5, 'optimizer': 'Adam'}]
hip.Experiment.from_iterable(data).display()
```

[![screenshot](/images/api/components/echarts.jpg)](https://github.com/andfanilo/streamlit-echarts)

#### [ECharts](https://github.com/andfanilo/streamlit-echarts)

[High dimensional Interactive Plotting.](https://github.com/andfanilo/streamlit-echarts) Created by [@andfanilo](https://github.com/andfanilo).

```python
from streamlit_echarts import st_echarts
st_echarts(options=options)
```

[![screenshot](/images/api/components/folium.jpg)](https://github.com/randyzwitch/streamlit-folium)

#### [Streamlit Folium](https://github.com/randyzwitch/streamlit-folium)

[Streamlit Component for rendering Folium maps.](https://github.com/randyzwitch/streamlit-folium) Created by [@randyzwitch](https://github.com/randyzwitch).

```python
m = folium.Map(location=[39.949610, -75.150282], zoom_start=16)
st_data = st_folium(m, width=725)
```

[![screenshot](/images/api/components/spacy.jpg)](https://github.com/explosion/spacy-streamlit)

#### [Spacy-Streamlit](https://github.com/explosion/spacy-streamlit)

[spaCy building blocks and visualizers for Streamlit apps.](https://github.com/explosion/spacy-streamlit) Created by [@explosion](https://github.com/explosion).

```python
models = ["en_core_web_sm", "en_core_web_md"]
spacy_streamlit.visualize(models, "Sundar Pichai is the CEO of Google.")
```

[![screenshot](/images/api/components/agraph.jpg)](https://github.com/ChrisDelClea/streamlit-agraph)

#### [Streamlit Agraph](https://github.com/ChrisDelClea/streamlit-agraph)

[A Streamlit Graph Vis, based on](https://github.com/ChrisDelClea/streamlit-agraph) [react-grah-vis](https://github.com/crubier/react-graph-vis). Created by [@ChrisDelClea](https://github.com/ChrisDelClea).

```python
from streamlit_agraph import agraph, Node, Edge, Config
agraph(nodes=nodes, edges=edges, config=config)
```

[![screenshot](/images/api/components/lottie.jpg)](https://github.com/andfanilo/streamlit-lottie)

#### [Streamlit Lottie](https://github.com/andfanilo/streamlit-lottie)

[Integrate](https://github.com/andfanilo/streamlit-lottie) [Lottie](https://lottiefiles.com/) animations inside your Streamlit app. Created by [@andfanilo](https://github.com/andfanilo).

```python
lottie_hello = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_V9t630.json")
st_lottie(lottie_hello, key="hello")
```

[![screenshot](/images/api/components/plotly-events.jpg)](https://github.com/null-jones/streamlit-plotly-events)

#### [Plotly Events](https://github.com/null-jones/streamlit-plotly-events)

[Make Plotly charts interactive!](https://github.com/null-jones/streamlit-plotly-events). Created by [@null-jones](https://github.com/null-jones/).

```python
fig = px.line(x=[1], y=[1])
selected_points = plotly_events(fig)
```

[![screenshot](/images/api/components/extras-chart-annotations.jpg)](https://extras.streamlit.app/)

#### [Streamlit Extras](https://extras.streamlit.app/)

A library with useful Streamlit extras. Created by [@arnaudmiribel](https://github.com/arnaudmiribel/).

```python
chart += get_annotations_chart(annotations=[("Mar 01, 2008", "Pretty good day for GOOG"), ("Dec 01, 2007", "Something's going wrong for GOOG & AAPL"), ("Nov 01, 2008", "Market starts again thanks to..."), ("Dec 01, 2009", "Small crash for GOOG after..."),],)
st.altair_chart(chart, use_container_width=True)
```

### Input widgets

#### [Button](/develop/api-reference/widgets/st.button)
Display a button widget.
```python
clicked = st.button("Click me")
```

#### [Download button](/develop/api-reference/widgets/st.download_button)
Display a download button widget.
```python
st.download_button("Download file", file)
```

#### [Form button](/develop/api-reference/execution-flow/st.form_submit_button)
Display a form submit button. For use with `st.form`.
```python
st.form_submit_button("Sign up")
```

#### [Link button](/develop/api-reference/widgets/st.link_button)
Display a link button.
```python
st.link_button("Go to gallery", url)
```

#### [Page link](/develop/api-reference/widgets/st.page_link)
Display a link to another page in a multipage app.
```python
st.page_link("app.py", label="Home", icon="🏠")
st.page_link("pages/profile.py", label="My profile")
```

#### [Checkbox](/develop/api-reference/widgets/st.checkbox)
Display a checkbox widget.
```python
selected = st.checkbox("I agree")
```

#### [Color picker](/develop/api-reference/widgets/st.color_picker)
Display a color picker widget.
```python
color = st.color_picker("Pick a color")
```

#### [Feedback](/develop/api-reference/widgets/st.feedback)
Display a rating or sentiment button group.
```python
st.feedback("stars")
```

#### [Multiselect](/develop/api-reference/widgets/st.multiselect)
Display a multiselect widget. The multiselect widget starts as empty.
```python
choices = st.multiselect("Buy", ["milk", "apples", "potatoes"])
```

#### [Pills](/develop/api-reference/widgets/st.pills)
Display a pill-button selection widget.
```python
st.pills("Tags", ["Sports", "AI", "Politics"])
```

#### [Radio](/develop/api-reference/widgets/st.radio)
Display a radio button widget.
```python
choice = st.radio("Pick one", ["cats", "dogs"])
```

#### [Segmented control](/develop/api-reference/widgets/st.segmented_control)
Display a segmented-button selection widget.
```python
st.segmented_control("Filter", ["Open", "Closed", "All"])
```

#### [Selectbox](/develop/api-reference/widgets/st.selectbox)
Display a select widget.
```python
choice = st.selectbox("Pick one", ["cats", "dogs"])
```

#### [Select-slider](/develop/api-reference/widgets/st.select_slider)
Display a slider widget to select items from a list.
```python
size = st.select_slider("Pick a size", ["S", "M", "L"])
```

#### [Toggle](/develop/api-reference/widgets/st.toggle)
Display a toggle widget.
```python
activated = st.toggle("Activate")
```

#### [Number input](/develop/api-reference/widgets/st.number_input)
Display a numeric input widget.
```python
choice = st.number_input("Pick a number", 0, 10)
```

#### [Slider](/develop/api-reference/widgets/st.slider)
Display a slider widget.
```python
number = st.slider("Pick a number", 0, 100)
```

#### [Date input](/develop/api-reference/widgets/st.date_input)
Display a date input widget.
```python
date = st.date_input("Your birthday")
```

#### [Time input](/develop/api-reference/widgets/st.time_input)
Display a time input widget.
```python
time = st.time_input("Meeting time")
```

#### [Chat input](/develop/api-reference/chat/st.chat_input)
Display a chat input widget.
```python
prompt = st.chat_input("Say something")
if prompt:
    st.write(f"The user has sent: {prompt}")
```

#### [Text-area](/develop/api-reference/widgets/st.text_area)
Display a multi-line text input widget.
```python
text = st.text_area("Text to translate")
```

#### [Text input](/develop/api-reference/widgets/st.text_input)
Display a single-line text input widget.
```python
name = st.text_input("First name")
```

#### [Audio input](/develop/api-reference/widgets/st.audio_input)
Display a widget that allows users to record with their microphone.
```python
speech = st.audio_input("Record a voice message")
```

#### [Data editor](/develop/api-reference/data/st.data_editor)
Display a data editor widget.
```python
edited = st.data_editor(df, num_rows="dynamic")
```

#### [File uploader](/develop/api-reference/widgets/st.file_uploader)
Display a file uploader widget.
```python
data = st.file_uploader("Upload a CSV")
```

#### [Camera input](/develop/api-reference/widgets/st.camera_input)
Display a widget that allows users to upload images directly from a camera.
```python
image = st.camera_input("Take a picture")
```

### Third-party components

These are featured components created by our lovely community. For more examples and inspiration, check out our [Components Gallery](https://streamlit.io/components) and [Streamlit Extras](https://extras.streamlit.app)!

#### [Streamlit Chat](https://github.com/AI-Yash/st-chat)
Streamlit Component for a Chatbot UI. Created by [@AI-Yash](https://github.com/AI-Yash).
```python
from streamlit_chat import message
message("My message")
message("Hello bot!", is_user=True) # align's the message to the right
```

#### [Streamlit Option Menu](https://github.com/victoryhb/streamlit-option-menu)
Select a single item from a list of options in a menu. Created by [@victoryhb](https://github.com/victoryhb).
```python
from streamlit_option_menu import option_menu
option_menu("Main Menu", ["Home", 'Settings'], icons=['house', 'gear'], menu_icon="cast", default_index=1)
```

#### [Streamlit Extras](https://extras.streamlit.app/)
A library with useful Streamlit extras. Created by [@arnaudmiribel](https://github.com/arnaudmiribel/).
```python
from streamlit_extras.stoggle import stoggle
stoggle(
    "Click me!",
    """🥷 Surprise! Here's some additional content""",
)
```

#### [Streamlit Elements](https://github.com/okld/streamlit-elements)
Create a draggable and resizable dashboard in Streamlit. Created by [@okls](https://github.com/okls).
```python
from streamlit_elements import elements, mui, html
with elements("new_element"):
    mui.Typography("Hello world")
```

#### [Tags](https://github.com/gagan3012/streamlit-tags)
Add tags to your Streamlit apps. Created by [@gagan3012](https://github.com/gagan3012).

#### Stqdm

](https://github.com/Wirg/stqdm)

[The simplest way to handle a progress bar in streamlit app. Created by](https://github.com/Wirg/stqdm) [@Wirg](https://github.com/Wirg).

```python
from stqdm import stqdm
from time import sleep

for _ in stqdm(range(50)):
    sleep(0.5)
```

#### Timeline

](https://github.com/innerdoc/streamlit-timeline)

[Display a Timeline in Streamlit apps using](https://github.com/innerdoc/streamlit-timeline) [TimelineJS](https://timeline.knightlab.com/). Created by [@innerdoc](https://github.com/innerdoc).

```python
from streamlit_timeline import timeline

with open('example.json', "r") as f:
    timeline(f.read(), height=800)
```

#### Camera input live

](https://github.com/blackary/streamlit-camera-input-live)

[Alternative for st.camera\_input which returns the webcam images live. Created by](https://github.com/blackary/streamlit-camera-input-live) [@blackary](https://github.com/blackary).

```python
from camera_input_live import camera_input_live

image = camera_input_live()
st.image(value)
```

#### Streamlit Ace

](https://github.com/okld/streamlit-ace)

[Ace editor component for Streamlit. Created by](https://github.com/okld/streamlit-ace) [@okld](https://github.com/okld).

```python
from streamlit_ace import st_ace

content = st_ace()
content
```

#### Streamlit Chat

](https://github.com/AI-Yash/st-chat)

[Streamlit Component for a Chatbot UI. Created by](https://github.com/AI-Yash/st-chat) [@AI-Yash](https://github.com/AI-Yash).

```python
from streamlit_chat import message

message("My message")
message("Hello bot!", is_user=True) # align's the message to the right
```

#### Streamlit Option Menu

](https://github.com/victoryhb/streamlit-option-menu)

[Select a single item from a list of options in a menu. Created by](https://github.com/victoryhb/streamlit-option-menu) [@victoryhb](https://github.com/victoryhb).

```python
from streamlit_option_menu import option_menu

option_menu("Main Menu", ["Home", 'Settings'], icons=['house', 'gear'], menu_icon="cast", default_index=1)
```

#### Streamlit Extras

](https://extras.streamlit.app/)

[A library with useful Streamlit extras. Created by](https://extras.streamlit.app/) [@arnaudmiribel](https://github.com/arnaudmiribel/).

```python
from streamlit_extras.stoggle import stoggle

stoggle(
    "Click me!",
    """
    🥷 Surprise! Here's some additional content
    """,
)
```

#### Streamlit Elements

](https://github.com/okld/streamlit-elements)

[Create a draggable and resizable dashboard in Streamlit. Created by](https://github.com/okld/streamlit-elements) [@okls](https://github.com/okls).

```python
from streamlit_elements import elements, mui, html

with elements("new_element"):
    mui.Typography("Hello world")
```

#### Tags

](https://github.com/gagan3012/streamlit-tags)

[Add tags to your Streamlit apps. Created by](https://github.com/gagan3012/streamlit-tags) [@gagan3012](https://github.com/gagan3012).

```python
from streamlit_tags import st_tags

st_tags(
    label='# Enter Keywords:',
    text='Press enter to add more',
    value=['Zero', 'One', 'Two'],
    suggestions=['five', 'six', 'seven', 'eight', 'nine', 'three', 'eleven', 'ten', 'four'],
    maxtags = 4,
    key='1'
)
```

### Media elements

#### Image

Display an image or list of images.

```python
st.image(numpy_array)
st.image(image_bytes)
st.image(file)
st.image("https://example.com/myimage.jpg")
```

#### Logo

Display a logo in the upper-left corner of your app and its sidebar.

```python
st.logo("logo.jpg")
```

#### PDF

Display a PDF file.

```python
st.pdf("my_document.pdf")
```

#### Audio

Display an audio player.

```python
st.audio(numpy_array)
st.audio(audio_bytes)
st.audio(file)
st.audio("https://example.com/myaudio.mp3", format="audio/mp3")
```

#### Video

Display a video player.

```python
st.video(numpy_array)
st.video(video_bytes)
st.video(file)
st.video("https://example.com/myvideo.mp4", format="video/mp4")
```

Third-party components

These are featured components created by our lovely community. For more examples and inspiration, check out our [Components Gallery](https://streamlit.io/components) and [Streamlit Extras](https://extras.streamlit.app)!

#### Streamlit Cropper

[A simple image cropper for Streamlit. Created by](https://github.com/turner-anderson/streamlit-cropper) [@turner-anderson](https://github.com/turner-anderson).

```python
from streamlit_cropper import st_cropper
st_cropper(img, realtime_update=realtime_update, box_color=box_color, aspect_ratio=aspect_ratio)
```

#### Image Coordinates

[Get the coordinates of clicks on an image. Created by](https://github.com/blackary/streamlit-image-coordinates) [@blackary](https://github.com/blackary/).

```python
from streamlit_image_coordinates import streamlit_image_coordinates
streamlit_image_coordinates("https://placekitten.com/200/300")
```

#### Streamlit Lottie

[Integrate](https://github.com/andfanilo/streamlit-lottie) [Lottie](https://lottiefiles.com/) animations inside your Streamlit app. Created by [@andfanilo](https://github.com/andfanilo).

```python
lottie_hello = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_V9t630.json")
st_lottie(lottie_hello, key="hello")
```

#### Streamlit Webrtc

[Handling and transmitting real-time video/audio streams with Streamlit. Created by](https://github.com/whitphx/streamlit-webrtc) [@whitphx](https://github.com/whitphx).

```python
from streamlit_webrtc import webrtc_streamer
webrtc_streamer(key="sample")
```

#### Drawable Canvas

[Provides a sketching canvas using](https://github.com/andfanilo/streamlit-drawable-canvas) [Fabric.js](http://fabricjs.com/). Created by [@andfanilo](https://github.com/andfanilo).

```python
from streamlit_drawable_canvas import st_canvas
st_canvas(fill_color="rgba(255, 165, 0, 0.3)", stroke_width=stroke_width, stroke_color=stroke_color, background_color=bg_color, background_image=Image.open(bg_image) if bg_image else None, update_streamlit=realtime_update, height=150, drawing_mode=drawing_mode, point_display_radius=point_display_radius if drawing_mode == 'point' else 0, key="canvas",)
```

#### Image Comparison

[Compare images with a slider using](https://github.com/fcakyon/streamlit-image-comparison) [JuxtaposeJS](https://juxtapose.knightlab.com/). Created by [@fcakyon](https://github.com/fcakyon).

```python
from streamlit_image_comparison import image_comparison
image_comparison(img1="image1.jpg", img2="image2.jpg",)
```

#### Streamlit Cropper

[A simple image cropper for Streamlit. Created by](https://github.com/turner-anderson/streamlit-cropper) [@turner-anderson](https://github.com/turner-anderson).

```python
from streamlit_cropper import st_cropper
st_cropper(img, realtime_update=realtime_update, box_color=box_color, aspect_ratio=aspect_ratio)
```

#### Image Coordinates

[Get the coordinates of clicks on an image. Created by](https://github.com/blackary/streamlit-image-coordinates) [@blackary](https://github.com/blackary/).

```python
from streamlit_image_coordinates import streamlit_image_coordinates
streamlit_image_coordinates("https://placekitten.com/200/300")
```

#### Streamlit Lottie

[Integrate](https://github.com/andfanilo/streamlit-lottie) [Lottie](https://lottiefiles.com/) animations inside your Streamlit app. Created by [@andfanilo](https://github.com/andfanilo).

```python
lottie_hello = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_V9t630.json")
st_lottie(lottie_hello, key="hello")
```

#### Streamlit Webrtc

[Handling and transmitting real-time video/audio streams with Streamlit. Created by](https://github.com/whitphx/streamlit-webrtc) [@whitphx](https://github.com/whitphx).

```python
from streamlit_webrtc import webrtc_streamer
webrtc_streamer(key="sample")
```

#### Drawable Canvas

[Provides a sketching canvas using](https://github.com/andfanilo/streamlit-drawable-canvas) [Fabric.js](http://fabricjs.com/). Created by [@andfanilo](https://github.com/andfanilo).

```python
from streamlit_drawable_canvas import st_canvas
st_canvas(fill_color="rgba(255, 165, 0, 0.3)", stroke_width=stroke_width, stroke_color=stroke_color, background_color=bg_color, background_image=Image.open(bg_image) if bg_image else None, update_streamlit=realtime_update, height=150, drawing_mode=drawing_mode, point_display_radius=point_display_radius if drawing_mode == 'point' else 0, key="canvas",)
```

#### Image Comparison

[Compare images with a slider using](https://github.com/fcakyon/streamlit-image-comparison) [JuxtaposeJS](https://juxtapose.knightlab.com/). Created by [@fcakyon](https://github.com/fcakyon).

```python
from streamlit_image_comparison import image_comparison
image_comparison(img1="image1.jpg", img2="image2.jpg",)
```

#### Streamlit Cropper

[A simple image cropper for Streamlit. Created by](https://github.com/turner-anderson/streamlit-cropper) [@turner-anderson](https://github.com/turner-anderson).

```python
from streamlit_cropper import st_cropper
st_cropper(img, realtime_update=realtime_update, box_color=box_color, aspect_ratio=aspect_ratio)
```

#### Image Coordinates

[Get the coordinates of clicks on an image. Created by](https://github.com/blackary/streamlit-image-coordinates) [@blackary](https://github.com/blackary/).

```python
from streamlit_image_coordinates import streamlit_image_coordinates
streamlit_image_coordinates("https://placekitten.com/200/300")
```

#### Streamlit Lottie

[Integrate](https://github.com/andfanilo/streamlit-lottie) [Lottie](https://lottiefiles.com/) animations inside your Streamlit app. Created by [@andfanilo](https://github.com/andfanilo).

```python
lottie_hello = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_V9t630.json")
st_lottie(lottie_hello, key="hello")
```

#### Streamlit Webrtc

[Handling and transmitting real-time video/audio streams with Streamlit. Created by](https://github.com/whitphx/streamlit-webrtc) [@whitphx](https://github.com/whitphx).

```python
from streamlit_webrtc import webrtc_streamer
webrtc_streamer(key="sample")
```

#### Drawable Canvas

[Provides a sketching canvas using](https://github.com/andfanilo/streamlit-drawable-canvas) [Fabric.js](http://fabricjs.com/). Created by [@andfanilo](https://github.com/andfanilo).

```python
from streamlit_drawable_canvas import st_canvas
st_canvas(fill_color="rgba(255, 165, 0, 0.3)", stroke_width=stroke_width, stroke_color=stroke_color, background_color=bg_color, background_image=Image.open(bg_image) if bg_image else None, update_streamlit=realtime_update, height=150, drawing_mode=drawing_mode, point_display_radius=point_display_radius if drawing_mode == 'point' else 0, key="canvas",)
```

#### Image Comparison

[Compare images with a slider using](https://github.com/fcakyon/streamlit-image-comparison) [JuxtaposeJS](https://juxtapose.knightlab.com/). Created by [@fcakyon](https://github.com/fcakyon).

```python
from streamlit_image_comparison import image_comparison
image_comparison(img1="image1.jpg", img2="image2.jpg",)
```

### Layouts and containers

#### Columns

Insert containers laid out as side-by-side columns.

```python
col1, col2 = st.columns(2)
col1.write("this is column 1")
col2.write("this is column 2")
```

#### Container

Insert a multi-element container.

```python
c = st.container()
st.write("This will show last")
c.write("This will show first")
c.write("This will show second")
```

#### Modal dialog

Insert a modal dialog that can rerun independently from the rest of the script.

```python
@st.dialog("Sign up")
def email_form():
    name = st.text_input("Name")
    email = st.text_input("Email")
```

#### Empty

Insert a single-element container.


```python
c = st.empty()
st.write("This will show last")
c.write("This will be replaced")
c.write("This will show first")
```

#### Expander

Insert a multi-element container that can be expanded/collapsed.

```python
with st.expander("Open to see more"):
    st.write("This is more content")
```

#### Popover

Insert a multi-element popover container that can be opened/closed.

```python
with st.popover("Settings"):
    st.checkbox("Show completed")
```

#### Sidebar

Display items in a sidebar.

```python
st.sidebar.write("This lives in the sidebar")
st.sidebar.button("Click me!")
```

#### Tabs

Insert containers separated into tabs.

```python
tab1, tab2 = st.tabs(["Tab 1", "Tab2"])
tab1.write("this is tab 1")
tab2.write("this is tab 2")
```

Third-party components

These are featured components created by our lovely community. For more examples and inspiration, check out our [Components Gallery](https://streamlit.io/components) and [Streamlit Extras](https://extras.streamlit.app)!

#### Streamlit Elements

[Create a draggable and resizable dashboard in Streamlit. Created by](https://github.com/okld/streamlit-elements) [@okls](https://github.com/okls).

```python
from streamlit_elements import elements, mui, html
with elements("new_element"):
    mui.Typography("Hello world")
```

#### Pydantic

[Auto-generate Streamlit UI from Pydantic Models and Dataclasses. Created by](https://github.com/lukasmasuch/streamlit-pydantic) [@lukasmasuch](https://github.com/lukasmasuch).

```python
import streamlit_pydantic as sp
sp.pydantic_form(key="my_form", model=ExampleModel)
```

#### Streamlit Pages

[An experimental version of Streamlit Multi-Page Apps. Created by](https://github.com/blackary/st_pages) [@blackary](https://github.com/blackary).

```python
from st_pages import Page, show_pages, add_page_title

show_pages(
    [
        Page("streamlit_app.py", "Home", "🏠"),
        Page("other_pages/page2.py", "Page 2", ":books:"),
    ]
)
```

### Chat elements

Streamlit provides a few commands to help you build conversational apps. These chat elements are designed to be used in conjunction with each other, but you can also use them separately.

`st.chat_message` lets you insert a chat message container into the app so you can display messages from the user or the app. Chat containers can contain other Streamlit elements, including charts, tables, text, and more. `st.chat_input` lets you display a chat input widget so the user can type in a message.

#### Chat input

Display a chat input widget.

```python
prompt = st.chat_input("Say something")
if prompt:
    st.write(f"The user has sent: {prompt}")
```

#### Chat message

Insert a chat message container.

```python
import numpy as np

with st.chat_message("user"):
    st.write("Hello 👋")
    st.line_chart(np.random.randn(30, 3))
```

#### Status container

Display output of long-running tasks in a container.

```python
with st.status('Running'):
    do_something_slow()
```

#### st.write_stream

Write generators or streams to the app with a typewriter effect.

```python
st.write_stream(my_generator)
st.write_stream(my_llm_stream)
```

### Status elements

#### Progress bar

Display a progress bar.

```python
for i in range(101):
    st.progress(i)
do_something_slow()
```

#### Spinner

Temporarily displays a message while executing a block of code.

```python
with st.spinner("Please wait..."):
    do_something_slow()
```

#### Status container

Display output of long-running tasks in a container.

```python
with st.status('Running'):
    do_something_slow()
```

#### Toast

Briefly displays a toast message in the bottom-right corner.

```python
st.toast('Butter!', icon='🧈')
```

#### Balloons

Display celebratory balloons!

```python
do_something() # Celebrate when all done!
st.balloons()
```

#### Snowflakes

Display celebratory snowflakes!

```python
do_something() # Celebrate when all done!
st.snow()
```

#### Success box

Display a success message.

```python
st.success("Match found!")
```

#### Info box

Display an informational message.

```python
st.info("Dataset is updated every day at midnight.")
```

#### Warning box

Display warning message.

```python
st.warning("Unable to fetch image. Skipping...")
```

#### Error box

Display error message.

```python
st.error("We encountered an error")
```

#### Exception output

Display an exception.

```python
e = RuntimeError("This is an exception of type RuntimeError")
st.exception(e)
```

Third-party components

These are featured components created by our lovely community. For more examples and inspiration, check out our [Components Gallery](https://streamlit.io/components) and [Streamlit Extras](https://extras.streamlit.app)!

#### Stqdm

[The simplest way to handle a progress bar in streamlit app. Created by](https://github.com/Wirg/stqdm) [@Wirg](https://github.com/Wirg).

```python
from stqdm import stqdm
for _ in stqdm(range(50)):
    sleep(0.5)
```

#### Custom notification box

[A custom notification box with the ability to close it out. Created by](https://github.com/Socvest/streamlit-custom-notification-box) [@Socvest](https://github.com/Socvest).

```python
from streamlit_custom_notification_box import custom_notification_box

styles = {'material-icons':{'color': 'red'}, 'text-icon-link-close-container': {'box-shadow': '#3896de 0px 4px'}, 'notification-text': {'':''}, 'close-button':{'':''}, 'link':{'':''}}
custom_notification_box(icon='info', textDisplay='We are almost done with your registration...', externalLink='more info', url='#', styles=styles, key="foo")
```

#### Streamlit Extras

[A library with useful Streamlit extras. Created by](https://extras.streamlit.app/) [@arnaudmiribel](https://github.com/arnaudmiribel/).

```python
from streamlit_extras.let_it_rain import rain

rain(
    emoji="🎈",
    font_size=54,
    falling_speed=5,
    animation_length="infinite",
)
```

## App logic and configuration
```

### Authentication and user info

#### [Log in a user](/develop/api-reference/user/st.login)
`st.login()` starts an authentication flow with an identity provider.

```python
st.login()
```

#### [Log out a user](/develop/api-reference/user/st.logout)
`st.logout()` removes a user's identity information.

```python
st.logout()
```

#### [User info](/develop/api-reference/user/st.user)
`st.user` returns information about a logged-in user.

```python
if st.user.is_logged_in: st.write(f"Welcome back, {st.user.name}!")
```

### Navigation and pages

![screenshot](/images/api/navigation.jpg)
#### [Navigation](/develop/api-reference/navigation/st.navigation)
Configure the available pages in a multipage app.

```python
st.navigation({ "Your account" : [log_out, settings], "Reports" : [overview, usage], "Tools" : [search] })
```

![screenshot](/images/api/page.jpg)
#### [Page](/develop/api-reference/navigation/st.page)
Define a page in a multipage app.

```python
home = st.Page( "home.py", title="Home", icon=":material/home:" )
```

![screenshot](/images/api/page_link.jpg)
#### [Page link](/develop/api-reference/widgets/st.page_link)
Display a link to another page in a multipage app.

```python
st.page_link("app.py", label="Home", icon="🏠")
st.page_link("pages/profile.py", label="My profile")
```

#### [Switch page](/develop/api-reference/navigation/st.switch_page)
Programmatically navigates to a specified page.

```python
st.switch_page("pages/my_page.py")
```

### Execution flow

![screenshot](/images/api/dialog.jpg)
#### [Modal dialog](/develop/api-reference/execution-flow/st.dialog)
Insert a modal dialog that can rerun independently from the rest of the script.

```python
@st.dialog("Sign up")
def email_form():
    name = st.text_input("Name")
    email = st.text_input("Email")
```

#### [Forms](/develop/api-reference/execution-flow/st.form)
Create a form that batches elements together with a “Submit" button.

```python
with st.form(key='my_form'):
    name = st.text_input("Name")
    email = st.text_input("Email")
    st.form_submit_button("Sign up")
```

#### [Fragments](/develop/api-reference/execution-flow/st.fragment)
Define a fragment to rerun independently from the rest of the script.

```python
@st.fragment(run_every="10s")
def fragment():
    df = get_data()
    st.line_chart(df)
```

#### [Rerun script](/develop/api-reference/execution-flow/st.rerun)
Rerun the script immediately.

```python
st.rerun()
```

#### [Stop execution](/develop/api-reference/execution-flow/st.stop)
Stops execution immediately.

```python
st.stop()
```

Third-party components

These are featured components created by our lovely community. For more examples and inspiration, check out our [Components Gallery](https://streamlit.io/components) and [Streamlit Extras](https://extras.streamlit.app)!

![screenshot](/images/api/components/autorefresh.jpg)
#### [Autorefresh](https://github.com/kmcgrady/streamlit-autorefresh)
Force a refresh without tying up a script. Created by [@kmcgrady](https://github.com/kmcgrady).

```python
from streamlit_autorefresh import st_autorefresh
st_autorefresh(interval=2000, limit=100, key="fizzbuzzcounter")
```

![screenshot](/images/api/components/pydantic.jpg)
#### [Pydantic](https://github.com/lukasmasuch/streamlit-pydantic)
Auto-generate Streamlit UI from Pydantic Models and Dataclasses. Created by [@lukasmasuch](https://github.com/lukasmasuch).

```python
import streamlit_pydantic as sp
sp.pydantic_form(key="my_form", model=ExampleModel)
```

![screenshot](/images/api/components/pages.jpg)
#### [Streamlit Pages](https://github.com/blackary/st_pages)
An experimental version of Streamlit Multi-Page Apps. Created by [@blackary](https://github.com/blackary).

```python
from st_pages import Page, show_pages, add_page_title
show_pages([
    Page("streamlit_app.py", "Home", "🏠"),
    Page("other_pages/page2.py", "Page 2", ":books:"),
])
```

### Caching and state

#### [Cache data](/develop/api-reference/caching-and-state/st.cache_data)
Function decorator to cache functions that return data (e.g. dataframe transforms, database queries, ML inference).

```python
@st.cache_data
def long_function(param1, param2):
    # Perform expensive computation here or
    # fetch data from the web here
    return data
```

#### [Cache resource](/develop/api-reference/caching-and-state/st.cache_resource)
Function decorator to cache functions that return global resources (e.g. database connections, ML models).

```python
@st.cache_resource
def init_model():
    # Return a global resource here
    return pipeline(
        "sentiment-analysis",
        model="distilbert-base-uncased-finetuned-sst-2-english"
    )
```

#### [Session state](/develop/api-reference/caching-and-state/st.session_state)
Session state is a way to share variables between reruns, for each user session.

```python
st.session_state['key'] = value
```

#### [Query parameters](/develop/api-reference/caching-and-state/st.query_params)
Get, set, or clear the query parameters that are shown in the browser's URL bar.

```python
st.query_params[key] = value
st.query_params.clear()
```

#### [Context](/develop/api-reference/caching-and-state/st.context)
`st.context` provides a read-only interface to access cookies, headers, locale, and other browser-session information.

```python
st.context.cookies
st.context.headers
```

### Connections and databases

#### Setup your connection

![screenshot](/images/api/connection.svg)
#### [Create a connection](/develop/api-reference/connections/st.connection)
Connect to a data source or API

```python
conn = st.connection('pets_db', type='sql')
pet_owners = conn.query('select * from pet_owners')
st.dataframe(pet_owners)
```

#### Built-in connections

![screenshot](/images/api/connections.SnowflakeConnection.svg)
#### [SnowflakeConnection](/develop/api-reference/connections/st.connections.snowflakeconnection)
A connection to Snowflake.

```python
conn = st.connection('snowflake')
```

![screenshot](/images/api/connections.SQLConnection.svg)
#### [SQLConnection](/develop/api-reference/connections/st.connections.sqlconnection)
A connection to a SQL database using SQLAlchemy.

```python
conn = st.connection('sql')
```

#### Build your own connections

#### [Connection base class](/develop/api-reference/connections/st.connections.baseconnection)
Build your own connection with `BaseConnection`.

```python
class MyConnection(BaseConnection[myconn.MyConnection]):
    def _connect(self, **kwargs) -> MyConnection:
        return myconn.connect(**self._secrets, **kwargs)
    def query(self, query):
        return self._instance.query(query)
```

#### Secrets management

#### [Secrets singleton](/develop/api-reference/connections/st.secrets)
Access secrets from a local TOML file.

```python
key = st.secrets["OpenAI_key"]
```

#### [Secrets file](/develop/api-reference/connections/secrets.toml)
Save your secrets in a per-project or per-profile TOML file.

```toml
OpenAI_key = "<YOUR_SECRET_KEY>"
```

Third-party components

These are featured components created by our lovely community. For more examples and inspiration, check out our [Components Gallery](https://streamlit.io/components) and [Streamlit Extras](https://extras.streamlit.app)!

![screenshot](/images/api/components/authenticator.jpg)
#### [Authenticator](https://github.com/mkhorasani/Streamlit-Authenticator)
A secure authentication module to validate user credentials. Created by [@mkhorasani](https://github.com/mkhorasani).

```python
import streamlit_authenticator as stauth
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)
```

[![screenshot](/images/api/components/localstorage.jpg)](https://github.com/gagangoku/streamlit-ws-localstorage)

#### WS localStorage

A simple synchronous way of accessing localStorage from your app. Created by [@gagangoku](https://github.com/gagangoku).

```python
from streamlit_ws_localstorage import injectWebsocketCode
ret = conn.setLocalStorageVal(key='k1', val='v1')
st.write('ret: ' + ret)
```

[![screenshot](/images/api/components/auth0.jpg)](https://github.com/conradbez/streamlit-auth0)

#### Streamlit Auth0

The fastest way to provide comprehensive login inside Streamlit. Created by [@conradbez](https://github.com/conradbez).

```python
from auth0_component import login_button
user_info = login_button(clientId, domain = domain)
st.write(user_info)
```

### Custom Components

#### Declare a component

Create and register a custom component.

```python
from st.components.v1 import declare_component
declare_component(
    "custom_slider",
    "/frontend",
)
```

#### HTML

Display an HTML string in an iframe.

```python
from st.components.v1 import html
html(
    "<p>Foo bar.</p>"
)
```

#### iframe

Load a remote URL in an iframe.

```python
from st.components.v1 import iframe
iframe(
    "docs.streamlit.io"
)
```

### Configuration

#### Configuration file

Configures the default settings for your app.

```
your-project/
├── .streamlit/
│   └── config.toml
└── your_app.py
```

#### Get config option

Retrieve a single configuration option.

```python
st.get_option("theme.primaryColor")
```

#### Set config option

Set a single configuration option. (This is very limited.)

```python
st.set_option("deprecation.showPyplotGlobalUse", False)
```

#### Set page title, favicon, and more

Configures the default settings of the page.

```python
st.set_page_config(
    page_title="My app",
    page_icon=":shark:",
)
```

## Developer tools

### App testing

#### st.testing.v1.AppTest

`st.testing.v1.AppTest` simulates a running Streamlit app for testing.

```python
from streamlit.testing.v1 import AppTest
at = AppTest.from_file("streamlit_app.py")
at.secrets["WORD"] = "Foobar"
at.run()
assert not at.exception
at.text_input("word").input("Bazbat").run()
assert at.warning[0].value == "Try again."
```

#### AppTest.from_file

`st.testing.v1.AppTest.from_file` initializes a simulated app from a file.

```python
from streamlit.testing.v1 import AppTest
at = AppTest.from_file("streamlit_app.py")
at.run()
```

#### AppTest.from_string

`st.testing.v1.AppTest.from_string` initializes a simulated app from a string.

```python
from streamlit.testing.v1 import AppTest
at = AppTest.from_string(app_script_as_string)
at.run()
```

#### AppTest.from_function

`st.testing.v1.AppTest.from_function` initializes a simulated app from a function.

```python
from streamlit.testing.v1 import AppTest
at = AppTest.from_function(app_script_as_callable)
at.run()
```

#### Block

A representation of container elements, including:

*   `st.chat_message`
*   `st.columns`
*   `st.sidebar`
*   `st.tabs`
*   The main body of the app.

```python
# at.sidebar returns a Block
at.sidebar.button[0].click().run()
assert not at.exception
```

#### Element

The base class for representation of all elements, including:

*   `st.title`
*   `st.header`
*   `st.markdown`
*   `st.dataframe`

```python
# at.title returns a sequence of Title
# Title inherits from Element
assert at.title[0].value == "My awesome app"
```

#### Button

A representation of `st.button` and `st.form_submit_button`.

```python
at.button[0].click().run()
```

#### ChatInput

A representation of `st.chat_input`.

```python
at.chat_input[0].set_value("What is Streamlit?").run()
```

#### Checkbox

A representation of `st.checkbox`.

```python
at.checkbox[0].check().run()
```

#### ColorPicker

A representation of `st.color_picker`.

```python
at.color_picker[0].pick("#FF4B4B").run()
```

#### DateInput

A representation of `st.date_input`.

```python
import datetime
release_date = datetime.date(2023, 10, 26)
at.date_input[0].set_value(release_date).run()
```

#### Multiselect

A representation of `st.multiselect`.

```python
at.multiselect[0].select("New York").run()
```

#### NumberInput

A representation of `st.number_input`.

```python
at.number_input[0].increment().run()
```

#### Radio

A representation of `st.radio`.

```python
at.radio[0].set_value("New York").run()
```

#### SelectSlider

A representation of `st.select_slider`.

```python
at.select_slider[0].set_range("A","C").run()
```

#### Selectbox

A representation of `st.selectbox`.

```python
at.selectbox[0].select("New York").run()
```

#### Slider

A representation of `st.slider`.

```python
at.slider[0].set_range(2,5).run()
```

#### TextArea

A representation of `st.text_area`.

```python
at.text_area[0].input("Streamlit is awesome!").run()
```

#### TextInput

A representation of `st.text_input`.

```python
at.text_input[0].input("Streamlit").run()
```

#### TimeInput

A representation of `st.time_input`.

```python
at.time_input[0].increment().run()
```

#### Toggle

A representation of `st.toggle`.

```python
at.toggle[0].set_value("True").run()
```

Third-party components

These are featured components created by our lovely community. For more examples and inspiration, check out our [Components Gallery](https://streamlit.io/components) and [Streamlit Extras](https://extras.streamlit.app)!
```

### Pandas Profiling

Pandas profiling component for Streamlit. Created by [@okld](https://github.com/okld/streamlit-pandas-profiling).

```python
df = pd.read_csv("https://storage.googleapis.com/tf-datasets/titanic/train.csv")
pr = df.profile_report()
st_profile_report(pr)
```

### Streamlit Ace

Ace editor component for Streamlit. Created by [@okld](https://github.com/okld/streamlit-ace).

```python
from streamlit_ace import st_ace

content = st_ace()
content
```

### Streamlit Analytics

Track & visualize user interactions with your streamlit app. Created by [@jrieke](https://github.com/jrieke/streamlit-analytics).

```python
import streamlit_analytics

with streamlit_analytics.track():
    st.text_input("Write something")
```

---

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.