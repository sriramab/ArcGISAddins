#!/bin/bash



build_addin (){
git clone --depth=50 --branch=master https://github.com/sriramab/ArcGISAddins.git /home/travis/build/sriramab/ArcGISAddinsTemp
cd /home/travis/build/sriramab/ArcGISAddinsTemp
ls /home/travis/build/sriramab/ArcGISAddinsTemp/Aggregate
python /home/travis/build/sriramab/ArcGISAddinsTemp/Aggregate/makeaddin.py
ls /home/travis/build/sriramab/ArcGISAddinsTemp/Aggregate
git remote show origin
git add -f /home/travis/build/sriramab/ArcGISAddinsTemp/Aggregate/Aggregate.esriaddin
git status
git commit -m "created addin"
git push
#git remote add origin https://sriramab:$sriramab_KEY@github.com/sriramab/ArcGISAddins.git

}


build_addin