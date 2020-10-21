# EAFP
# Easy ask forgiveness than permission
# É melhor pedir perdão do que permissão
# faça primeiro, n fique checando 
from pathlib import Path
caminho_arquivo = "pandas/dataset1.csvd"

# ============ ERRADO ===============
if Path(caminho_arquivo).exists():
    with open(caminho_arquivo) as f:
        f.read()
        print(f)
else:
    print("O arquivo nao existe")

# ============ CERTO ==============
try:
    with open(caminho_arquivo) as f:
        f.read()
        print(f)
except FileNotFoundError:
    print("o arquivo nao existe")
