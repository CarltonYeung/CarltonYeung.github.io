#!/usr/bin/python3
from itertools import product


A = 'A'
B = 'B'
C = 'C'
D = 'D'
E = 'E'
F = 'F'
MIN_SEPARATION = 4  # established on final


def calculate_separation(sequence):
    total_separation = 0

    for lead_idx in range(len(sequence)-1):
        follower_idx = lead_idx + 1

        lead = sequence[lead_idx]
        follower = sequence[follower_idx]

        separation = MIN_SEPARATION

        if lead == A:
            if follower == B:
                separation = 7
            elif follower == C:
                separation = 8
            elif follower == D or follower == E:
                separation = 9
            elif follower == F:
                separation = 10
        elif lead == B:
            if follower == B:
                separation = 5
            elif follower == C:
                separation = 6
            elif follower == D or follower == E:
                separation = 7
            elif follower == F:
                separation = 9
        elif lead == C:
            if follower == D or follower == E:
                separation = 5
            elif follower == F:
                separation = 8
        elif lead == D:
            if follower == F:
                separation = 6
        
        total_separation += separation
    
    return total_separation


def visualize(sequence):
    ords = list(map(lambda x: ord('F')-ord(x)+1, list(sequence)))
    visual = '   '.join(map(lambda x: '*' * x, ords))
    return visual


def main():
    sequences = {
        ''.join(sequence): calculate_separation(sequence)
        for sequence in product(A+B+C+D+E+F, repeat=3)
    }

    for k in sequences.keys():
        last_two_reversed = k[1:][::-1]
        recip_k = k[0] + last_two_reversed
        if sequences[k] < sequences[recip_k]:
            print('{:<5} {:<4} {:<40}'.format(k, sequences[recip_k]-sequences[k], visualize(k)))


if __name__ == '__main__':
    main()
