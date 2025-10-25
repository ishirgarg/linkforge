Here is the HTML content converted to clean Markdown:

# st.camera_input
## Streamlit Version
* Version 1.50.0
* Version 1.49.0
* Version 1.48.0
* Version 1.47.0
* Version 1.46.0
* Version 1.45.0
* Version 1.44.0
* Version 1.43.0
* Version 1.42.0
* Version 1.41.0
* Version 1.40.0
* Version 1.39.0
* Version 1.38.0
* Version 1.37.0
* Version 1.36.0
* Version 1.35.0
* Version 1.34.0
* Version 1.33.0
* Version 1.32.0
* Version 1.31.0
* Version 1.30.0
* Version 1.29.0
* Version 1.28.0
* Version 1.27.0
* Version 1.26.0
* Version 1.25.0
* Version 1.24.0
* Version 1.23.0
* Version 1.22.0

Display a widget that returns pictures from the user's webcam.

### Function signature
```python
st.camera_input(label, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible", width="stretch")
```

### Parameters
* `label` (str): A short label explaining to the user what this widget is used for.
* `key` (str or int): An optional string or integer to use as the unique key for the widget.
* `help` (str or None): A tooltip that gets displayed next to the widget label.
* `on_change` (callable): An optional callback invoked when this camera_input's value changes.
* `args` (list or tuple): An optional list or tuple of args to pass to the callback.
* `kwargs` (dict): An optional dict of kwargs to pass to the callback.
* `disabled` (bool): An optional boolean that disables the camera input if set to True. Default is False.
* `label_visibility` ("visible", "hidden", or "collapsed"): The visibility of the label.
* `width` ("stretch" or int): The width of the camera input widget.

### Returns
* `(None or UploadedFile)`: The UploadedFile class is a subclass of BytesIO, and therefore is "file-like".

### Examples
```python
import streamlit as st

enable = st.checkbox("Enable camera")
picture = st.camera_input("Take a picture", disabled=not enable)

if picture:
    st.image(picture)
```

To read the image file buffer as bytes, you can use `getvalue()` on the `UploadedFile` object.
```python
import streamlit as st

img_file_buffer = st.camera_input("Take a picture")
if img_file_buffer is not None:
    bytes_data = img_file_buffer.getvalue()
    st.write(type(bytes_data))
```

## Image processing examples
You can use the output of `st.camera_input` for various downstream tasks, including image processing.

### Pillow (PIL) and NumPy
```python
import streamlit as st
from PIL import Image
import numpy as np

img_file_buffer = st.camera_input("Take a picture")
if img_file_buffer is not None:
    img = Image.open(img_file_buffer)
    img_array = np.array(img)
    st.write(type(img_array))
    st.write(img_array.shape)
```

### OpenCV (cv2)
```python
import streamlit as st
import cv2
import numpy as np

img_file_buffer = st.camera_input("Take a picture")
if img_file_buffer is not None:
    bytes_data = img_file_buffer.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
    st.write(type(cv2_img))
    st.write(cv2_img.shape)
```

### TensorFlow
```python
import streamlit as st
import tensorflow as tf

img_file_buffer = st.camera_input("Take a picture")
if img_file_buffer is not None:
    bytes_data = img_file_buffer.getvalue()
    img_tensor = tf.io.decode_image(bytes_data, channels=3)
    st.write(type(img_tensor))
    st.write(img_tensor.shape)
```

### Torchvision
```python
import streamlit as st
import torch
import torchvision

img_file_buffer = st.camera_input("Take a picture")
if img_file_buffer is not None:
    bytes_data = img_file_buffer.getvalue()
    torch_img = torchvision.io.decode_image(torch.frombuffer(bytes_data, dtype=torch.uint8))
    st.write(type(torch_img))
    st.write(torch_img.shape)
```

### PyTorch
```python
import streamlit as st
import torch
import numpy as np

img_file_buffer = st.camera_input("Take a picture")
if img_file_buffer is not None:
    bytes_data = img_file_buffer.getvalue()
    torch_img = torch.ops.image.decode_image(torch.from_numpy(np.frombuffer(bytes_data, np.uint8)), 3)
    st.write(type(torch_img))
    st.write(torch_img.shape)
```