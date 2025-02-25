import argparse
import os
from pathlib import Path
from pillow_heif import register_heif_opener
from PIL import Image
from tqdm import tqdm

def convert_heic_to_jpg(input_folder):
    # Register HEIC file opener
    register_heif_opener()
    
    # Create output folder
    output_folder = os.path.join(input_folder, 'converted_jpg')
    os.makedirs(output_folder, exist_ok=True)
    
    # Get all HEIC files
    heic_files = list(Path(input_folder).glob('*.HEIC')) + list(Path(input_folder).glob('*.heic'))
    
    if not heic_files:
        print("No HEIC files found!")
        return
    
    # Convert each HEIC file with progress bar
    for heic_file in tqdm(heic_files, desc="Converting HEIC files"):
        try:
            # Read HEIC file
            image = Image.open(heic_file)
            
            # Create output file path
            output_path = os.path.join(output_folder, f"{heic_file.stem}.jpg")
            
            # Save as JPG
            image.save(output_path, 'JPEG')
            # print(f"Converted: {heic_file.name} -> {os.path.basename(output_path)}")
            
        except Exception as e:
            print(f"\nError converting {heic_file.name}: {str(e)}")

def main():
    # Create argument parser
    parser = argparse.ArgumentParser(description='Convert HEIC files to JPG format')
    parser.add_argument('folder_path', help='Path to folder containing HEIC files')
    
    # Parse arguments
    args = parser.parse_args()
    
    # Check if folder exists
    if not os.path.exists(args.folder_path):
        print("Error: Specified folder does not exist!")
        return
    
    if not os.path.isdir(args.folder_path):
        print("Error: Specified path is not a folder!")
        return
    
    # Execute conversion
    convert_heic_to_jpg(args.folder_path)

if __name__ == '__main__':
    main() 