pip install readimg

```
from readimg.read import load_image_files
image_dataset = load_image_files("./demo_images/", output_shape=(64, 64, 3))
print(image_dataset)
```