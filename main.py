import medidas_dispersao as md
import medidas_tendencia_central as mtc
import entrada_saida as es

if __name__ == "__main__":
    print("-=-=" * 20)
    print("Bem vindo a Calculadora Estatística!")
    print("-=-=" * 20)

    print("\nComo os dados estão organizados?")
    print("\n1 - Dados brutos")
    print("\n2 - Dados agrupados mas sem classes")
    print("\n3 - Dados agrupados com classes")

    tipo = int(input("\nDigite o número correspondente ao tipo de dado: "))
    print("-=-=" * 20)

    if tipo == 1:
        numeros = es.entrada_de_dados(tipo)

        print("\nAnálises Estatísticas para Dados Brutos:")
        print(f"Mínimo: {md.minimo(numeros):.2f}")
        print(f"Máximo: {md.maximo(numeros):.2f}")
        print(f"Amplitude: {md.amplitude_total_dados_brutos(numeros):.2f}")
        print(f"Média: {mtc.media_aritmetica(numeros):.2f}")
        print(f"Mediana: {mtc.mediana_nao_agrupados(numeros):.2f}")
        print(f"Moda: {mtc.moda_simples(numeros)}")
        print(f"Variância populacional: {md.variancia_nao_agrupados(numeros):.2f}")
        print(f"Desvio padrão populacional: {md.desvio_padrao_nao_agrupados(numeros):.2f}")
        print(f"Coeficiente de variação: {md.coeficiente_de_variacao_nao_agrupados(numeros):.2f}%")

    elif tipo == 2:
        classes, frequencias = es.entrada_de_dados(tipo)

        print("\nAnálises Estatísticas para Dados Agrupados sem Classes:")
        print(f"Mínimo: {md.minimo(classes):.2f}")
        print(f"Máximo: {md.maximo(classes):.2f}")
        print(f"Amplitude: {md.amplitude_total_dados_brutos(classes):.2f}")
        print(f"Média: {mtc.media_ponderada(classes, frequencias):.2f}")
        print(f"Mediana: {mtc.mediana_agrupados_sem_intervalos(classes, frequencias):.2f}")
        print(f"Moda: {mtc.moda_agrupado_sem_classes(classes, frequencias)}")
        print(f"Variância populacional: {md.variancia_agrupados_sem_classes(frequencias, classes):.2f}")
        print(f"Desvio padrão populacional: {md.desvio_padrao_agrupados_sem_classes(frequencias, classes):.2f}")
        print(f"Coeficiente de variação: {md.coeficiente_de_variacao_agrupados_sem_classes(frequencias, classes):.2f}%")

    elif tipo == 3:
        classes, frequencias, limite_inferior, limite_superior = es.entrada_de_dados(tipo)

        print("\nAnálises Estatísticas para Dados Agrupados com Classes:")
        print(f"Mínimo: {md.minimo(limite_inferior):.2f}")
        print(f"Máximo: {md.maximo(limite_superior):.2f}")
        print(f"Amplitude: {md.amplitude_total_dados_agrupados_com_classes(limite_inferior, limite_superior):.2f}")
        print(f"Média: {mtc.media_ponderada_classes(limite_inferior, limite_superior, frequencias):.2f}")
        print(f"Mediana: {mtc.mediana_agrupados_com_intervalos(classes, limite_inferior, limite_superior, frequencias):.2f}")
        print(f"Moda Bruta: {mtc.moda_bruta_agrupado_com_classes(classes, limite_inferior, limite_superior, frequencias)}")
        print(f"Moda de Pearson: {mtc.moda_pearson_agrupado_com_classes(classes, limite_inferior, limite_superior, frequencias):.2f}")
        print(f"Moda de Czuber: {mtc.moda_czuber_agrupado_com_classes(classes, limite_inferior, limite_superior, frequencias):.2f}")
        print(f"Variância populacional: {md.variancia_agrupados_com_classes(frequencias, limite_inferior, limite_superior):.2f}")
        print(f"Desvio padrão populacional: {md.desvio_padrao_agrupados_com_classes(frequencias, limite_inferior, limite_superior):.2f}")
        print(f"Coeficiente de variação: {md.coeficiente_de_variacao_agrupados_com_classes(frequencias, limite_inferior, limite_superior):.2f}%")

    else:
        print("\nOpção inválida. Execute o programa novamente e escolha uma opção entre 1, 2 ou 3.")