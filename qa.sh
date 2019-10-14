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
    "alexander_basovets"
    "alexander_sidorov"
    "alina_ageeva"
    "anton_davidovich"
    "artem_daniluk"
    "daniil_volk"
    "diana_okrut"
    "lizaveta_stasevich"
    "maximilian_sklyar"
    "oleg_vasilchik"
    "pavel_titov"
    "peter_bykau"
    "yauheniy_parafenovich"
  )

  for n in ${dir_names}; do
    if [[ $(contains "${github_names[@]}" "$n") == "n" ]]; then
      echo "unknown Github name in homeworks/: '$n'"
      return 1
    fi
  done
}

# ---------------------------------------------------------

rm -rf homeworks/__pycache__

# checks

assert_names || abort "HOMEWORKS USERS"

pipenv run python -m run_hw_tests

pipenv run black --check . || abort 'CODE COLOR'

# ---------------------------------------------------------
trap : 0
# ---------------------------------------------------------
