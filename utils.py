def is_palindrome(s: str) -> bool:
	"""Return whether ``s`` reads the same forwards and backwards.

	Letter case and non-alphanumeric characters are ignored.
	"""
	normalized = "".join(character.lower() for character in s if character.isalnum())
	return normalized == normalized[::-1]


def count_word(text: str) -> int:
	"""Return the number of whitespace-separated words in ``text``."""
	return len(text.split())


def celsius_to_fahrenheit(c: float) -> float:
	"""Convert a temperature in degrees Celsius to degrees Fahrenheit."""
	return (c * 9 / 5) + 32

