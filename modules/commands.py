import webbrowser
import wikipedia
import pywhatkit
import requests
import geocoder
import os
from datetime import datetime

class CommandProcessor:
    def __init__(self, tts):
        self.tts = tts
        wikipedia.set_lang("pt")
    
    def process_command(self, command):
        """Processa o comando de voz"""
        if not command:
            self.tts.speak("Não entendi o comando.")
            return None
            
        command = command.lower().strip()
        print(f"🔧 Processando comando: {command}")
        
        try:
            # HORA
            if any(palavra in command for palavra in ['hora', 'horas', 'relógio', 'que horas']):
                self.tell_time()
                return None
            
            # DATA
            elif any(palavra in command for palavra in ['data', 'dia', 'calendário', 'que dia']):
                self.tell_date()
                return None
            
            # YOUTUBE
            elif any(palavra in command for palavra in ['youtube', 'vídeo', 'video']):
                if 'pesquisar' in command or 'buscar' in command or 'procure' in command:
                    self.search_youtube(command)
                else:
                    self.open_youtube()
                return None
            
            # WIKIPEDIA
            elif any(palavra in command for palavra in ['wikipedia', 'pesquisar', 'buscar', 'procure']):
                self.search_wikipedia(command)
                return None
            
            # FARMÁCIA
            elif any(palavra in command for palavra in ['farmácia', 'farmacia', 'drogaria', 'remédio', 'farmácias']):
                self.find_pharmacy()
                return None
            
            # SAIR
            elif any(palavra in command for palavra in ['sair', 'parar', 'encerrar', 'fechar']):
                self.tts.speak("Encerrando assistente. Até logo!")
                return "exit"
            
            # AGRADECIMENTO
            elif any(palavra in command for palavra in ['obrigado', 'valeu', 'obrigada', 'agradeço']):
                self.tts.speak("De nada! Estou aqui para ajudar.")
                return None
            
            else:
                self.tts.speak("Desculpe, não reconheci este comando. Tente dizer hora, data, YouTube ou Wikipedia.")
                return None
                
        except Exception as e:
            print(f"❌ Erro ao processar comando: {e}")
            self.tts.speak("Ocorreu um erro ao processar seu comando.")
            return None
    
    def search_wikipedia(self, command):
        """Pesquisa no Wikipedia"""
        try:
            # Extrair termo de pesquisa
            search_term = command
            remove_words = ['pesquisar', 'wikipedia', 'sobre', 'buscar', 'procure', 'no', 'na', 'em']
            for word in remove_words:
                search_term = search_term.replace(word, '')
            search_term = search_term.strip()
            
            if not search_term:
                self.tts.speak("O que você gostaria de pesquisar na Wikipedia?")
                return
            
            print(f"🔍 Pesquisando Wikipedia: {search_term}")
            self.tts.speak(f"Pesquisando sobre {search_term}")
            
            # Buscar resumo
            summary = wikipedia.summary(search_term, sentences=2)
            self.tts.speak(summary)
            
            # Abrir no navegador
            webbrowser.open(f"https://pt.wikipedia.org/wiki/{search_term.replace(' ', '_')}")
            
        except wikipedia.exceptions.DisambiguationError:
            self.tts.speak("Encontrei várias opções. Por favor, seja mais específico.")
        except wikipedia.exceptions.PageError:
            self.tts.speak("Não encontrei informações sobre este assunto.")
        except Exception as e:
            print(f"❌ Erro Wikipedia: {e}")
            self.tts.speak("Não consegui acessar a Wikipedia.")
    
    def open_youtube(self):
        """Abre o YouTube"""
        try:
            print("📺 Abrindo YouTube")
            self.tts.speak("Abrindo YouTube")
            webbrowser.open("https://www.youtube.com")
        except Exception as e:
            print(f"❌ Erro YouTube: {e}")
            self.tts.speak("Não consegui abrir o YouTube")
    
    def search_youtube(self, command):
        """Pesquisa no YouTube"""
        try:
            search_term = command
            remove_words = ['youtube', 'pesquisar', 'buscar', 'procure', 'vídeo', 'video', 'no', 'no youtube', 'em']
            for word in remove_words:
                search_term = search_term.replace(word, '')
            search_term = search_term.strip()
            
            if not search_term:
                self.open_youtube()
                return
            
            print(f"🎥 Pesquisando YouTube: {search_term}")
            self.tts.speak(f"Procurando {search_term} no YouTube")
            pywhatkit.playonyt(search_term)
            
        except Exception as e:
            print(f"❌ Erro pesquisa YouTube: {e}")
            self.tts.speak("Não consegui pesquisar no YouTube")
    
    def find_pharmacy(self):
        """Encontra farmácias próximas"""
        try:
            print("🏥 Procurando farmácias")
            self.tts.speak("Procurando farmácias próximas")
            webbrowser.open("https://www.google.com/maps/search/farmácia")
        except Exception as e:
            print(f"❌ Erro farmácia: {e}")
            self.tts.speak("Não consegui buscar farmácias")
    
    def tell_time(self):
        """Diz a hora atual"""
        try:
            now = datetime.now()
            hora = now.strftime("%H horas e %M minutos")
            print(f"⏰ Hora: {hora}")
            self.tts.speak(f"Agora são {hora}")
        except Exception as e:
            print(f"❌ Erro hora: {e}")
            self.tts.speak("Não consegui verificar a hora")
    
    def tell_date(self):
        """Diz a data atual"""
        try:
            now = datetime.now()
            meses = [
                'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
                'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'
            ]
            dia = now.day
            mes = meses[now.month - 1]
            ano = now.year
            data_str = f"{dia} de {mes} de {ano}"
            print(f"📅 Data: {data_str}")
            self.tts.speak(f"Hoje é {data_str}")
        except Exception as e:
            print(f"❌ Erro data: {e}")
            self.tts.speak("Não consegui verificar a data")