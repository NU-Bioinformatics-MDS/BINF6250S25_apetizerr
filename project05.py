import numpy as np


def cal_score(matrix, seq1, seq2, i, j, match, mismatch, gap):
    '''Calculate score for position (i,j) in scoring matrix, also record move to trace back
    Args:
        matrix (numpy array): scoring matrix
        seq1 (str): sequence 1
        seq2 (str): sequence 2
        i (int): current row number
        j (int): current column number

    Returns:
        score in position (i,j)
        move to trace back: 0-END, 1-DIAG, 2-UP, 3-LEFT

    Pseudocode:
        Calculate scores based on upper-left, up, and left neighbors:
            diag_score = upper-left + (match or mismatch)
            up_score = up + gap
            left_score = left + gap
        score = max(0, diag_score, up_score, left_score)
        traceback = maximum direction or end

    '''

    # calculate diagonal score
    diag_score = matrix[i-1, j-1] + \
        (match if seq1[i-1] == seq2[j-1] else mismatch)

    # calculate up score
    up_score = matrix[i-1, j] + gap

    # calculate left score
    left_score = matrix[i, j-1] + gap

    # get max score
    score = max(0, diag_score, up_score, left_score)

    # get move (0-END, 1-DIAG, 2-UP, 3-LEFT)
    if score == 0:
        move = 0
    elif score == diag_score:
        move = 1
    elif score == up_score:
        move = 2
    else:
        move = 3

    return score, move


def traceback(seq1, seq2, traceback_matrix, maximum_position):
    '''Find the optimal path through scoring marix

        diagonal: match/mismatch
        up: gap in seq1
        left: gap in seq2

    Args:
        seq1 (str) : First sequence being aligned
        seq2 (str) : Second sequence being aligned
        traceback_matrix (numpy array): traceback matrix
        maximum_position (tuple): starting position to trace back from

    Returns:
        aligned_seq1 (str): e.g. GTTGAC
        aligned_seq2 (str): e.g. GTT-AC

    Pseudocode:
        while current_move != END:
            current_move = traceback_matrix[current_row][current_col]
            if current_move == DIAG:
                ...
            elif current_move == UP:
                ...
            elif current_move == LEFT:
                ...
    '''

    # get starting position
    current_row, current_col = maximum_position

    # initialize aligned sequences
    aligned_seq1 = ''
    aligned_seq2 = ''

    # initialize current move
    current_move = traceback_matrix[current_row, current_col]

    # trace back until reach the end
    while current_move != 0:
        if current_move == 1:  # DIAG
            aligned_seq1 += seq1[current_row-1]
            aligned_seq2 += seq2[current_col-1]
            current_row -= 1
            current_col -= 1
        elif current_move == 2:  # UP
            aligned_seq1 += seq1[current_row-1]
            aligned_seq2 += '-'
            current_row -= 1
        else:  # LEFT
            aligned_seq1 += '-'
            aligned_seq2 += seq2[current_col-1]
            current_col -= 1

        # update current move
        current_move = traceback_matrix[current_row, current_col]

    # reverse the aligned sequences
    aligned_seq1 = aligned_seq1[::-1]
    aligned_seq2 = aligned_seq2[::-1]

    return aligned_seq1, aligned_seq2


def smith_waterman(seq1, seq2, match=1, mismatch=-1, gap=-1):
    '''Smith-Waterman algorithm for local alignment

    Args:
        seq1 (str): input seq 1
        seq2 (str): input seq 2
        match: default = +1
        mismatch: default = -1
        gap: default = -1

    Returns:
        aligned_seq1 (str)
        aligned_seq2 (str)
        score_matrix (numpy array): scoring matrix
    '''

    # initialize scoring matrix
    score_matrix = np.zeros((len(seq1)+1, len(seq2)+1)).astype(int)

    # initialize traceback matrix
    traceback_matrix = np.zeros((len(seq1)+1, len(seq2)+1)).astype(int)

    # fill in scoring matrix
    for i in range(1, len(seq1)+1):
        for j in range(1, len(seq2)+1):
            score_matrix[i, j], traceback_matrix[i, j] = cal_score(
                score_matrix, seq1, seq2, i, j, match, mismatch, gap)

    # find maximum position in scoring matrix
    max_pos = np.unravel_index(score_matrix.argmax(), score_matrix.shape)

    # traceback
    aligned_seq1, aligned_seq2 = traceback(
        seq1, seq2, traceback_matrix, max_pos)

    return aligned_seq1, aligned_seq2, score_matrix


seq1 = 'TACTTAG'
seq2 = 'CACATTAA'

aligned_seq1, aligned_seq2, score_matrix = smith_waterman(seq1, seq2)

print(aligned_seq1)
print(aligned_seq2)
print(score_matrix)
