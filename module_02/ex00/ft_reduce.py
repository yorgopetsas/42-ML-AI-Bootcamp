
def ft_reduce(function_to_apply, iterable):
	result = 0
	for i in iterable:
		if i == iterable[-1]:
			yield result
		if i == iterable[0]:
			result = i + iterable[1]
		result = function_to_apply(result, iterable[2])	
	return result