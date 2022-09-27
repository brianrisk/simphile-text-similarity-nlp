from simphile import jaccard_list_similarity

list_a = ['cat', 'cat', 'dog']
list_b = ['dog', 'dog', 'cat']

print(f"Jaccard Similarity: {jaccard_list_similarity(list_a, list_b)}")
