# Médias
def media_aritmetica (numeros: list) -> float:
    '''
        media_aritimetica serve para calcular a média de uma série de dados.
        Deve-se considerar uma lista contendo os números que serão utilizados 
        para o cálculo da média.

        numeros:
            uma lista de números (int ou float) contendo os valores que serão utilizados
            para o cálculo da média aritimética.
    '''
    if len(numeros) == 0:
        return 0
        
    else:
        return sum(numeros) / len(numeros)

def media_ponderada_classes (intervalo_inferior: list, intervalo_superior: list, frequencias:list) -> float:
    '''
    media_ponderada_classes serve para calcular a média de uma série de dados agrupados com intervalos de classes.
    Deve-se considerar os intervalos da classe (superior e inferior) e as frequências de cada intervalo.
    
    intervalo_inferior:
        uma lista de números (int ou float) que contenha os valores dos limites inferiores dos intervalos de classes.
    
    intervalo_superior:
        uma lista de números (int ou float) que contenha os valores dos limites superiores dos intervalos de classes.
    
    frequencias:
        uma lista de números inteiros que contenha as frequências de cada intervalo de classe.
    '''
    if sum(frequencias) == 0:
        return 0

    if not (len(intervalo_inferior) == len (intervalo_superior) == len(frequencias)):
        raise ValueError("As listas devem ter o mesmo tamanho.")
    
    ponto_medio = []
    for inferior, superior in zip (intervalo_inferior, intervalo_superior):
        ponto_medio.append((inferior + superior) / 2)

    soma_ponderada = 0

    for ponto, frequencia in zip (ponto_medio, frequencias):
        soma_ponderada += ponto * frequencia
    
    total_frequencias = sum(frequencias)

    return soma_ponderada / total_frequencias

def media_ponderada (numeros: list, frequencias: list) -> float:
    '''
    media_ponderada serve para calcular a média ponderada de uma série de dados.
    Deve-se considerar a lista de números e a lista de frequências/pesos associadas a cada número.
    
    numeros:
        Uma lista que contem os núneros (int ou float) que serão utilizados para o cálculo da média ponderada.
    
    frequencias:
        Uma lista que contem a frequência ou os pesos (int ou float) associados a cada número na lista de números.
    '''
    if sum(numeros) == 0  or sum(frequencias) == 0:
        return 0
    
    if not (len(numeros) == len(frequencias)):
        raise ValueError("As listas devem conter a mesma quantidade de elementos.")
    
    soma_ponderada = 0

    for numeros, frequencia in zip (numeros, frequencias):
        soma_ponderada += numeros * frequencia
    
    total_frequencias = sum(frequencias)

    return soma_ponderada / total_frequencias

# Medianas
def mediana_nao_agrupados (numeros: list) -> float:
    '''
    mediana_nao_agrupados realiza o cálculo da mediana para uma série de dados não agrupados.
    Deve-se considerar uma lista contendo a série de dados que deseja-se obter a mediana.

    numeros:
        uma lista de números (int ou float) contendo os valores que serão utilizados
        para o cálculo da mediana.

    '''
    if (sum(numeros) or len(numeros)) == 0:
        return 0
       
    numeros_ordenados = sorted(numeros)

    if len(numeros_ordenados) % 2 == 0: 
        meio_direita = len(numeros_ordenados) // 2
        meio_esquerda = meio_direita - 1
        mediana = (numeros_ordenados[meio_esquerda] + numeros_ordenados[meio_direita]) / 2
    
    else:
        meio = len(numeros_ordenados) // 2
        mediana = numeros_ordenados[meio]
    
    return mediana

def mediana_agrupados_sem_intervalos (elementos: list, frequencias: list) -> float:
    '''
    mediana_agrupados_sem_intervalos realiza o cálculo da mediana para uma série de dados (elementos) agrupados
    sem intervalo de classes, considerando as frequências associadas a cada elemento.
    Deve-se considerar a lista de elementos e a lista de frequências associadas a cada elemento.

    elementos:
        uma lista de elementos (int, float, str) que contém as classes ou categorias dos dados agrupados.
    
    frequencias:
        uma lista de números inteiros que contém as frequências associadas a cada elemento na lista de elementos.
        
    '''
    if sum(frequencias) == 0:
        return 0

    if not (len(elementos) == len(frequencias)):
        raise ValueError("As listas devem ter o mesmo tamanho.")
    
    frequencia_acumulada = []
    acumulado = 0

    for freq in frequencias:
        acumulado += freq
        frequencia_acumulada.append(acumulado)
    
    n = sum (frequencias)
    metade = n / 2

    indice_mediana = 0

    for i, freq_acumulada in enumerate (frequencia_acumulada):
        if freq_acumulada >= metade: 
            indice_mediana = i
            break
    
    return elementos[indice_mediana]

