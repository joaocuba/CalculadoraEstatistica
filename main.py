import math
import re

import streamlit as st

import entrada_saida as es
import medidas_dispersao as md
import medidas_tendencia_central as mtc


def ler_numeros(texto):
    try:
        valores = [float(item) for item in re.split(r"[,;\s]+", texto.strip()) if item]
    except ValueError:
        raise ValueError("Use apenas números separados por vírgula, ponto e vírgula ou espaço.")
    if not valores or not all(math.isfinite(valor) for valor in valores):
        raise ValueError("Preencha todas as listas com números finitos.")
    return valores


def mostrar_resultado(calculo):
    try:
        st.write(calculo())
    except (ZeroDivisionError, IndexError, ValueError, OverflowError):
        st.caption("Medida indisponível para estes dados.")


st.set_page_config(page_title="Calculadora Estatística", page_icon="📊")
st.title("Calculadora Estatística")
st.caption("Informe seus dados para consultar as medidas estatísticas e visualizar a distribuição.")
opcao = st.selectbox("Como os dados estão organizados?", ["Dados brutos", "Agrupados sem intervalos", "Agrupados com intervalos"])
tipo = ["Dados brutos", "Agrupados sem intervalos", "Agrupados com intervalos"].index(opcao) + 1

with st.form("entrada"):
    st.caption("Separe os números por vírgula ou espaço. Para decimais, use ponto (ex.: 2.5).")
    if tipo == 1:
        entrada = st.text_area("Valores", "2, 4, 4, 6, 8")
    elif tipo == 2:
        entrada = st.text_area("Valores", "2, 4, 6, 8")
        entrada_f = st.text_input("Frequências", "1, 2, 3, 1")
    else:
        entrada_inf = st.text_input("Limites inferiores", "0, 10, 20")
        entrada_sup = st.text_input("Limites superiores", "10, 20, 30")
        entrada_f = st.text_input("Frequências", "2, 5, 3")
    enviado = st.form_submit_button("Calcular", type="primary")

if not enviado:
    st.stop()

try:
    if tipo == 1:
        numeros = ler_numeros(entrada)
    else:
        frequencias = ler_numeros(entrada_f)
        if any(f < 0 or not f.is_integer() for f in frequencias) or sum(frequencias) == 0:
            raise ValueError("As frequências devem ser inteiros não negativos, com pelo menos uma positiva.")
        if tipo == 2:
            classes = ler_numeros(entrada)
            if len(classes) != len(frequencias):
                raise ValueError("Informe uma frequência para cada valor.")
            agrupados = {}
            for valor, freq in zip(classes, frequencias):
                agrupados[valor] = agrupados.get(valor, 0) + freq
            pares = sorted((v, f) for v, f in agrupados.items() if f > 0)
            classes, frequencias = map(list, zip(*pares))
        else:
            limite_inferior = ler_numeros(entrada_inf)
            limite_superior = ler_numeros(entrada_sup)
            if not len(limite_inferior) == len(limite_superior) == len(frequencias):
                raise ValueError("As listas de limites e frequências devem ter o mesmo tamanho.")
            linhas = sorted(zip(limite_inferior, limite_superior, frequencias))
            if any(a >= b for a, b, _ in linhas) or any(linhas[i][1] > linhas[i+1][0] for i in range(len(linhas)-1)):
                raise ValueError("Os intervalos devem ter largura positiva e não podem se sobrepor.")
            limite_inferior, limite_superior, frequencias = map(list, zip(*linhas))
            classes = list(range(1, len(frequencias) + 1))
except ValueError as erro:
    st.error(str(erro))
    st.stop()

