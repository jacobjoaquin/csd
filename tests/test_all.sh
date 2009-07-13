#!/bin/bash

# Runs all python scripts in current folder.
for f in `ls *.py`; do python $f; done | grep \(False

