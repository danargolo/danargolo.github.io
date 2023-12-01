import os
import re

from format_html_page import write_html

styles = {
    "page": 'index',
    "class": 'posts'
}

def generate_post_link(file_path):
    with open(file_path, 'r', encoding='utf-8') as post_file:
        file_content = post_file.read()

    match_title = re.search(r'<h1>(.*?)<\/h1>', file_content)
    match_content = re.search(r'<p>(.*?)<\/p>', file_content, re.DOTALL)
    match_author = re.search(r'<author>(.*?)<\/author>', file_content)

    post_title = match_title.group(1) if match_title else 'No Title'
    post_content = match_content.group(1) if match_content else 'No Content'
    post_author = match_author.group(1) if match_author else 'No Author'

    return (
    f"""<article class="post">
        <h3 class="post_title"><a href="{file_path}">{post_title}</a></h3>
        <p>{post_content[0:500]}...<br/><strong>Continue lendo
        </strong></p>
        <h5>Author: {post_author}</h5>
      </article>
      """)

def is_folder_empty(folder_path):
    return not os.listdir(folder_path)

def get_posts_contents(posts_folder):
    posts_contents = ''
    
    for year in os.listdir(posts_folder):
        folder_year = os.path.join(posts_folder, year)

        for month in os.listdir(folder_year):
            folder_month = os.path.join(folder_year, month)

            for post_file in reversed(sorted(os.listdir(folder_month))):
                if post_file.endswith('.html'):
                    post_path = os.path.join(folder_month, post_file)
                    posts_contents += generate_post_link(post_path)
                    
    return posts_contents
    

def generate_index():
    posts_folder = './posts'
    posts_contents = get_posts_contents(posts_folder)

    if not posts_contents:
        posts_contents = 'No content posted.'

    write_html('./index.html', posts_contents, styles)

    print('Index created.')

generate_index()