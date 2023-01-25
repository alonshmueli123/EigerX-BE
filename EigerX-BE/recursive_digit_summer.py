def summer(n):
	"""
	This function receives a number, and returns the sum of the of its digits.
	"""
	if n < 10:
		return n
	return n % 10 + summer(int(n / 10))


def summer_tail_call(n, temp_sum=0):
	"""
	This function receives a number and a number that defaults to 0, and returns the sum of the of its digits.
	Because I wanted to implemant it as a tail call used anoter parameter to store the temporary digit sum.
	"""

	if n < 10:
		return n + temp_sum

	temp_sum += n % 10
	return summer_tail_call(int(n / 10), temp_sum)


if __name__ == '__main__':
	print(summer(6748))



