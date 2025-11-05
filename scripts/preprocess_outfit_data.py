import pandas as pd
import os

# Input and output paths
INPUT_CSV = r"BAE--Bringing-Aesthetics-to-Emotions\data\outfit_data\Fashion Product Images (Small)\styles.csv"
OUTPUT_CSV = r"BAE--Bringing-Aesthetics-to-Emotions\data\outfit_data\Fashion Product Images (Small)\filtered_top_bottom.csv"
IMAGE_DIR = r"BAE--Bringing-Aesthetics-to-Emotions\data\outfit_data\Fashion Product Images (Small)\images"

def preprocess_top_bottom():
    df = pd.read_csv(INPUT_CSV, on_bad_lines='skip')

    # Keep only Topwear & Bottomwear based on masterCategory
    df_filtered_category = df[df['masterCategory'].isin(['Apparel'])] # Apparel contains Topwear and Bottomwear

    # Further filter by subCategory to get only Topwear and Bottomwear
    df_filtered_sub = df_filtered_category[df_filtered_category['subCategory'].isin(['Topwear', 'Bottomwear'])]


    # Keep only essential columns, including masterCategory for the value_counts() call
    required_cols = ['id', 'gender', 'masterCategory', 'subCategory', 'articleType', 'season', 'usage']
    df_final = df_filtered_sub[required_cols]

    # Add image path
    df_final['image_path'] = df_final['id'].astype(str) + ".jpg"
    df_final['image_full_path'] = df_final['image_path'].apply(lambda x: os.path.join(IMAGE_DIR, x))


    # Remove missing images
    df_final = df_final[df_final['image_full_path'].apply(os.path.exists)]

    print("Filtered dataset shape:", df_final.shape)
    # Now masterCategory should be available for value_counts()
    print(df_final['masterCategory'].value_counts())
    print(df_final['subCategory'].value_counts())


    df_final.to_csv(OUTPUT_CSV, index=False)
    print(f"Saved filtered CSV at: {OUTPUT_CSV}")
    print(df_final.head())


if __name__ == "__main__":
    preprocess_top_bottom()