FROM python:3.10.4

RUN adduser --disabled-password --disabled-login qauser
USER qauser
ENV PATH="/home/qauser/.local/bin:${PATH}"

RUN pip3 install --upgrade pip
WORKDIR /home/qauser
COPY requirements.txt .
COPY --chown=qauser:qauser requirements.txt requirements.txt
RUN pip install --user -r requirements.txt

COPY --chown=qauser:qauser . .
COPY webserver/ .
CMD ["python", "app.py"]
