# Python Image Processing
This is a simple set of utilities for image processing written in Python.

## image_renaming.py
This utility allows a variable number of images to be renamed based upon their original names, the containing directory name, or a JSON file with data about the images.
The user will be prompted for the input directory and whether they want to use the JSON data (if available), the directory name, or the original names.  In all three cases, the images will be ordered by filename, and a new leading number sequence added.
The intention of this simple utility is bulk renaming and ordering of images for websites.  Ordering is handled by the filename order in some of my other utilities.
See image_renaming_sample.json for example format.  Currently this is hardcoded to iamges.json.

#### To Do:
- [ ] Swap input/output folder options so that originals are in a new folder.
- [ ] Thumbnail creation.
- [ ] Image resizing to specified max size.


###### **All code, projects, and samples have no warranty expressed or implied. Code samples have the ability to overwrite output files. Code is meant for education and evaluation purposes only. Sample data should be used.
