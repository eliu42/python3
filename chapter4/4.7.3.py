def f(pos1, /, pos_or_kwd, *, kwd1):
	print(pos1, pos_or_kwd, kwd1);

f('Hello ', 'World', exclamation='!')
