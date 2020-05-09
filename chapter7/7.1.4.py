# 7.1.4 Old string formatting

# The % operator can also be used for string formatting. It interprets the left argument much like a sprintf()-style format string to be applied to the right argument, and returns the string resulting from this formatting operation. For example:

import math
print('The value of pi is approximaately %5.3f.' % math.pi)
