# Streamlit Documentation
## Table of Contents
1. [Get Started](#get-started)
2. [Develop](#develop)
3. [Deploy](#deploy)
4. [Knowledge Base](#knowledge-base)

## Get Started
* [Installation](/get-started/installation)
* [Fundamentals](/get-started/fundamentals)
* [First Steps](/get-started/tutorials)

## Develop
### Concepts
* [API Reference](/develop/api-reference)
    + [Write and Magic](/develop/api-reference/write-magic)
    + [Text Elements](/develop/api-reference/text)
        - [HEADINGS AND BODY](#headings-and-body)
            - [st.title](/develop/api-reference/text/st.title)
            - [st.header](/develop/api-reference/text/st.header)
            - [st.subheader](/develop/api-reference/text/st.subheader)
            - [st.markdown](/develop/api-reference/text/st.markdown)
        - [FORMATTED TEXT](#formatted-text)
            - [st.badge](/develop/api-reference/text/st.badge)
            - [st.caption](/develop/api-reference/text/st.caption)
            - [st.code](/develop/api-reference/text/st.code)
            - [st.divider](/develop/api-reference/text/st.divider)
            - [st.echo](/develop/api-reference/text/st.echo)
            - [st.latex](/develop/api-reference/text/st.latex)
            - [st.text](/develop/api-reference/text/st.text)
        - [UTILITIES](#utilities)
            - [st.help](/develop/api-reference/text/st.help)
            - [st.html](/develop/api-reference/text/st.html)
    + [Data Elements](/develop/api-reference/data)
    + [Chart Elements](/develop/api-reference/charts)
    + [Input Widgets](/develop/api-reference/widgets)
    + [Media Elements](/develop/api-reference/media)
    + [Layouts and Containers](/develop/api-reference/layout)
    + [Chat Elements](/develop/api-reference/chat)
    + [Status Elements](/develop/api-reference/status)
    + [Third-party Components](https://streamlit.io/components)
    + [APPLICATION LOGIC](#application-logic)
        - [Authentication and User Info](/develop/api-reference/user)
        - [Navigation and Pages](/develop/api-reference/navigation)
        - [Execution Flow](/develop/api-reference/execution-flow)
        - [Caching and State](/develop/api-reference/caching-and-state)
        - [Connections and Secrets](/develop/api-reference/connections)
        - [Custom Components](/develop/api-reference/custom-components)
        - [Configuration](/develop/api-reference/configuration)
    + [TOOLS](#tools)
        - [App Testing](/develop/api-reference/app-testing)
        - [Command Line](/develop/api-reference/cli)
* [Tutorials](/develop/tutorials)
* [Quick Reference](/develop/quick-reference)

### st.header
```python
st.header("Header Text")
```

## Deploy
* [Concepts](/deploy/concepts)
* [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
* [Snowflake](/deploy/snowflake)
* [Other Platforms](/deploy/tutorials)

## Knowledge Base
* [FAQ](/knowledge-base/using-streamlit)
* [Installing Dependencies](/knowledge-base/dependencies)
* [Deployment Issues](/knowledge-base/deploy)

### API Reference
The Streamlit API reference is available [here](/develop/api-reference).

### Text Elements
The Streamlit text elements are available [here](/develop/api-reference/text).

### Code Blocks
Code blocks are denoted using triple backticks:
```python
# example code block
print("Hello World!")
```

## st.header
### Display text in header formatting

The `st.header` function is used to display text in header formatting.

#### Function Signature
```python
st.header(body, anchor=None, *, help=None, divider=False, width="stretch")
```

### Parameters

* **body** (str): The text to display as GitHub-flavored Markdown. Syntax information can be found at: [https://github.github.com/gfm](https://github.github.com/gfm). See the body parameter of [st.markdown](https://docs.streamlit.io/develop/api-reference/text/st.markdown) for additional, supported Markdown directives.
* **anchor** (str or False): The anchor name of the header that can be accessed with #anchor in the URL. If omitted, it generates an anchor using the body. If False, the anchor is not shown in the UI.
* **help** (str or None): A tooltip that gets displayed next to the header. If this is None (default), no tooltip is displayed. The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of st.markdown.
* **divider** (bool, "blue", "green", "orange", "red", "violet", "yellow", "gray"/"grey", or "rainbow"): Shows a colored divider below the header. If this is True, successive headers will cycle through divider colors, except gray and rainbow. That is, the first header will have a blue line, the second header will have a green line, and so on. If this is a string, the color can be set to one of the following: blue, green, orange, red, violet, yellow, gray/grey, or rainbow.
* **width** ("stretch", "content", or int): The width of the header element. This can be one of the following:
	+ "stretch" (default): The width of the element matches the width of the parent container.
	+ "content": The width of the element matches the width of its content, but doesn't exceed the width of the parent container.
	+ An integer specifying the width in pixels: The element has a fixed width. If the specified width is greater than the width of the parent container, the width of the element matches the width of the parent container.

#### Examples
```python
import streamlit as st

st.header("_Streamlit_ is :blue[cool] :sunglasses:")
st.header("This is a header with a divider", divider="gray")
st.header("These headers have rotating dividers", divider=True)
st.header("One", divider=True)
st.header("Two", divider=True)
st.header("Three", divider=True)
st.header("Four", divider=True)
```

### Need Help?
Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.