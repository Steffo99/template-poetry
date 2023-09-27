# TODO: If you're building a library, remove this file!

FROM python:3-alpine AS system
# TODO: Add whatever dependency your image may require
RUN apk add --update build-base python3-dev py-pip musl-dev
RUN pip install "poetry"

FROM system AS workdir
# TODO: Use the name of your project
WORKDIR /usr/src/{{ cookiecutter.project_name }}

FROM workdir AS dependencies
COPY pyproject.toml ./pyproject.toml
COPY poetry.lock ./poetry.lock
RUN poetry install --no-root --no-dev

FROM dependencies AS package
COPY . .
RUN poetry install

FROM package AS entrypoint
ENV PYTHONUNBUFFERED=1
ENTRYPOINT ["poetry", "run", "python", "-m"]
# TODO: Set the name of your Python module
CMD ["{{ cookiecutter.project_identifier }}"]

FROM entrypoint AS final
# TODO: Set a Docker image title
LABEL org.opencontainers.image.title="{{ cookiecutter.project_name }}"
# TODO: Set a Docker image decription
LABEL org.opencontainers.image.description="{{ cookiecutter.project_description }}"
# TODO: Set a Docker image license
LABEL org.opencontainers.image.licenses="{{ cookiecutter.project_license }}"
# TODO: Set a Docker image URL
LABEL org.opencontainers.image.url="https://github.com/{{ cookiecutter.github_owner }}/{{ cookiecutter.project_name }}/"
# TODO: Set the Docker image authors
LABEL org.opencontainers.image.authors="{{ cookiecutter.project_author_full }}"
