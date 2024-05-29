import os

# Get the current directory
current_directory = os.getcwd()

# Generate HTML code
html_code = '<!DOCTYPE html>\n<html>\n<head>\n<title>Image Gallery</title>\n</head>\n<body>\n'

# Loop through files in the current directory
for filename in os.listdir(current_directory):
    if filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.jpeg'):
        # Create a link to each image
        html_code += f'<a href="{filename}"><img src="{filename}" alt="{filename}"></a>\n'

# Close HTML tags
html_code += '</body>\n</html>'

# Write HTML code to a file
with open('image_gallery.html', 'w') as f:
    f.write(html_code)

print('HTML code generated successfully!')

