# st.echo

**URL:** https://docs.streamlit.io/develop/api-reference/text/st.echo

Use in a `with` block to draw some code on the app, then execute it.

## Function signature

[`source`](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/commands/echo.py#L33 "View st.echo source code on GitHub")

```python
st.echo(code_location="above")
```

## Parameters

*   **code_location** (`"above"` or `"below"`)
    Whether to show the echoed code before or after the results of the executed code block.

## Example

```python
import streamlit as st

with st.echo():
    st.write('This code will be printed')
```

### Display code

Sometimes you want your Streamlit app to contain _both_ your usual Streamlit graphic elements _and_ the code that generated those elements. That's where `st.echo()` comes in.

Ok so let's say you have the following file, and you want to make its app a little bit more self-explanatory by making that middle section visible in the Streamlit app:

```python
import streamlit as st

def get_user_name():
    return 'John'

# ------------------------------------------------
# Want people to see this part of the code...
def get_punctuation():
    return '!!!'

greeting = "Hi there, "
user_name = get_user_name()
punctuation = get_punctuation()
st.write(greeting, user_name, punctuation)
# ...up to here
# ------------------------------------------------

foo = 'bar'
st.write('Done!')
```

The file above creates a Streamlit app containing the words "Hi there, `John`", and then "Done!".

Now let's use `st.echo()` to make that middle section of the code visible in the app:

```python
import streamlit as st

def get_user_name():
    return 'John'

with st.echo():
    # Everything inside this block will be both printed to the screen
    # and executed.
    def get_punctuation():
        return '!!!'

    greeting = "Hi there, "
    value = get_user_name()
    punctuation = get_punctuation()
    st.write(greeting, value, punctuation)

# And now we're back to _not_ printing to the screen
foo = 'bar'
st.write('Done!')
```

It's _that_ simple!

> **Note**
> You can have multiple `st.echo()` blocks in the same file. Use it as often as you wish!

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.
