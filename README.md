# Calculadora Estatística em Python

Calculadora de estatística descritiva com interface web em **Streamlit** e gráficos em **Matplotlib**.

O projeto foi desenvolvido para praticar funções, listas, estruturas condicionais, laços de repetição e modularização em Python, aplicando manualmente conceitos estatísticos utilizados em análise de dados.

## Funcionalidades

- Entrada de dados brutos, agrupados sem intervalos ou agrupados com intervalos de classes.
- Cálculo de mínimo, máximo, amplitude, média, mediana, moda, variância populacional, desvio padrão populacional e coeficiente de variação, conforme o tipo de dados.
- Validação das entradas e apresentação dos resultados na interface.
- Gráfico de dispersão para dados brutos, mostrando os valores na ordem de entrada.
- Histograma ponderado pelas frequências para dados agrupados sem intervalos.
- Histograma com os limites informados para dados agrupados com intervalos. A área de cada barra representa a frequência, permitindo intervalos de larguras diferentes.

## Tecnologias utilizadas

- Python 3
- Streamlit
- Matplotlib

## Como executar

Com Python instalado, abra o terminal na pasta do projeto e execute:

```bash
python -m pip install -r requirements.txt
python -m streamlit run main.py
```

A interface será disponibilizada no navegador. Mantenha o terminal aberto durante o uso. Para encerrar, pressione `Ctrl+C`.

Use o mesmo ambiente Python para instalar as dependências e iniciar a aplicação.

## Como usar

1. Escolha como os dados estão organizados.
2. Preencha os valores e, quando solicitado, as frequências e os limites dos intervalos.
3. Clique em **Calcular** para consultar os resultados e o gráfico.

Separe os números por vírgula, ponto e vírgula ou espaço. Use ponto como separador decimal, por exemplo: `2.5, 4, 6.8`.

As frequências devem ser inteiros não negativos, com pelo menos uma frequência positiva. Os intervalos devem ter largura positiva e não podem se sobrepor.

## Estrutura do projeto

```text
CalculadoraEstatistica/
├── main.py                       # Interface, validação e fluxo da aplicação
├── entrada_saida.py              # Visualização dos gráficos e entrada legada pelo terminal
├── medidas_tendencia_central.py  # Funções de média, mediana e moda
├── medidas_dispersao.py          # Funções de amplitude, variância, desvio e coeficiente
├── requirements.txt             # Dependências da aplicação
└── README.md
```

## Escopo e limitações

Os módulos de cálculo foram preservados durante a migração da interface para Streamlit. O projeto tem finalidade educacional e não representa uma implementação completa dos princípios SOLID.

Medidas que geram erros tratados pela interface são sinalizadas como indisponíveis. A moda de Czuber é sinalizada como indisponível quando a classe modal está na primeira ou na última posição, devido à limitação da função atual. Para dados com intervalos, medidas baseadas nos pontos médios são aproximações.
