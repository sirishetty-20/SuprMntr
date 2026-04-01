from nltk.corpus import wordnet as wn


def get_similarity(word1, word2):
    syn1 = wn.synsets(word1)
    syn2 = wn.synsets(word2)
    
    if syn1 and syn2:
        return syn1[0].wup_similarity(syn2[0])
    else:
        return None


pairs = [
    ("car", "automobile"),
    ("dog", "cat"),
    ("teacher", "student"),
    ("tree", "plant"),
    ("computer", "laptop")
]


for w1, w2 in pairs:
    score = get_similarity(w1, w2)
    print(f"{w1} - {w2} → Similarity Score: {round(score,2)}")