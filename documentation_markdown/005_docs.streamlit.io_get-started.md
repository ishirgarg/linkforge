# Get started with Streamlit
This Get Started guide explains how Streamlit works, how to install Streamlit on your preferred operating system, and how to create your first Streamlit app.

## Table of Contents
1. [Installation](#installation)
2. [Fundamentals](#fundamentals)
3. [First steps](#first-steps)
4. [30 Days of Streamlit](#30-days-of-streamlit)

## Installation
[Installation](/get-started/installation) helps you set up your development environment. Walk through installing Streamlit on Windows, macOS, or Linux. Alternatively, code right in your browser with GitHub Codespaces or Streamlit in Snowflake.

```bash
# Example installation command
pip install streamlit
```

## Fundamentals
[Fundamentals](/get-started/fundamentals) introduces you to Streamlit's data model and development flow. You'll learn what makes Streamlit the most powerful way to build data apps, including the ability to display and style data, draw charts and maps, add interactive widgets, customize app layouts, cache computation, and define themes.

```python
# Example code
import streamlit as st
st.write("Hello, World!")
```

## First steps
[First steps](/get-started/tutorials) walks you through creating apps using core features to fetch and cache data, draw charts, plot information on a map, and use interactive widgets to filter results.

```python
# Example code
import pandas as pd
import streamlit as st

# Create a sample dataframe
data = {'Name': ['John', 'Mary', 'David'], 
        'Age': [25, 31, 42]}
df = pd.DataFrame(data)

# Display the dataframe
st.write(df)
```

## 30 Days of Streamlit 
30 Days of Streamlit is a free, self-paced 30 day challenge that teaches you how to build and deploy data apps with Streamlit. Complete the daily challenges, share your solutions with us on Twitter and LinkedIn, and stop by the forum with any questions!

[Start the challenge](https://30days.streamlit.app/)

### Still have questions?
Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

### Useful Links
* [Home](/)
* [Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)
* [Community](https://discuss.streamlit.io)
* [GitHub](https://github.com/streamlit)
* [YouTube](https://www.youtube.com/channel/UC3LD42rjj-Owtxsa6PwGU5Q)
* [Twitter](https://twitter.com/streamlit)
* [LinkedIn](https://www.linkedin.com/company/streamlit)
* [Newsletter](https://info.snowflake.com/streamlit-newsletter-sign-up.html)