#!/bin/bash
mkdir ./new
cd touch newdocument.txt
git add -A
git commit -m "added new dir"
git push origin HEAD:master
