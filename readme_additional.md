* Need to start the virtual environment with this command: *.venv\Scripts\activate*

* Run *deactivate* to shut down the virtual environment.

* Run *.\make html* to build the docs.

* Delete the /docs directory with *rm -r docs*.  Do this before each build.

* For GitHub, need to add this line to the *index.html* file in the root of the /docs directory.  I have stored a copy of this file in the root of the project:
    *<meta http-equiv="refresh" content="0; url=./html/index.html" />*

* Put an empty *.nojekyll* file in the root of the */docs* build folder.

* Need to create a */docs* folder as per this article.  This requires a configuration change in the *conf.py* file: https://python.plainenglish.io/how-to-host-your-sphinx-documentation-on-github-550254f325ae


## Notes

* You can use this format in MD to open links in another tab:  *<a href="https://youtu.be/6WfF_JHMtnU" target="_blank" rel="noopener" title="alt text to specify">https://youtu.be/6WfF_JHMtnU</a>*
