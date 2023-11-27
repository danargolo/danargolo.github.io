#!/usr/bin/env python3

import json
import markdown
from generate_post_page import generate_post_page


def load_json():
  data = {}
  with open('post_blog.md', 'r') as md_file:
      md_content = md_file.read()
      md_data = markdown.markdown(md_content)

  with open('config_blog.json', 'r') as config_file:
      config_data = json.load(config_file)

      data['configs'] = config_data
      data['content'] = md_data
  
  generate_post_page(data)

load_json() 