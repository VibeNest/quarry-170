
_model = None

def get_model():
    from sentence_transformers import SentenceTransformer

    global _model

    if _model is None:
        _model = SentenceTransformer(
            "all-MiniLM-L6-v2"    #produces 384 Dimensional Embeddings
        )

    return _model

def generate_embedding(text):

    model = get_model()

    return model.encode(text).tolist()