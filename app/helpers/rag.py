import numpy as np
from helpers.embeding import embed
from services.split_service import SplitServiceImpl
from sklearn.metrics.pairwise import cosine_similarity


def rag(query):
    split_service = SplitServiceImpl()

    splits = split_service.get_all_splits()
    if not splits:
        return []
    topic_vectors = []
    content_vectors = []
    for split in splits:
        topic_vectors.append(split.topic_vector)
        content_vectors.append(split.content_vector)
    vectors = topic_vectors + content_vectors

    query_vector = embed(query, "Snowflake/snowflake-arctic-embed-s").flatten().reshape(1, -1)
    print("Question", query)
    similarity_threshold = 0.75

    similarities = cosine_similarity(vectors, query_vector)

    # Find the most similar vector
    most_similar_index = np.argmax(similarities)

    # Assuming topic_vectors and content_vectors are of equal length
    split_index = (
        most_similar_index
        if most_similar_index < len(splits)
        else most_similar_index - len(splits)
    )

    # Find the split that corresponds to the most similar vector
    best_split = splits[split_index]
    print("Similarity scoore: ", similarities[most_similar_index])
    if similarities[most_similar_index] < similarity_threshold:
        return []
    else:
        return best_split


    
