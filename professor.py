import subprocess, time, os, re
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

MAPA = "MAPA_DE_APRENDIZADO.md"
ULTIMA_ANALISE = {}

def alimentar_grafo(caminho_arquivo):
    global ULTIMA_ANALISE
    filename = os.path.basename(caminho_arquivo)
    
    # Evita processar o mesmo arquivo em menos de 3 segundos (estabilidade para auto-save)
    agora = time.time()
    if filename in ULTIMA_ANALISE and agora - ULTIMA_ANALISE[filename] < 3:
        return
    ULTIMA_ANALISE[filename] = agora

    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            content = f.read()
    except: return

    # Detecta o que você está aprendendo agora
    regras = {
        "[[Lógica Condicional]]": r'\b(if|elif|else)\b',
        "[[Entrada de Dados]]": r'input\(',
        "[[Tratamento de Erros]]": r'\b(try|except)\b',
        "[[Loops e Repetição]]": r'\b(for|while)\b',
        "[[Programação OO]]": r'\bclass\b',
        "[[Funções]]": r'\bdef\b'
    }
    
    conceitos_encontrados = [tag for tag, regex in regras.items() if re.search(regex, content)]

    if conceitos_encontrados:
        # Lê o que já existe para não duplicar linhas idênticas
        existente = ""
        if os.path.exists(MAPA):
            with open(MAPA, 'r') as f: existente = f.read()
        
        linha = f"- [[{filename}]] conectado a: {' '.join(conceitos_encontrados)}\n"
        
        if linha not in existente:
            with open(MAPA, "a") as f: f.write(linha)
            print(f"🧠 Grafo evoluiu: {filename} -> {len(conceitos_encontrados)} conceitos.")

class GraphArchitect(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith(".py") and "professor.py" not in event.src_path:
            # Roda o verificador de erros rápido
            subprocess.run(["pylint", "--errors-only", event.src_path])
            # Alimenta o mapa/grafo
            alimentar_grafo(event.src_path)

observer = Observer()
observer.schedule(GraphArchitect(), path=".", recursive=True)
observer.start()
print("🔥 Professor em Tempo Real (Auto-save detectado). O Grafo está aprendendo agora!")
try:
    while True: time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