st.subheader("Resultados")
if tipo == 1:
    mostrar_resultado(lambda: f"Mínimo: {md.minimo(numeros):.2f}")
    mostrar_resultado(lambda: f"Máximo: {md.maximo(numeros):.2f}")
    mostrar_resultado(lambda: f"Amplitude: {md.amplitude_total_dados_brutos(numeros):.2f}")
    mostrar_resultado(lambda: f"Média: {mtc.media_aritmetica(numeros):.2f}")
    mostrar_resultado(lambda: f"Mediana: {mtc.mediana_nao_agrupados(numeros):.2f}")
    mostrar_resultado(lambda: f"Moda: {mtc.moda_simples(numeros)}")
    mostrar_resultado(lambda: f"Variância populacional: {md.variancia_nao_agrupados(numeros):.2f}")
    mostrar_resultado(lambda: f"Desvio padrão populacional: {md.desvio_padrao_nao_agrupados(numeros):.2f}")
    mostrar_resultado(lambda: f"Coeficiente de variação: {md.coeficiente_de_variacao_nao_agrupados(numeros):.2f}%")
elif tipo == 2:
    mostrar_resultado(lambda: f"Mínimo: {md.minimo(classes):.2f}")
    mostrar_resultado(lambda: f"Máximo: {md.maximo(classes):.2f}")
    mostrar_resultado(lambda: f"Amplitude: {md.amplitude_total_dados_brutos(classes):.2f}")
    mostrar_resultado(lambda: f"Média: {mtc.media_ponderada(classes, frequencias):.2f}")
    mostrar_resultado(lambda: f"Mediana: {mtc.mediana_agrupados_sem_intervalos(classes, frequencias):.2f}")
    mostrar_resultado(lambda: f"Moda: {mtc.moda_agrupado_sem_classes(classes, frequencias)}")
    mostrar_resultado(lambda: f"Variância populacional: {md.variancia_agrupados_sem_classes(frequencias, classes):.2f}")
    mostrar_resultado(lambda: f"Desvio padrão populacional: {md.desvio_padrao_agrupados_sem_classes(frequencias, classes):.2f}")
    mostrar_resultado(lambda: f"Coeficiente de variação: {md.coeficiente_de_variacao_agrupados_sem_classes(frequencias, classes):.2f}%")
elif tipo == 3:
    mostrar_resultado(lambda: f"Mínimo: {md.minimo(limite_inferior):.2f}")
    mostrar_resultado(lambda: f"Máximo: {md.maximo(limite_superior):.2f}")
    mostrar_resultado(lambda: f"Amplitude: {md.amplitude_total_dados_agrupados_com_classes(limite_inferior, limite_superior):.2f}")
    mostrar_resultado(lambda: f"Média: {mtc.media_ponderada_classes(limite_inferior, limite_superior, frequencias):.2f}")
    mostrar_resultado(lambda: f"Mediana: {mtc.mediana_agrupados_com_intervalos(classes, limite_inferior, limite_superior, frequencias):.2f}")
    mostrar_resultado(lambda: f"Moda Bruta: {mtc.moda_bruta_agrupado_com_classes(classes, limite_inferior, limite_superior, frequencias)}")
    mostrar_resultado(lambda: f"Moda de Pearson: {mtc.moda_pearson_agrupado_com_classes(classes, limite_inferior, limite_superior, frequencias):.2f}")
    if frequencias.index(max(frequencias)) in (0, len(frequencias) - 1):
        st.caption("Moda de Czuber indisponível: a função atual requer uma classe modal interior.")
    else:
        mostrar_resultado(lambda: f"Moda de Czuber: {mtc.moda_czuber_agrupado_com_classes(classes, limite_inferior, limite_superior, frequencias):.2f}")
    mostrar_resultado(lambda: f"Variância populacional: {md.variancia_agrupados_com_classes(frequencias, limite_inferior, limite_superior):.2f}")
    mostrar_resultado(lambda: f"Desvio padrão populacional: {md.desvio_padrao_agrupados_com_classes(frequencias, limite_inferior, limite_superior):.2f}")
    mostrar_resultado(lambda: f"Coeficiente de variação: {md.coeficiente_de_variacao_agrupados_com_classes(frequencias, limite_inferior, limite_superior):.2f}%")

if tipo == 1:
    es.visualizar_dados(tipo, numeros=numeros)
elif tipo == 2:
    es.visualizar_dados(tipo, classes=classes, frequencias=frequencias)
else:
    es.visualizar_dados(
        tipo,
        frequencias=frequencias,
        limite_inferior=limite_inferior,
        limite_superior=limite_superior,
    )
