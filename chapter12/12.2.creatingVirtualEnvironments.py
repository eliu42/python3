# 12.2 Creating Virtual Environments

# The module used to create and manage virtual environments is called venv. venv will usually install the most recent version of Python that you have available. If you have multiple versions of Python on your system, you can select a specific Python version by running Python3 or whichever version you want.

# To create a virtual environment, decide upon a directory where you want to place it, and run to venv module as a script with the directory path:

# python3 -m venv tutorial-env

# This will create the tutorial-env direcotry if it doesn't exist, and also create directories inside it containing a copy of the Python interpreter, the standard library, and various supporting files.

# A common directory location for a virtual enviroment is .venv. The name keeps the directory typically hidden in your shell and thus out of the way while giving it a name that explains why the directory exists. It also prevents clashing with .env environment varialbe definition files that some tooling supports.

# Once you've created a virtual environments, you may activate it.

# On windows, run:
# tutorial-env\Scripts\activate.bat

# On Unix or MacOS, run:
# source tutorial-env/bin/activate

# This script is written for the bash shell. If you use the csh or fish shells, there are alternate activate.csh and activate.fish scripts you should use instead.

# Activating the virtual environment will change your shell's prompt to show what virtual environment you're using, and modify the environment so that running python will get you that particular version and installation of Python. For example

# source ~/envs/tutorial-env/bin/activate
# python
# import sys
# sys.path
