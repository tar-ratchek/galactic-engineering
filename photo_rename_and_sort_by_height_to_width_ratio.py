import os
from PIL import Image
from shutil import copyfile

# Change this to the directory containing your photos
photo_dir = "/ADD/YOUR/PATH/HERE"

# List to hold (height, filename) tuples
photos = []

# Iterate over each photo in the directory
for photo in os.listdir(photo_dir):
    if photo.lower().endswith((".png", ".jpg", ".jpeg")):
        path = os.path.join(photo_dir, photo)
        with Image.open(path) as img:
            # Append tuple of (height, filename) to the list
            photos.append((img.height, img.width, photo))

# Sort photos by height
photos.sort(key=lambda x: x[0] / x[1])

# Iterate and rename photos
for i, (height, width, photo) in enumerate(photos, start=1):
    original = os.path.join(photo_dir, photo)
    print(f"Working on {photo} that has a height of {height}")
    renamed = os.path.join(photo_dir, f"{i}.jpg")
    copy_renamed = os.path.join(photo_dir, f"{i}_bg.jpg")

    # Rename original photo
    os.rename(original, renamed)

    # Make a copy
    copyfile(renamed, copy_renamed)

print("Renaming completed.")