def mediana_agrupados_com_intervalos(classe:list ,intervalo_inferior: list, intervalo_superior: list, frequencias: list) -> float:
    '''
    mediana_agrupados_com_intervalos realiza o cálculo da mediana para uma série de dados agrupados 
    com intervalos de classes.
    Deve-se considerar as classes, os intervalos da classe (superior e inferior) e as frequências de cada intervalo.

    classe:
        uma lista de elementos (int, float, str) que contém as classes ou categorias dos dados agrupados.

    intervalo_inferior:
        uma lista de números (int ou float) que contenha os valores dos limites inferiores 
        dos intervalos de classes.
    
    intervalo_superior:
        uma lista de números (int ou float) que contenha os valores dos limites superiores
        dos intervalos de classes.
    
    frequencias:
        uma lista de números inteiros que contenha as frequências de cada intervalo de classe.
    '''

    if sum(frequencias) == 0:
        return 0
    
    if not (len(intervalo_inferior) == len(intervalo_superior) == len(frequencias)):
        raise ValueError("As listas devem ter o mesmo tamanho.")
    
    frequencia_acumulada = []
    acumulado = 0

    for freq in frequencias:
        acumulado += freq
        frequencia_acumulada.append(acumulado)
    
    media = sum (frequencias) / 2

    indice_mediana = 0

    for i, freq_acumulada in enumerate (frequencia_acumulada):
        if freq_acumulada >= media:
            indice_mediana = i
            break
    
    if indice_mediana == 0:
        frequencia_anterior = frequencia_acumulada[0]
    else:
        frequencia_anterior = frequencia_acumulada[indice_mediana - 1]

    limite_inferior = intervalo_inferior[indice_mediana]
    frequencia_acumulada_anterior = frequencia_acumulada[indice_mediana - 1] if indice_mediana > 0 else 0
    frequencia_intervalo = frequencias[indice_mediana]
    amplitude_intervalo = intervalo_superior[indice_mediana] - intervalo_inferior[indice_mediana]

    mediana = limite_inferior + ((media - frequencia_acumulada_anterior) / frequencia_intervalo) * amplitude_intervalo

    return mediana

# Modas
def moda_simples(numeros: list) -> dict:
    '''
    moda_simples calcula a moda de uma série de dados simples (não agrupados).

    numeros:
        uma lista de números (int ou float) para os quais se deseja calcular a moda.
    '''
    if len(numeros) == 0:
        return []
    
    frequencias = {}

    for valor in numeros:
        frequencias[valor] = frequencias.get(valor, 0) + 1
    
    maior_frequencia = max(frequencias.values())

    moda = [valor for valor, freq in frequencias.items() if freq == maior_frequencia]

    resultado = {}

    if maior_frequencia == 1:
        resultado['Tipo'] = 'Amodal'
        resultado['Moda'] = []
        return resultado
    
    if len(moda) == 1:
        resultado['Tipo'] = 'Unimodal'

    if len(moda) == 2:
        resultado['Tipo'] = 'Bimodal'
    
    if len(moda) == 3:
        resultado['Tipo'] = 'Trimodal'
    
    if len(moda) >= 4:
        resultado['Tipo'] = 'Multimodal'
    
    resultado['Moda'] = moda

    return resultado

def moda_agrupado_sem_classes (elementos: list, frequencias: list) -> float:
    '''
    moda_agrupado_sem_classes calcula a moda para uma série de dados agrupados sem intervalo de classes.
    Deve-se considerar a lista de elementos (int, float, str) e a lista de frequências associadas a cada elemento.

    elementos:
        uma lista de elementos (int, float, str) que contém as classes ou categorias dos dados agrupados.
    
    frequencias:
        uma lista de números inteiros que contém as frequências associadas a cada elemento na lista de elementos.
    '''

    maior_frequencia = max(frequencias)
    indice_moda = frequencias.index(maior_frequencia)

    return elementos[indice_moda]

