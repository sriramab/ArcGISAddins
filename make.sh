#!/bin/bash



build_addin (){
git clone --depth=50 --branch=master https://github.com/sriramab/ArcGISAddins.git /home/travis/build/sriramab/ArcGISAddinsTemp
cd /home/travis/build/sriramab/ArcGISAddinsTemp
git rm /home/travis/build/sriramab/ArcGISAddinsTemp/Aggregate/Aggregate.esriaddin
git commit -m "remove previous addin"
ls /home/travis/build/sriramab/ArcGISAddinsTemp/Aggregate
python /home/travis/build/sriramab/ArcGISAddinsTemp/Aggregate/makeaddin.py
ls /home/travis/build/sriramab/ArcGISAddinsTemp/Aggregate
git remote rm origin
git remote add origin https://sriramab:$sriramab_KEY@github.com/sriramab/ArcGISAddins.git

git remote show origin
git add -f /home/travis/build/sriramab/ArcGISAddinsTemp/Aggregate/Aggregate.esriaddin
git status
git commit -m "created addin [skip ci]"
git push origin HEAD:master
git checkout deploy
git rm -rf .
git checkout master -- ./Aggregate/Aggregate.esriaddin ./Aggregate/how_to.pdf
git commit -m "create new branch with only two files [skip ci]"
git push --all origin
git checkout deploy

#set -e
#COMMIT=$@
#COMMIT="${COMMIT:0:7}"
#timestamp = --date=format:short
#echo timestamp
#timestamp=$(date '+_%D')

#SUFFIX=$timestamp'_'$COMMIT'.zip'
#echo $SUFFIX
git tag -a v1.6 -m "my version - $(date)"
git push origin v1.6

#git remote add origin https://sriramab:$sriramab_KEY@github.com/sriramab/ArcGISAddins.git

}


build_addin