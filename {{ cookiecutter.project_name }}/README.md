# `{{ cookiecutter.project_name | lower | kebab }}`

{{ cookiecutter.project_description }}


## Installation

{% if project_type == "application" %}

<details>
<summary>Using pip</summary>

1. Create a new venv:

    ```console
    $ python -m venv .venv
    ```

2. Activate it:
    
    ```console
    $ source venv/bin/activate
    ```

3. Install `{{ cookiecutter.project_name | lower | snake }}`:

    ```console
    $ pip install {{ cookiecutter.project_name | lower | snake }}
    ```

</details>

{% elif project_type == "library" %}

<details>
<summary>Using pip</summary>

1. Create a new venv:

    ```console
    $ python -m venv .venv
    ```

2. Activate it:
    
    ```console
    $ source venv/bin/activate
    ```

3. Add it to your `requirements.txt` file:

    ```text
    {{ project_name | lower | snake }}
    ```

3. Install your dependencies:

    ```console
    $ pip install -r requirements.txt
    ```

</details>

{% endif %}



## Usage

```console
$ PACKAGE-NAME
```


## Development

```console
$ poetry install
```
