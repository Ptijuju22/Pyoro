import os
from PIL import Image


def resize_images(input_folder: str, size: tuple[int, int]):
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(("png", "jpg", "jpeg", "bmp", "gif")):
            image_path = os.path.join(input_folder, filename)
            img = Image.open(image_path)  # type: ignore

            # Resize without interpolation
            img_resized = img.resize(size, Image.NEAREST)  # type: ignore

            # Save resized image
            output_path = os.path.join(input_folder, filename)
            img_resized.save(output_path)  # type: ignore


input_folder = input("Input folder=")
size = (int(input("New width=")), int(input("New height=")))

resize_images(input_folder, size)
