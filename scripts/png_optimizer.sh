#!/bin/bash

dist_path="../dist"
if [ ! -d "${dist_path}" ]; then
	dist_path="./dist"
	if [ ! -d "${dist_path}" ]; then
		echo "Please run the script from the script dir."
		exit 2
	fi
fi

find "${dist_path}" -type f -name "*.png" -size +1M | sort | while read -r png_file; do
	echo "Compressing ${png_file} ..."
	convert "${png_file}" -colors 256 -depth 8 -strip -quality 95 "${png_file}"
done