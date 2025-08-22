import kagglehub
import pandas as pd
import numpy as np
from PIL import Image
import os
import shutil
import requests
import gzip

def download_dataset():
    """Download and prepare Fashion Product Images dataset from Kaggle"""
    data_dir = "data"
    img_dir = os.path.join(data_dir, "images")
    os.makedirs(img_dir, exist_ok=True)
    
    print("Downloading Fashion Product Images dataset from Kaggle...")
    
    # Download do dataset
    path = kagglehub.dataset_download("paramaggarwal/fashion-product-images-dataset")
    print(f"Dataset downloaded to: {path}")
    
    # Caminho correto para as imagens baseado na estrutura explorada
    source_images_dir = os.path.join(path, "fashion-dataset", "fashion-dataset", "images")
    
    if not os.path.exists(source_images_dir):
        # Tenta caminho alternativo
        source_images_dir = os.path.join(path, "images")
    
    if os.path.exists(source_images_dir):
        # Lista todos os arquivos de imagem
        image_files = [f for f in os.listdir(source_images_dir) 
                        if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
        
        print(f"Found {len(image_files)} images. Copying subset...")
        
        # Copia um subconjunto de imagens (500 para treinamento rápido)
        for i, filename in enumerate(image_files[:500]):
            src_path = os.path.join(source_images_dir, filename)
            dst_path = os.path.join(img_dir, filename)
            
            # Garante que não sobrescrevemos arquivos com mesmo nome
            counter = 1
            base_name, ext = os.path.splitext(filename)
            while os.path.exists(dst_path):
                dst_path = os.path.join(img_dir, f"{base_name}_{counter}{ext}")
                counter += 1
            
            shutil.copy2(src_path, dst_path)
            
            if (i + 1) % 100 == 0:
                print(f"Copied {i + 1} images...")
        
        print(f"Successfully copied {min(500, len(image_files))} images to {img_dir}")
        
        # Também copia o metadata se existir
        metadata_path = os.path.join(path, "fashion-dataset", "fashion-dataset", "styles.csv")
        if os.path.exists(metadata_path):
            shutil.copy2(metadata_path, data_dir)
            print("Metadata file copied")
        else:
            # Tenta caminho alternativo para metadata
            metadata_path = os.path.join(path, "styles.csv")
            if os.path.exists(metadata_path):
                shutil.copy2(metadata_path, data_dir)
                print("Metadata file copied")
    
    return True


def load_and_preprocess_images(img_dir, max_images=1000):
    """Load and preprocess images from directory"""
    image_paths = []
    images = []
    
    if not os.path.exists(img_dir):
        raise ValueError(f"Image directory {img_dir} does not exist")
    
    all_files = [f for f in os.listdir(img_dir) if f.endswith(('.png', '.jpg', '.jpeg'))]
    
    if not all_files:
        raise ValueError(f"No images found in {img_dir}")
    
    # Limita o número de imagens para processamento
    files_to_process = all_files[:max_images]
    
    print(f"Loading {len(files_to_process)} images...")
    
    for i, filename in enumerate(files_to_process):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            img_path = os.path.join(img_dir, filename)
            try:
                img = Image.open(img_path).convert('RGB')
                img = img.resize((224, 224))  # Resize for VGG16
                
                # Convert to array and normalize
                img_array = np.array(img) / 255.0
                
                images.append(img_array)
                image_paths.append(img_path)
                
                if (i + 1) % 100 == 0:
                    print(f"Loaded {i + 1} images...")
                    
            except Exception as e:
                print(f"Error loading image {filename}: {e}")
                continue
    
    if not images:
        raise ValueError("No images were successfully loaded")
    
    print(f"Successfully loaded {len(images)} images")
    return np.array(images), image_paths

def remove_duplicate_images(img_dir):
    """Remove imagens duplicadas baseado em hash"""
    import hashlib
    
    print("Checking for duplicate images...")
    image_hashes = {}
    duplicates = []
    
    for filename in os.listdir(img_dir):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            img_path = os.path.join(img_dir, filename)
            
            try:
                with open(img_path, 'rb') as f:
                    file_hash = hashlib.md5(f.read()).hexdigest()
                
                if file_hash in image_hashes:
                    duplicates.append(img_path)
                    print(f"Duplicate found: {filename}")
                else:
                    image_hashes[file_hash] = img_path
                    
            except Exception as e:
                print(f"Error processing {filename}: {e}")
    
    # Remove duplicatas
    for duplicate in duplicates:
        os.remove(duplicate)
        print(f"Removed duplicate: {os.path.basename(duplicate)}")
    
    print(f"Removed {len(duplicates)} duplicate images")