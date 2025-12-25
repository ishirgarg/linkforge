# Installing Dependencies
====================================

## Introduction
---------------

This documentation provides guidelines on installing dependencies for Streamlit. It covers various topics, including troubleshooting common errors and installing packages not available on PyPI or Conda.

## Topics
---------

* [ModuleNotFoundError: No module named](#module-not-found-error)
* [ImportError: libGL.so.1: cannot open shared object file: No such file or directory](#import-error-libgl)
* [ERROR: No matching distribution found for](#no-matching-distribution)
* [How to install a package not on PyPI/Conda but available on GitHub](#install-package-not-pypi-conda)

## Module Not Found Error
-------------------------

### Description

This error occurs when Python cannot find a module that is being imported.

### Solution

To resolve this error, ensure that the module is installed correctly. You can try reinstalling the module using pip or Conda.

```bash
pip install module_name
```

or

```bash
conda install module_name
```

## Import Error: libGL.so.1
---------------------------

### Description

This error occurs when the `libGL.so.1` shared object file is not found.

### Solution

To resolve this error, you need to install the `libgl1` package. On Ubuntu-based systems, you can use the following command:

```bash
sudo apt-get install libgl1
```

## No Matching Distribution
---------------------------

### Description

This error occurs when pip cannot find a matching distribution for a package.

### Solution

To resolve this error, check if the package is available on PyPI or Conda. If not, you may need to install it from a different source, such as GitHub.

## Install Package Not on PyPI/Conda
-----------------------------------

### Description

This section provides guidelines on installing packages not available on PyPI or Conda but available on GitHub.

### Solution

To install a package from GitHub, you can use the following command:

```bash
pip install git+https://github.com/username/package_name.git
```

Replace `username` and `package_name` with the actual values.

## Still Have Questions?
-------------------------

If you have any further questions or need help with installing dependencies, you can visit our [forums](https://discuss.streamlit.io) for assistance.

## Contact Us
--------------

You can contact us at [hello@streamlit.io](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20) for any questions or feedback.

## Community
------------

Join our community on [GitHub](https://github.com/streamlit), [YouTube](https://www.youtube.com/channel/UC3LD42rjj-Owtxsa6PwGU5Q), [Twitter](https://twitter.com/streamlit), [LinkedIn](https://www.linkedin.com/company/streamlit), or sign up for our [newsletter](https://info.snowflake.com/streamlit-newsletter-sign-up.html).

&copy; 2025 Snowflake Inc. [Cookie policy](https://www.streamlit.io/cookie-policy)