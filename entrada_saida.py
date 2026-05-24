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