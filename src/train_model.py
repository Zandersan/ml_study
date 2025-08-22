import numpy as np
import pickle
import os
from .data_processing import download_dataset, load_and_preprocess_images,remove_duplicate_images
from .feature_extraction import FeatureExtractor

def train_system(max_images=500, model_name='resnet50'):
    """Treina o sistema de recomendação com embeddings normalizados"""
    print("Carregando imagens...")
    images, image_paths = load_and_preprocess_images("data/images", max_images=max_images)
    
    print("Extraindo características...")
    extractor = FeatureExtractor(model_name=model_name)
    embeddings = extractor.extract_features(images)  # Já retorna normalizado
    
    # Salvar
    np.save("models/embeddings.npy", embeddings)
    with open("models/image_paths.pkl", "wb") as f:
        pickle.dump(image_paths, f)
    
    return embeddings, image_paths