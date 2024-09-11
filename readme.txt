Image to Pencil Drawing Application
===================================

This is a simple Python application using tkinter and OpenCV that allows users to convert images to pencil drawings.

Features
--------
- Select an image from your file system.
- Convert the selected image to a pencil drawing.
- Save the converted image.

Requirements
------------
- Python 3.x
- tkinter
- PIL (Pillow)
- OpenCV

Usage
Run the application.

The application window will appear with the following options:

Select Image: Click this button to choose an image from your file system.
Save Image: Click this button to convert the selected image to a pencil drawing and save it.
Use the scale to adjust the pencil effect before saving the image.

Code Overview
choose_img(): Opens a file dialog to select an image, resizes it, and displays it in the application window.
convert_img(): Converts the selected image to a pencil drawing using OpenCV, saves the converted image, and 
displays it in the application window.
The application uses tkinter for the GUI, PIL for image handling, and OpenCV for image processing.

Acknowledgements
tkinter for the GUI.
Pillow for image handling.
OpenCV for image processing.

Author
Kimathi K.