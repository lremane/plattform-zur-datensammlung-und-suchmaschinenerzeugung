curl https://qanswer-core1.univ-st-etienne.fr/v2/api-docs > api-docs.json
java -jar openapi-generator-cli.jar generate -g python -i api-docs.json -o qa_client --package-name qa-client --skip-validate-spec
pip install qa_client/
