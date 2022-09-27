from simphile import jaccard_similarity, euclidian_similarity, compression_similarity

text_a = "I love dogs"
text_b = "I love cats"

print(f"Jaccard Similarity: {jaccard_similarity(text_a, text_b)}")
print(f"Euclidian Similarity: {euclidian_similarity(text_a, text_b)}")
print(f"Compression Similarity: {compression_similarity(text_a, text_b)}")
