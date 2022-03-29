# files-data-pandas
 read and write files txt, CSV, using "with open()" and pandas package and operatinge on data from files

>>>with open("./file.txt", mode="r") as x:
>>>		list_of_names = names.readlines
or 
>>>import pandas
>>>with open("./birthdays.csv", mode="r") as days:
>>>    df = pandas.read_csv(days)	#reading csv
>>>    data = df.to_dict()			#saving data frame as a dict

>>>a = [1, 7, 2] #pandas Series data
>>>myvar = pd.Series(a)

>>>mydataset = {
>>>  			'cars': ["BMW", "Volvo", "Ford"],
>>>		  		'passings': [3, 7, 2]
>>>				}
>>>
>>>myvar = pandas.DataFrame(mydataset)

„r” – read
„w” – write
„a” – append
„r+” – read and write data to the file
„w+” – write and read data from the file
„a+” – appending and reading data from the file 

close()	Closes the file
detach()	Returns the separated raw stream from the buffer
fileno()	Returns a number that represents the stream, from the operating system's perspective
flush()	Flushes the internal buffer
isatty()	Returns whether the file stream is interactive or not
read()	Returns the file content
readable()	Returns whether the file stream can be read or not
readline()	Returns one line from the file
readlines()	Returns a list of lines from the file
seek()	Change the file position
seekable()	Returns whether the file allows us to change the file position
tell()	Returns the current file position
truncate()	Resizes the file to a specified size
writable()	Returns whether the file can be written to or not
write()	Writes the specified string to the file
writelines()	Writes a list of strings to the file
