FROM python:3.10.4

RUN useradd -ms /bin/bash qauser
USER qauser
WORKDIR /home/qauser

ENV PATH="/home/qauser/.local/bin:${PATH}"

RUN pip install api-client --upgrade pip
RUN pip --version

COPY requirements.txt .
COPY --chown=qauser:qauser requirements.txt requirements.txt
RUN pip install --user -r requirements.txt

COPY --chown=qauser:qauser . .
COPY src/ .
CMD ["python", "app.py"]
