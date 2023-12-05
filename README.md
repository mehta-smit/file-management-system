# File Management System

## Table of Contents
- [Approach](#Approach)
- [Random Writer](#Random-Writer)
- [File Management System](#File-Management-System)
- [Binary Executables](#binary-executables)

## Approach
This Demo will create following file system:
 - `~/crest`: Home Directory
 - `~/crest/data`: Will contain all the random files generated via [Random Writer](#random-writer)
 - `~/crest/last_run`: Last Run text file is used to store the last run timestamp
 - `~/crest/search_results.log`: Log file will store the stdout output of the filenames that consists of **CDS** keyword.

Basically, My Approach is simple and straight forward, Everytime we run the [Random Writer](#random-writer) will create a 100 files in a single run. Each file name has the prefix of current timestamp.  And, Last Run file will store the timestamp of last processed files. So, the next time we run the [File Management System](#File-Management-System) it will figure out the all unprocessed files based on the content of last run file and the prefix of random files that are generated in the data folder.   


## Random Writer
 ```random_file_writer.py```: Contains a Custom Context Manager class named `PseudoRandomWriter` upon executing that class it will note the current date and time and create a timestamp, that time stamp will be used as prefix of randomly generated 100 files in single run.

## File Management System
```file_management_system.py```: Contains a Custom Logger for storing all the stdout streams in `search_results.log` file. And, Context Manager named `FileManagementSystem` Which will be responsible for all the business logic like performing the OS File operations and maintaining the **last_run** file.   

## Binary Executables
Using a `pyinstaller` python library, I have managed to create a binary executables of [Random Writer](#Random-Writer) & [File Management System](#File-Management-System) using which we can easily run the python scripts. The both python scripts does not require any python package and written the code in core python.