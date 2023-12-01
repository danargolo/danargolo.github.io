#!/usr/bin/env python3

import json

def load_json():

  with open('config_blog.json', 'r') as config_file:
      config_data = json.load(config_file)

  return config_data
  