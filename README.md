# Bayesian-Classifier-for-RTE-TF-IDF

# Classifier E/NE Representation

Este projeto implementa um classificador de representação E/NE utilizando dados do corpus ASSIN (assin-ptbr-train.xml e assin-ptbr-test.xml). O classificador utiliza técnicas de processamento de linguagem natural e aprendizado de máquina para prever se uma sentença implica outra.

## Estrutura do Projeto
project/
│
├── data_processing.py
├── vectorization.py
├── model.py
├── main.py
├── requirements.txt
└── README.md


## Pré-requisitos

Certifique-se de ter o [Conda](https://docs.conda.io/en/latest/miniconda.html) instalado em seu sistema.

## Configuração do Ambiente

1. **Clone o repositório:**

```bash
git clone <url-do-repositorio>
cd project

conda create --name classifier_env --file requirements.txt
conda activate classifier_env

python -c "import nltk; nltk.download('stopwords')"

