import speech_recognition as sr
import warnings
warnings.filterwarnings("ignore")

class SpeechToText:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.setup_microphone()
    
    def setup_microphone(self):
        """Configura o microfone e ajusta para ruído ambiente"""
        try:
            print("🔧 Ajustando para ruído ambiente...")
            with self.microphone as source:
                self.recognizer.adjust_for_ambient_noise(source, duration=2)  # Aumentei para 2 segundos
            print("✅ Microfone configurado!")
        except Exception as e:
            print(f"❌ Erro ao configurar microfone: {e}")
    
    def listen(self, timeout=5, phrase_time_limit=8):  # Aumentei os timeouts
        """Ouve e converte áudio em texto"""
        try:
            with self.microphone as source:
                print("👂 Ouvindo...")
                self.recognizer.pause_threshold = 1.0  # Aumenta a pausa para detecção
                audio = self.recognizer.listen(
                    source, 
                    timeout=timeout, 
                    phrase_time_limit=phrase_time_limit
                )
            
            print("🔄 Processando áudio...")
            text = self.recognizer.recognize_google(audio, language='pt-BR')
            print(f"💬 Você disse: {text}")
            return text.lower()
            
        except sr.WaitTimeoutError:
            # print("⏰ Tempo de espera excedido.")
            return None
        except sr.UnknownValueError:
            print("❓ Não foi possível entender o áudio.")
            return None
        except sr.RequestError as e:
            print(f"🌐 Erro no serviço de reconhecimento: {e}")
            return None
        except Exception as e:
            print(f"⚠️ Erro inesperado no STT: {e}")
            return None