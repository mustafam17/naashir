import re


def parse_text_to_pairs(text: str):
    sections = re.split(r"\n\s*\n", text.strip())

    text_pairs = []

    for i in range(0, len(sections), 2):
        text_ar = sections[i].strip()
        text_en = sections[i + 1].strip()

        text_pairs.append((text_ar, text_en))

    return text_pairs
