#!/bin/bash

# Runs all python scripts in current folder.
for f in `ls *.py`; do ./$f; done | grep False

