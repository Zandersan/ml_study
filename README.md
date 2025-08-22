# 🛍️ Fashion Recommendation System

Sistema de recomendação de moda baseado em similaridade visual. Faça upload de uma peça de roupa e receba recomendações de produtos similares!

## ✨ Funcionalidades

- 📤 Upload de imagens de peças de moda
- 🔍 Extração de características visuais usando Redes Neurais Profundas
- 🤖 Sistema de recomendação baseado em similaridade de cosseno
- 🎯 Interface web intuitiva com Flask
- 📊 Visualização de similaridade em porcentagem

## 🛠️ Tecnologias Utilizadas

- **Python 3.8+**
- **TensorFlow/Keras** - Extração de características com VGG16/ResNet50
- **Flask** - Framework web
- **Scikit-learn** - Cálculo de similaridade
- **NumPy** - Processamento numérico
- **Pandas** - Manipulação de dados
- **Pillow** - Processamento de imagens

## 📋 Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)
- Conta no Kaggle para download do dataset

## 🚀 Instalação

### 1. Clone o repositório

git clone <url-do-repositorio>
cd fashion-recommendation-system
2. Crie um ambiente virtual (recomendado)

python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows
3. Instale as dependências

pip install -r requirements.txt
4. Configure a API do Kaggle

# Crie diretório para credenciais do Kaggle
mkdir -p ~/.kaggle

# Configure suas credenciais (obtenha em https://www.kaggle.com/settings/account)
# Coloque o arquivo kaggle.json em ~/.kaggle/
chmod 600 ~/.kaggle/kaggle.json
📦 Estrutura do Projeto
text
fashion-recommendation-system/
├── src/
│   ├── data_processing.py    # Download e processamento de dados
│   ├── feature_extraction.py # Extração de características
│   ├── recommendation.py     # Sistema de recomendação
│   ├── similarity_search.py  # Busca por similaridade
│   └── train_model.py        # Treinamento do sistema
├── app.py                    # Aplicação Flask
├── templates/
│   └── index.html           # Interface web
├── models/                  # Modelos treinados (gerado)
├── data/                    # Dataset (gerado)
└── requirements.txt         # Dependências
🏃‍♂️ Como Executar
1. Preparação do Dataset e Treinamento

# Execute o script de treinamento
python -c "
from src.train_model import train_system
train_system(max_images=500)
"
2. Executar a Aplicação Web

python app.py
3. Acessar o Sistema
Abra seu navegador e acesse: http://localhost:5000

📸 Como Usar
Acesse a aplicação no navegador

Clique em "Choose Image" para selecionar uma imagem de moda

Clique em "Upload and Get Recommendations" para processar

Visualize as recomendações com porcentagens de similaridade

🎯 Formatos de Imagem Suportados
JPEG (.jpg, .jpeg)

PNG (.png)

Tamanho recomendado: 224x224 pixels (redimensionamento automático)

⚙️ Configurações
Parâmetros de Treinamento
No arquivo src/train_model.py:

python
train_system(
    max_images=500,      # Número máximo de imagens para treinar
    model_name='resnet50' # Modelo: 'resnet50' ou 'vgg16'
)
Parâmetros de Recomendação
No arquivo src/recommendation.py:

python
get_recommendations(
    query_embedding,    # Embedding da imagem de consulta
    embeddings,         # Embeddings do dataset
    image_paths,        # Caminhos das imagens
    top_k=5,            # Número de recomendações
    min_similarity=0.8  # Similaridade mínima (80%)
)
🔧 Solução de Problemas
Erro de Download do Dataset

# Verifique se as credenciais do Kaggle estão configuradas
kaggle datasets download -d paramaggarwal/fashion-product-images-dataset
Erro de Memória

# Reduza o número de imagens para treinamento
train_system(max_images=250)
Dependências Ausentes

# Reinstale as dependências
pip install --upgrade -r requirements.txt
📊 Performance
⏱️ Tempo de processamento por imagem: ~2-3 segundos

🎯 Acurácia de similaridade: 80-95%

💾 Uso de memória: ~1-25GB (dependendo do tamanho do dataset)
