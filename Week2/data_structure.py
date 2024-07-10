def solve(num_list, k):
    length = len(num_list)
    res = []
    for i in range(length):
        list_sliding_window = num_list[i:i+k]
        res.append(max(list_sliding_window))
    print(res)


def count_chars(string):
    d = {}
    for char in string:
        if char in d:
            d[char] += 1
        else:
            d[char] = 1
    print(d)


def word_count(file_path):
    f = open(f'{file_path}', 'r')
    data = f.read()
    data = sorted(data.lower().split())
    d = {}
    for word in data:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    return d


def initialize_distances(source, target):
    distances = [[0 for _ in range(len(target) + 1)] for _ in range(len(source) + 1)]
    for t1 in range(len(source) + 1):
        distances[t1][0] = t1
    for t2 in range(len(target) + 1):
        distances[0][t2] = t2
    return distances


def compute_costs(source, target, distances, i, j):
    if source[i - 1] == target[j - 1]:
        return distances[i - 1][j - 1]
    del_cost = distances[i - 1][j]
    in_cost = distances[i][j - 1]
    sub_cost = distances[i - 1][j - 1]
    return min(del_cost, in_cost, sub_cost) + 1


def levenshtein_distance(source, target):
    distances = initialize_distances(source, target)
    for i in range(1, len(source) + 1):
        for j in range(1, len(target) + 1):
            distances[i][j] = compute_costs(source, target, distances, i, j)
    return distances[-1][-1]


if __name__ == '__main__':
    # Bài 1:
    num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
    k = 3
    solve(num_list, k)
    # Bài 2:
    string = 'Happiness'
    count_chars(string)
    string = 'smiles'
    count_chars(string)
    # Bài 3:
    file_path = 'Week2\P1_data.txt'
    print(word_count(file_path))
    # Bài 4:
    print(levenshtein_distance('hi', 'heloo'))
