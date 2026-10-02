def is_palindrome(s):
	"""Check whether a string reads the same forwards and backwards.

	Args:
		s: The string to check.

	Returns:
		True if s is a palindrome, otherwise False.
	"""
	return s == s[::-1]


def count_words(text):
	"""Count the words in a piece of text.

	Args:
		text: The text whose words will be counted.

	Returns:
		The number of words in text.
	"""
	return len(text.split())


def celsius_to_fahrenheit(c):
	"""Convert a temperature from Celsius to Fahrenheit.

	Args:
		c: The temperature in degrees Celsius.

	Returns:
		The temperature in degrees Fahrenheit.
	"""
	return (c * 9 / 5) + 32
