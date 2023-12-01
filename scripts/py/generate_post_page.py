import os

from load_md import load_md
from format_html_page import write_html

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

    write_html(file_path,md,styles)

    print(f'{file_name} created.')

    
generate_post_page()
    
