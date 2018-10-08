# Configuration file for jupyter-notebook.

## The default URL to redirect to from `/`
## This assumes we launch from the directory
## where the built files all live (seems safest)

c.NotebookApp.default_url = '/tree/notebooks/Underworld_Introduction.ipynb'

# c.NotebookApp.file_to_run="Notebooks/StartHere.ipynb"
# c.NotebookApp.allow_origin="*"
# c.NotebookApp.disable_check_xsrf=True

c.NotebookApp.nbserver_extensions.jupyter_nbextensions_configurator=True


"""
{
  "NotebookApp": {
    "nbserver_extensions": {
      "jupyter_nbextensions_configurator": true
    }
    "default_url":"Underworld_Introduction.ipynb"
  }
}
"""
