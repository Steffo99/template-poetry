# `{{ cookiecutter.project_identifier }}` [![Available on PyPI](https://img.shields.io/pypi/v/{{ cookiecutter.project_identifier }})](https://pypi.org/project/{{ cookiecutter.project_identifier }}/)

{{ cookiecutter.project_description }}

\[ **[Documentation]** | **[Available on PyPI]** | [Repository] \]

<!-- Add an image or some examples here, if available! -->


[Documentation]: https://{{ cookiecutter.project_name }}.readthedocs.io/latest/
[Available on PyPI]: https://pypi.org/project/{{ cookiecutter.project_identifier }}
[Repository]: https://github.com/{{ cookiecutter.github_owner }}/{{ cookiecutter.project_name }}/



## Installation

{% if cookiecutter.project_type == "application" -%}
<details>
<summary>Recommended: Using pipx</summary>

1. Install `{{ cookiecutter.project_identifier }}`:

    ```console
    $ pipx install {{ cookiecutter.project_identifier }}
    ```

</details>

<details>
<summary>Using venv</summary>

1. Create a new venv:

    ```console
    $ python -m venv .venv
    ```

2. Activate it:
    
    ```console
    $ source venv/bin/activate
    ```

3. Install `{{ cookiecutter.project_identifier }}`:

    ```console
    $ pip install {{ cookiecutter.project_identifier }}
    ```

</details>
{%- elif cookiecutter.project_type == "library" -%}
<details>
<summary>Recommended: Using poetry</summary>

1. Add `{{ cookiecutter.project_identifier }}` to your dependencies:

    ```console
    $ poetry add {{ cookiecutter.project_identifier }}
    ```

</details>

<details>
<summary>Using pip</summary>

1. Add `{{ cookiecutter.project_identifier }}` to your `requirements.txt` file:

    ```text
    {{ cookiecutter.project_identifier }}
    ```

2. Update your dependencies:

    ```console
    $ pip install --upgrade --requirement requirements.txt
    ```

</details>

<details>
<summary>Using pipenv</summary>

1. Install `{{ cookiecutter.project_identifier }}`:

    ```console
    $ pipenv install {{ cookiecutter.project_identifier }}
    ```

</details>
{%- endif %}
