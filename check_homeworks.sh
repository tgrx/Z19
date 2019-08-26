#!/usr/bin/env bash

# ---------------------------------------------------------
abort()
{
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

# check static typing

python -m mypy \
    homeworks/ \
    lessons/ \
|| abort 'STATIC TYPING CHECK'

# ---------------------------------------------------------
trap : 0
# ---------------------------------------------------------
