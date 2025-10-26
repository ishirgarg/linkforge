# Installing Dependencies
=====================================

## Overview
------------

This section provides guidance on installing dependencies for Streamlit. It covers various topics, including troubleshooting common errors and installing packages not available on PyPI or Conda.

## Topics
-----------

* [ModuleNotFoundError: No module named](#module-not-found-error)
* [ImportError: libGL.so.1: cannot open shared object file: No such file or directory](#libgl-error)
* [ERROR: No matching distribution found for](#no-matching-distribution-error)
* [How to install a package not on PyPI/Conda but available on GitHub](#installing-packages-from-github)

## Module Not Found Error
-------------------------

### Description

This error occurs when Python cannot find a module that is being imported.

### Solution

To resolve this error, ensure that the module is installed and imported correctly.

## LibGL Error
---------------

### Description

This error occurs when the `libGL.so.1` shared object file is missing.

### Solution

To resolve this error, install the required library and update the environment variables.

## No Matching Distribution Error
---------------------------------

### Description

This error occurs when a package is not available on PyPI or Conda.

### Solution

To resolve this error, use alternative installation methods, such as installing from source or using a different package manager.

## Installing Packages from GitHub
------------------------------------

### Description

This section provides guidance on installing packages not available on PyPI or Conda but available on GitHub.

### Solution

To install a package from GitHub, use the following command:
```bash
pip install git+https://github.com/username/repository.git
```
Replace `username` and `repository` with the actual GitHub repository details.

## Additional Resources
-------------------------

* [Streamlit Forums](https://discuss.streamlit.io): A community-driven forum for discussing Streamlit-related topics.
* [Streamlit Documentation](https://docs.streamlit.io): The official Streamlit documentation, covering various topics, including installation, development, and deployment.
* [GitHub Repository](https://github.com/streamlit/streamlit): The official Streamlit GitHub repository, containing the source code and issue tracker.

## Contact Us
--------------

For further assistance, please contact us at [hello@streamlit.io](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20).

## Social Media
----------------

* [Twitter](https://twitter.com/streamlit)
* [LinkedIn](https://www.linkedin.com/company/streamlit)
* [YouTube](https://www.youtube.com/channel/UC3LD42rjj-Owtxsa6PwGU5Q)
* [Newsletter](https://info.snowflake.com/streamlit-newsletter-sign-up.html)

## Copyright and Cookie Policy
------------------------------

&copy; 2025 Snowflake Inc. [Cookie policy](https://www.snowflake.com/cookie-policy/)