Projeto de Detecção e Reconhecimento Facial com TensorFlow no Google Colab
Descrição
Este projeto implementa um sistema de detecção e reconhecimento facial usando o framework TensorFlow e a biblioteca MTCNN para detecção de faces. O objetivo é detectar e reconhecer múltiplas faces simultaneamente em imagens.

O treinamento é feito usando o dataset público Celebrity Face Image Dataset, baixado automaticamente via kagglehub. O projeto é pensado para rodar em máquinas compartilhadas no Google Colab.

Funcionalidades
Detecção de múltiplas faces em imagens utilizando MTCNN.

Classificação das faces detectadas com uma rede neural convolucional (CNN) treinada no TensorFlow/Keras.

Treinamento automático com dataset de celebridades.

Teste de reconhecimento em imagens do dataset e imagens enviadas pelo usuário.

Código totalmente configurado para execução no Google Colab.

Como usar
Passo a passo
Abra este notebook no Google Colab.

Execute todas as células para:

Instalar as dependências;

Baixar e preparar o dataset;

Treinar o modelo;

Testar o reconhecimento em uma imagem do dataset.

Faça upload de suas próprias imagens para testar o reconhecimento facial em tempo real.

Teste com suas imagens
Após o treinamento, faça upload da imagem com uma ou mais faces para que o sistema realize a detecção e reconhecimento, exibindo a imagem anotada.

Estrutura do código
Download do dataset: Via kagglehub, automaticamente.

Pré-processamento: Carregamento e redimensionamento das imagens.

Detecção de faces: Com MTCNN na fase de teste.

Treinamento: CNN com Keras para classificar as faces.

Teste: Reconhecimento em imagens do dataset e imagens externas.

Dependências
Python 3

TensorFlow

MTCNN

OpenCV

Matplotlib

Kagglehub

Scikit-learn

Autor