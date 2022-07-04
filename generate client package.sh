openapi-generator generate -g python -i https://qanswer-core1.univ-st-etienne.fr/v2/api-docs -o qa_client --package-name qaclient --skip-validate-spec \
 && pip install qa_client/
