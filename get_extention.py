import json
import argparse
import requests
import os

from urllib.parse import urlparse
from pathlib import Path
from os.path import join

def get_ext(url):
  path = urlparse(url).path
  ext = os.path.splitext(path)[1]
  return ext