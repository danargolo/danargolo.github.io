#!/usr/bin/env python3

import json
from markdown2 import markdown
from generate_post_page import generate_post_page


def load_json():
  data = {}
  with open('post_blog.md') as md_file:
      md_content = markdown(
         md_file.read(),
         extras=['fenced-code-blocks', 'code-friendly']
      )

  with open('config_blog.json', 'r') as config_file:
      config_data = json.load(config_file)

      data['configs'] = config_data
  
  generate_post_page(data, md_content)

load_json() 