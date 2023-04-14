# python3
# Matīss Lakševics 4.grupa, DITF, IT
def read_input():
    return (input().rstrip(), input().rstrip())
def print_occurrences(output):
    print(' '.join(map(str, output)))
def get_occurrences(pattern, text):
    p = 10**9+7
    x = 263
    positions = []
    p_hash = hash(pattern, p, x)
    for i in range(len(text)-len(pattern)+1):
        if hash(text[i:i+len(pattern)], p, x) == p_hash:
            if text[i:i+len(pattern)] == pattern:
                positions.append(i)
    return positions
def hash(s, p, x):
    h = 0
    for c in reversed(s):
        h = (h * x + ord(c)) % p
    return h
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))