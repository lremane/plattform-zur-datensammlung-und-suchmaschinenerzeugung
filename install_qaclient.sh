#!/bin/bash
set -e

docker run --user "$(id -u):$(id -g)" --rm -v "${PWD}:/local" openapitools/openapi-generator-cli generate \
  -i https://qanswer-core1.univ-st-etienne.fr/v2/api-docs \
  -g python \
  --package-name qaclient \
  -o /local/qaclient \
  --skip-validate-spec

pip install qaclient/

rm -r qaclient/
