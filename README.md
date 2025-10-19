# Mapa Interativo de Acidentes no Estado de São Paulo em 2025

Aplicação desenvolvida em Python para ciência de dados utilizando as lib do Flask, Pandas e Folium para mapeamento e Estátisticas de Acidentes ocorridos no estado de São Paulo e cidades paulistas no ano de 2025.

## Requisitos
- `python` 3.8+ (recomendado 3.12)
- `git`
- Acesso à internet para instalar dependências

## Passos para executar localmente 

1. Clonar o repositório
```bash
git clone https://github.com/erika263/acidentes_estadoSP2025
cd acidentes_estadoSP2025
```
2.  Atualizar e instalar o pip e dependências + Python

```bash
pip install --upgrade pip
pip install flask pandas folium jinja2
```

3. Identificar o ponto de entrada do Flask
<br>Verifique qual arquivo cria Flask(...) (ex.: app.py, run.py, mapa_acidentes.py).
<br>Usaremos mapa_acidentes.py como exemplo abaixo; substitua pelo arquivo correto se for outro.
<br>Configurar variáveis de ambiente e rodar (modo desenvolvimento)
```bash
export FLASK_APP=mapa_acidentes.py
export FLASK_ENV=development
flask run --host=127.0.0.1 --port=5000
```

4. Alternativa, se o arquivo já contém if __name__ == '__main__': app.run(...):
```bash
python mapa_acidentes.py
Abrir no navegador
Acesse: http://127.0.0.1:5000
```
<p> Desenvolvido por : Érika Cristina Castro</p>
<p>email : erika.contax@gmail.com</p>
<p>Linkedin: https://www.linkedin.com/in/erika-cristina-castro/</p>

