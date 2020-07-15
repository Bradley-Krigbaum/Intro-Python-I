"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE


def workFile( fileLocation, mode ):
    if mode == 'r':
        with open( fileLocation, mode ) as fileToRead:
            readFile = fileToRead.read()
            print( readFile )
            input( '\n\n\npress any key to continue...\n\n\n' )
            fileToRead.close()
    elif mode == 'w':
        with open( fileLocation, 'w+' ) as fileToWrite:
            fileToWrite.write(
                "This is line 01!\nThis is line 02!\nThis is line 03!")
            fileToWrite.close()

            with open( fileLocation, 'r') as readNewFile:
                readFile = readNewFile.read()
                print( readFile )
                input( '\n\n\npress any key to quit...\n\n\n' )
                readNewFile.close()
            
    else:
        pass


workFile('foo.txt', 'r')


# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE

workFile('bar.txt', 'w')
