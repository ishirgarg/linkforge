```markdown
# Chart elements

[Original URL](https://docs.streamlit.io/develop/api-reference/charts)

Streamlit supports several different charting libraries, and our goal is to continually add support for more. Right now, the most basic library in our arsenal is [Matplotlib](https://matplotlib.org/). Then there are also interactive charting libraries like [Vega Lite](https://vega.github.io/vega-lite/) (2D charts) and [deck.gl](https://github.com/uber/deck.gl) (maps and 3D charts). And finally we also provide a few chart types that are "native" to Streamlit, like `st.line_chart` and `st.area_chart`.

## Simple chart elements

[![screenshot](/images/api/area_chart.jpg)

#### Simple area charts

Display an area chart.

`st.area_chart(my_data_frame)`

[![screenshot](/images/api/bar_chart.jpg)

#### Simple bar charts

Display a bar chart.

`st.bar_chart(my_data_frame)`

[![screenshot](/images/api/line_chart.jpg)

#### Simple line charts

Display a line chart.

`st.line_chart(my_data_frame)`

[![screenshot](/images/api/scatter_chart.svg)

#### Simple scatter charts

Display a line chart.

`st.scatter_chart(my_data_frame)`

[![screenshot](/images/api/map.jpg)

#### Scatterplots on maps

Display a map with points on it.

`st.map(my_data_frame)`

## Advanced chart elements
```

#### Matplotlib

Display a matplotlib.pyplot figure.

`st.pyplot(my_mpl_figure)`

#### Altair

Display a chart using the Altair library.

`st.altair_chart(my_altair_chart)`

#### Vega-Lite

Display a chart using the Vega-Lite library.

`st.vega_lite_chart(my_vega_lite_chart)`

#### Plotly

Display an interactive Plotly chart.

`st.plotly_chart(my_plotly_chart)`

#### Bokeh

Display an interactive Bokeh chart.

`st.bokeh_chart(my_bokeh_chart)`

#### PyDeck

Display a chart using the PyDeck library.

`st.pydeck_chart(my_pydeck_chart)`

#### GraphViz

Display a graph using the dagre-d3 library.

`st.graphviz_chart(my_graphviz_spec)`

### Third-party components

