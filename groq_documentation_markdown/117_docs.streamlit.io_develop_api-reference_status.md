Here is the HTML converted to clean Markdown:

# Display progress and status - Streamlit Docs

## Documentation

### Get started
* [Installation](/get-started/installation)
* [Fundamentals](/get-started/fundamentals)
* [First steps](/get-started/tutorials)

### Develop
* [Concepts](/develop/concepts)
* [API reference](/develop/api-reference)
	+ PAGE ELEMENTS
		- [Write and magic](/develop/api-reference/write-magic)
		- [Text elements](/develop/api-reference/text)
		- [Data elements](/develop/api-reference/data)
		- [Chart elements](/develop/api-reference/charts)
		- [Input widgets](/develop/api-reference/widgets)
		- [Media elements](/develop/api-reference/media)
		- [Layouts and containers](/develop/api-reference/layout)
		- [Chat elements](/develop/api-reference/chat)
		- [Status elements](/develop/api-reference/status)
			- CALLOUTS
			- [st.success](/develop/api-reference/status/st.success)
			- [st.info](/develop/api-reference/status/st.info)
			- [st.warning](/develop/api-reference/status/st.warning)
			- [st.error](/develop/api-reference/status/st.error)
			- [st.exception](/develop/api-reference/status/st.exception)
			- OTHER
			- [st.progress](/develop/api-reference/status/st.progress)
			- [st.spinner](/develop/api-reference/status/st.spinner)
			- [st.status](/develop/api-reference/status/st.status)
			- [st.toast](/develop/api-reference/status/st.toast)
			- [st.balloons](/develop/api-reference/status/st.balloons)
			- [st.snow](/develop/api-reference/status/st.snow)
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
* [Tutorials](/develop/tutorials)
* [Quick reference](/develop/quick-reference)

### Deploy
* [Concepts](/deploy/concepts)
* [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
* [Snowflake](/deploy/snowflake)
* [Other platforms](/deploy/tutorials)

### Knowledge base
* [FAQ](/knowledge-base/using-streamlit)
* [Installing dependencies](/knowledge-base/dependencies)
* [Deployment issues](/knowledge-base/deploy)

### Links
* [Home](/)
* [Develop](/develop)
* [API reference](/develop/api-reference)
* [Status elements](/develop/api-reference/status)

# Display progress and status
Streamlit provides a few methods that allow you to add animation to your apps. These animations include progress bars, status messages (like warnings), and celebratory balloons.

## Animated status elements
### Progress bar
Display a progress bar.
```python
for i in range(101):
    st.progress(i)
    do_something_slow()
```
### Spinner
Temporarily displays a message while executing a block of code.
```python
with st.spinner("Please wait..."):
    do_something_slow()
```
### Status container
Display output of long-running tasks in a container.
```python
with st.status('Running'):
    do_something_slow()
```
### Toast
Briefly displays a toast message in the bottom-right corner.
```python
st.toast('Butter!', icon='🧈')
```
### Balloons
Display celebratory balloons!
```python
st.balloons()
```
### Snowflakes
Display celebratory snowflakes!
```python
st.snow()
```

## Simple callout messages
### Success box
Display a success message.
```python
st.success("Match found!")
```
### Info box
Display an informational message.
```python
st.info("Dataset is updated every day at midnight.")
```
### Warning box
Display warning message.
```python
st.warning("Unable to fetch image. Skipping...")
```
### Error box
Display error message.
```python
st.error("We encountered an error")
```
### Exception output
Display an exception.
```python
e = RuntimeError("This is an exception of type RuntimeError")
st.exception(e)
```

## Third-party components
These are featured components created by our lovely community. For more examples and inspiration, check out our [Components Gallery](https://streamlit.io/components) and [Streamlit Extras](https://extras.streamlit.app).

### Stqdm
The simplest way to handle a progress bar in streamlit app. Created by [@Wirg](https://github.com/Wirg).
```python
from stqdm import stqdm
for _ in stqdm(range(50)):
    sleep(0.5)
```
### Custom notification box
A custom notification box with the ability to close it out. Created by [@Socvest](https://github.com/Socvest).
```python
from streamlit_custom_notification_box import custom_notification_box
styles = {'material-icons':{'color': 'red'}, 'text-icon-link-close-container': {'box-shadow': '#3896de 0px 4px'}, 'notification-text': {'':''}, 'close-button':{'':''}, 'link':{'':''}}
custom_notification_box(icon='info', textDisplay='We are almost done with your registration...', externalLink='more info', url='#', styles=styles, key="foo")
```
### Streamlit Extras
A library with useful Streamlit extras. Created by [@arnaudmiribel](https://github.com/arnaudmiribel/).
```python
from streamlit_extras.let_it_rain import rain
rain(emoji="🎈", font_size=54, falling_speed=5, animation_length="infinite",)
```
Still have questions? Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.