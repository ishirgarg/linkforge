# Data elements - Streamlit

> Source: [https://docs.streamlit.io/develop/api-reference/data](https://docs.streamlit.io/develop/api-reference/data)

This document outlines the data elements available in the Streamlit API.


When you're working with data, it is extremely valuable to visualize that data quickly, interactively, and from multiple different angles. That's what Streamlit is actually built and optimized for.

You can display data via [charts](/develop/api-reference/data#display-charts), and you can display it in raw form. These are the Streamlit commands you can use to display and interact with raw data.

### Dataframes

Display a dataframe as an interactive table.

```python
st.dataframe(my_data_frame)
```

### Data editor

Display a data editor widget.

```python
edited = st.data_editor(df, num_rows="dynamic")
```

### Column configuration

Configure the display and editing behavior of dataframes and data editors.

```python
st.column_config.NumberColumn("Price (in USD)", min_value=0, format="$%d")
```

### Static tables

Display a static table.

```python
st.table(my_data_frame)
```

### Metrics

Display a metric in big bold font, with an optional indicator of how the metric changed.

```python
st.metric("My metric", 42, 2)
```

### Dicts and JSON

Display object or string as a pretty-printed JSON string.

```python
st.json(my_dict)
```

### Third-party components

These are featured components created by our lovely community. For more examples and inspiration, check out our [Components Gallery](https://streamlit.io/components) and [Streamlit Extras](https://extras.streamlit.app)!

#### Image Coordinates

[Get the coordinates of clicks on an image. Created by](https://github.com/blackary/streamlit-image-coordinates) [@blackary](https://github.com/blackary/).

```python
from streamlit_image_coordinates import streamlit_image_coordinates
value = streamlit_image_coordinates("https://placekitten.com/200/300")
st.write(value)
```

#### Plotly Events

[Make Plotly charts interactive!. Created by](https://github.com/null-jones/streamlit-plotly-events) [@null-jones](https://github.com/null-jones/).

```python
from streamlit_plotly_events import plotly_events
fig = px.line(x=[1], y=[1])
selected_points = plotly_events(fig)
```

#### Streamlit Extras

[A library with useful Streamlit extras. Created by](https://extras.streamlit.app/) [@arnaudmiribel](https://github.com/arnaudmiribel/).

```python
from streamlit_extras.metric_cards import style_metric_cards
col3.metric(label="No Change", value=5000, delta=0)
style_metric_cards()
```

#### Streamlit Aggrid

[Implementation of Ag-Grid component for Streamlit. Created by](https://github.com/PablocFonseca/streamlit-aggrid) [@PablocFonseca](https://github.com/PablocFonseca).

```python
df = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6]})
grid_return = AgGrid(df, editable=True)
new_df = grid_return['data']
```

#### Streamlit Folium

[Streamlit Component for rendering Folium maps. Created by](https://github.com/randyzwitch/streamlit-folium) [@randyzwitch](https://github.com/randyzwitch).

```python
m = folium.Map(location=[39.949610, -75.150282], zoom_start=16)
folium.Marker([39.949610, -75.150282], popup="Liberty Bell", tooltip="Liberty Bell").add_to(m)
st_data = st_folium(m, width=725)
```

#### Pandas Profiling

[Pandas profiling component for Streamlit. Created by](https://github.com/okld/streamlit-pandas-profiling) [@okld](https://github.com/okld/).

```python
df = pd.read_csv("https://storage.googleapis.com/tf-datasets/titanic/train.csv")
pr = df.profile_report()
st_profile_report(pr)
```

#### Image Coordinates

[Get the coordinates of clicks on an image. Created by](https://github.com/blackary/streamlit-image-coordinates) [@blackary](https://github.com/blackary/).

```python
from streamlit_image_coordinates import streamlit_image_coordinates
value = streamlit_image_coordinates("https://placekitten.com/200/300")
st.write(value)
```

#### Plotly Events

[Make Plotly charts interactive!. Created by](https://github.com/null-jones/streamlit-plotly-events) [@null-jones](https://github.com/null-jones/).

```python
from streamlit_plotly_events import plotly_events
fig = px.line(x=[1], y=[1])
selected_points = plotly_events(fig)
```

#### Streamlit Extras

[A library with useful Streamlit extras. Created by](https://extras.streamlit.app/) [@arnaudmiribel](https://github.com/arnaudmiribel/).

```python
from streamlit_extras.metric_cards import style_metric_cards
col3.metric(label="No Change", value=5000, delta=0)
style_metric_cards()
```


A library with useful Streamlit extras. Created by [Arnaud Miribel](https://extras.streamlit.app/) [@arnaudmiribel](https://github.com/arnaudmiribel/).

```python
from streamlit_extras.metric_cards import style_metric_cards

col3.metric(label="No Change", value=5000, delta=0)
style_metric_cards()
```

Next

[_arrow_back_Previous: Text elements](/develop/api-reference/text) [_arrow_forward_Next: st.dataframe](/develop/api-reference/data/st.dataframe)


### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

***

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

[GitHub](https://github.com/streamlit "GitHub") [YouTube](https://www.youtube.com/channel/UC3LD42rjj-Owtxsa6PwGU5Q "YouTube") [Twitter](https://twitter.com/streamlit "Twitter") [LinkedIn](https://www.linkedin.com/company/streamlit "LinkedIn") [Newsletter](https://info.snowflake.com/streamlit-newsletter-sign-up.html "Newsletter")

© 2025 Snowflake Inc. [Cookie policy](https://www.snowflake.com/legal/cookie-policy/)

_forum_ Ask A