These are featured components created by our lovely community. For more examples and inspiration, check out our [Components Gallery](https://streamlit.io/components) and [Streamlit Extras](https://extras.streamlit.app)!

#### Streamlit Lottie

[Integrate](https://github.com/andfanilo/streamlit-lottie) [Lottie](https://lottiefiles.com/) animations inside your Streamlit app. Created by [@andfanilo](https://github.com/andfanilo).

```python
lottie_hello = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_V9t630.json")
st_lottie(lottie_hello, key="hello")
```

#### Plotly Events

[Make Plotly charts interactive!. Created by](https://github.com/null-jones/streamlit-plotly-events) [@null-jones](https://github.com/null-jones/).

```python
fig = px.line(x=[1], y=[1])
selected_points = plotly_events(fig)
```

#### Streamlit Extras

[A library with useful Streamlit extras. Created by](https://extras.streamlit.app/) [@arnaudmiribel](https://github.com/arnaudmiribel/).

```python
chart += get_annotations_chart(annotations=[("Mar 01, 2008", "Pretty good day for GOOG"), ("Dec 01, 2007", "Something's going wrong for GOOG & AAPL"), ("Nov 01, 2008", "Market starts again thanks to..."), ("Dec 01, 2009", "Small crash for GOOG after..."),],)
st.altair_chart(chart, use_container_width=True)
```

#### Plost

[A deceptively simple plotting library for Streamlit. Created by](https://github.com/tvst/plost) [@tvst](https://github.com/tvst).

```python
import plost
plost.line_chart(my_dataframe, x='time', y='stock_value', color='stock_name',)
```

#### HiPlot

[High dimensional Interactive Plotting. Created by](https://github.com/facebookresearch/hiplot) [@facebookresearch](https://github.com/facebookresearch).

```python
data = [{'dropout':0.1, 'lr': 0.001, 'loss': 10.0, 'optimizer': 'SGD'}, {'dropout':0.15, 'lr': 0.01, 'loss': 3.5, 'optimizer': 'Adam'}, {'dropout':0.3, 'lr': 0.1, 'loss': 4.5, 'optimizer': 'Adam'}]
hip.Experiment.from_iterable(data).display()
```

#### ECharts

[High dimensional Interactive Plotting. Created by](https://github.com/andfanilo/streamlit-echarts) [@andfanilo](https://github.com/andfanilo).

```python
from streamlit_echarts import st_echarts
st_echarts(options=options)
```

#### Streamlit Folium



[Streamlit Component for rendering Folium maps. Created by](https://github.com/randyzwitch/streamlit-folium) [@randyzwitch](https://github.com/randyzwitch).

```python
m = folium.Map(location=[39.949610, -75.150282], zoom_start=16) st_data = st_folium(m, width=725)
```

#### [Spacy-Streamlit](https://github.com/explosion/spacy-streamlit)
![screenshot](/images/api/components/spacy.jpg)

[spaCy building blocks and visualizers for Streamlit apps. Created by](https://github.com/explosion/spacy-streamlit) [@explosion](https://github.com/explosion).

```python
models = ["en_core_web_sm", "en_core_web_md"] spacy_streamlit.visualize(models, "Sundar Pichai is the CEO of Google.")
```

#### [Streamlit Agraph](https://github.com/ChrisDelClea/streamlit-agraph)
![screenshot](/images/api/components/agraph.jpg)

[A Streamlit Graph Vis, based on](https://github.com/ChrisDelClea/streamlit-agraph) [react-grah-vis](https://github.com/crubier/react-graph-vis). Created by [@ChrisDelClea](https://github.com/ChrisDelClea).

```python
from streamlit_agraph import agraph, Node, Edge, Config agraph(nodes=nodes, edges=edges, config=config)
```

#### [Streamlit Lottie](https://github.com/andfanilo/streamlit-lottie)
![screenshot](/images/api/components/lottie.jpg)

[Integrate](https://github.com/andfanilo/streamlit-lottie) [Lottie](https://lottiefiles.com/) animations inside your Streamlit app. Created by [@andfanilo](https://github.com/andfanilo).

```python
lottie_hello = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_V9t630.json") st_lottie(lottie_hello, key="hello")
```

#### [Plotly Events](https://github.com/null-jones/streamlit-plotly-events)
![screenshot](/images/api/components/plotly-events.jpg)

[Make Plotly charts interactive!. Created by](https://github.com/null-jones/streamlit-plotly-events) [@null-jones](https://github.com/null-jones/).

```python
fig = px.line(x=[1], y=[1]) selected_points = plotly_events(fig)
```

#### [Streamlit Extras](https://extras.streamlit.app/)
![screenshot](/images/api/components/extras-chart-annotations.jpg)

[A library with useful Streamlit extras. Created by](https://extras.streamlit.app/) [@arnaudmiribel](https://github.com/arnaudmiribel/).

```python
chart += get_annotations_chart(annotations=[("Mar 01, 2008", "Pretty good day for GOOG"), ("Dec 01, 2007", "Something's going wrong for GOOG & AAPL"), ("Nov 01, 2008", "Market starts again thanks to..."), ("Dec 01, 2009", "Small crash for GOOG after..."),],) st.altair_chart(chart, use_container_width=True)
```

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

***

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

[GitHub](https://github.com/streamlit "GitHub") [YouTube](https://www.youtube.com/channel/UC3LD42rjj-Owtxsa6PwGU5Q "YouTube") [Twitter](https://twitter.com/streamlit "Twitter") [LinkedIn](https://www.linkedin.com/company/streamlit "LinkedIn") [Newsletter](https://info.snowflake.com/streamlit-newsletter-sign-up.html "Newsletter")

© 2025 Snowflake Inc. [Cookie policy](https://www.snowflake.com/legal/cookie-policy/)

_forum_ Ask A