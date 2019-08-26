#!/usr/bin/env bash

# ---------------------------------------------------------
abort() {
  if test -n "$1"; then
    echo >&2 -e "\n\nFAILED: $1\n\n"
  fi
  exit 1
}

trap 'abort' 0

set -e
set -o pipefail

# ---------------------------------------------------------

# check code format

python -m black --check . || abort 'CODE COLOR'

python -m flake8 homeworks/ || abort 'CODE STYLE'

python -m pylint homeworks/ || abort 'CODE QUALITY'

# ---------------------------------------------------------
trap : 0
# ---------------------------------------------------------
