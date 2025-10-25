# Display Progress and Status

Streamlit provides several methods to add animations and status indicators to your applications. These include progress bars, status messages (like warnings), and celebratory effects.

**URL:** https://docs.streamlit.io/develop/api-reference/status

## Animated Status Elements

### Progress Bar

Displays a progress bar to indicate the completion of a task.

```python
for i in range(101):
    st.progress(i)
    do_something_slow()
```

### Spinner

Temporarily displays a message while a block of code is executing.

```python
with st.spinner("Please wait..."):
    do_something_slow()
```

### Status Container

Shows the output of long-running tasks within a dedicated container.

```python
with st.status('Running'):
    do_something_slow()
```

### Toast

Briefly displays a message in the bottom-right corner of the screen.

```python
st.toast('Butter!', icon='🧈')
```

### Balloons

Adds a celebratory balloon animation to the app.

```python
st.balloons()
```

### Snowflakes

Adds a celebratory snowflake animation to the app.

```python
st.snow()
```

## Simple Callout Messages

Here's the Markdown conversion of the provided HTML content, structured and formatted as requested:

![screenshot](/images/api/success.jpg)
#### Success box
Display a success message.

```python
st.success("Match found!")
```

![screenshot](/images/api/info.jpg)
#### Info box
Display an informational message.

```python
st.info("Dataset is updated every day at midnight.")
```

![screenshot](/images/api/warning.jpg)
#### Warning box
Display warning message.

```python
st.warning("Unable to fetch image. Skipping...")
```

![screenshot](/images/api/error.jpg)
#### Error box
Display error message.

```python
st.error("We encountered an error")
```

![screenshot](/images/api/exception.jpg)
#### Exception output
Display an exception.

```python
e = RuntimeError("This is an exception of type RuntimeError")
st.exception(e)
```

## Third-party components

These are featured components created by our lovely community. For more examples and inspiration, check out our [Components Gallery](https://streamlit.io/components) and [Streamlit Extras](https://extras.streamlit.app)!

![screenshot](/images/api/components/stqdm.jpg)
#### [Stqdm](https://github.com/Wirg/stqdm)
The simplest way to handle a progress bar in Streamlit app. Created by [@Wirg](https://github.com/Wirg).

```python
from stqdm import stqdm
from time import sleep

for _ in stqdm(range(50)):
    sleep(0.5)
```

![screenshot](/images/api/components/custom-notification-box.jpg)
#### [Custom notification box](https://github.com/Socvest/streamlit-custom-notification-box)
A custom notification box with the ability to close it out. Created by [@Socvest](https://github.com/Socvest).

```python
from streamlit_custom_notification_box import custom_notification_box

styles = {'material-icons':{'color': 'red'},
          'text-icon-link-close-container': {'box-shadow': '#3896de 0px 4px'},
          'notification-text': {'':''},
          'close-button':{'':''},
          'link':{'':''}}

custom_notification_box(icon='info', textDisplay='We are almost done with your registration...',
                        externalLink='more info', url='#', styles=styles, key="foo")
```

![screenshot](/images/api/components/extras-emojis.jpg)
#### [Streamlit Extras](https://extras.streamlit.app/)
A library with useful Streamlit extras. Created by [@arnaudmiribel](https://github.com/arnaudmiribel/).

```python
from streamlit_extras.let_it_rain import rain

rain(
    emoji="🎈",
    font_size=54,
    falling_speed=5,
    animation_length="infinite",
)
```

### Still have questions?
Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.