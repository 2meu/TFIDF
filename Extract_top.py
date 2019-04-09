from sklearn.metrics.pairwise import cosine_similarity
from operator import itemgetter

# extract top 5

def extract_top5(captions, clean_captions, tfidf_matrix):
    checked_similarity = []

    for i in range(len(clean_captions)):

        if cosine_similarity(tfidf_matrix[-1], tfidf_matrix[i]) != 0:

            checked_similarity.append([captions[i][0], cosine_similarity(tfidf_matrix[-1], tfidf_matrix[i])])

    checked_similarity = sorted(checked_similarity, key=itemgetter(1), reverse=True)
    top_5 = checked_similarity[1:6]
    return top_5
