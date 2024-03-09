import sys
import os
from PIL import Image, ImageSequence

def save_gif_frames(gif_path, output_dir):
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Open the animated GIF
    with Image.open(gif_path) as gif:
        # Iterate through each frame in the animated GIF
        for i, frame in enumerate(ImageSequence.Iterator(gif)):
            # Save each frame as a separate image
            frame_path = os.path.join(output_dir, f'{output_dir}_{i:03}.png')
            frame.save(frame_path, format='PNG')
            print(f'Frame {i} saved as: {frame_path}')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py path_to_animated_gif.gif output_directory")
    else:
        gif_path = sys.argv[1]
        output_dir = sys.argv[2]
        save_gif_frames(gif_path, output_dir)
