#!/bin/bash

#
# This script generates the latest version of a python QAnswer client from swagger and installs it via pip.
#

set -e # Exit on errors

# Generate client using openapi-generator-cli from swagger
docker run --user "$(id -u):$(id -g)" --rm -v "${PWD}:/local" openapitools/openapi-generator-cli generate \
  -i https://qanswer-core1.univ-st-etienne.fr/v2/api-docs \
  -g python \
  --package-name qaclient \
  -o /local/qaclient \
  --skip-validate-spec

pip install qaclient/ # Install client to pip

rm -r qaclient/ # Remove client files
