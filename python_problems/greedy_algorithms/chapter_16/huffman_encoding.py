"""
Heapq notes:

1. pop returns the smallest item (not the largest)

heap[0] is the smallest item
heap.sort() maintains the heap invariant


"""
import heapq

"""
huffman -
map each symbol to a specific sequence of bits
use fewer bit symbols that occur more frequently and vice versa.


"""

from collections import namedtuple, Counter

Input = [
    ["a", 8.167], ["b", 1.492], ["c", 2.782], ["d", 4.253],
    ["e", 12.702], ["f", 2.228], ["g", 2.015], ["h", 6.094],
    ["i", 6.966], ["j", 0.153], ["k", 0.772], ["l", 4.025],
    ["m", 2.406], ["n", 6.749], ["o", 7.507], ["p", 1.929],
    ["q", 0.095], ["r", 5.987], ["s", 6.327], ["t", 9.056],
    ["u", 2.758], ["v", 0.978], ["w", 2.36], ["x", 0.15],
    ["y", 1.974], ["z", 0.074]
]

"""
Variant
- Given a string, calculate the frequencies of each symbol yourself.
a symbol's frequency would be the percentage value of the number of occurrences over the size of the input.
"""

char_with_frequency = namedtuple("CharWithFrequency", ('c', 'freq'))


def get_char_with_frequencies(s):
    """
    Getting character frequencies given a string.
    Create symbols list
    for character in the counter, calculate the frequency of a letter in the stirng over the
    number of occurrences.
    :param s: str
    :return: list of CharWithFrequency
    """
    ctr = Counter(s)
    symbols = []
    for char in ctr:
        char_frequency_calc = char_with_frequency(char, (ctr[char] * 100) / len(s))
        symbols.append(char_frequency_calc)
    return symbols


x = get_char_with_frequencies("aaccbbcc")
print(x)

"""
Selecting Bits for Huffman Coding
"""


class Node:
    def __init__(self, c=None, freq=None):
        self.c = c  # Characters
        self.freq = freq  # Frequency
        self.left = self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def huffman_coding(symbols):
    # Store symbols as nodes, and heapify them
    q = []
    for cwf in symbols:
        heapq.heappush(q, (cwf.freq, Node(cwf.c, cwf.freq)))

    # Bottom Up Construction of the Huffman Tree
    # Pop nodes and subtrees into pairs, and then combine them
    while len(q) >= 2:
        node1 = heapq.heappop(q)[1]
        node2 = heapq.heappop(q)[2]
        node3 = Node(c=None, freq=node1.freq + node2.freq)
        node3.left = node1
        node3.right = node2
        heapq.heappush(q, (node3.freq, node3))

    codewords = {}

    # Generate codewords
    def DFS(node, acc_code):
        # If node.c, then do this, etc.
        if not node:
            return None
        if node.c:
            codewords[node.c] = (acc_code, node.freq)
        DFS(node.left, acc_code + '0')
        DFS(node.right, acc_code + '1')

    DFS(q[0][1], '')

    # Calculate avg code length
    res = 0
    for char in codewords:
        code, freq = codewords[char]
        res += (freq / 100) * len(code)
    return res
