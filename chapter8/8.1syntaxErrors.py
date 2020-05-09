# Syntax errors, also known as parsing errors, are perhaps the most common kind of complaint you get while you are still learning Python:
while True print('Hello world')

# The parse repeats the offending line and displays a little 'arrow' poitning at the earliest point in the line where the error was detected. The error is caused by (or at least detcted at) the token preceding the arrow: in the example, the error is detected at the function print(), since a colon (':') is missing before it. File name and line number are printed so you know where to look in case the input came from a script.

