#!/bin/sh

PYTHONPATH=../ python -m doctest ./test.doctest ../README.md
