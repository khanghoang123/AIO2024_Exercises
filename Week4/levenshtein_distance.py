import streamlit as st

def levenshtein_distance(source, target):
    distances = [[0 for _ in range(len(target)+1)]
                for _ in range(len(source)+1)]
    for i in range(len(source)+1):
        distances[i][0] = i
    for i in range(len(target)+1):
        distances[0][i] = i
    del_cost, ins_cost, sub_cost = 0, 0, 0
    for i in range(1, len(source)+1):
        for j in range(1, len(target)+1):
            if source[i-1] == target[j-1]:
                distances[i][j] = distances[i-1][j-1]
            else:
                del_cost,ins_cost,sub_cost = distances[i-1][j],distances[i][j-1],distances[i-1][j-1]
                distances[i][j] = min(del_cost, ins_cost, sub_cost) + 1
    return distances[-1][-1]


def load_vocab(file_path):
    with open(file_path, 'r') as f:
        words = sorted(set(f.read().lower().splitlines()))
    return words


vocabs = load_vocab(file_path='../Data/docs/vocab.txt')
print(vocabs)
st.title("Word Correction using Levenshtein Distance")
word = st.text_input('Word:')
if st.button('Compute'):
    levenshtein_distances = {}
    for vocab in vocabs:
        levenshtein_distances[vocab] = levenshtein_distance(word, vocab)
    sorted_levenshtein_distances = dict(
        sorted(levenshtein_distances.items(), key=lambda x: x[1]))
    correct_word = list(sorted_levenshtein_distances.keys())[0]
    st.write('Correct: ', correct_word)
col1, col2 = st.columns(2)
col1.write('Vocabulary:')
col1.write(vocabs)

col2.write('Distances:')
col2.write(sorted_levenshtein_distances)
