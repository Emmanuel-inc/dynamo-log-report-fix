#!/bin/bash

# pytest and pytest-json-ctrf are baked into the environment image
# (environment/Dockerfile). Report results via /logs/verifier/reward.txt
# and /logs/verifier/ctrf.json as required by the Harbor verifier contract.

mkdir -p /logs/verifier

pytest /tests/test_outputs.py -rA --ctrf /logs/verifier/ctrf.json
status=$?

if [ $status -eq 0 ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
