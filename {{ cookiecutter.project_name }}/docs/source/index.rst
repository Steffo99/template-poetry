###############################################################################
{{ cookiecutter.project_identifier }}
###############################################################################

{{ cookiecutter.project_description }}


=================
Table of contents
=================

.. 
   If you create more pages, add them in the toctree!

.. toctree::
   
   installation
   {% if cookiecutter.project_tests == "pytest" -%}
   testing
   {%- endif %}


============
Useful links
============

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
* `{{ cookiecutter.project_identifier }} on PyPI <https://pypi.org/project/{{ cookiecutter.project_identifier }}>`_
* `{{ cookiecutter.project_name }} on GitHub <https://github.com/{{ cookiecutter.github_owner }}/{{ cookiecutter.project_name }}/>`_
