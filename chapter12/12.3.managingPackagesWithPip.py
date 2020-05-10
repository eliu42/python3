# 12.3 Managing Packages with pip

# You can install, upgrade, and remove packages using a program called pip. By default pip will install packages from Python Package Index, <https://ppypi.org>. You can browse the Python Package Index by going to it in your web brwoser, or you can use pip's limited search feature:

# tutorial-env) $ pip search astronomy

# pip has a number of subcommnands: "search", "install", "uninstall", "freeze", etc. (consult the Installing Python Modules guide for complete documentation for pip.)

# You can install the lastest version of a package by specifing a package's name:

# (tutorial-env) $ pip install novas

# You can also install a specific version of a package by giving the package name followed by == and the version number:

# (tutorial-env) $ pip install requests==2.6.0

# If you re=run this command, pip will notice that the requested version is already installed and do nothing. You can supply a different version number to get that version, or you can run pip install --upgrade to upgrade the package to the latest version:

# (tutorial-env) $ pip install --upgrade requests

# pip uninstall followed by one or more package names will remove the packages from the virtual environment.

# pip show will display information about a particular package:

# (tutorial-env) $ pip show requests

# pip list will display all of the packages installed in the virtual environment:

# (tutorial-env) $ pip list

# pip freeze will produce a similar list of the installed packages, but the output uses the format that pip install expects. A common convention is to put this list in a requirements.txt file:

# (tutorial-env) $ pip freeze > requirements.txt
# (tutorial-env) $ cat reqreuiments.txt

# The requirements.txt can then be commited to version control and shipped as part of an application. Users can then install all the necessary packages with install -r:

# (tutorial-env) $ pip install -r requirements.txt

# pip has many more options. Consult the Installing Python Modules guide for omplete documentation for pip. When you've written a package and want to make it available on the Python Package Index, consult the Distributing Python Modules guide.
