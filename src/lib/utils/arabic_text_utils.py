import re


def is_all_arabic(text: str) -> bool:
    """Check if all characters in the string are Arabic."""
    return bool(re.fullmatch(r"[\u0600-\u06FF\s]+", text))
