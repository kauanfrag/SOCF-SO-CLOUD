from flask import Flask, jsonify
import os
import platfor
import psutil

APP = Flask(__name__)


processo_atual = psutil.Process(os.getpid())

def pegar_info_sistema():
 
    
 
    mem_info = processo_atual.memory_info()
    memoria_mb = mem_info.rss / (1024 * 1024)
    

    processo_atual.cpu_percent(interval=0.1)
    uso_cpu = processo_atual.cpu_percent(interval=0.1)
    

    so_nome = platform.system()
    so_versao = platform.release()
    
    dados = {
        'pid': os.getpid(),
        'memoria': round(memoria_mb, 2),
        'cpu': uso_cpu,
        'sistema': f"{so_nome} ({so_versao})"
    }
    
    return dados

@APP.route('/')
def pagina_inicial():
  
    info = pegar_info_sistema():
    
    html_resposta = f"""
    <html>
    <head><title>Info do Sistema</title></head>
    <body style="font-family: Arial; padding: 20px;">
        <h2>Informações do Sistema - SOCF</h2>
        <p><strong>Nome:</strong> [KAUAN FRAGOSO]</p>
        <p><strong>PID:</strong> {info['pid']}</p>
        <p><strong>Memória usada:</strong> {info['memoria']} MB</p>
        <p><strong>CPU:</strong> {info['cpu']}%</p>
        <p><strong>Sistema Operacional:</strong> {info['sistema']}</p>
    </body>
    </html>
    """
    
    return html_resposta

@APP.route('/info')
def rota_info():
    # só o nome mesmo
    return jsonify({
        'integrante': '[KAUAN FRAGOSO]'
    })

@APP.route('/metricas')
def rota_metricas():
    # retorna as métricas em json
    info = pegar_info_sistema()
    
    resposta = {
        'nome': '[KAUAN FRAGOSO]',
        'pid': info['pid'],
        'memoria_mb': info['memoria'],
        'cpu_percent': info['cpu'],
        'sistema_operacional': info['sistema']
    }
    
    return jsonify(resposta)

if __name__ == '__main__':
    # pra rodar local
    APP.run(debug=True, host='0.0.0.0', port=5000)
