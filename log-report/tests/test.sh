#!/bin/bash

# pytest and its ctrf plugin are already baked into the environment image
# so nothing gets installed here. The verifier reads the reward from
# /logs/verifier/reward.txt and the test results from /logs/verifier/ctrf.json.

mkdir -p /logs/verifier

pytest /tests/test_outputs.py -rA --ctrf /logs/verifier/ctrf.json
status=$?

if [ $status -eq 0 ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
