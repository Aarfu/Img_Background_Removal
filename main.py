from rembg import remove
import os
from PIL import Image

#file type should be jpg , jpeg, webp
#dont use png file in resize


input_directory = 'C:\\Users\\Lenovo\\Downloads\\Suspension and arms images\\Strut mount and bearing'
output_directory = 'C:\\Users\\Lenovo\\Downloads\\Suspension and arms images\\Strut mount and bearing\\bg_remove'

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

print('Aarfu Background removal completed.')



##code resize and convert images to jpg


def resize_and_convert_to_jpeg(input_image_path, output_image_path, min_dimension):
    try:
        # Open the image file
        with Image.open(input_image_path) as img:
            width, height = img.size

            # Check if height > min_dimension and width < min_dimension
            if height > min_dimension and width < min_dimension:
                new_width = min_dimension
                new_height = height

            # Check if height < min_dimension and width > min_dimension
            elif height < min_dimension and width > min_dimension:
                new_height = min_dimension
                new_width = width

            # If neither condition is met, keep the original dimensions
            elif height < min_dimension and width < min_dimension:
                new_width = min_dimension
                new_height = min_dimension

            else:
                new_width = width
                new_height = height

            # Resize the image
            resized_img = img.resize((new_width, new_height))

            # Convert to RGB mode (removing alpha channel if present)
            if resized_img.mode == 'RGBA':
                resized_img = resized_img.convert('RGB')

            # Ensure the output path has a .jpg or .jpeg extension
            output_image_path = output_image_path.lower()
            if not output_image_path.endswith(('.jpg', '.jpeg')):
                output_image_path += '.jpg'

            # Save the resized image as JPEG
            resized_img.save(output_image_path, 'JPEG')

            print(f"Processed {input_image_path}, resized to {new_width}x{new_height}, and saved as {output_image_path}")

    except Exception as e:
        print(f"Error processing {input_image_path}: {str(e)}")

if __name__ == "__main__":
    input_directory = 'C:\\Users\\Lenovo\\Downloads\\Suspension and arms images\\Stabilizer bush\\bg_remove'
    output_directory = 'C:\\Users\\Lenovo\\Downloads\\Suspension and arms images\\Stabilizer bush\\final'
    min_dimension = 800

    # Ensure the output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Loop through all files in the input directory
    for filename in os.listdir(input_directory):
        input_image_path = os.path.join(input_directory, filename)
        output_image_path = os.path.join(output_directory, filename)

        # Check if the file has a WebP, JPEG, or JPG extension
        if filename.lower().endswith(('.webp', '.jpeg', '.jpg')):
            resize_and_convert_to_jpeg(input_image_path, output_image_path, min_dimension)


