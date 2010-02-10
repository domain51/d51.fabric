.. d51.fabric documentation master file, created by
   sphinx-quickstart on Tue Feb  9 19:42:20 2010.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

d51.fabric
==========
This is a collection of re-usable tasks for Fabric.


Requirements
------------
These tasks have all been built to be used with the 1.0a version of the `Fabric
fork <http://github.com/tswicegood/fabric>`_ maintained by `Travis Swicegood
<http://www.travisswicegood.com>`_.  It might be usable with other versions of
Fabric, but your mileage may vary.


Installation
------------
Each of these packages are installable by themselves, or they can be built as
one über-package.  See individual packages for instructions on installing them
individually.


Installing Fabric
^^^^^^^^^^^^^^^^^

To install ``d51.fabric``, you must have Fabric installed.  You can do this via
`pip <http://pip.openplans.org/>`_::

    prompt> pip install -e git://github.com/tswicegood/fabric.git#egg=fabric

You can also install it by creating a clone of the repository and installing
via the provided ``setup.py``::

    prompt> git clone git://github.com/tswicegood/fabric.git
    ... git clone output ...
    prompt> python setup.py install

Depending on the configuration of your system, you may have to prefix the ``pip``
or ``python`` commands above with ``sudo``.

**Important Note**: This installs Travis Swicegood's fork of Fabric.  This is
necessary if you wish to utilize the tasks in ``d51.fabric``, as they utilize
features that have yet to be merged back into the main line of development.

Packaging ``d51.fabric``
^^^^^^^^^^^^^^^^^^^^^^^^
``d51.fabric`` is a package that contains the code necessary to assemble all of
its separate pieces into one, installable package.  Once Fabric is installed,
create a clone of the ``d51.fabric`` repository, then run the ``install``
command::

    prompt> git clone git://github.com/domain51/d51.fabric.git
    prompt> cd d51.fabric
    prompt> fab install

You can also work directly with the ``setup.py`` file, however, you must run
``fab src`` to assemble all of the various repositories and place their files
in the correct location.


Building This Documentation
^^^^^^^^^^^^^^^^^^^^^^^^^^^
You can build this documentation from within the repository by using the ``docs``
task from Fabric::

    prompt> fab docs

This places the HTML documentation into the ``docs/_build/html``.

If you prefer, you can run the command individually to build the documentation::

    prompt> fab src
    prompt> cd docs
    prompt> make html


Table of Contents
-----------------

.. toctree::
   :maxdepth: 2

   d51.fabric.tasks.django/index
   d51.fabric.tasks.mosso/index
   d51.fabric.tasks.rabbitmq/index
   d51.fabric.tasks.ubuntu/index

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

