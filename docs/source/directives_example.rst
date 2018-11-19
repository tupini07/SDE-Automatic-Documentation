Example Directives
==================

Ths is just a demonstration of the most common directives. For a complete list check `this page <http://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#rst-directives>`_  for basic ``rst`` directives or `this other page <http://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html>`_ for more advanced sphinx directives.

Basic Directives
################

These are directives for everyday use, mainly text formatting and similar


Basic Text formatting
*********************

.. code-block:: rst
    
    * one asterisk: *text* for emphasis (italics),
    * two asterisks: **text** for strong emphasis (boldface), and
    * backquotes: ``text`` for code samples.


* one asterisk: *text* for emphasis (italics),
* two asterisks: **text** for strong emphasis (boldface), and
* backquotes: ``text`` for code samples.


Lists
*****

Normal list

.. code-block:: rst

    * this is
    * a list

        * with a nested list
        * and some subitems

    * and here the parent list continues

* this is
* a list

  * with a nested list
  * and some subitems

* and here the parent list continues

Numbered list:

.. code-block:: rst

    1. some item
    2. Another item

1. some item
2. Another item

Automatic numbering is also supported


.. code-block:: rst

    #. hi
    #. how
    #. are
    #. you


#. hi
#. how
#. are
#. you


Term Definition
***************

.. code-block:: rst

    term (up to a line of text)
        Definition of the term, which must be indented

        and can even consist of multiple paragraphs

    next term
        Description.

term (up to a line of text)
   Definition of the term, which must be indented

   and can even consist of multiple paragraphs

next term
   Description.


Normal Links
*************

You can define links directly in the body, for example: `this page <https://sites.google.com/unitn.it/introsde2018-19>`_

.. code-block:: rst

     You can define links directly in the body, for example: `this page <https://sites.google.com/unitn.it/introsde2018-19>`_



Special Links
*************

You can also define where the link text is defined in the body and the actuali link is defined later on in the document: `a link`_.

.. _a link: https://sites.google.com/unitn.it/introsde2018-19

.. code-block:: rst

     Some text `a link`_.

    .. _a link: https://sites.google.com/unitn.it/introsde2018-19


Sections
********

As you can see in this document, each section is separated by a *heading*. To define a Section headers are created by underlining (and optionally overlining) the section title with a punctuation character, at least as long as the text: ::

    =================
    Heading example
    =================


Normally, there are no heading levels assigned to certain characters as the structure is determined from the succession of headings. However, this convention is used in `Python’s Style Guide <https://docs.python.org/devguide/documenting.html#style-guide>`_ for documenting which you may follow:

* \# with overline, for parts
* \* with overline, for chapters
* \=, for sections
* \-, for subsections
* \^, for subsubsections
* \", for paragraphs



More "Advanced" directives
##########################


Code block
**********

This directive is used to highlight code, note that we can pass the name of the language as a parameter.

.. code-block:: rst

    .. code-block:: python

        def some_python_function(yes: int) -> str:
            return "testing done"


.. code-block:: python

    def some_python_function(yes: int) -> str:
        return "testing done"


Block Messages
**************
.. code-block:: rst

    .. warning::
        for example, here you are being warned

    .. note::
        This is letting you know something

    .. seealso::
        Used to add references

.. warning::
    for example, here you are being warned

.. note::
    This is letting you know something

.. seealso::

    Used to add references

Math
****

You can define some math inline :math:`a^2 + b^2 = c^2` or you can define it as a block.

.. code-block:: rst

    You can define some math inline :math:`a^2 + b^2 = c^2`

.. code-block:: rst

    .. math::

        (a + b)^2 = a^2 + 2ab + b^2

        (a - b)^2 = a^2 - 2ab + b^2


.. math::

   (a + b)^2 = a^2 + 2ab + b^2

   (a - b)^2 = a^2 - 2ab + b^2


Images
******

Adding images is very simple

.. code-block:: rst

    .. image:: https://images-na.ssl-images-amazon.com/images/I/41ksQMuhtpL.jpg

.. image:: https://images-na.ssl-images-amazon.com/images/I/41ksQMuhtpL.jpg


Footnotes
*********
.. code-block:: rst

    Here we talk about `x` [#f1]_ and here about `y` [#f2]_

    .. rubric:: Footnotes
    .. [#f1] This text explains `x` more in depth.
    .. [#f2] And this one explains `y`.


Here we talk about `x` [#f1]_ and here about `y` [#f2]_

.. rubric:: Footnotes
.. [#f1] This text explains `x` more in depth.
.. [#f2] And this one explains `y`.


Comments
********

Just a way to add comments to your markup

.. code-block:: rst

    .. This is a comment in one line.

    ..
        This whole indented block
        is a comment.

        Still in the comment.

.. this comment won't appear in rendered page


Table of Contents
*****************

.. code-block:: rst

    .. toctree::
        :maxdepth: 2
        :caption: Other pages:

        directives_example
