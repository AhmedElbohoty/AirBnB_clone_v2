#!/usr/bin/env bash

find . -type f -name "*.py" | while read -r file_path; do
    /Library/Frameworks/Python.framework/Versions/3.12/bin/pycodestyle "$file_path"
done