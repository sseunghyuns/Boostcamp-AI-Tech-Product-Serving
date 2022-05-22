import yaml
import torch
import streamlit as st
from typing import Tuple
from model import MyEfficientNet
from utils import transform_image

# Load model같은 경우, Streamlit이 실행될 때마다 실행되어 리소스를 계속 사용하게 된다. 
# cache를 사용하자.
@st.cache
def load_model() -> MyEfficientNet:
    with open("config.yaml") as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    model = MyEfficientNet(num_classes=18).to(device)
    model.load_state_dict(torch.load(config['model_path'], map_location=device))
    model.eval()
    return model

def get_prediction(model:MyEfficientNet, image_bytes: bytes) -> Tuple[torch.Tensor, torch.Tensor]:
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    tensor = transform_image(image_bytes=image_bytes).to(device)
    outputs = model.forward(tensor)
    _, y_hat = outputs.max(1)
    return tensor, y_hat
