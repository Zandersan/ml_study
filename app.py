from flask import Flask, request, render_template_string, render_template

app = Flask(__name__)

# Página inicial
HTML_FORM = """
<!DOCTYPE html>
<html>
<head>
    <title>Simulador de Vulnerabilidades</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        .vuln-section { border: 1px solid #ccc; padding: 20px; margin: 10px 0; }
    </style>
</head>
<body>
    <h1>Simulador de Vulnerabilidades Educacional</h1>
    
    <div class="vuln-section">
        <h2>1. XSS Refletido (Simulado)</h2>
        <form action="/search" method="GET">
            <input type="text" name="q" placeholder="Buscar...">
            <input type="submit" value="Buscar">
        </form>
        <p><small>Tente: &lt;script&gt;alert('teste')&lt;/script&gt;</small></p>
    </div>
    
    <div class="vuln-section">
        <h2>2. Entrada Não Validada (Simulado)</h2>
        <form action="/calc" method="GET">
            <input type="text" name="expr" placeholder="Expressão (ex: 5+3)">
            <input type="submit" value="Calcular">
        </form>
    </div>
    
    <div class="vuln-section">
        <h2>3. Exposição de Informação</h2>
        <p><a href="/debug">Visualizar página de debug</a></p>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    return HTML_FORM

@app.route('/search')
def search():
    query = request.args.get('q', '')
    # Simulação de XSS refletido (para educação)
    return f"<h2>Resultados para: {query}</h2><a href='/'>Voltar</a>"

@app.route('/calc')
def calculate():
    expr = request.args.get('expr', '')
    try:
        # AVISO: Isto é intencionalmente inseguro para fins educacionais
        result = eval(expr)  # Nunca use eval() com entrada do usuário em produção!
        return f"<h2>Resultado: {result}</h2><a href='/'>Voltar</a>"
    except:
        return f"<h2>Erro ao calcular: {expr}</h2><a href='/'>Voltar</a>"

@app.route('/debug')
def debug_info():
    # Simulação de informação de debug exposta
    debug_data = {
        "server_version": "Python/3.9",
        "framework": "Flask/2.0",
        "debug_mode": True,
        "environment": "development"
    }
    return f"<h2>Informações de Debug</h2><pre>{debug_data}</pre><a href='/'>Voltar</a>"

if __name__ == '__main__':
    print("⚠️  AVISO: Este é um simulador educacional com vulnerabilidades intencionais!")
    print("NUNCA implante este código em produção!")
    app.run(debug=True, host='0.0.0.0', port=5000)