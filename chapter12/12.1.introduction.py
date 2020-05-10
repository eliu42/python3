# Python applications will often use packages and modules that don't come as part of the standard library. Applications will sometimes need a specific version of a libray, because the application may require that a particular bug has beeen fixed or the application may be writen using an obsolete version of the library's interface.

# This means it may not be possible for one Python installation to meet the requirements of every application. If application A needs version 1.0 of a particular module but application B needs version 2.0, then the requirements are in conflit and installing either version 1.0 or 2.0 will leave one application unable to run.

# The solution for this problem is to create a virtual enrionment, a self-cotained directory tree that contains a Python installation for a particular version of Python, plus a number of additional packages.

# Different applications can then use different virtual environments. To resolve the earlier example of conflicting requirements, application A can have its own virtual enironment with version 1.0 installed while appolication B has another virtual environment with versio 2.0 If application B requires a library upgraded to version 3.0 this will not affect applicatoin A's enviornment.
