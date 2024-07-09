import re

def find_substring_indices(content: str, substring: str) -> tuple:
    """
    Find the indices of the first occurrence of a substring in content.

    Args:
        content (str): The content string to search within.
        substring (str): The substring to find in the content.

    Returns:
        tuple: A tuple containing start index and end index of the substring in content.
               Returns (None, None) if the substring is not found.
    """
    # Remove quotes and trim whitespace from the substring
    substring = substring.replace('"', "'").strip(' "\'')
    content = content.replace('"', "'").strip(' "\'')
    
    # Escape special characters in substring
    start_part = re.escape(substring.split()[0])
    end_part = re.escape(substring.split()[-1])

    # Create a regex pattern to match the first and last words
    pattern = f"({start_part}).*?({end_part})"

    # Find the match
    match = re.search(pattern, content)

    if match:
        start_idx = match.start()
        end_idx = match.end() - 1  # Adjust end index to point to the last character of substring
        return start_idx, end_idx

    return None, None
