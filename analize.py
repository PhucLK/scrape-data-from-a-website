from bs4 import BeautifulSoup

# Read the HTML content from the file
with open('page_content2.txt', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Extract data from specific divs
# product_divs = soup.find_all('div', class_=['sc-kUmlZZ cDEwep', 'sc-hbOKPk iqZqIQ'])

# Define the headers
headers = ['Ten', 'Sản phẩm (link of the image)', 'Mau', 'Đơn giá', 'Tiền hàng']

# Initialize a list to store the extracted data
extracted_data = []

# Iterate over each product div and extract the required details
for div in soup:
    product_name = soup.find('a', class_='sc-eDuEge dtfBoI sc-dGcaAO bmgVmI').text.strip()  # Adjust the class name as necessary
    product_image_link = soup.find('a', class_='sc-eDuEge dtfBoI sc-dGcaAO bmgVmI')['href']  # Adjust the class name as necessary
    # product_image_link = soup.find('div', class_='sc-ivSfqT eQFJgN')['href']  # Adjust the class name as necessary
    product_type = soup.find('div', class_='sc-itajox krqqyP').text.strip()  # Adjust the class name as necessary
    # product_number = soup.find('span', class_='product-number-class').get_text(strip=True)  # Adjust the class name as necessary
    # unit_price = soup.find('div', class_='sc-hnhRqi fiAaOb')[p][1]  # Adjust the class name as necessary
    # total_price = soup.find('div', class_='sc-ijELWj kwZtLd')[p][1]  # Adjust the class name as necessary
    
    # Append the extracted data to the list
    extracted_data.append([product_name, product_image_link,product_type])

# Create the formatted table content
table_content = [headers] + extracted_data

# Convert the table content to a string format
table_string = '\n'.join(['\t'.join(row) for row in table_content])

# Save the formatted table content to a text file
output_file_path = 'formatted_table.txt'
with open(output_file_path, 'w', encoding='utf-8') as file:
    file.write(table_string)

# Print a success message
print(f"Formatted table content saved to {output_file_path}")
