In order for a program to be really useful, it needs to interact with real-world data. Images, webpages, databases are all examples of files, and we routinely create, move, manipulate, and read these files in our daily digital lives.

All kinds of files have a similar structure on a computer - they are strings of characters that encode some information. 
The specific file format (often indicated by the extension of the filename, such as .txt or .mp3) will indicate how those characters are organised. 
The characters in the file are interpreted by the various programs we use to work with them - for example, an image editing program will interpret the information of a digital photograph file and display the image. If we then edit the image in the program, we're using the program to make changes to the characters in the file.

In Python, we can read those file characters directly. The experience will seem quite different from opening a file in a desktop application. 
Opening files in Python gives us a common programmatic interface to all kinds of files without the need for a graphical user interface - which means we can automate tasks involving files with Python programs!

# Opening and Reading from Files

In order to read from a file we must first open it, and we can do so with the open function. We mist give it a path where the file resides, and we can also specify several optional parameters. We can then assign the value returned from this function to a variable. For example:

f = open('/my_path/my_file.txt','r')

The open function will return a file object - a Python object through which Python will interact with the file itself.

In this example the second parameter r specifies the mode in which we opened the file, and in our case we opened in read only mode (because we only want to read from the file, we don't want to change the file's contents). 
We did not need to specify this parameter, because by default (if we don't specify mode) open will open files in read mode.

Next, in order to access the contents of the file we can use read. f.read() creates a string object containing the text in the file. This string gets assigned to the variable named file_data.:

file_data = f.read()

Once we are finished with the file f we should close it. This will free up any system resources taken up by the file:

f.close()

It is important to remember to always close files we have opened, once we no longer need them. 
If we open a lot of files without closing them, we can run out of file handles, and we will not be able to open any new files (exactly how many files you can open before running out of handles will depend on your operating system).

To convince yourself, you can try running the following in your python interpreter:

>>> files = []
>>> for i in range(100000):
...     files.append(open('somefile.txt'))

Try editing the number in range in the for loop. At some point, for a large enough number, you will receive an error.

Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
OSError: [Errno 24] Too many open files: 'somefile.txt'
>>> i
7164

We can see that at 7164 open files the system no longer had available resources to open any new files. To avoid this, it is always a good idea to close any files you no longer need.
