# Sistema de Assistência Virtual com PLN

Um sistema de assistência virtual completo desenvolvido em Python que utiliza Processamento de Linguagem Natural (PLN) para reconhecimento de voz e síntese de fala.

## 🚀 Funcionalidades

- **🎤 Speech-to-Text**: Conversão de fala em texto usando Google Speech Recognition
- **🔊 Text-to-Speech**: Conversão de texto em áudio usando gTTS (Google Text-to-Speech)
- **🤖 Comandos de Voz**: Acionamento por comando de voz com wake word "assistente"
- **🌐 Integrações**: 
  - Pesquisa no Wikipedia
  - Abertura do YouTube
  - Localização de farmácias próximas
  - Informações de data e hora

## 📋 Pré-requisitos

- Python 3.8 ou superior
- Microfone funcionando
- Conexão com internet (para reconhecimento de voz e síntese de fala)

## 🔧 Instalação

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/assistente-virtual.git
cd assistente-virtual

# Instale as dependências
pip install -r requirements.txt

# Para Windows, instale também:
pip install pyaudio

# Para Linux/Mac:
# sudo apt-get install python3-pyaudio
# ou
# brew install portaudio
# pip install pyaudio
```

## 🎯 Como Usar

### Execução do Sistema Principal

```bash
python main.py
```

### Comandos Disponíveis

Após iniciar o sistema, diga **"Assistente"** para ativar e em seguida um dos comandos:

- **"Assistente, que horas são?"** - Informa a hora atual
- **"Assistente, que dia é hoje?"** - Informa a data atual
- **"Assistente, abrir YouTube"** - Abre o YouTube no navegador
- **"Assistente, pesquisar [tópico] no YouTube"** - Pesquisa vídeos no YouTube
- **"Assistente, pesquisar [tópico] na Wikipedia"** - Pesquisa na Wikipedia
- **"Assistente, onde tem farmácia?"** - Abre mapa com farmácias próximas
- **"Assistente, sair"** - Encerra o assistente

## 🏗️ Estrutura do Projeto

```
assistente_virtual/
├── main.py                 # Arquivo principal
├── modules/
│   ├── speech_to_text.py   # Módulo de reconhecimento de voz
│   ├── text_to_speech.py   # Módulo de síntese de fala
│   └── commands.py         # Processador de comandos
├── requirements.txt        # Dependências do projeto
├── assistente_simples.py   # Versão simplificada
└── README.md              # Este arquivo
```

## 🔧 Módulos Principais

### Speech-to-Text (`speech_to_text.py`)
Utiliza a biblioteca `SpeechRecognition` com o Google Speech Recognition API para converter áudio em texto.

### Text-to-Speech (`text_to_speech.py`)
Usa `gTTS` (Google Text-to-Speech) para converter texto em áudio natural em português.

### Command Processor (`commands.py`)
Processa os comandos de voz e executa as ações correspondentes:
- Controle de data e hora
- Integração com Wikipedia
- Integração com YouTube
- Localização de serviços

## 🐛 Solução de Problemas

### Problemas Comuns:

1. **Microfone não detectado**: Verifique se o microfone está conectado e configurado
2. **Erro de áudio**: Instale o PyAudio corretamente para seu sistema operacional
3. **Sem conexão com internet**: Algumas funcionalidades requerem internet


## 📝 Exemplos de Uso

```python
# Uso programático
from modules.text_to_speech import TextToSpeech
from modules.speech_to_text import SpeechToText

tts = TextToSpeech()
stt = SpeechToText()

tts.speak("Olá, como posso ajudar?")
comando = stt.listen()
```

---

**Nota**: Este projeto requer conexão com internet para funcionalidades de reconhecimento de voz e síntese de fala.
