
## Sample Jupyter / iPython notebook

Louis Moresi  
School of Earth Sciences  
University of Melbourne  
[louis.moresi@unimelb.edu.au](mailto:louis.moresi@unimelb.edu.au)  
[www.moresi.info](http://www.moresi.info)

### Docker containers

This notebook 


### Quick links

 - [Home](/) - the static web pages on this site
 - [This Page](/notebooks/Content/Notebooks/StartHere.ipynb)
 - [Browse](/notebooks/Content/Notebooks/) the jupyter filesystem, create and edit notebooks
 

### What is this ?


This is an example of the iPython / Jupyter notebook system. They are a form of literate programming in which we can mix textbook instruction and explanations with code (in this case, python) that can also be run and edited. The text and mathematics in the notebooks requires a little preliminary learning. 

The notebook system also includes a [file browser](/notebooks/Content/Notebooks/) which also allows you to add your own notebook, add a text file or start a terminal on the machine running this notebook. 

NOTE that this content is ephemeral - it will disappear with the container if you do not capture the output by mounting the volume or copying the data to your local machine. 


### Markdown

You can document your iPython notebooks by making some cells into **Markdown** cells. Markdown is a way of formatting text that is supposed to be almost as readable un-rendered as when it is tidied up. You might argue that it looks equally bad either way, but that's tough because the notebooks use it and that's how I want you to produce nice looking output to hand in as an assignment !

If you look at the **Markdown** cells as source code (by double-clicking on them) you will see how the raw text looks. To get back to the pretty version of the text, hit shift-enter.

### Maths

In a browser, you can render beautiful equations using a javascript tool called **Mathjax** which is build into the iPython notebooks. 


You can build in symbols to your text such as $\pi$ and $\epsilon$ if you use the \$ signs to indicate where your equations begin and end, and you know enough $\LaTeX$ [try it here !](http://www.codecogs.com/latex/eqneditor.php) to get by.


Equations in 'display' mode are written like this (again look at the source for this cell to see what is used)

\\[ e^{i\pi} + 1 = 0 \\]

or even like this

\begin{equation}
%%
    \nabla^4 \psi = \frac{\partial T}{\partial x}
%%    
\end{equation}

Go back to the rendered form of the cell by 'running' it.

### Links 

[Markdown Website](http://daringfireball.net/projects/markdown/)  
[Mathjax Website](http://docs.mathjax.org)  
[Jupyter Notebooks](http://www.jupyter.org)





```python
## This is a live notebook where you can execute python code

print "Hello world"

```


```sh
%%sh

## This cell is now running shell (bash) commands

ls -l
echo "---"

whoami
echo "---"

uname -a
echo "---"

```


```python
# A blank canvas

## Feel free to run your own code in this cell (then hit shift-return to execute it)


```
