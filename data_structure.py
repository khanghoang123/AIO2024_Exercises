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


def edit_distance(source, target):
    distances = [[0 for j in range(len(target)+1)]
                 for i in range(len(source)+1)]

    for t1 in range(len(source)+1):
        distances[t1][0] = t1
    for t2 in range(len(target)+1):
        distances[0][t2] = t2

    del_cost = 0
    in_cost = 0
    sub_cost = 0

    for i in range(1, len(source)+1):
        for j in range(1, len(target)+1):
            if source[i-1] == target[j-1]:
                distances[i][j] = distances[i-1][j-1]
            else:
                del_cost = distances[i-1][j]
                in_cost = distances[i][j-1]
                sub_cost = distances[i-1][j-1]

                if (del_cost <= in_cost) and (del_cost <= sub_cost):
                    distances[i][j] = del_cost+1
                elif (in_cost <= del_cost) and (in_cost <= sub_cost):
                    distances[i][j] = in_cost+1
                else:
                    distances[i][j] = sub_cost+1
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
    file_path = 'P1_data.txt'
    print(word_count('P1_data.txt'))
    # Bài 4:
    print(edit_distance('hi', 'heloo'))
