# Análise de Grãos com Redes Neurais

Este projeto tem como objetivo a análise de imagens de grãos, utilizando técnicas de processamento de imagens e redes neurais para classificar e segmentar diferentes tipos de grãos a partir de amostras coletadas com 31 diferentes ondas de luz.

## Descrição do Projeto

O conjunto de dados contém imagens de 10 tipos diferentes de grãos, com 5 amostras distintas para cada tipo. As categorias de grãos são:

- Soja comum
- Soja B
- Queimados
- Púrpuras
- Mofados
- Imaturos
- Fermentados
- Choco
- Bandinhas
- Ardidos

Cada amostra é composta por 31 imagens capturadas em diferentes ondas de luz, e o objetivo é realizar a segmentação e classificação dessas imagens para análise detalhada.

## Tecnologias Utilizadas

- **Python**: Linguagem principal para processamento e modelagem.
- **TensorFlow e Keras**: Frameworks para construção e treinamento de redes neurais profundas.
- **Scikit-Learn**: Utilizado para análise de componentes principais (PCA) e geração de métricas.
- **Cellpose**: Rede neural para segmentação de imagens.
- **skimage (scikit-image)**: Biblioteca para leitura e manipulação de imagens.

## Arquitetura do Modelo

O modelo utiliza uma rede neural convolucional (CNN) para classificar os grãos com base nas características extraídas das imagens multiespectrais. A arquitetura da CNN é composta pelas seguintes camadas:

- **Camadas Conv2D**: Para extração de características.
- **MaxPooling2D**: Para redução de dimensionalidade.
- **Flatten()**: Para converter a saída das camadas convolucionais em um vetor unidimensional.
- **Camada Densa**: Para modelar relações não lineares.
- **Dropout e Regularização L2**: Para evitar overfitting e melhorar a generalização.

O modelo foi otimizado com uma taxa de aprendizado personalizada de 0.0001.
