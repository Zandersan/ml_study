from flask import Flask, render_template, request, jsonify, send_from_directory
import numpy as np
import pandas as pd
import pickle
from PIL import Image
import io
import os
from src.feature_extraction import FeatureExtractor
from src.recommendation import get_recommendations
from tensorflow.keras.applications.vgg16 import preprocess_input

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

def load_metadata():
    try:
        metadata = pd.read_csv("data/styles.csv")
        return metadata
    except:
        return None

# Load precomputed data
def load_model_data():
    try:
        embeddings = np.load("models/embeddings.npy")
        with open("models/image_paths.pkl", "rb") as f:
            image_paths = pickle.load(f)
        return embeddings, image_paths
    except FileNotFoundError:
        return None, None

embeddings, image_paths = load_model_data()
extractor = FeatureExtractor(model_name='resnet50')

# Rota para servir arquivos estáticos da pasta data
@app.route('/images/<path:filename>')
def serve_images(filename):
    return send_from_directory('data/images', filename)

@app.route('/data/<path:filename>')
def serve_static(filename):
    return send_from_directory('data', filename)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file uploaded'}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        if file:
            # Processar imagem corretamente
            from tensorflow.keras.applications.resnet50 import preprocess_input
            img = Image.open(io.BytesIO(file.read())).convert('RGB')
            img_array = np.array(img)
            img_array = preprocess_input(img_array.astype('float32'))
            img_array = np.expand_dims(img_array, axis=0)
            
        # Extrair features
        query_embedding = extractor.extract_features(img_array)
        print(f"Shape do embedding de query: {query_embedding.shape}")
        print(f"Valores do embedding: min={np.min(query_embedding)}, max={np.max(query_embedding)}")
        
        # Calcular similaridade média com o dataset para debug
        if embeddings is not None:
            from sklearn.metrics.pairwise import cosine_similarity
            from sklearn.preprocessing import normalize
            query_norm = normalize(query_embedding.reshape(1, -1))
            embeddings_norm = normalize(embeddings)
            all_similarities = cosine_similarity(query_norm, embeddings_norm).flatten()
            print(f"Similaridade média: {np.mean(all_similarities):.3f}")
            print(f"Similaridade máxima: {np.max(all_similarities):.3f}")
            print(f"Similaridade mínima: {np.min(all_similarities):.3f}")
        
        # DEBUG: Verificar o cálculo de similaridade
        from sklearn.metrics.pairwise import cosine_similarity
        from sklearn.preprocessing import normalize
        
        # Calcular similaridades manualmente para debug
        query_norm = normalize(query_embedding.reshape(1, -1))
        embeddings_norm = normalize(embeddings)
        manual_similarities = cosine_similarity(query_norm, embeddings_norm).flatten()
        
        print(f"DEBUG - Similaridades calculadas:")
        print(f"Média: {np.mean(manual_similarities):.3f}")
        print(f"Máxima: {np.max(manual_similarities):.3f}")
        print(f"Mínima: {np.min(manual_similarities):.3f}")
        print(f"Top 5: {np.sort(manual_similarities)[-5:][::-1]}")
        
        # Get recommendations
        recommendations = get_recommendations(
            query_embedding, embeddings, image_paths, 
            top_k=5, min_similarity=0.8
        )
        
        
        print(f"Encontradas {len(recommendations)} recomendações")
        for path, sim in recommendations:
            print(f"  {os.path.basename(path)}: {sim:.3f}")
            
            # Convert recommendations to web paths - CORRIGIDO
            web_recommendations = []
            for path, similarity in recommendations:
                # Extrai apenas o nome do arquivo
                filename = os.path.basename(path)
                # Cria o caminho web correto
                web_path = f"images/{filename}"
                
                web_recommendations.append({
                    'path': web_path,
                    'similarity': float(similarity)
                })
            
            return jsonify({'recommendations': web_recommendations})
    
    except Exception as e:
        print(f"Error processing image: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)