import os
import shutil


def organize_data(input_dir, output_dir):
    # Create output directories if they don't exist
    os.makedirs(os.path.join(output_dir, 'images'), exist_ok=True)
    os.makedirs(os.path.join(output_dir, 'labels'), exist_ok=True)

    # Iterate through folders inside the input directory
    for folder_name in os.listdir(input_dir):
        folder_path = os.path.join(input_dir, folder_name)

        # Check if it's a directory and has 'image' and 'label' subdirectories
        if os.path.isdir(folder_path) and 'image' in os.listdir(folder_path) and 'label' in os.listdir(folder_path):
            # Get paths to image and label files
            image_file = os.path.join(folder_path, 'image', os.listdir(os.path.join(folder_path, 'image'))[0])
            label_file = os.path.join(folder_path, 'label', os.listdir(os.path.join(folder_path, 'label'))[0])

            # Copy files to the output directories
            shutil.copy(image_file, os.path.join(output_dir, 'images', f'{folder_name}.nii.gz'))
            shutil.copy(label_file, os.path.join(output_dir, 'labels', f'{folder_name}.nii.gz'))


if __name__ == "__main__":
    input_directory = "../train-parse2022"
    output_directory = "output"

    organize_data(input_directory, output_directory)
    print("Data organization completed.")
