import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import normalize

def get_recommendations(query_embedding, embeddings, image_paths, top_k=5, min_similarity=0.8):
    """
    Encontra as imagens mais similares com similaridade mínima
    
    Args:
        query_embedding: Embedding da imagem de consulta
        embeddings: Array com todos os embeddings do dataset
        image_paths: Lista com caminhos das imagens correspondentes
        top_k: Número máximo de recomendações
        min_similarity: Similaridade mínima para considerar (0.8 = 80%)
    
    Returns:
        Lista de tuplas (caminho_da_imagem, similaridade)
    """
    if embeddings is None or len(embeddings) == 0:
        raise ValueError("No embeddings available for comparison")
    
    # Garantir shapes consistentes
    if query_embedding.ndim == 1:
        query_embedding = query_embedding.reshape(1, -1)
    
    # Normalizar embeddings para melhor performance
    query_norm = normalize(query_embedding)
    embeddings_norm = normalize(embeddings)
    
    # Calcular similaridades
    similarities = cosine_similarity(query_norm, embeddings_norm)
    similarities = similarities.flatten()
    
    # DEBUG: Verificar a distribuição
    print(f"Distribuição de similaridades:")
    print(f"  >= 0.9: {np.sum(similarities >= 0.9)} imagens")
    print(f"  >= 0.8: {np.sum(similarities >= 0.8)} imagens") 
    print(f"  >= 0.7: {np.sum(similarities >= 0.7)} imagens")
    print(f"  >= 0.6: {np.sum(similarities >= 0.6)} imagens")
    
    # Obter índices ordenados por similaridade (maior primeiro)
    sorted_indices = np.argsort(similarities)[::-1]
    
    # Coletar recomendações que atendem à similaridade mínima
    recommendations = []
    seen_paths = set()
    
    for idx in sorted_indices:
        similarity = similarities[idx]
        image_path = image_paths[idx]
        
        # Parar se a similaridade cair abaixo do mínimo
        if similarity < min_similarity and len(recommendations) > 0:
            break
            
        # Apenas adicionar se atender à similaridade mínima
        if similarity >= min_similarity:
            # Pular duplicatas
            if image_path not in seen_paths:
                seen_paths.add(image_path)
                recommendations.append((image_path, similarity))
                
                # Parar se atingir o número máximo
                if len(recommendations) >= top_k:
                    break
    
    # Se não encontrou recomendações com similaridade alta, retornar as melhores disponíveis
    if not recommendations:
        print("Nenhuma recomendação com similaridade >= 80%. Retornando as melhores disponíveis.")
        for idx in sorted_indices[:top_k]:
            similarity = similarities[idx]
            image_path = image_paths[idx]
            if image_path not in seen_paths:
                recommendations.append((image_path, similarity))
                if len(recommendations) >= top_k:
                    break
    
    return recommendations