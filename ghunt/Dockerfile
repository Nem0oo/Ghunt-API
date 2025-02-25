FROM python:3.11-slim
ENV PIPX_HOME=/root/.local
ENV PATH=$PIPX_HOME/bin:$PATH

RUN apt update && apt install -y pipx coreutils
RUN pipx install ghunt

WORKDIR /app
CMD ["tail", "-f", "/dev/null"] #keeps the container running