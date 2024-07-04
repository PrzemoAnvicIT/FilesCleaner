File Organizer Project

This project is a simple file organizer written in Python that allows users to automatically sort files in a selected folder based on their extensions. 
The application uses the Tkinter library to create a graphical user interface (GUI) and the ttkthemes library for applying themes.

Features

Select a folder to scan.

Automatically sort files based on their extensions into appropriate folders.

Display information about the sorting process in the application window.

Notification upon completion of the sorting process.

Requirements

Python 3.6+
Python libraries: ttkthemes, tkinter


Using the application

After launching the application, a GUI window will appear.
Click the "Select Folder" button to choose a folder to scan. If you don't select a folder, the default will be the Downloads folder.
Click the "Clean" button to start the file sorting process. Files will be moved to appropriate folders based on their extensions.


Extension Mapping

Files are sorted based on the following mapping of extensions to folder names:

Programs: exe, bat, msi
Images: jpg, png, gif, bmp
Documents: doc, docx, txt, pdf
Presentations: ppt, pptx
Archives: zip, bz2, gz
ISO Images: iso, img
Logs: log
Others: all other extensions

Example

If the folder being scanned contains files example.exe, picture.jpg, document.pdf, after running the application, these files will be moved to the Programs, Images, and Documents folders respectively.
