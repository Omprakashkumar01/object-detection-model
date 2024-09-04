
import torch
from IPython.display import Image
from google.colab import files

model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
uploaded = files.upload()
image_path = list(uploaded.keys())[0]
results = model(image_path)
results.print()
results.show()
results.save()
