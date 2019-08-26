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

function contains() {
    local n=$#
    local value=${!n}
    for ((i=1;i < $#;i++)) {
        if [ "${!i}" == "${value}" ]; then
            echo "y"
            return 0
        fi
    }
    echo "n"
    return 1
}

assert_names() {
  dir_names=$(ls -d homeworks/* | sed -e 's/homeworks\///g')
  github_names=(
    "AlexandrZ1913"
    "Dalalaler"
    "daniluuuuuuuk"
    "davidovichanton"
    "diana-okrut"
    "Evgen1177"
    "Kefir331"
    "lizaveta-stasevich"
    "maximilian-sklyar"
    "OswinOswalt"
    "PierreBykov"
    "python77777121"
  )

  for n in ${dir_names}; do
    if [[ $(contains "${github_names[@]}" "$n") == "n" ]]; then
      echo "unknown Github name in homeworks/: '$n'"
      return 1
    fi
  done
}

# ---------------------------------------------------------

# check code format

assert_names || abort "HOMEWORKS USERS"

python -m black --check . || abort 'CODE COLOR'

python -m flake8 homeworks/ || abort 'CODE STYLE'

python -m pylint homeworks/ || abort 'CODE QUALITY'

# ---------------------------------------------------------
trap : 0
# ---------------------------------------------------------
