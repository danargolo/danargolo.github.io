#!/usr/bin/env python3
from markdown2 import markdown

def load_md():

  with open('post_blog.md', 'r') as md_file:
      md_content = markdown(
         md_file.read(),
         extras=['fenced-code-blocks', 'code-friendly']
      )
  return md_content