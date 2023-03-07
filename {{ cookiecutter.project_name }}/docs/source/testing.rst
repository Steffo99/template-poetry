*******************************************************************************
Testing
*******************************************************************************

To run tests on |this|, you'll need to use :mod:`pytest`.


=================
Running all tests
=================

To perform a full test run:

#. Access the project's main directory:

    .. code-block:: console

        $ cd {{ cookiecutter.project_name }}

#. Run :mod:`pytest`:

    .. code-block:: console

        $ poetry run pytest --verbose --cov=. --cov-report=html
