#!/bin/bash
# Script which contains all the custom steps for setting up symlinks
# and the environment for the workspace.
#
# Note it is run with `source script.sh`

# by installing the correct version here, we don't need
# to change the content or their requirements.

python -m pip install optimum-graphcore<0.4
