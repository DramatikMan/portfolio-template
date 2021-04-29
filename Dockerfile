FROM python:slim AS base
SHELL ["/bin/bash", "-c"]
WORKDIR /project
COPY Pipfile scripts ./
ARG build_env
RUN ./pipenv_install.sh

FROM base AS development
COPY . .
CMD ./devserver.sh

FROM base AS production
COPY core_app core_app
COPY config.py .
CMD ./deploy.sh
