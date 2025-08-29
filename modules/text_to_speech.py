from gtts import gTTS
import tempfile
import os
import threading
from playsound import playsound

class TextToSpeech:
    def __init__(self):
        self.is_speaking = False
    
    def speak(self, text, lang='pt-br'):
        """Fala o texto de forma assíncrona usando gTTS"""
        def speak_thread():
            try:
                print(f"🎤 Falando: {text}")
                self.is_speaking = True
                
                # Criar áudio com gTTS
                tts = gTTS(text=text, lang=lang, slow=False)
                
                # Salvar em arquivo temporário
                with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as tmp_file:
                    tts.save(tmp_file.name)
                    tmp_file_path = tmp_file.name
                
                # Reproduzir áudio
                playsound(tmp_file_path)
                
                # Limpar arquivo temporário
                os.unlink(tmp_file_path)
                
                self.is_speaking = False
                
            except Exception as e:
                print(f"❌ Erro ao falar: {e}")
                self.is_speaking = False
        
        if not text.strip() or self.is_speaking:
            return
            
        thread = threading.Thread(target=speak_thread, daemon=True)
        thread.start()
    
    def speak_sync(self, text, lang='pt-br'):
        """Fala o texto de forma síncrona (bloqueante)"""
        try:
            print(f"🎤 Falando (sync): {text}")
            
            # Criar áudio com gTTS
            tts = gTTS(text=text, lang=lang, slow=False)
            
            # Salvar em arquivo temporário
            with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as tmp_file:
                tts.save(tmp_file.name)
                tmp_file_path = tmp_file.name
            
            # Reproduzir áudio
            playsound(tmp_file_path)
            
            # Limpar arquivo temporário
            os.unlink(tmp_file_path)
            
        except Exception as e:
            print(f"❌ Erro ao falar sincronamente: {e}")
    
    def wait_until_done(self):
        """Espera até terminar de falar"""
        while self.is_speaking:
            import time
            time.sleep(0.1)