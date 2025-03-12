
from collections import Counter
import numpy as np

def bwt(text: str) -> str:
    """Function to calculate Burrows-Wheeler Transform for a given string.

    Computes the Burrows-Wheeler Transform by creating all rotations of the input
    string, sorting them lexicographically, and extracting the last column.

    Args:
        string: The input string to transform.

    Returns:
        The Burrows-Wheeler Transform of the input string.

    Examples:
        BWT('googol')
        'lo$oogg'

        BWT('banana$')
        'annb$aa'
    """
    text_list = []
    if text[-1] != "$":
        text += "$"
    # this rotates the string and puts it into a list
    for i in range(len(text)):
        text_list.append(text[i::1]+text[:i])
    text_list.sort()
    bwt_text =""
    for j in text_list:
        bwt_text += j[-1]
    return bwt_text


def suffix_array(string: str) -> list[int]:
    """Function to calculate suffix-array for a given string.

    Computes the suffix array by sorting all suffixes of the input string
    lexicographically and returning their starting positions.

    Args:
        string: The input string to process.

    Returns:
        A list of integers representing the starting positions of the
        lexicographically sorted suffixes.

    Examples:
        suffix_array('googol')
        [6, 3, 0, 5, 2, 4, 1]

        suffix_array('banana$')
        [6, 5, 3, 1, 0, 4, 2]
    """
    text_list = []
    suffix_array = []
    if string[-1] != "$":
        string += "$"
    # this rotates the string and puts it into a list
    for i in range(len(string)):
        text_list.append(string[i::1]+string[:i])
    text_list.sort()
    for j in text_list:
        string_index = len(j[j.index("$")+1:])
        suffix_array.append(string_index)

    return suffix_array
suffix_array = suffix_array(bwt("googol"))

suffix_array('banana')
print(bwt('banana'))
def BWT_from_suffix_array(
        text: str,
        suffix_positions: list[int]
) -> str:
    """Function to calculate the Burrows-Wheeler Transform from a suffix array.

    Computes the Burrows-Wheeler Transform by using the suffix array to identify
    the character that precedes each suffix in the sorted order.

    Args:
        text: The input string to transform.
        suffix_positions: The suffix array for the input string, containing the
            starting positions of all suffixes in lexicographical order.

    Returns:
        The Burrows-Wheeler Transform of the input string.

    Examples:
         BWT_from_suffix_array("banana$", [6, 5, 3, 1, 0, 4, 2])
        'annb$aa'

         BWT_from_suffix_array("googol$", [6, 3, 0, 5, 2, 4, 1])
        'lo$oogg'
    """
    bwt_text = ""
    for i in suffix_positions:
        bwt_text += text[i-1]
    return bwt_text


def cal_count(string: str) -> dict[str, int]:
    """Function to count characters lexicographically smaller than each character.

    For each character in the alphabet, calculates how many characters in the
    input string are lexicographically smaller than it.

    Args:
        string: The input string to analyze.

    Returns:
        A dictionary mapping each character to the count of characters
        lexicographically smaller than it.

    Examples:
        >>> cal_count('ATGACG')
        {'A': 0, 'C': 2, 'G': 3, 'T': 5}

        >>> cal_count('banana')
        {'a': 0, 'b': 3, 'n': 4}
    """
    result_dict = dict()
    string_list = list(string)
    string_list.sort()
    track_char = dict(Counter(string_list))
    for i in track_char:
        result_dict[i] = track_char[i]
        # sets the values to 0
        result_dict = {key: 0 for key in result_dict}
    count = 0
    for j in track_char:
        result_dict[j] = count
        count += track_char[j]
    return result_dict


def cal_occur(bwt_string: str) -> dict[str, list[int]]:
    """Function to calculate occurrences of each character up to each position.
    
    For each character and each position i, calculates how many times the
    character appears in the substring bwt_string[0:i].
    
    Args:
        bwt_string: The BWT string to analyze.
    
    Returns:
        A dictionary mapping each character to a list of occurrence counts,
        where occur[char][i] is the number of occurrences of char in
        bwt_string[0:i].
    
    Examples:
        >>> cal_occur('AG$CG')
        {'$': [0, 0, 1, 1, 1], 'A': [1, 1, 1, 1, 1], 'C': [0, 0, 0, 1, 1], 'G': [0, 1, 1, 1, 2]}
        
        >>> cal_occur('annb$aa')
        {'$': [0, 0, 0, 0, 1, 1, 1], 'a': [0, 1, 1, 1, 1, 2, 3], 'b': [0, 0, 0, 1, 1, 1, 1], 'n': [0, 0, 2, 2, 2, 2, 2]}
    """
    
    character_dict = {}
    
    for char in bwt_string:
        character_dict[char] = np.zeros(len(bwt_string))
    for pos in range(len(bwt_string)):
        curr = bwt_string[pos:pos + 1]
        for pos2 in bwt_string:
            character_dict[pos2][pos] = character_dict[pos2][pos - 1]
        character_dict[curr][pos] = character_dict[curr][pos] + 1
    return character_dict


def update_range(
        lower: int,
        upper: int,
        count: dict[str, int],
        occur: dict[str, list[int]],
        a: str) -> tuple[int, int]:
    """Function to update range given character a.

    Updates the search range during backward search in the BWT pattern matching
    algorithm when processing character a.

    Args:
        lower: The lower boundary of the current range.
        upper: The upper boundary of the current range.
        count: Dictionary mapping each character to the count of lexicographically
            smaller characters.
        occur: Dictionary mapping each character to its occurrence counts at each
            position.
        a: The character being processed in the pattern.

    Returns:
        A tuple containing the updated lower and upper boundaries of the range.

    Note:
        This function assumes occur[a][-1] = 0 for boundary conditions.
    """
    pass


def find_match(query: str, reference: str) -> list[int]:
    """Function to find exact matching by applying Burrows-Wheeler Transform.

    Searches for all occurrences of the query string within the reference string
    using the Burrows-Wheeler Transform algorithm for efficient pattern matching.

    Args:
        query: The pattern string to search for.
        reference: The text string to search within.

    Returns:
        A list of integers representing the 0-based starting positions of all
        occurrences of the query string within the reference string. Returns an
        empty list if no matches are found.

    Examples:
        >>> find_match('ana', 'banana')
        [1, 3]

        >>> find_match('xyz', 'banana')
        []
    """
    pass