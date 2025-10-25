```markdown
# Input Widgets

[Original URL](https://docs.streamlit.io/develop/api-reference/widgets)

With widgets, Streamlit allows you to bake interactivity directly into your apps with buttons, sliders, text inputs, and more.

## Button elements
```


### Button

Display a button widget.

```python
clicked = st.button("Click me")
```

### Download button

Display a download button widget.

```python
st.download_button("Download file", file)
```

### Form button

Display a form submit button. For use with `st.form`.

```python
st.form_submit_button("Sign up")
```

### Link button

Display a link button.

```python
st.link_button("Go to gallery", url)
```

### Page link

Display a link to another page in a multipage app.

```python
st.page_link("app.py", label="Home", icon="🏠")
st.page_link("pages/profile.py", label="My profile")
```

## Selection elements

### Checkbox

Display a checkbox widget.

```python
selected = st.checkbox("I agree")
```

### Color picker

Display a color picker widget.

```python
color = st.color_picker("Pick a color")
```

### Feedback

Display a rating or sentiment button group.

```python
st.feedback("stars")
```

### Multiselect

Display a multiselect widget. The multiselect widget starts as empty.

```python
choices = st.multiselect("Buy", ["milk", "apples", "potatoes"])
```

### Pills

Display a pill-button selection widget.

```python
st.pills("Tags", ["Sports", "AI", "Politics"])
```

### Radio

Display a radio button widget.

```python
choice = st.radio("Pick one", ["cats", "dogs"])
```

### Segmented control

Display a segmented-button selection widget.

```python
st.segmented_control("Filter", ["Open", "Closed", "All"])
```

### Select slider

Display a slider widget to select items from a list.

```python
size = st.select_slider("Pick a size", ["S", "M", "L"])
```

### Selectbox

Display a select widget.

```python
choice = st.selectbox("Pick one", ["cats", "dogs"])
```

### Toggle

Display a toggle widget.

```python
activated = st.toggle("Activate")
```

## Numeric input elements

### Number input

Display a numeric input widget.

```python
choice = st.number_input("Pick a number", 0, 10)
```

### Slider

Display a slider widget.

```python
number = st.slider("Pick a number", 0, 100)
```

## Date and time input elements

### Date input

Display a date input widget.

```python
date = st.date_input("Your birthday")
```

### Time input

Display a time input widget.

```python
time = st.time_input("Meeting time")
```

## Text input elements

### Text input

Display a single-line text input widget.

```python
name = st.text_input("First name")
```

### Text area

Display a multi-line text input widget.

```python
text = st.text_area("Text to translate")
```

### Chat input

Display a chat input widget.

```python
prompt = st.chat_input("Say something")
if prompt:
    st.write(f"The user has sent: {prompt}")
```

## Other input elements


#### Audio input

Display a widget that allows users to record with their microphone.

```python
speech = st.audio_input("Record a voice message")
```

#### Data editor

Display a data editor widget.

```python
edited = st.data_editor(df, num_rows="dynamic")
```

#### File uploader

Display a file uploader widget.

```python
data = st.file_uploader("Upload a CSV")
```

#### Camera input

Display a widget that allows users to upload images directly from a camera.

```python
image = st.camera_input("Take a picture")
```

### Third-party components

These are featured components created by our lovely community. For more examples and inspiration, check out our [Components Gallery](https://streamlit.io/components) and [Streamlit Extras](https://extras.streamlit.app)!

#### Streamlit Chat

[Streamlit Component for a Chatbot UI. Created by](https://github.com/AI-Yash/st-chat) [@AI-Yash](https://github.com/AI-Yash).

```python
from streamlit_chat import message
message("My message")
message("Hello bot!", is_user=True) # align's the message to the right
```

#### Streamlit Option Menu

[Select a single item from a list of options in a menu. Created by](https://github.com/victoryhb/streamlit-option-menu) [@victoryhb](https://github.com/victoryhb).

```python
from streamlit_option_menu import option_menu
option_menu("Main Menu", ["Home", 'Settings'], icons=['house', 'gear'], menu_icon="cast", default_index=1)
```

#### Streamlit Extras

[A library with useful Streamlit extras. Created by](https://extras.streamlit.app/) [@arnaudmiribel](https://github.com/arnaudmiribel/).

```python
from streamlit_extras.stoggle import stoggle
stoggle(
    "Click me!",
    """🥷 Surprise! Here's some additional content""",
)
```

#### Streamlit Elements

[Create a draggable and resizable dashboard in Streamlit. Created by](https://github.com/okld/streamlit-elements) [@okls](https://github.com/okls).

```python
from streamlit_elements import elements, mui, html

with elements("new_element"):
    mui.Typography("Hello world")
```

#### Tags

[Add tags to your Streamlit apps. Created by](https://github.com/gagan3012/streamlit-tags) [@gagan3012](https://github.com/gagan3012).

```python
from streamlit_tags import st_tags

st_tags(label='# Enter Keywords:', text='Press enter to add more', value=['Zero', 'One', 'Two'], suggestions=['five', 'six', 'seven', 'eight', 'nine', 'three', 'eleven', 'ten', 'four'], maxtags = 4, key='1')
```

#### Stqdm

[The simplest way to handle a progress bar in streamlit app. Created by](https://github.com/Wirg/stqdm) [@Wirg](https://github.com/Wirg).

```python
from stqdm import stqdm
for _ in stqdm(range(50)):
    sleep(0.5)
```

#### Timeline

[Display a Timeline in Streamlit apps using](https://github.com/innerdoc/streamlit-timeline) [TimelineJS](https://timeline.knightlab.com/). Created by [@innerdoc](https://github.com/innerdoc).

```python
from streamlit_timeline import timeline
with open('example.json', "r") as f:
    timeline(f.read(), height=800)
```

#### Camera input live

[Alternative for st.camera\_input which returns the webcam images live. Created by](https://github.com/blackary/streamlit-camera-input-live) [@blackary](https://github.com/blackary).

```python
from camera_input_live import camera_input_live
image = camera_input_live()
st.image(value)
```

#### Streamlit Ace

[Ace editor component for Streamlit. Created by](https://github.com/okld/streamlit-ace) [@okld](https://github.com/okld).


### Streamlit Ace

[Ace editor component for Streamlit.](https://github.com/okld/streamlit-ace) Created by [@okld](https://github.com/okld).

```python
from streamlit_ace import st_ace
content = st_ace()
content
```

### Streamlit Chat

[Streamlit Component for a Chatbot UI.](https://github.com/AI-Yash/st-chat) Created by [@AI-Yash](https://github.com/AI-Yash).

```python
from streamlit_chat import message
message("My message")
message("Hello bot!", is_user=True) # align's the message to the right
```

### Streamlit Option Menu

[Select a single item from a list of options in a menu.](https://github.com/victoryhb/streamlit-option-menu) Created by [@victoryhb](https://github.com/victoryhb).

```python
from streamlit_option_menu import option_menu
option_menu("Main Menu", ["Home", 'Settings'], icons=['house', 'gear'], menu_icon="cast", default_index=1)
```

### Streamlit Extras

[A library with useful Streamlit extras.](https://extras.streamlit.app/) Created by [@arnaudmiribel](https://github.com/arnaudmiribel/).

```python
from streamlit_extras.stoggle import stoggle
stoggle(
    "Click me!",
    """🥷 Surprise! Here's some additional content""",
)
```

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.
