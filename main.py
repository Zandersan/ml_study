from modules.speech_to_text import SpeechToText
from modules.text_to_speech import TextToSpeech
from modules.commands import CommandProcessor
import time
import re

class VirtualAssistant:
    def __init__(self):
        print("🚀 Inicializando assistente virtual...")
        self.stt = SpeechToText()
        self.tts = TextToSpeech()
        self.commands = CommandProcessor(self.tts)
        self.wake_word = "assistente"
        self.running = True
    
    def clean_command(self, command):
        """Remove a wake word do comando"""
        if not command:
            return ""
        
        # Remove a wake word e espaços extras
        cleaned = re.sub(r'\b' + self.wake_word + r'\b', '', command, flags=re.IGNORECASE)
        cleaned = cleaned.strip()
        return cleaned
    
    def wait_for_speech_completion(self):
        """Aguarda a fala atual terminar"""
        while self.tts.is_speaking:
            time.sleep(0.1)
    
    def start(self):
        """Inicia o assistente virtual"""
        self.tts.speak_sync("Assistente virtual iniciado. Diga assistente para ativar.")
        print("✅ Assistente virtual pronto!")
        print("🎯 Diga 'Assistente' para ativar")
        
        while self.running:
            try:
                print("\n🔊 Aguardando wake word...")
                
                # Aguardar se estiver falando
                self.wait_for_speech_completion()
                
                # Ouvir por wake word
                audio_text = self.stt.listen(timeout=4, phrase_time_limit=4)
                
                if audio_text and self.wake_word.lower() in audio_text.lower():
                    print("✅ Wake word detectada!")
                    
                    # Aguardar um pouco antes de responder
                    time.sleep(0.3)
                    self.tts.speak("Sim, como posso ajudar?")
                    
                    # Aguardar a fala terminar
                    self.wait_for_speech_completion()
                    time.sleep(0.5)
                    
                    # Ouvir comando específico
                    print("🎤 Aguardando comando...")
                    command = self.stt.listen(timeout=6, phrase_time_limit=8)
                    
                    if command:
                        # Limpar a wake word do comando
                        clean_command = self.clean_command(command)
                        print(f"📝 Comando: {clean_command}")
                        
                        if clean_command:
                            result = self.commands.process_command(clean_command)
                            if result == "exit":
                                self.running = False
                        else:
                            self.tts.speak("Desculpe, não entendi o comando.")
                    
                    time.sleep(1)
                
            except KeyboardInterrupt:
                print("\n🛑 Interrupção do usuário")
                self.tts.speak_sync("Encerrando assistente virtual. Até logo!")
                break
            except Exception as e:
                print(f"❌ Erro no loop principal: {e}")
                time.sleep(1)

if __name__ == "__main__":
    try:
        assistant = VirtualAssistant()
        assistant.start()
    except Exception as e:
        print(f"💥 Erro fatal: {e}")
    finally:
        print("👋 Assistente encerrado.")