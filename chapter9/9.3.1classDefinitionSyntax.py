# The simplest form of class definition looks like this:
class ClassName:
	# <statement-1>
	# <statement-N>

# Class definitions, like function definitions (def statements) must be executed before they have any effect. (You could conceivably place a class definition in a branch of an if statement, or inside a function.)

# In practice, the statements inside a class definition will usually be function defintions, but other statements are allowed, and sometimes useful — we'll come back to this later. The function defintions inside a class normally have a peculiar form of argument list, dictated by the calling conventions for methods — again, this is explained later.

# When a class definition is entered, a new namespace is created, and used at the local scope — thus, all assignments to local varaibles go into this new namespace. In particular, function definitions bind the name of the new function here.

# When a class defintion is left normally (via the end), a class object is created. This is basically a wrapper around the contents of the namespace created by the lass defintion; we'll learn omre about class objects in the next section. The original local scope (the one in effect just before the class definition was entered) is reinstated, and class object is bound here to the class name given in the class defintion header (ClassName in the example).
