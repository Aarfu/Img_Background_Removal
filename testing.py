from rembg import remove
import os
from PIL import Image
import pandas as pd
import io
import requests

# Function to remove background and save images
def remove_background_and_save(input_url, output_path):
    try:
        # Fetch the image from the URL
        response = requests.get(input_url)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Create a file-like object from the response content
            image_data = response.content

            # Remove the background
            output_data = remove(image_data)


            with Image.open(io.BytesIO(output_data)) as img:
                # Resize the image
                width, height = img.size
                print("initial resolution",width ,"*",height)

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
                img = img.resize((new_width, new_height))

                # Convert to RGB mode (removing alpha channel if present)
                if img.mode == 'RGBA':
                    img = img.convert('RGB')

                # Save the resized image as JPEG
                img.save(output_path, 'JPEG')



            print(f"Background removed, resized, and saved as {output_path}")
        else:
            print(f"Failed to fetch image from URL: {input_url}")
    except Exception as e:
        print(f"Error processing {input_url}: {str(e)}")

# Load the Excel file containing image URLs
excel_file = 'C:\\Users\\Lenovo\\Downloads\\testing.xlsx'  # aarf's file path

df = pd.read_excel(excel_file)

# Create the output directory if it doesn't exist
output_directory = 'C:\\Users\\Lenovo\\Downloads\\testing'  # Adjust the output directory path
os.makedirs(output_directory, exist_ok=True)

# Aarfu's desired dimension for resizing is 800
min_dimension = 800

# Iterate through the rows and process each image URL
for index, row in df.iterrows():
    image_url = row['URL']  # 'URL' should match the column name in  Excel file
    output_path = os.path.join(output_directory, f'image_{index}.jpg')  # Adjusting the naming and extension
    remove_background_and_save(image_url, output_path)
#
# # Check if the file has a WebP, JPEG, or JPG extension
#         if filename.lower().endswith(('.webp', '.jpeg', '.jpg')):
#             resize_and_convert_to_jpeg(input_image_path, output_image_path, min_dimension)





print("Hey Aarfu ,Bulk image processing completed.")
