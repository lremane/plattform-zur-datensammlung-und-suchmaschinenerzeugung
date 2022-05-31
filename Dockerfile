FROM python:3.10.4

RUN pip install --upgrade pip

RUN adduser --disabled-password --disabled-login qauser
USER qauser
WORKDIR /home/qauser

COPY requirements.txt .
COPY --chown=qauser:qauser requirements.txt requirements.txt
RUN pip install --user -r requirements.txt

ENV PATH="/home/qauser/.local/bin:${PATH}"

COPY --chown=qauser:qauser . .

COPY webserver/ .

CMD ["python", "app.py"]
