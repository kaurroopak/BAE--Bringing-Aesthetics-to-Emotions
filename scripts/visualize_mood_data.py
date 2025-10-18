# visualize_mood_data.py
import pandas as pd
import matplotlib.pyplot as plt
import cv2, os, random

LABEL_PATH = r"BAE--Bringing-Aesthetics-to-Emotions\data\mood_data\filtered_labels_auto.csv"
IMG_DIR = r"BAE--Bringing-Aesthetics-to-Emotions\data\mood_data"

df = pd.read_csv(LABEL_PATH)
classes = df['label'].unique()

plt.figure(figsize=(10,3))
for i, cls in enumerate(classes):
    sample = df[df['label']==cls].sample(1).iloc[0] 
    img_path = os.path.join(IMG_DIR, sample['full_path']) 
    img = cv2.cvtColor(cv2.imread(img_path), cv2.COLOR_BGR2RGB)
    plt.subplot(1,3,i+1)
    plt.imshow(img)
    plt.title(cls)
    plt.axis('off')
plt.tight_layout()
plt.show()