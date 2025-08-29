# 🧪 Gerador de Testes Unitários com LangChain e Azure ChatGPT

Este projeto é uma automação simples para geração de testes unitários utilizando LangChain e Azure OpenAI ChatGPT.

## 📋 Pré-requisitos

- Python 3.8+
- Conta no Azure OpenAI Service
- Chave de API do Azure OpenAI

## ⚙️ Configuração

1. Clone o repositório:
```bash
git clone <url-do-repositorio>
cd gerador-testes-unitarios
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Configure as variáveis de ambiente:
```bash
# Crie um arquivo .env com as seguintes variáveis:
AZURE_OPENAI_API_KEY=sua_chave_aqui
AZURE_OPENAI_ENDPOINT=seu_endpoint_aqui
AZURE_OPENAI_API_VERSION=2023-05-15
AZURE_OPENAI_DEPLOYMENT_NAME=nome_do_seu_deployment
```

## 🚀 Como Usar

Execute o script principal:

```bash
python gerador_testes.py
```

O script irá:
1. Conectar-se ao Azure ChatGPT
2. Analisar o código Python
3. Gerar testes unitários automaticamente
4. Salvar os testes em um arquivo

## 📁 Estrutura do Projeto

```
├── gerador_testes.py    # Script principal
├── requirements.txt     # Dependências do projeto
├── .env.example        # Exemplo de variáveis de ambiente
└── README.md           # Este arquivo
```

## 📝 Exemplo de Saída

O script gera testes unitários no formato:

```python
import unittest

class TestFuncoesMatematicas(unittest.TestCase):
    
    def test_soma_positivos(self):
        self.assertEqual(soma(2, 3), 5)
    
    def test_soma_negativos(self):
        self.assertEqual(soma(-1, -1), -2)
    
    def test_subtracao_positivos(self):
        self.assertEqual(subtracao(5, 3), 2)
    
    def test_subtracao_negativos(self):
        self.assertEqual(subtracao(-1, -1), 0)

if __name__ == '__main__':
    unittest.main()
```

## 🧪 Como Executar os Testes

```bash
python -m unittest testes_gerados.py
```

## 📊 Benefícios

- ✅ Automatiza a criação de testes unitários
- ✅ Mantém a consistência dos testes
- ✅ Economiza tempo no desenvolvimento
- ✅ Integra-se com o ecossistema Azure OpenAI