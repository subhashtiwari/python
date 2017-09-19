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

# Writing to a file

n addition to reading from a file, you can also write to a file, in which case you will change the content of the file. To do so, you must open the file in writing mode:

f = open('/my_path/my_file.txt','w')

Caution: once you open a file in writing mode, anything that it had contained previously will be deleted. If you're interested in adding to an existing file (without deleting its content) you should use append instead of write and open in append mode (using a instead of w).

If the file does not exist, python will create it for you.

We can now write to the file:

f.write("Hello World!")

And after we are done we will close it, like good citizens.

f.close()

# with

Python allows you to open a file, do operations on it, and automatically close it afterwards using with.

>>> with open('/my_path/my_file.txt','r') as f:
>>>   file_data = f.read()

In the example above we open a file, perform the operations in the block below the with statement (in this case read from the file) and afterwards Python closes it for us. No need to call f.close()!

        with open('/my_path/my_file.txt','r') as f:
            file_data = f.read()

In this code, the function open takes as input a path to a file ('/my_path/my_file.txt') on the file system and creates a file object. 
As we have already seen the 'r' means this object can be used for read mode only. 'r' is actually the default mode so it's not really strictly necessary when calling open.

The code as f assigns the file object created by the call to open to the variable name f - it's similar to saying f = open('/my_path/my_file.txt','r').

In the call f.read(), the file object f reads (all of) the content of the underlying file /my_path/my_file.txt and so f.read() creates a string object containing that text. This string gets assigned to the variable named file_data.

After a with open(filename) as f: statement (don't forget the ending colon), write an indented block to use that opened file object f however you need to. Once the indented block has been executed, the file will be closed automatically. 
This is another kind of scope - you can only access the data in the file via f inside that indented block. Once the file has been closed, you will be unable to interact with it.

After the example code has executed, the string file_data contains the whole file in a single string. You can use all the usual string methods on that string and process its contents.

# How to Read

Opening a file object is like opening a window to look into the file. To be more precise, it's a window that's just one character wide, and it always starts off at the very start of the file. 
This is very different from reading a book or a document, where you can look at multiple words or even pages at once. Think instead of the file as a long stream of characters; the file object can look at just one character at a time, in order.

In the previous code, the call to f.read() had no arguments passed to it; it defaults to reading all the remainder of the file from its current position - the whole file. If you pass .read() an integer argument, it will read up to that number of characters, output all of them, and keep the 'window' at that position ready to read on.

This makes moving around in the open file a little tricky, as there are not many landmarks to navigate by.

The \ns in the text are newline characters. The newline character marks the end of a line, and tells a program (such as a text editor) to go down to the next line. However, looking at the stream of characters in the file, \nis just another character. 

Conveniently, Python will loop over the lines of a file using the syntax for line in file. I can use this to create a list of lines in the file. Because each line still has its newline character attached, I remove this using .strip().

>>> camelot_lines = []
>>> with open("camelot.txt") as f:
...     for line in f:
...         camelot_lines.append(line.strip())
... 
>>> print(camelot_lines)
["We're the knights of the round table", "We dance whenever we're able"]            