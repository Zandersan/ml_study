# exploration.py
import os
import kagglehub

def explore_dataset_structure():
    """Explora a estrutura real do dataset"""
    path = kagglehub.dataset_download("paramaggarwal/fashion-product-images-dataset")
    print(f"Dataset path: {path}")
    
    # Lista todos os arquivos e pastas
    print("\nEstrutura do dataset:")
    for root, dirs, files in os.walk(path):
        level = root.replace(path, '').count(os.sep)
        indent = ' ' * 2 * level
        print(f"{indent}{os.path.basename(root)}/")
        subindent = ' ' * 2 * (level + 1)
        for file in files[:10]:  # Mostra apenas os primeiros 10 arquivos
            print(f"{subindent}{file}")
        if len(files) > 10:
            print(f"{subindent}... and {len(files) - 10} more files")
    
    # Verifica especificamente por imagens
    print("\nProcurando por imagens...")
    image_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.bmp')
    image_count = 0
    
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.lower().endswith(image_extensions):
                image_count += 1
                if image_count <= 5:  # Mostra os primeiros 5 caminhos
                    print(f"Imagem encontrada: {os.path.join(root, file)}")
    
    print(f"\nTotal de imagens encontradas: {image_count}")

if __name__ == "__main__":
    explore_dataset_structure()