Local spelling
==============

Developed by Fast Data Science, https://fastdatascience.com

Source code at https://github.com/fastdatascience/localspelling

Python library for localising spelling between British and American conventions, conserving case.

Please note this library converts only spelling variants such as US "honour" vs UK "honor".

It does not localise vocabulary such as "pavement" vs "sidewalk" or "aubergine" vs "eggplant".

It also does not localise spellings where there is more than one correct conversion, such as US "program", which corresponds to both "programme" and "program" in British spelling.

Requirements
============

Python 3.6 and above

Installation
============

::

  pip install localspelling

Usage examples
==============

.. code:: python

  from localspelling import convert_spelling
  convert_spelling("it has been an honor", "gb")

outputs 'it has been an honour'

Who to contact
==============

Thomas Wood at https://fastdatascience.com

