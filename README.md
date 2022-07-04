# Flac converter

Walks through all files and folders from the specified directory and converts flac files to specified file type, saving in the destination folder. 

This is useful when working with software or hardware that are incompatible with flac files.

Other filetypes (can be changed on the whitelist) will be copied, without alteration to the destination.

## Prerequisites
Have `pipenv` and `ffmpeg` both installed, with ffmpeg on your path.

## How to use 
Navigate to the github folder, and use `pipenv shell` to enter the python environment.

Run with `python flac_converter.py <folder-with-flac-files> <destination-folder> <new-filetype>`

The script will iterate through all folders and subfolders, and all flac files / music files will be copied to the destination-folders with flac files getting converted to the specified new-filetype
