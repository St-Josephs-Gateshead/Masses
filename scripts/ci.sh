#!/usr/bin/env bash

# Exit immediately if a command exits with a non-zero status.
set -e

# Treat unset variables as an error.
set -u

# Exit on error in pipeline (e.g. cmd1 | cmd2)
set -o pipefail

JOBS=4

monitor() {
    while true
    do
        free -h
        w
        sleep 30
    done &
}

init() {
    git config --global --add safe.directory "$GITHUB_WORKSPACE"
    bash scripts/post-xxx-sample.txt # gitinfo2 script
}

configure() {
    python scripts/configure.py

    echo "Generated makefile:"
    cat makefile
}

build () {
    make -j $JOBS || make -j $JOBS
    python scripts/package.py
}

update () {
    python scripts/update_release_page.py
    git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
    git config user.name "github-actions[bot]"
    git add releases.md
    git commit -m "[skip ci] update: releases"
    git push
}

monitor
init
configure
build
update



