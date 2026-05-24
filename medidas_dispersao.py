from medidas_tendencia_central import media_ponderada, media_ponderada_classes

# Maior e Menor Valor
def minimo (numeros: list) -> float:
    '''
    Retorna o menor valor de uma lista de números.
    
    numeros:
        Lista de números (int ou float) que deseja-se encontrar o menor valor.
    '''
    if not numeros:
        raise ValueError("A lista não pode estar vazia.")

    menor = numeros[0]
    for numero in numeros:
        if numero < menor:
            menor = numero
    
    return menor

def maximo (numeros: list) -> float:
    '''
    Retorna o maior valor de uma lista de números.

    numeros:
        Lista de números (int ou float) que deseja-se encontrar o maior valor.
    '''
    if not numeros:
        raise ValueError("A lista não pode estar vazia.")
    
    maior = numeros[0]
    for numero in numeros:
        if numero > maior:
            maior = numero
    
    return maior

# Amplitude
def amplitude_total_dados_brutos (numeros: list) -> float:  
    '''
    Returna a amplitude de uma lista de números.

    numeros:
        Lista de números (int ou float) que deseja-se encontrar a amplitude.
    '''

    if not numeros:
        raise ValueError("A lista não pode estar vazia.")
    maior = maximo(numeros)
    menor = minimo(numeros)
       
    amplitude = maior - menor

    return amplitude

def amplitude_total_dados_agrupados_com_classes (limite_inferior: list, limite_superior: list) -> float:
    '''
    amplitude_total_dados_agrupados_com_classes returna a amplitude dos dados agrupados em classes.

    limite_inferior:
        Lista de limites inferiores das classes.

    limite_superior:
        Lista de limites superiores das classes.
    '''

    if not limite_inferior or not limite_superior:
        raise ValueError("As listas não podem estar vazias.")
    
    if len(limite_inferior) != len(limite_superior):
        raise ValueError("As listas devem ter o mesmo tamanho.")
    
    maior = maximo(limite_superior)
    menor = minimo(limite_inferior)

    amplitude = maior - menor

    return amplitude

# Desvio Padrão
def desvio_padrao_nao_agrupados (numeros:list) -> float:
    '''
    desvio_padrao_nao_agrupados retorna o desvio padrão para uma lista de dados não agrupados.

    numeros:
        Lista de números (int ou float) que deseja-se calcular o desvio padrão.
    '''

    if not numeros:
        raise ValueError("A lista não pode estar vazia.")
    
    n = len(numeros)
    media = sum(numeros) / n

    soma_quadrados = 0
    for numero in numeros:
        soma_quadrados += numero**2
    
    variancia = soma_quadrados/n - media**2
    desvio_padrao = variancia ** 0.5

    return desvio_padrao

def desvio_padrao_agrupados_sem_classes (frequencias:list, classes:list) -> float:
    '''
    desvio_padrao_agrupados_sem_classes retorna o desvio padrão para uma lista de dados agrupados sem classes.
    
    frequencias:
        Lista de frequências (int) que deseja-se calcular o desvio padrão.
    
    classes:
        Lista de classes (int ou float) que deseja-se calcular o desvio padrão.
        
    '''

    desvio_padrao = variancia_agrupados_sem_classes(frequencias, classes) ** 0.5

    return desvio_padrao

def desvio_padrao_agrupados_com_classes (frequencias:list, limite_inferior:list, limite_superior:list) -> float:
    '''
    desvio_padrao_agrupados_com_classes retorna o desvio padrão para uma lista de dados agrupados com classes.

    frequencias:
        Lista de frequências (int) que deseja-se calcular o desvio padrão.
    
    limite_inferior:
        Lista de limites inferiores das classes.
    
    limite_superior:
        Lista de limites superiores das classes.
    '''

    desvio_padrao = variancia_agrupados_com_classes(frequencias, limite_inferior, limite_superior) ** 0.5

    return desvio_padrao

# Variancia
def variancia_nao_agrupados (numeros: list) -> float:
    '''
    desvio_padrao_nao_agrupados retorna o desvio padrão para uma lista de dados não agrupados.

    numeros:
        Lista de números (int ou float) que deseja-se calcular o desvio padrão.
    '''
    if not numeros:
        raise ValueError("A lista não pode estar vazia.")
    
    n = len(numeros)
    media = sum(numeros) / n

    soma_quadrados = 0
    for numero in numeros:
        soma_quadrados += numero**2
    
    variancia = soma_quadrados/n - media**2
    return variancia

