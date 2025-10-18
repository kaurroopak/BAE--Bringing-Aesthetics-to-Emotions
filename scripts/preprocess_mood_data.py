import pandas as pd
import os

IMG_BASE_DIR = r"BAE--Bringing-Aesthetics-to-Emotions\data\mood_data"
OUTPUT_PATH = r"BAE--Bringing-Aesthetics-to-Emotions\data\mood_data\filtered_labels_auto.csv"
TARGET_CLASSES = ['happy', 'neutral', 'sad']
SUBSETS = ['Train', 'Test']

data = []

for subset in SUBSETS:
    for mood in TARGET_CLASSES:
        img_folder = os.path.join(IMG_BASE_DIR, subset, mood)
        if not os.path.exists(img_folder):
            continue
        for img_file in os.listdir(img_folder):
            if img_file.endswith(".png") or img_file.endswith(".jpg"):
                data.append({
                    "subset": subset,
                    "label": mood,
                    "filename": img_file,
                    "full_path": os.path.join(img_folder, img_file)
                })

df = pd.DataFrame(data)
print(f"Total images found: {len(df)}")
df.to_csv(OUTPUT_PATH, index=False)
print(f"Saved filtered CSV to {OUTPUT_PATH}")
