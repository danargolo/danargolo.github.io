import os

from load_md import load_md
from scripts.py.format_html_page import format_header 

from datetime import datetime

def generate_post_page():
    md = load_md()
    styles = {
        "page": 'posts',
        "class": 'post'
    }

    current_date = datetime.now()
    year_folder = current_date.strftime('%Y')
    month_folder = current_date.strftime('%m')

    folder_path = os.path.join('posts', year_folder, month_folder)
    os.makedirs(folder_path, exist_ok=True)

    file_name = f"post_{current_date.strftime('%Y%m%d_%H%M')}.html"
    file_path = os.path.join(folder_path, file_name)

    with open(file_path, 'w') as html_file:
        html_file.write(
            format_header(
                md,
                styles
            )
        ) 
    print(f'{file_name} created.')

    
generate_post_page()
    
