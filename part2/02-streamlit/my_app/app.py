import io
import yaml
from PIL import Image
import streamlit as st
from predict import load_model, get_prediction
from confirm_button_hack import cache_on_button_press

# SETTING PAGE CONFIG TO WIDE MODE
st.set_page_config(layout="wide")

st.write("Hello World!")

# TODO: Streamlit App 만들기
# TODO: Voila 코드 리펙토링(app.py, model.py, predict.py, utils.py)
# TODO: File Uploader 구현
# TODO: 이미지 View
# TODO: 예측 결과 출력
# TODO: 암호 입력

def main(): 
    st.title("Mask Classification Model")

    # Load yaml
    with open("config.yaml") as f:
        config = yaml.load(f, Loader=yaml.FullLoader)

    # Load model
    model = load_model()

    # File Uploader
    uploaded_file = st.file_uploader("Choose an Image file", type=["png", "jpg", "jpeg"])
    uploaded_file
    if uploaded_file: # Not None
        image_bytes = uploaded_file.getvalue()
        value = io.BytesIO(image_bytes) # Bytes -> IO
        image = Image.open(value)
        st.image(image, caption="Uploaded Image") 

        # 예측 결과 출력
        st.write("Classifying...")
        _, y_hat = get_prediction(model, image_bytes)
        label = config['classes'][y_hat.item()]

        # st.write(f"Prediction Response is {label}")
        col1, col2, col3 = st.columns(3)
        col1.metric("Mask", label[0])
        col2.metric("Gender", label[1])
        col3.metric("Age", label[2])

# 암호 입력
root_password = 'password'
password = st.text_input('password', type='password')


@cache_on_button_press('Authenticate')
def authenticate(password) -> bool:
    st.write(type(password))
    return password == root_password

if authenticate(password):
    st.success("인증 완료")
    main()
else:
    st.error("비밀번호 오류")
