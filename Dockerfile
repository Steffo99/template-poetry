FROM python AS metadata
LABEL maintainer="Your Name <you@example.org>"

FROM metadata AS workdir
WORKDIR /usr/src/PACKAGE_NAME

FROM workdir AS poetry
RUN pip install "poetry"

FROM poetry AS dependencies
COPY pyproject.toml ./pyproject.toml
COPY poetry.lock ./poetry.lock
RUN poetry install --no-root --no-dev

FROM dependencies AS package
COPY . .
RUN poetry install

FROM package AS environment
ENV PYTHONUNBUFFERED=1

FROM environment AS entrypoint
ENTRYPOINT ["poetry", "run", "python", "-m", "PACKAGE_NAME"]
CMD []
