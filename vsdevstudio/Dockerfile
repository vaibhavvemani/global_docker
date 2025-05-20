FROM python:3.10

RUN apt-get update && \
    apt-get install -y zsh && \
    chsh -s $(which zsh)

WORKDIR /workspace

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
