import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

class SimilaritySearch:
    def __init__(self, embeddings, image_paths):
        self.embeddings = embeddings
        self.image_paths = image_paths
    
    def find_similar_images(self, query_embedding, top_k=5):
        """Encontra imagens similares"""
        similarities = cosine_similarity(query_embedding.reshape(1, -1), 
                                       self.embeddings)
        similar_indices = np.argsort(similarities[0])[::-1][:top_k]
        
        results = []
        for idx in similar_indices:
            results.append({
                'path': self.image_paths[idx],
                'similarity': float(similarities[0][idx])
            })
        
        return results