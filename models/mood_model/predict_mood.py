import os, numpy as np, tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

MODEL_PATH = r"C:\Users\janvi\OneDrive\Desktop\SEM 5\BAE\BAE--Bringing-Aesthetics-to-Emotions\models\mood_model\mobilenetv2_mood_3class.h5"
MOOD_LABELS = ['happy', 'neutral', 'sad']

model = tf.keras.models.load_model(MODEL_PATH)

def predict_mood(img_path):
    img = image.load_img(img_path, target_size=(224,224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    preds = model.predict(x)
    idx = np.argmax(preds)
    return MOOD_LABELS[idx], float(np.max(preds))

if __name__ == "__main__":
    test_img =  r"C:\Users\janvi\Downloads\trump.jpg"
    mood, conf = predict_mood(test_img)
    print(f"Predicted mood: {mood} ({conf*100:.2f}%)")  