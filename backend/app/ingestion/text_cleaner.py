import re


def clean_for_chunking(text: str) -> str:
    """
    Light cleanup applied BEFORE chunking.

    Only collapses spaces/tabs. Line breaks and paragraph breaks are kept
    intact on purpose: the splitter's separators ("\\n\\n", "\\n", ...) rely
    on them to find natural section/paragraph boundaries. Flattening
    newlines here would make every page one long blob and force the
    splitter to cut chunks mid-sentence.
    """

    text = text.replace("\r\n", "\n").replace("\r", "\n")

    # Collapse repeated spaces/tabs, but never touch newlines
    text = re.sub(r"[ \t]+", " ", text)

    # Strip trailing spaces at the end of each line
    text = re.sub(r" +\n", "\n", text)

    # Collapse 3+ blank lines down to a single paragraph break
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()


def clean_for_storage(text: str) -> str:
    """
    Final cleanup applied to each chunk AFTER splitting, right before it is
    embedded/stored. Safe to flatten all whitespace here since chunk
    boundaries have already been decided.
    """

    text = text.strip()
    text = re.sub(r"\s+", " ", text)

    return text


def is_table_of_contents(text: str) -> bool:
    """
    Detect whether a page is likely a Table of Contents.
    """

    text = text.lower()

    # Case 1 : Explicit heading
    if "table of contents" in text:
        return True

    # Case 2 : Too many dot leaders
    dot_leaders = len(re.findall(r"\.{5,}", text))

    if dot_leaders >= 3:
        return True

    return False
