import argparse
from PIL import Image
import json
import os

def convert_to_gif(input_file, output_file=None):
    # Load the image using Pillow
    img = Image.open(input_file)
    
    # Convert the image to a list of frames
    frames = [img]
    
    # Save the frame to a temporary file and convert it to GIF
    while True:
        try:
            temp_output_file = f"temp_{os.path.splitext(output_file)[0]}.png"
            img.save(temp_output_file)
            gif = Image.open(temp_output_file)
            frames.append(gif)
            os.remove(temp_output_file)  # Remove the temporary file after use
        except Exception as e:
            break
    
    # Create the GIF using all frames
    frames[0].save(output_file, save_all=True, append_images=frames[1:], duration=0.5, loop=0)
    
    if output_file is None:
        print(f"Output saved to temp_{os.path.splitext(input_file)[0]}.gif")
    else:
        print(f"Saved as {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Video to GIF converter with optimization.")
    parser.add_argument('input_file', type=str, help='Input video file')
    parser.add_argument('--json', action='store_true', help='Output in JSON format')
    parser.add_argument('--output', type=str, help='Output file name (optional)')
    
    args = parser.parse_args()
    
    try:
        if args.json:
            # Perform JSON conversion
            print("JSON output not supported yet.")
        else:
            convert_to_gif(args.input_file, args.output)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()