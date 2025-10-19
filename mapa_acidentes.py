import folium
import pandas as pd
from folium.plugins import MarkerCluster
from flask import Flask, render_template

app = Flask(__name__)


def mostrar_acidentes_cidades():
    try:
        df = pd.read_csv('base_dados/acidentes_2025_SP.csv')
        nomes_cidades = df['MUNICÍPIO'].dropna().astype(str)
        cidades_unicas = sorted(nomes_cidades.unique(), key=lambda s: s.lower())
        return cidades_unicas

    except FileNotFoundError:
        print(f"Erro: O arquivo não foi encontrado.")
        return []
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return []


def qtd_municipios_sp():
    try:
        df = pd.read_csv('base_dados/acidentes_2025_SP.csv', dtype={'MUNICÍPIO': 'string'})
        qtd_cidades = df['MUNICÍPIO'].dropna().astype(str)
        qtd_cidades = sorted(qtd_cidades.unique(), key=lambda s: s.lower())
        return len(qtd_cidades)
    except FileNotFoundError:
        print(f"Erro: O arquivo não foi encontrado.")
        return []
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return []


def contar_acidentes_estadoSP():
    try:
        df = pd.read_csv('base_dados/acidentes_2025_SP.csv')
        qtd_acidentes_estado = len(df['DATA'])
        return qtd_acidentes_estado
    except FileNotFoundError:
        print(f"Erro: O arquivo não foi encontrado.")
        return 0
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return 0


def contar_acidentes_por_cidade():
    try:
        df = pd.read_csv('base_dados/acidentes_2025_SP.csv')
        acidentes_por_cidade = df['MUNICÍPIO'].value_counts().to_dict()
        return acidentes_por_cidade
    except Exception as e:
        print(f"Erro ao contar acidentes por cidade: {e}")
        return {}


def criar_mapa_acidentes():
    try:
        df = pd.read_csv('base_dados/acidentes_2025_SP.csv')
        mapa_estado_sp = folium.Map(location=[-23.5062, -47.4559], width="100%", height="100%", zoom_start=7)

        # Adiciona marcadores para cada acidente
        for idx, row in df.iterrows():
            if not pd.isna(row['LATITUDE']) and not pd.isna(row['LONGITUDE']):
                folium.Marker(
                    location=[row['LATITUDE'], row['LONGITUDE']],
                    popup=f"""
                    <b>Cidade:</b> {row['MUNICÍPIO']}<br>
                    <b>Rodovia:</b> {row['RODOVIA']}<br>
                    <b>Tipo:</b> {row['TIPO_ACID']}<br>
                    <b>Data:</b> {row['DATA']}<br>
                    <b>Hora:</b> {row['HR_ACID']}
                    """,
                    tooltip=f"Acidente em {row['MUNICÍPIO']}",
                    icon=folium.Icon(color='red', icon='car', prefix='fa')
                ).add_to(mapa_estado_sp)

        return mapa_estado_sp._repr_html_()
    except Exception as e:
        print(f"Erro ao criar mapa: {e}")
        return ""


@app.route('/')
def index():
    cidades = mostrar_acidentes_cidades()
    total_acidentes = contar_acidentes_estadoSP()
    acidentes_por_cidade = contar_acidentes_por_cidade()
    total_cidades = qtd_municipios_sp()
    mapa_html = criar_mapa_acidentes()

    return render_template('mapa_acidentes.html',
                           cidades=cidades,
                           total_cidades=total_cidades,
                           total_acidentes=total_acidentes,
                           acidentes_por_cidade=acidentes_por_cidade,
                           mapa_html=mapa_html)


if __name__ == '__main__':
    app.run(debug=True)
