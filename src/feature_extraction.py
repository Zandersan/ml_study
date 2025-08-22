import tensorflow as tf
from tensorflow.keras.applications import VGG16, ResNet50
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.models import Model
import numpy as np

class FeatureExtractor:
    def __init__(self, model_name='resnet50'):
        self.model_name = model_name.lower()
        
        if self.model_name == 'resnet50':
            base_model = ResNet50(weights='imagenet', include_top=False, pooling='avg')
            self.model = Model(inputs=base_model.input, outputs=base_model.output)
        else:
            raise ValueError(f"Model {model_name} not supported")
    
    def extract_features(self, images):
        """Extract and normalize features from images"""
        if len(images) == 0:
            raise ValueError("No images provided for feature extraction")
        
        # Ensure input is 4D
        if images.ndim == 3:
            images = np.expand_dims(images, axis=0)
        
        # Preprocess images
        from tensorflow.keras.applications.resnet50 import preprocess_input
        images_preprocessed = preprocess_input(images.astype('float32'))
        
        # Extract features
        print(f"Extracting features from {len(images)} images...")
        features = self.model.predict(images_preprocessed, verbose=1)
        
        # NORMALIZAR OS EMBEDDINGS - ESSENTIAL!
        from sklearn.preprocessing import normalize
        features_normalized = normalize(features)
        
        print(f"Embeddings - antes normalização: min={np.min(features):.3f}, max={np.max(features):.3f}")
        print(f"Embeddings - após normalização: min={np.min(features_normalized):.3f}, max={np.max(features_normalized):.3f}")
        
        return features_normalized