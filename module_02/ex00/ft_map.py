
def ft_map(function_to_apply, iterable):
	# check_input(function_to_apply, iterable)
	for i in iterable:
		yield function_to_apply(i)
