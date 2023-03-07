# Steffo's Python Template

Easy-to-use and full-featured template for Python projects.

Includes testing, documentation, and CI/CD setup!

## Usage

This template is intended to be used with [`pipx`] and [`cookiecutter`].

To initialize a new project with this template:

1. Install [`pipx`] following the instructions for your platform.

2. Install [`cookiecutter`] using [`pipx`]:

    ```console
    $ pipx install cookiecutter
    ```

3. Use [`cookiecutter`] to initialize a new project, then answer the questions to fill in the template:

    ```console
    $ cookiecutter gh:Steffo99/template-poetry
    project_name [example-project]: 
    project_identifier [example_project]: 
    Select project_type:
    1 - application
    2 - library
    Choose from 1, 2 [1]: 
    project_description [A demo of Steffo99/template-poetry]: 
    Select project_docs:
    1 - sphinx
    2 - none
    Choose from 1, 2 [1]: 
    Select project_tests:
    1 - compileall
    2 - none
    3 - pytest
    Choose from 1, 2, 3 [1]: 2
    project_license [AGPL-3.0-or-later]: 
    project_author_name [Firstname Lastname]: 
    project_author_email [somebody@example.org]: 
    project_author_full [Firstname Lastname <somebody@example.org>]: 
    docs_theme_color [#123abc]: 
    github_owner [YourGitHubUsername]: 
    ```


[`pipx`]: https://pypa.github.io/pipx/
[`cookiecutter`]: https://cookiecutter.readthedocs.io/en/stable/README.html
