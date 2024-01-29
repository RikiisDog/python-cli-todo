FROM ubuntu:22.04

# Set variables
ARG PYTHON_VERSION="3.11.5"
ARG USER_NAME="vscode"
ARG USER_GROUP_NAME="python"
ARG USER_UID="1000"
ARG USER_GID="1000"
ARG PKG="sudo git curl wget unzip build-essential libffi-dev libssl-dev zlib1g-dev liblzma-dev libbz2-dev libreadline-dev libsqlite3-dev libopencv-dev tk-dev"

# Set timezone
ENV TZ=Asia/Tokyo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Update system
RUN apt-get update \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install package
RUN apt-get update && apt-get install -y ${PKG}

# Create user and group
RUN groupadd --gid ${USER_GID} ${USER_GROUP_NAME}
RUN useradd --uid ${USER_UID} --gid ${USER_GROUP_NAME} --shell /bin/bash -m ${USER_NAME}
RUN echo "%${USER_GROUP_NAME} ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/${USER_GROUP_NAME}
RUN chmod 0440 /etc/sudoers.d/${USER_GROUP_NAME}

# Copy project
COPY app/ /app
RUN chown -R ${USER_NAME}:${USER_GROUP_NAME} /app

# Switch to the user
USER ${USER_NAME}

# Install pyenv
RUN git clone https://github.com/pyenv/pyenv.git ~/.pyenv

# Install poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# aaa
ENV PYENV_ROOT="/home/${USER_NAME}/.pyenv"
ENV PATH="${PYENV_ROOT}/bin:${PYENV_ROOT}/shims:/home/${USER_NAME}/.local/bin:${PATH}"

# Install Python using pyenv
RUN echo 'eval "$(pyenv init --path)"' >> ~/.bashrc
RUN pyenv install ${PYTHON_VERSION} && pyenv global ${PYTHON_VERSION}

# Setup Poetry
WORKDIR /app