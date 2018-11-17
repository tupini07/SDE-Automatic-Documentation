.. toctree::
    :maxdepth: 2
    :caption: Other pages:

    directives_example

Automatic API Documentation with Sphinx
=======================================


.. 
    Note that :undoc-static: simply means that
    we don't want to document funcitons that don't to anything
    (that only return a static file).


.. qrefflask:: app:app
   :undoc-static:


=======================================
Api details!
=======================================

.. autoflask:: app:app
   :undoc-static:


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
