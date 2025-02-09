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
    diag_score = matrix[i - 1, j - 1]
    up_score = matrix[i - 1, j]
    left_score = matrix[i - 1, j - 1]
    if seq1[i] == seq2[j]:
        diag_score = diag_score + match
        up_score = up_score + gap
        left_score = left_score + gap
    else:
        diag_score = diag_score + mismatch
        up_score = up_score + gap
        left_score = left_score + gap
    score = max(diag_score, up_score, left_score)

    return score



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
    pass


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

    S = np.zeros((len(seq1)+1, len(seq2)+1)) # makes initial matrix for score only 0
    T = np.zeros((len(seq1)+1, len(seq2)+1))

    for i in range(S.shape[0]):
        for j in range(T.shape[1]):
            S[i][j] =
            T[i][j] =
seq1 = 'TACTTAG'
seq2 = 'CACATTAA'

aligned_seq1, aligned_seq2, score_matrix = smith_waterman(seq1, seq2)

print (aligned_seq1)
print (aligned_seq2)
print (score_matrix)