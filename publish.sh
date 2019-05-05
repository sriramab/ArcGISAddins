#!/bin/bash

commit_io_website_files() {

	git config --global user.email "travis@travis-ci.org"
	git config --global user.name "Travis CI"
	git config --global push.default simple		
	git clone --depth=50 --branch=master https://github.com/sriramab/ArcGISAddins.git /home/travis/build/sriramab/ArcGISAddins	
	git clone --depth=50 --branch=master https://github.com/sriramab/ArcGISAddins_release.git /home/travis/build/sriramab/ArcGISAddins_release
	cp /home/travis/build/sriramab/ArcGISAddins/Aggregate/Aggregate.esriaddin /home/travis/build/sriramab/ArcGISAddins_release/Aggregate.esriaddin
	cp /home/travis/build/sriramab/ArcGISAddins/Aggregate/how_to.pdf /home/travis/build/sriramab/ArcGISAddins_release/how_to.pdf
	cd /home/travis/build/sriramab/ArcGISAddins_release
	git add -A		
	git commit -m "Trigger to generate ArcGISAddins_release - $(date)"
	git push origin HEAD:master
}

commit_io_website_files
