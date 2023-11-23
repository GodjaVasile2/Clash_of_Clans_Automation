from ultralytics import YOLO
import torch

# Check for CUDA device and set it
device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(f'Using device: {device}')


# TO DO anayze how its working with other model

model = YOLO("yolov8x.yaml").to(device)

# Train the model
trained_model = model.train(data="defences/data.yaml", epochs=100)


# terminal command for predincting images
# yolo task=detect mode=predict model=runs/detect/train/weights/best.pt conf=0.25 source = "resources/test/images"
