#!/bin/bash



build_addin (){
git clone --depth=50 --branch=master https://github.com/sriramab/ArcGISAddins.git /home/travis/build/sriramab/ArcGISAddinsTemp
cd /home/travis/build/sriramab/ArcGISAddinsTemp
ls ./Aggregate
python ./Aggregate/makeaddin.py
git status
#git remote add origin https://sriramab:$sriramab_KEY@github.com/sriramab/ArcGISAddins.git

}


build_addin