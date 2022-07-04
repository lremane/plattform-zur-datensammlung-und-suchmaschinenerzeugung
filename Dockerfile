# Builds the QAnswer client python module
FROM openapitools/openapi-generator-cli AS client-builder
RUN java -jar /opt/openapi-generator/modules/openapi-generator-cli/target/openapi-generator-cli.jar generate \
  -i https://qanswer-core1.univ-st-etienne.fr/v2/api-docs \
  -g python \
  --package-name qaclient \
  -o /local/qaclient \
  --skip-validate-spec


FROM python:3.10.4 AS app

# Add user to run the server
RUN useradd -ms /bin/bash qauser
USER qauser
WORKDIR /home/qauser
ENV PATH="/home/qauser/.local/bin:${PATH}"

# Installs all python requirements, including the qaclient package built by the client-builder stage
COPY requirements.txt .
COPY --chown=qauser:qauser requirements.txt requirements.txt
COPY --from=client-builder  --chown=qauser:qauser /local/qaclient ./qaclient/
RUN pip install --user -r requirements.txt

# Copy source files and start flask server
COPY src/ .
CMD ["flask", "run", "--host", "0.0.0.0"]
