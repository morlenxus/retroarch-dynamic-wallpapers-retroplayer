#!/bin/bash

dist_path="../dist"
if [ ! -d "${dist_path}" ]; then
	dist_path="./dist"
	if [ ! -d "${dist_path}" ]; then
		echo "Please run the script from the script dir."
		exit 2
	fi
fi

find "${dist_path}" -type f -name "*.png" | sort | while read -r png_file; do
	echo "Compressing ${png_file} ..."
	convert "${png_file}" -strip -define png:compression-level=9 PNG24:"${png_file}"
done
