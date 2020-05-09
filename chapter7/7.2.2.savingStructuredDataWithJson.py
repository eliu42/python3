#  7.2.2 Saving structured data with json

# Strings can easily be written to and read from a file. Numbers take a bit more effort, since the read() method only returns strings, which will have to be passed to a function like int(), which takes a string like '123' and returns its numeric value 123. When you want to save more complex data types like nested lists and dictionaries, parsing and serializing by hand becomes complicated.

# Rather than having users constantly writing and debugging code to sae complicated data types to files, Python allows you to use the popular data interchange format called JSON (JavaScript Ojbect Notation). The stadard module called json can take Python data hierarchies, and convert them to string representations; this process is called serializing. Reconstructing the data from the string representation is called deserializing. Between serializing and desserializing, the string representing the object may have been stored in a file or data, or sent over a network connection to some distant machine.

# Note: The JSON format is commonly used by modern applicatoins to allow for data exchange. Many programmers are already  familiar with it, which makes it a good choice for interoperability.

# If you have an object x, you can view its JSON string representation with a simple line of code:

import json
print(json.dumps([1, 'simple', 'list']))

# Another variant of the dumps() functions, called dump(), simply serializes  the object to a text file. So if f is a text file object opened for writing, we can do this:

print(json.dump(x,f))

# To decode the object again, if f is a text file object which has been opened for reading:

x = json.load(f)

# This simple serialization technique can handle lists and dictionaries, but serializing arbitary class instances in JSON requires a bit of extra effort. The reference for the json module contains an explanation of this
