import os
from PIL import Image

INPUT_FOLDER = "input_images"
OUTPUT_FOLDER = "output_images"
RESIZE_TO = (800, 800)
OUTPUT_FORMAT = "JPEG"

if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

extensions = (".jpg", ".jpeg", ".png", ".webp")

print("Processing images...")

for filename in os.listdir(INPUT_FOLDER):
    if filename.lower().endswith(extensions):
        try:
            img_path = os.path.join(INPUT_FOLDER, filename)
            img = Image.open(img_path)
            img = img.resize(RESIZE_TO)
            base_name = os.path.splitext(filename)[0]
            new_filename = f"{base_name}_resized.{OUTPUT_FORMAT.lower()}"
            save_path = os.path.join(OUTPUT_FOLDER, new_filename)
            img.save(save_path, OUTPUT_FORMAT)
            print(f"✔ Saved: {new_filename}")
        except Exception as e:
            print(f"❌ Error processing {filename}: {e}")

print("\nDone! All images resized successfully.")