def variancia_agrupados_sem_classes (frequencias:list, classes:list) -> float:
    '''
    variancia_agrupado_sem_classes retorna a variancia para uma lista de dados agrupados sem classes.

    frequencias:
        Lista de frequências (int) que deseja-se calcular a variancia.
    
    classes:
        Lista de classes (int ou float) que deseja-se calcular a variancia.
    '''

    if not frequencias or not classes:
        raise ValueError("As listas não podem estar vazias.")
    
    if len(frequencias) != len(classes):
        raise ValueError("As listas devem ter o mesmo tamanho.")
    
    soma_quadrada_ponderada = 0
    soma_ponderada = 0

    n = sum(frequencias)
    for i in range (len(classes)):
        soma_quadrada_ponderada += frequencias[i] * classes[i]**2
        soma_ponderada += frequencias[i] * classes[i]

    variancia = (soma_quadrada_ponderada/n) - (soma_ponderada/n)**2

    return variancia

def variancia_agrupados_com_classes (frequencias:list, limite_inferior:list, limite_superior:list) -> float:
    '''
    variancia_agrupados_com_classes retorna a variancia para uma lista de dados agrupados com classes.

    frequencias:
        Lista de frequências (int) que deseja-se calcular a variancia.
    
    limite_inferior:
        Lista de limites inferiores das classes.
    
    limite_superior:
        Lista de limites superiores das classes.
    '''
    if not frequencias or not limite_inferior or not limite_superior:
        raise ValueError("As listas não podem estar vazias.")

    if len(frequencias) != len(limite_inferior) or len(frequencias) != len(limite_superior):
        raise ValueError("As listas devem ter o mesmo tamanho.")
    
    classe_media = []
    for i in range(len(limite_inferior)):
        classe_media.append((limite_inferior[i] + limite_superior[i])/2)
    
    variancia = variancia_agrupados_sem_classes(frequencias, classe_media)
    return variancia

# Coeficiente de Variação
def coeficiente_de_variacao_nao_agrupados (numeros: list) -> float:
    '''
    coeficiente_de_variacao_nao_agrupados retorna o coeficiente de variação para uma lista de dados não agrupados.

    numeros:
        Lista de números (int ou float) que deseja-se calcular o coeficiente de variação.
    '''

    if not numeros:
        raise ValueError("A lista não pode estar vazia.")
    
    n = len(numeros)
    media = sum(numeros) / n
    soma_quadrados = 0
    for numero in numeros:
        soma_quadrados += numero**2
    
    variancia = soma_quadrados/n - media**2
    desvio_padrao = variancia ** 0.5

    coeficiente_variacao = (desvio_padrao / media) * 100

    return coeficiente_variacao

def coeficiente_de_variacao_agrupados_sem_classes (frequencias:list, classes:list) -> float:
    '''
    coeficiente_de_variacao_agrupados_sem_classes retorna o coeficiente de variação para uma lista de dados agrupados sem classes.

    frequencias:
        Lista de frequências (int) que deseja-se calcular o coeficiente de variação.
    
    classes:
        Lista de classes (int ou float) que deseja-se calcular o coeficiente de variação.
    
    '''

    desvio_padrao = desvio_padrao_agrupados_sem_classes(frequencias, classes)
    media = media_ponderada(classes, frequencias)

    coeficiente = (desvio_padrao / media) * 100

    return coeficiente

def coeficiente_de_variacao_agrupados_com_classes (frequencias:list, limite_inferior:list, limite_superior:list) -> float:
    '''
    coeficiente_de_variacao_agrupados_com_classes retorna o coeficiente de variação para uma lista de dados agrupados com classes.

    frequencias:
        Lista de frequências (int) que deseja-se calcular o coeficiente de variação.
    
    limite_inferior:
        Lista de limites inferiores das classes.
    
    limite_superior:
        Lista de limites superiores das classes.
    '''

    desvio_padrao = desvio_padrao_agrupados_com_classes(frequencias, limite_inferior, limite_superior)

    media = media_ponderada_classes (limite_inferior, limite_superior, frequencias)

    coeficiente = (desvio_padrao / media) * 100

    return coeficiente