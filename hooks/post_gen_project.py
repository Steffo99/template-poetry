import pathlib
import shutil


PATHS_TO_DELETE = {
    {% if cookiecutter.project_type != "application" -%}
    "{{ cookiecutter.project_identifier }}/__main__.py",
    "Dockerfile",
    "docker-compose.yml",
    {%- endif %}
    {% if cookiecutter.project_docs != "sphinx" -%}
    "docs",
    ".readthedocs.yml"
    {%- endif %}
    {% if cookiecutter.project_tests != "pytest" -%}
    "{{ cookiecutter.project_identifier }}/tests",
    "docs/source/testing.rst",
    {%- endif %}
    {% if cookiecutter.project_tests == "none" -%}
    ".github/workflows/test.yml",
    {%- endif %}
}


for path in PATHS_TO_DELETE:
    path = pathlib.Path(path).absolute()
    try:
        if path.is_dir():
            shutil.rmtree(path)
        else:
            path.unlink()
    except FileNotFoundError:
        continue