def moda_bruta_agrupado_com_classes (elementos: list, intervalo_inferior: list, intervalo_superior: list, frequencias: list) -> float: 
    '''
    moda_bruta_agrupado_com_classes calcula a moda bruta para uma série de dados agrupados com intervalos de classes.
    Deve-se considerar a lista de elementos (int, float, str), a lista de intervalos inferiores e superiores,
    e a lista de frequências associadas a cada intervalo.

    elementos:
        uma lista de elementos (int, float, str) que contêm as classes ou categorias dos dados agrupados.
    
    intervalo_inferior: 
        uma lista de números (int ou float) que contém os valores dos limites inferiores dos intervalos de classes.
    
    intervalo_superior:
        uma lista de números (int ou float) que contém os valores dos limites superiores dos intervalos de classes.
    
    frequencias:
        uma lista de números inteiros que contém as frequências associadas a cada intervalo de classe.
   
    '''
    maior_frequencia = max(frequencias)
    indice_moda = frequencias.index(maior_frequencia)
    limite_inferior = intervalo_inferior[indice_moda]
    limite_superior = intervalo_superior[indice_moda]
    moda = (limite_inferior + limite_superior)/2

    return moda

def moda_pearson_agrupado_com_classes (classe:list ,intervalo_inferior: list, intervalo_superior: list, frequencias: list) -> float:
    '''
    moda_pearson_agrupado_com_classes calcula a moda de pearson para uma série de dados agrupados com intervalos de classes,
    Deve-se considerar as classes, os intervalos superior e inferior, e as frequências de cada intervalo.

    classe:
        uma lista de elementos (int, float, str) que contém as classes ou categorias dos dados agrupados.
    
    intervalo_inferior:
        uma lista de números (int ou float) que contenha os valores dos limites inferiores 
        dos intervalos de classes.
    
    intervalo_superior:
        uma lista de números (int ou float) que contenha os valores dos limites superiores
        dos intervalos de classes.
    
    frequencias:
        uma lista de números inteiros que contenha as frequências de cada intervalo de classe.
    '''
    moda_pearson = (3* mediana_agrupados_com_intervalos(classe , intervalo_inferior, intervalo_superior, frequencias)) - (2 * media_ponderada_classes(intervalo_inferior, intervalo_superior, frequencias))

    return moda_pearson

def moda_czuber_agrupado_com_classes (classe:list ,intervalo_inferior: list, intervalo_superior: list, frequencias: list) -> float:
    '''
    moda_czuber_agrupado_com_classes calcula a moda de czuber para uma série de dados agrupados com intervalos de classes.
    Deve-se considerar as classes, os intervalos superior e inferior, e as frequências de cada intervalo.

    classe:
        uma lista de elementos (int, float, str) que contém as classes ou categorias dos dados agrupados.
    
    intervalo_inferior:
        uma lista de números (int ou float) que contenha os valores dos limites inferiores 
        dos intervalos de classes.
    
    intervalo_superior:
        uma lista de números (int ou float) que contenha os valores dos limites superiores
        dos intervalos de classes.
    
    frequencias:
        uma lista de números inteiros que contenha as frequências de cada intervalo de classe.
        
    '''

    if sum(frequencias) == 0:
        return 0
    
    if not (len(intervalo_inferior) == len(intervalo_superior) == len(frequencias)):
        raise ValueError("As listas devem ter o mesmo tamanho.")

    maior_frequencia = max(frequencias)
    indice_moda = frequencias.index(maior_frequencia)
    limite_inferior = intervalo_inferior[indice_moda]
    intervalo_classes = intervalo_superior[indice_moda] - intervalo_inferior[indice_moda]
    delta_1 = maior_frequencia - frequencias[indice_moda - 1] 
    delta_2 = maior_frequencia - frequencias[indice_moda + 1]
    moda_czuber = limite_inferior + (delta_1 / (delta_1 + delta_2)) * intervalo_classes
    return moda_czuber