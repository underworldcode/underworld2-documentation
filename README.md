# Docker container with static website / jupyter notebook server


This is a collection of tools to set up a web server in a docker
container that mixes static html content and dynamic
 "literate-programming" content via jupyter notebooks.

It uses `mkdocs` to build / manage the static content.

The Dockerfiles tell you how to build a suitable image.


https://mybinder.org/v2/gh/lmoresi/uw-docker-landing-page/master



```python
  import os
  print os.environ['JUPYTERHUB_SERVICE_PREFIX']
```
