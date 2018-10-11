import os

def declare_variables(variables, macro):
    """
    This is the hook for the functions

    - variables: the dictionary that contains the variables
    - macro: a decorator function, to declare a macro.
    """

    variables['baz'] = "John Doe"


    uw_version = '2.6.0b'
    uw_gh_code = 'https://github.com/underworldcode/underworld2/tree/'+uw_version
    uw_gh_docs = 'https://github.com/underworldcode/underworld2-documentation/tree/master'
    uw_nbviewer_base_url = 'https://nbviewer.jupyter.org/github/underworldcode/underworld2-documentation/blob/master'

    variables['uw_version'] = uw_version


    print(uw_version)
    print(uw_gh_code)

    @macro
    def bar(x):
        return (2.3 * x) + 7



    # If you wish, you can  declare a macro with a different name:
    def f(x):
        return x * x

    macro(f, 'barbaz')

    # or to export some predefined function
    import math
    macro(math.floor) # will be exported as 'floor'


    @macro
    def embed_notebook(name):
        HTMLtemplate = """<iframe height="500" width="100%" src="{}""></iframe>"""
        HTML = HTMLtemplate.format(name)
        return HTML



# @macro
# def button(label, url):
#     "Add a button"
#     url = fix_url(url)
#     HTML = """<a class='button' href="%s">%s</a>"""
#     return HTML % (url, label)
