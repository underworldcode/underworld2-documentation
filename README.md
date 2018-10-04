# Docker container with static website / jupyter notebook server


This is a collection of tools to set up a web server in a docker
container that mixes static html content and dynamic
 "literate-programming" content via jupyter notebooks.

It uses `mkdocs` to build / manage the static content.

The Dockerfiles tell you how to build a suitable image.


https://mybinder.org/v2/gh/lmoresi/uw-docker-landing-page/master

https://mybinder.org/v2/gh/lmoresi/uw-docker-landing-page/master?filepath=index.ipynb

```python
  import os
  print os.environ['JUPYTERHUB_SERVICE_PREFIX']
```


/usr/bin/python/usr/local/bin/jupyter-notebook--ip=0.0.0.0--port=8888--NotebookApp.base_url=/user/lmoresi-uw-docker-landing-page-fr2c4att/--NotebookApp.token=_D8ff0AySOuU3DZy-yNdow--NotebookApp.trust_xheaders=True--NotebookApp.allow_origin=*jovyan@jupyter-lmoresi-2duw-2ddocker-2dlanding-2dpage-2dfr2c4att:~/www$
