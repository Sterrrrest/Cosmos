import os


from urllib.parse import urlparse

def get_ext(url):
  path = urlparse(url).path
  ext = os.path.splitext(path)[1]
  return ext