from PIL import Image
import os

# Define input and output folders
input_folder = "C:\\Users\\neila\\Downloads\\landscape"
output_folder = "C:\\Users\\neila\\Downloads\\resized1"

# Ensure output folder exists, create if not
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Initialize a counter for renaming
counter = 1

# Define the desired dimensions
target_width = 1280
target_height = 720

# Iterate over each image in the input folder
for filename in os.listdir(input_folder):
    # Check if file is an image
    if filename.endswith(('.png', '.JPG', '.jpeg', '.jpg', '.JPEG', '.PNG')):
        # Open the image
        img = Image.open(os.path.join(input_folder, filename))

        # Calculate padding to maintain aspect ratio without stretching
        width_ratio = target_width / img.width
        height_ratio = target_height / img.height
        ratio = min(width_ratio, height_ratio)
        new_width = int(img.width * ratio)
        new_height = int(img.height * ratio)
        padding_width = (target_width - new_width) // 2
        padding_height = (target_height - new_height) // 2

        # Resize the image without fitting using thumbnail method and pad with white color
        resized_img = img.resize((new_width, new_height))
        padded_img = Image.new("RGB", (target_width, target_height), (255, 255, 255))
        padded_img.paste(resized_img, (padding_width, padding_height))

        # Define the new filename with the counter
        new_filename = f"{counter}.jpg"  # Change the extension if needed

        # Save the padded image with the new filename to the output folder
        padded_img.save(os.path.join(output_folder, new_filename))

        print(f"Resized {filename} and padded to {new_filename} without fitting or stretching.")

        # Increment the counter for the next image
        counter += 1
    else:
        print(f"{filename} is not an image.")

print("All images resized and padded successfully.")
