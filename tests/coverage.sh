#!/bin/sh


PYTHONPATH=../ coverage run -m doctest test.doctest ../README.md
coverage html
