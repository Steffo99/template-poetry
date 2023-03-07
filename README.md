# Steffo's Python Template

Full-featured, very opinionated template for Python projects

## Features

- Packaging with [`poetry`]
- Documentation with [`sphinx`] and [Read the Docs]
- Testing with either [`compileall`] or [`pytest`]
- CI/CD with [GitHub Actions], [Docker] and [Portainer Business]

## Usage

This template is intended to be used with [`pipx`] and [`cookiecutter`].

To initialize a new project with this template, follow the instructions in the next sections.

### Pre-requisites

1. Install [`pipx`] following the instructions for your platform.

2. Install [`cookiecutter`] using [`pipx`]:

    ```console
    $ pipx install cookiecutter
    ```

### Project creation

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
    Choose from 1, 2, 3 [1]:
    project_license [AGPL-3.0-or-later]: 
    project_author_name [Firstname Lastname]: 
    project_author_email [somebody@example.org]: 
    project_author_full [Firstname Lastname <somebody@example.org>]: 
    docs_theme_color [#123abc]: 
    github_owner [ghost]: 
    ```

4. Access the created directory:

    ```console
    $ cd example-project
    ```

5. Create a new repository on GitHub for it:

    - Either [create a new repository via the web interface](https://github.com/Steffo99/template-poetry/generate), then add it as a remote on your local copy of the repository and push to it:

        ```console
        $ git init
        $ git commit --message "First commit"
        $ git remote add origin git@github.com:ghost/example-project.git
        $ git branch --move --force main
        $ git push --force --set-upstream origin main

    - Or use [`gh`] to automatically initialize it:

        ```console
        $ gh repo create --push 
        ```

### Publishing

6. [Create an API token on PyPI](https://pypi.org/manage/account/) and set it on GitHub as the `PYPI_TOKEN` repository secret.

### Documentation

7. [Register your project on Read the Docs](https://readthedocs.org/dashboard/).

### Deploying

8. Create a stack on [Portainer], configure it to be updated via webhook, and set the webhook URL on GitHub as the `PORTAINER_HOOK_URL` repository secret.


[`pipx`]: https://pypa.github.io/pipx/
[`cookiecutter`]: https://cookiecutter.readthedocs.io/en/stable/README.html
[`poetry`]: https://python-poetry.org/docs/
[`sphinx`]: https://www.sphinx-doc.org/en/master/
[Read the Docs]: https://readthedocs.org
[`compileall`]: https://docs.python.org/3/library/compileall.html
[`pytest`]: https://docs.pytest.org/en/stable/
[GitHub Actions]: https://docs.github.com/en/actions
[Docker]: https://www.docker.com
[Portainer Business]: https://www.portainer.io
[`gh`]: https://cli.github.com
