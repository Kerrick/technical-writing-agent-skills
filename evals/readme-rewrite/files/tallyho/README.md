# tallyho

tallyho is honestly the most powerful way to count words — it's fast and lightweight.

## Install

pip install tallyho (needs Python 3.8+)

## Usage

    tallyho --top 5 notes.txt

## Update 2026-03-02

Added the --top flag. The counter decides how to break ties (see ADR 3).

## Running the tests

Run `pytest` from the repo root. CI runs it on every push.

## Release procedure

Bump the version in pyproject.toml, tag it, and push the tag — the workflow handles the rest.

## Update 2026-05-19

The latest version is 0.4.0.
