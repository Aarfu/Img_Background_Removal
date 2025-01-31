from bs4 import BeautifulSoup

# Replace with the actual file path to your HTML file
file_path = "C:\\Users\\Lenovo\\Downloads\\Suspension and arms images\\Bulk\\final\\image_links\\1.jpeg"

# Read the HTML content from the local file
with open(file_path, "r", encoding="utf-8") as file:
    html = file.read()

# Parse the HTML content
soup = BeautifulSoup(html, 'html.parser')

# Find all image tags and extract their source URLs
image_tags = soup.find_all('img')
image_urls = [tag['src'] for tag in image_tags]

# Print the extracted image URLs
for url in image_urls:
    print(url)
