import re
import html


def sanitize_text(text: str) -> str:
    """
    Clean AI-generated text before displaying/exporting it.
    """

    if not text:
        return ""

    replacements = {
        "\u2018": "'",
        "\u2019": "'",
        "\u201c": '"',
        "\u201d": '"',
        "\u2013": "-",
        "\u2014": "-",
        "\u2026": "...",
        "\u00a0": " ",
        "\ufeff": ""
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    text = re.sub(
        r"[ \t]+",
        " ",
        text
    )

    text = re.sub(
        r"\n{3,}",
        "\n\n",
        text
    )

    return text.strip()


def escape_html(text: str) -> str:
    """
    Safely escape text before placing it into HTML.
    """

    return html.escape(
        sanitize_text(text)
    )


def terms_to_list(terms: str):
    """
    Convert semicolon-separated terms into a Python list.

    Example:
        "Payment within 30 days; Confidentiality; Termination"

    becomes:

        [
            "Payment within 30 days",
            "Confidentiality",
            "Termination"
        ]
    """

    if not terms:
        return []

    result = []

    for item in terms.split(";"):

        cleaned = sanitize_text(item)

        if cleaned:
            result.append(cleaned)

    return result