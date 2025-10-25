Here is the converted markdown:
### Input widgets - Streamlit Docs
#### Documentation

[Search](/)

### Menu
* [Get started](/get-started)
	+ [Installation](/get-started/installation)
	+ [Fundamentals](/get-started/fundamentals)
	+ [First steps](/get-started/tutorials)
* [Develop](/develop)
	+ [Concepts](/develop/concepts)
	+ [API reference](/develop/api-reference)
		- [Write and magic](/develop/api-reference/write-magic)
		- [Text elements](/develop/api-reference/text)
		- [Data elements](/develop/api-reference/data)
		- [Chart elements](/develop/api-reference/charts)
		- [Input widgets](/develop/api-reference/widgets)
			- BUTTONS
				- [st.button](/develop/api-reference/widgets/st.button)
				- [st.download_button](/develop/api-reference/widgets/st.download_button)
				- [st.form_submit_button](/develop/api-reference/execution-flow/st.form_submit_button)
				- [st.link_button](/develop/api-reference/widgets/st.link_button)
				- [st.page_link](/develop/api-reference/widgets/st.page_link)
			- SELECTIONS
				- [st.checkbox](/develop/api-reference/widgets/st.checkbox)
				- [st.color_picker](/develop/api-reference/widgets/st.color_picker)
				- [st.feedback](/develop/api-reference/widgets/st.feedback)
				- [st.multiselect](/develop/api-reference/widgets/st.multiselect)
				- [st.pills](/develop/api-reference/widgets/st.pills)
				- [st.radio](/develop/api-reference/widgets/st.radio)
				- [st.segmented_control](/develop/api-reference/widgets/st.segmented_control)
				- [st.selectbox](/develop/api-reference/widgets/st.selectbox)
				- [st.select_slider](/develop/api-reference/widgets/st.select_slider)
				- [st.toggle](/develop/api-reference/widgets/st.toggle)
			- NUMERIC
				- [st.number_input](/develop/api-reference/widgets/st.number_input)
				- [st.slider](/develop/api-reference/widgets/st.slider)
			- DATE AND TIME
				- [st.date_input](/develop/api-reference/widgets/st.date_input)
				- [st.time_input](/develop/api-reference/widgets/st.time_input)
			- TEXT
				- [st.chat_input](/develop/api-reference/chat/st.chat_input)
				- [st.text_area](/develop/api-reference/widgets/st.text_area)
				- [st.text_input](/develop/api-reference/widgets/st.text_input)
			- MEDIA AND FILES
				- [st.audio_input](/develop/api-reference/widgets/st.audio_input)
				- [st.camera_input](/develop/api-reference/widgets/st.camera_input)
				- [st.data_editor](/develop/api-reference/data/st.data_editor)
				- [st.file_uploader](/develop/api-reference/widgets/st.file_uploader)
		- [Media elements](/develop/api-reference/media)
		- [Layouts and containers](/develop/api-reference/layout)
		- [Chat elements](/develop/api-reference/chat)
		- [Status elements](/develop/api-reference/status)
		- [Third-party components](https://streamlit.io/components)
		- APPLICATION LOGIC
			- [Authentication and user info](/develop/api-reference/user)
			- [Navigation and pages](/develop/api-reference/navigation)
			- [Execution flow](/develop/api-reference/execution-flow)
			- [Caching and state](/develop/api-reference/caching-and-state)
			- [Connections and secrets](/develop/api-reference/connections)
			- [Custom components](/develop/api-reference/custom-components)
			- [Configuration](/develop/api-reference/configuration)
		- TOOLS
			- [App testing](/develop/api-reference/app-testing)
			- [Command line](/develop/api-reference/cli)
	+ [Tutorials](/develop/tutorials)
	+ [Quick reference](/develop/quick-reference)
* [Deploy](/deploy)
	+ [Concepts](/deploy/concepts)
	+ [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
	+ [Snowflake](/deploy/snowflake)
	+ [Other platforms](/deploy/tutorials)
* [Knowledge base](/knowledge-base)
	+ [FAQ](/knowledge-base/using-streamlit)
	+ [Installing dependencies](/knowledge-base/dependencies)
	+ [Deployment issues](/knowledge-base/deploy)

### Links
* [Home](/)
* [Develop](/develop)
* [API reference](/develop/api-reference)
* [Input widgets](/develop/api-reference/widgets)

# Input widgets

With widgets, Streamlit allows you to bake interactivity directly into your apps with buttons, sliders, text inputs, and more.

## Button elements

### Button

* Display a button widget.
* Example: `clicked = st.button("Click me")`

### Download button

* Display a download button widget.
* Example: `st.download_button("Download file", file)`

### Form button

* Display a form submit button. For use with `st.form`.
* Example: `st.form_submit_button("Sign up")`

### Link button

* Display a link button.
* Example: `st.link_button("Go to gallery", url)`

### Page link

* Display a link to another page in a multipage app.
* Example: 
```python
st.page_link("app.py", label="Home", icon="🏠")
st.page_link("pages/profile.py", label="My profile")
```

## Selection elements

### Checkbox

* Display a checkbox widget.
* Example: `selected = st.checkbox("I agree")`

### Color picker

* Display a color picker widget.
* Example: `color = st.color_picker("Pick a color")`

### Feedback

* Display a rating or sentiment button group.
* Example: `st.feedback("stars")`

### Multiselect

* Display a multiselect widget. The multiselect widget starts as empty.
* Example: `choices = st.multiselect("Buy", ["milk", "apples", "potatoes"])`

### Pills

* Display a pill-button selection widget.
* Example: `st.pills("Tags", ["Sports", "AI", "Politics"])`

### Radio

* Display a radio button widget.
* Example: `choice = st.radio("Pick one", ["cats", "dogs"])`

### Segmented control

* Display a segmented-button selection widget.
* Example: `st.segmented_control("Filter", ["Open", "Closed", "All"])`

### Select slider

* Display a slider widget to select items from a list.
* Example: `size = st.select_slider("Pick a size", ["S", "M", "L"])`

### Selectbox

* Display a select widget.
* Example: `choice = st.selectbox("Pick one", ["cats", "dogs"])`

### Toggle

* Display a toggle widget.
* Example: `activated = st.toggle("Activate")`

## Numeric input elements

### Number input

* Display a numeric input widget.
* Example: `choice = st.number_input("Pick a number", 0, 10)`

### Slider

* Display a slider widget.
* Example: `number = st.slider("Pick a number", 0, 100)`

## Date and time input elements

### Date input

* Display a date input widget.
* Example: `date = st.date_input("Your birthday")`

### Time input

* Display a time input widget.
* Example: `time = st.time_input("Meeting time")`

## Text input elements

### Text input

* Display a single-line text input widget.
* Example: `name = st.text_input("First name")`

### Text area

* Display a multi-line text input widget.
* Example: `text = st.text_area("Text to translate")`

### Chat input

* Display a chat input widget.
* Example: 
```python
prompt = st.chat_input("Say something")
if prompt:
    st.write(f"The user has sent: {prompt}")
```

## Other input elements

### Audio input

* Display a widget that allows users to record with their microphone.
* Example: `speech = st.audio_input("Record a voice message")`

### Data editor

* Display a data editor widget.
* Example: `edited = st.data_editor(df, num_rows="dynamic")`

### File uploader

* Display a file uploader widget.
* Example: `data = st.file_uploader("Upload a CSV")`

### Camera input

* Display a widget that allows users to upload images directly from a camera.
* Example: `image = st.camera_input("Take a picture")`

Third-party components
-----------------------

These are featured components created by our lovely community. For more examples and inspiration, check out our [Components Gallery](https://streamlit.io/components) and [Streamlit Extras](https://extras.streamlit.app)!

### Streamlit Chat

* Streamlit Component for a Chatbot UI.
* Created by [@AI-Yash](https://github.com/AI-Yash).
* Example: 
```python
from streamlit_chat import message
message("My message")
message("Hello bot!", is_user=True)  # align's the message to the right
```

### Streamlit Option Menu

* Select a single item from a list of options in a menu.
* Created by [@victoryhb](https://github.com/victoryhb).
* Example: 
```python
from streamlit_option_menu import option_menu
option_menu("Main Menu", ["Home", 'Settings'], icons=['house', 'gear'], menu_icon="cast", default_index=1)
```

### Streamlit Extras

* A library with useful Streamlit extras.
* Created by [@arnaudmiribel](https://github.com/arnaudmiribel/).
* Example: 
```python
from streamlit_extras.stoggle import stoggle
stoggle("Click me!", """🥷 Surprise! Here's some additional content""")
```

### Streamlit Elements

* Create a draggable and resizable dashboard in Streamlit.
* Created by [@okld](https://github.com/okld).
* Example: 
```python
from streamlit_elements import elements, mui, html
with elements("new_element"):
    mui.Typography("Hello world")
```

### Tags

* Add tags to your Streamlit apps.
* Created by [@gagan3012](https://github.com/gagan3012).
* Example: 
```python
from streamlit_tags import st_tags
st_tags(label='# Enter Keywords:', text='Press enter to add more', value=['Zero', 'One', 'Two'], suggestions=['five', 'six', 'seven', 'eight', 'nine', 'three', 'eleven', 'ten', 'four'], maxtags = 4, key='1')
```

### Stqdm

* The simplest way to handle a progress bar in streamlit app.
* Created by [@Wirg](https://github.com/Wirg).
* Example: 
```python
from stqdm import stqdm
for _ in stqdm(range(50)):
    sleep(0.5)
```

### Timeline

* Display a Timeline in Streamlit apps using [TimelineJS](https://timeline.knightlab.com/).
* Created by [@innerdoc](https://github.com/innerdoc).
* Example: 
```python
from streamlit_timeline import timeline
with open('example.json', "r") as f:
    timeline(f.read(), height=800)
```

### Camera input live

* Alternative for st.camera_input which returns the webcam images live.
* Created by [@blackary](https://github.com/blackary).
* Example: 
```python
from camera_input_live import camera_input_live
image = camera_input_live()
st.image(value)
```

### Streamlit Ace

* Ace editor component for Streamlit.
* Created by [@okld](https://github.com/okld).
* Example: 
```python
from streamlit_ace import st_ace
content = st_ace()
content
```