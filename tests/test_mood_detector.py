import os
from models.mood_model.predict_mood import predict_mood

def test_prediction():
    img_path = r"D:\BE 24-27\5th sem\SE\SE LAB\Project\BAE\BAE--Bringing-Aesthetics-to-Emotions\data\mood_data\Test\neutral\ffhq_1000.png"
    mood, conf = predict_mood(img_path)
    assert mood in ['happy','neutral','sad'], "Invalid mood"
    print(f"Test Passed: {mood} ({conf*100:.2f}%)")

if __name__ == "__main__":
    test_prediction()
