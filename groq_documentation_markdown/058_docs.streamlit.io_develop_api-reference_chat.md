Here is the clean markdown version of the provided HTML:

# Chat Elements
Streamlit provides a few commands to help you build conversational apps. These chat elements are designed to be used in conjunction with each other, but you can also use them separately.

## Chat Message
`st.chat_message` lets you insert a chat message container into the app so you can display messages from the user or the app. Chat containers can contain other Streamlit elements, including charts, tables, text, and more.

## Chat Input
`st.chat_input` lets you display a chat input widget so the user can type in a message. Remember to check out `st.status` to display output from long-running processes and external API calls.

### Example: Chat Input
```python
prompt = st.chat_input("Say something")
if prompt:
    st.write(f"The user has sent: {prompt}")
```

### Example: Chat Message
```python
import numpy as np
with st.chat_message("user"):
    st.write("Hello ")
    st.line_chart(np.random.randn(30, 3))
```

## Status Container
`st.status` lets you display output of long-running tasks in a container.

### Example: Status Container
```python
with st.status('Running'):
    do_something_slow()
```

## Write Stream
`st.write_stream` lets you write generators or streams to the app with a typewriter effect.

### Example: Write Stream
```python
st.write_stream(my_generator)
st.write_stream(my_llm_stream)
```

Still have questions? Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

[Home](/) | [Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20) | [Community](https://discuss.streamlit.io)

Follow us on:
[GitHub](https://github.com/streamlit) | [YouTube](https://www.youtube.com/channel/UC3LD42rjj-Owtxsa6PwGU5Q) | [Twitter](https://twitter.com/streamlit) | [LinkedIn](https://www.linkedin.com/company/streamlit) | [Newsletter](https://info.snowflake.com/streamlit-newsletter-sign-up.html)

&copy; 2025 Snowflake Inc. [Cookie policy](https://www.streamlit.io/cookie-policy)