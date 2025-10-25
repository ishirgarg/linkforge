# Magic
Magic commands are a feature in Streamlit that allows you to write almost anything (markdown, data, charts) without having to type an explicit command at all. Just put the thing you want to show on its own line of code, and it will appear in your app. Here's an example:
```python
# Draw a title and some text to the app: 
'''
# This is the document title
This is some _markdown_.
'''
import pandas as pd
df = pd.DataFrame({'col1': [1,2,3]})
df  # Draw the dataframe
x = 10
'x', x  # Draw the string 'x' and then the value of x
# Also works with most supported chart types
import matplotlib.pyplot as plt
import numpy as np
arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)
fig  # Draw a Matplotlib chart
```

## How Magic works
Any time Streamlit sees either a variable or literal value on its own line, it automatically writes that to your app using [`st.write`](#) (which you'll learn about later).

Also, magic is smart enough to ignore docstrings. That is, it ignores the strings at the top of files and functions.

If you prefer to call Streamlit commands more explicitly, you can always turn magic off in your `~/.streamlit/config.toml` with the following setting:
```toml
[runner]
magicEnabled = false
```
### Important
Right now, Magic only works in the main Python app file, not in imported files. See GitHub issue #288 for a discussion of the issues.

## Featured video
Learn what the [`st.write`](#) and [magic](#) commands are and how to use them.

[Previous: st.write_stream](#)
[Next: Text elements](#)

### Still have questions?
Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

[Home](/)
[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)
[Community](https://discuss.streamlit.io)

[GitHub](https://github.com/streamlit)
[YouTube](https://www.youtube.com/channel/UC3LD42rjj-Owtxsa6PwGU5Q)
[Twitter](https://twitter.com/streamlit)
[LinkedIn](https://www.linkedin.com/company/streamlit)
[Newsletter](https://info.snowflake.com/streamlit-newsletter-sign-up.html)

 2025 Snowflake Inc.
[Cookie policy](#)