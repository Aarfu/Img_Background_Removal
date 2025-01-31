from rembg import remove
import os
#file type should be png or jpg not jpeg
# Specify the input and output directories
input_directory = 'C:\\Users\\Lenovo\\Downloads\\Suspension and arms images\\processed ball joint'
output_directory = 'C:\\Users\\Lenovo\\Downloads\\Suspension and arms images\\Testing'

# Create the output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# List all image files in the input directory
image_files = os.listdir(input_directory)

# Loop through the image files and remove the background
for image_file in image_files:
    # Specify the input and output file paths
    input_path = os.path.join(input_directory, image_file)
    output_path = os.path.join(output_directory, image_file)

    # Read the image data from the input file
    with open(input_path, 'rb') as inp:
        image_data = inp.read()

    # Remove the background and save the result
    output_data = remove(image_data)

    # Write the resulting image data to the output file
    with open(output_path, 'wb') as out:
        out.write(output_data)

print('Background removal completed.')
