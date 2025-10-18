import os
import pandas as pd
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense, Dropout
from tensorflow.keras.models import Model
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
import matplotlib.pyplot as plt

BASE_DIR = "BAE--Bringing-Aesthetics-to-Emotions\data\mood_data"
IMG_DIR = "BAE--Bringing-Aesthetics-to-Emotions\data\mood_data"
CSV_PATH = "BAE--Bringing-Aesthetics-to-Emotions\data\mood_data\labels.csv"
SAVE_PATH = "BAE--Bringing-Aesthetics-to-Emotions\models\mood_model\mobilenetv2_mood_3class.h5" 

os.makedirs(os.path.dirname(SAVE_PATH), exist_ok=True)

# ==== Load metadata ====
df = pd.read_csv(CSV_PATH)

# ==== Data generators ====
datagen = ImageDataGenerator(
    preprocessing_function=preprocess_input,
    validation_split=0.2
)

train_gen = datagen.flow_from_dataframe(
    dataframe=df,
    directory=IMG_DIR,
    x_col="full_path",  
    y_col="label",    
    target_size=(224,224),
    batch_size=32,
    class_mode="categorical",
    subset="training"
)
val_gen = datagen.flow_from_dataframe(
    dataframe=df,
    directory=IMG_DIR,
    x_col="full_path", 
    y_col="label",  
    target_size=(224,224),
    batch_size=32,
    class_mode="categorical",
    subset="validation"
)

# ==== Build model ====
base_model = MobileNetV2(weights="imagenet", include_top=False, input_shape=(224,224,3))
for layer in base_model.layers[:-30]:
    layer.trainable = False

x = GlobalAveragePooling2D()(base_model.output)
x = Dropout(0.4)(x)
x = Dense(64, activation='relu')(x)
output = Dense(3, activation='softmax')(x)
mood_model = Model(inputs=base_model.input, outputs=output)

mood_model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
mood_model.summary()

# ==== Callbacks ====
callbacks = [
    EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True),
    ModelCheckpoint(SAVE_PATH, save_best_only=True, monitor='val_accuracy', mode='max')
]

# ==== Train ====
history = mood_model.fit(train_gen, validation_data=val_gen, epochs=20, callbacks=callbacks)

# ==== Ensure model is saved ====
# Manual save in case ModelCheckpoint did not trigger
if not os.path.exists(SAVE_PATH):
    print("[WARN] ModelCheckpoint did not save the model, saving manually...")
    mood_model.save(SAVE_PATH)
    print(f"[INFO] Model manually saved to {SAVE_PATH}")
else:
    print(f"[INFO] Model saved automatically to {SAVE_PATH}")

# ==== Plot ====
plt.plot(history.history['accuracy'], label='Train')
plt.plot(history.history['val_accuracy'], label='Val')
plt.legend(); plt.title("Training Accuracy"); plt.show()