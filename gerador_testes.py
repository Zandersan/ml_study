# gerador_testes.py
import os
from langchain.llms import AzureOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

class GeradorTestesUnitarios:
    def __init__(self):
        self.llm = AzureOpenAI(
            deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
            model_name="gpt-35-turbo",
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
        )
        
        self.prompt_template = PromptTemplate(
            input_variables=["codigo"],
            template="""
            Gere testes unitários para o seguinte código Python:
            
            {codigo}
            
            Forneça apenas o código dos testes unitários usando a biblioteca unittest, sem explicações adicionais.
            """
        )
        
        self.chain = LLMChain(llm=self.llm, prompt=self.prompt_template)
    
    def gerar_testes(self, codigo):
        try:
            resposta = self.chain.run(codigo=codigo)
            return resposta
        except Exception as e:
            return f"Erro ao gerar testes: {str(e)}"

def main():
    # Exemplo de código para testar
    codigo_exemplo = """
    def soma(a, b):
        return a + b
    
    def subtracao(a, b):
        return a - b
    """
    
    gerador = GeradorTestesUnitarios()
    testes = gerador.gerar_testes(codigo_exemplo)
    
    print("🔧 Testes Unitários Gerados:\n")
    print(testes)
    
    # Salvar em arquivo
    with open("testes_gerados.py", "w") as f:
        f.write(testes)
    
    print("\n✅ Testes salvos em 'testes_gerados.py'")

if __name__ == "__main__":
    main()