FROM python:3.10.4

RUN useradd -ms /bin/bash qauser
USER qauser
WORKDIR /home/qauser

ENV PATH="/home/qauser/.local/bin:${PATH}"

RUN pip install api-client Flask PyYAML --upgrade pip
RUN pip --version

COPY --chown=qauser:qauser . .
COPY src/ .
CMD ["flask", "run", "--host", "0.0.0.0"]
