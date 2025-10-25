Here is the converted markdown:

# st.dialog - Streamlit Docs
![Logo](/logo.svg)

## Documentation

### Search
Search

### Menu
* **Get started**
	+ [Installation](/get-started/installation)
	+ [Fundamentals](/get-started/fundamentals)
	+ [First steps](/get-started/tutorials)
* **Develop**
	+ [Concepts](/develop/concepts)
	+ [API reference](/develop/api-reference)
		- PAGE ELEMENTS
			- [Write and magic](/develop/api-reference/write-magic)
			- [Text elements](/develop/api-reference/text)
			- [Data elements](/develop/api-reference/data)
			- [Chart elements](/develop/api-reference/charts)
			- [Input widgets](/develop/api-reference/widgets)
			- [Media elements](/develop/api-reference/media)
			- [Layouts and containers](/develop/api-reference/layout)
			- [Chat elements](/develop/api-reference/chat)
			- [Status elements](/develop/api-reference/status)
			- [Third-party components](https://streamlit.io/components)
		- APPLICATION LOGIC
			- [Authentication and user info](/develop/api-reference/user)
			- [Navigation and pages](/develop/api-reference/navigation)
			- [Execution flow](/develop/api-reference/execution-flow)
				- [st.dialog](/develop/api-reference/execution-flow/st.dialog)
				- [st.form](/develop/api-reference/execution-flow/st.form)
				- [st.form_submit_button](/develop/api-reference/execution-flow/st.form_submit_button)
				- [st.fragment](/develop/api-reference/execution-flow/st.fragment)
				- [st.rerun](/develop/api-reference/execution-flow/st.rerun)
				- [st.stop](/develop/api-reference/execution-flow/st.stop)
			- [Caching and state](/develop/api-reference/caching-and-state)
			- [Connections and secrets](/develop/api-reference/connections)
			- [Custom components](/develop/api-reference/custom-components)
			- [Configuration](/develop/api-reference/configuration)
		- TOOLS
			- [App testing](/develop/api-reference/app-testing)
			- [Command line](/develop/api-reference/cli)
	+ [Tutorials](/develop/tutorials)
	+ [Quick reference](/develop/quick-reference)
* **Deploy**
	+ [Concepts](/deploy/concepts)
	+ [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
	+ [Snowflake](/deploy/snowflake)
	+ [Other platforms](/deploy/tutorials)
* **Knowledge base**
	+ [FAQ](/knowledge-base/using-streamlit)
	+ [Installing dependencies](/knowledge-base/dependencies)
	+ [Deployment issues](/knowledge-base/deploy)

### Links
* [Home](/)
* [Develop](/develop)
* [API reference](/develop/api-reference)
* [Execution flow](/develop/api-reference/execution-flow)
* [st.dialog](/develop/api-reference/execution-flow/st.dialog)

## st.dialog
### Function Decorator to Create a Modal Dialog

A function decorated with `@st.dialog` becomes a dialog function. When you call a dialog function, Streamlit inserts a modal dialog into your app. Streamlit element commands called within the dialog function render inside the modal dialog.

### Parameters
* `title`: The title to display at the top of the modal dialog. It cannot be empty. The title can optionally contain GitHub-flavored Markdown.
* `width`: The width of the modal dialog. This can be one of the following:
	+ "small" (default): The modal dialog will be a maximum of 500 pixels wide.
	+ "medium": The modal dialog will be up to 750 pixels wide.
	+ "large": The modal dialog will be up to 1280 pixels wide.
* `dismissible`: Whether the modal dialog can be dismissed by the user. If this is `True` (default), the user can dismiss the dialog by clicking outside of it, clicking the "**X**" in its upper-right corner, or pressing ESC on their keyboard. If this is `False`, the "**X**" in the upper-right corner is hidden and the dialog must be closed programmatically by calling `st.rerun()` inside the dialog function.
* `on_dismiss`: How the dialog should respond to dismissal events. This can be one of the following:
	+ "ignore" (default): Streamlit will not rerun the app when the user dismisses the dialog.
	+ "rerun": Streamlit will rerun the app when the user dismisses the dialog.
	+ A callable: Streamlit will rerun the app when the user dismisses the dialog and execute the callable as a callback function before the rest of the app.

### Examples
The following example demonstrates the basic usage of `@st.dialog`. In this app, clicking "**A**" or "**B**" will open a modal dialog and prompt you to enter a reason for your vote. In the modal dialog, click "**Submit**" to record your vote into Session State and rerun the app. This will close the modal dialog since the dialog function is not called during the full-script rerun.
```python
import streamlit as st

@st.dialog("Cast your vote")
def vote(item):
    st.write(f"Why is {item} your favorite?")
    reason = st.text_input("Because...")
    if st.button("Submit"):
        st.session_state.vote = {"item": item, "reason": reason}
        st.rerun()

if "vote" not in st.session_state:
    st.write("Vote for your favorite")
    if st.button("A"):
        vote("A")
    if st.button("B"):
        vote("B")
else:
    f"You voted for {st.session_state.vote['item']} because {st.session_state.vote['reason']}"
```