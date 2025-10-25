Here is the HTML content converted to clean Markdown:

# secrets.toml - Streamlit Docs
## Introduction
`secrets.toml` is an optional file you can define for your working directory or global development environment. When `secrets.toml` is defined both globally and in your working directory, Streamlit combines the secrets and gives precedence to the working-directory secrets. For more information, see [Secrets management](/develop/concepts/connections/secrets-management).

### File Location
To define your secrets locally or per-project, add `.streamlit/secrets.toml` to your working directory. Your working directory is wherever you call `streamlit run`. If you haven't previously created the `.streamlit` directory, you will need to add it.

To define your configuration globally, you must first locate your global `.streamlit` directory. Streamlit adds this hidden directory to your OS user profile during installation. For MacOS/Linux, this will be `~/.streamlit/secrets.toml`. For Windows, this will be `%userprofile%/.streamlit/secrets.toml`.

Optionally, you can change where Streamlit searches for secrets through the configuration option, [`secrets.files`](/develop/api-reference/configuration/config.toml#secrets).

### File Format
`secrets.toml` is a [TOML](https://toml.io/en/) file.

#### Example
```toml
OpenAI_key = "your OpenAI key"
whitelist = ["sally", "bob", "joe"]
[database]
user = "your username"
password = "your password"
```
In your Streamlit app, the following values would be true:
* `st.secrets["OpenAI_key"] == "your OpenAI key"`
* `"sally" in st.secrets.whitelist`
* `st.secrets["database"]["user"] == "your username"`
* `st.secrets.database.password == "your password"`

## Navigation
* [Previous: st.secrets](/develop/api-reference/connections/st.secrets)
* [Next: st.connection](/develop/api-reference/connections/st.connection)

## Still have questions?
Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

## Footer
* [Home](/)
* [Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)
* [Community](https://discuss.streamlit.io)
* [GitHub](https://github.com/streamlit)
* [YouTube](https://www.youtube.com/channel/UC3LD42rjj-Owtxsa6PwGU5Q)
* [Twitter](https://twitter.com/streamlit)
* [LinkedIn](https://www.linkedin.com/company/streamlit)
* [Newsletter](https://info.snowflake.com/streamlit-newsletter-sign-up.html)
* [Cookie policy](#)
* Copyright 2025 Snowflake Inc.