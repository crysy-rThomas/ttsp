from sentence_transformers import SentenceTransformer


def embed(splits, model):
    return SentenceTransformer(model).encode(splits, convert_to_numpy=True)
