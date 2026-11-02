import matplotlib.pyplot as plt
import streamlit as st

def entrada_de_dados(tipo:int) ->list:
    '''
    entrada_de_dados solicita ao usuário os dados que serão utilizados para a realização das analises
    e retorna esses dados em forma de lista.
    '''
    if tipo == 1:
        dados = input("\nDigite os dados separados por vírgula: ")
        numeros = [float(num.strip()) for num in dados.split(",")]
        return numeros
    
    elif tipo == 2:
        dados_classes = input("\nDigite as classes separadas por vírgula (Classes devem ser numéricas): ")
        classes = [float(classe.strip()) for classe in dados_classes.split(",")]

        dados_frequencias = input("\nDigite as frequências separadas por vírgula: ")
        frequencias = [float(frequencias.strip()) for frequencias in dados_frequencias.split(",")]
        return classes, frequencias
    
    elif tipo == 3:
        dados_classes = input("\nDigite as classes separadas por vírgula (Classes devem ser numéricas): ")
        classes = [float(classe.strip()) for classe in dados_classes.split(",")]

        dados_frequencias = input("\nDigite as frequências separadas por vírgula: ")
        frequencias = [float(frequencias.strip()) for frequencias in dados_frequencias.split(",")]

        dados_limite_inferior = input("\nDigite os limites inferiores separados por vírgula: ")
        limite_inferior = [float(limite.strip()) for limite in dados_limite_inferior.split(",")]

        dados_limite_superior = input("\nDigite os limites superiores separados por vírgula: ")
        limite_superior = [float(limite.strip()) for limite in dados_limite_superior.split(",")]

        return classes, frequencias, limite_inferior, limite_superior

def visualizar_dados(tipo, *, numeros=None, classes=None, frequencias=None,
                     limite_inferior=None, limite_superior=None):
    """Exibe o gráfico dos dados já validados, conforme o tipo de entrada."""
    st.subheader("Visualização dos dados")
    fig, ax = plt.subplots()
    if tipo == 1:
        ax.scatter(range(1, len(numeros) + 1), numeros)
        ax.set(xlabel="Observação (ordem de entrada)", ylabel="Valor", title="Dispersão dos dados brutos")
    elif tipo == 2:
        ax.hist(classes, weights=frequencias, bins=min(10, len(classes)))
        ax.set(xlabel="Valor", ylabel="Frequência", title="Histograma dos dados agrupados")
    else:
        larguras = [b - a for a, b in zip(limite_inferior, limite_superior)]
        ax.bar(limite_inferior, [f / largura for f, largura in zip(frequencias, larguras)], width=larguras, align="edge", edgecolor="white")
        ax.set(xlabel="Intervalo", ylabel="Densidade de frequência", title="Histograma por intervalos")
        st.caption("A área de cada barra corresponde à frequência do intervalo.")
    ax.grid(axis="y", alpha=0.2)
    st.pyplot(fig)
    plt.close(fig)
