import sys
import os
from PIL import Image

def scale_image(input_path, output_path, scale_factor=5):
    try:
        # Open the original image
        original_image = Image.open(input_path)

        # Calculate the new size
        original_width, original_height = original_image.size
        new_size = (original_width * scale_factor, original_height * scale_factor)

        # Resize the image
        scaled_image = original_image.resize(new_size, Image.NEAREST)

        # Save the scaled-up image
        scaled_image.save(output_path)

        print(f'Scaled up {os.path.basename(input_path)} by {scale_factor} and saved as: {output_path}')
    except Exception as e:
        print(f"Error processing {input_path}: {e}")

def scale_images_in_folder(source_folder, dest_folder, scale_factor=5):
    # Ensure the destination folder exists
    os.makedirs(dest_folder, exist_ok=True)
    
    # Iterate over all PNG files in the source folder
    for filename in os.listdir(source_folder):
        if filename.lower().endswith('.png'):
            input_path = os.path.join(source_folder, filename)
            output_path = os.path.join(dest_folder, filename)
            scale_image(input_path, output_path, scale_factor)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py source_folder dest_folder [scale_factor]")
    else:
        source_folder = sys.argv[1]
        dest_folder = sys.argv[2]
        scale_factor = int(sys.argv[3]) if len(sys.argv) > 3 else 10
        scale_images_in_folder(source_folder, dest_folder, scale_factor)
