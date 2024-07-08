# Bayesian-Classifier-for-RTE-TF-IDF

# Classifier E/NE Representation

This project implements a classifier for E/NE representation using data from the ASSIN corpus (`assin-ptbr-train.xml` and `assin-ptbr-test.xml`). The classifier utilizes TF- IDF representation and a Bayesian Method from machine learning to predict if one sentence entails another.

## Prerequisites

Make sure you have [Conda](https://docs.conda.io/en/latest/miniconda.html) installed on your system.

## Environment Setup

1. **Clone the repository:**

   ```bash
   
   git clone <url-of-your-repository>
   cd project
   
2. **Create a Conda env and install dependencies:**

  ```bash
  conda create --name classifier_env --file requirements.txt
  conda activate classifier_env
```

3. **Install NLTK Stopwords:**

  ```bash
  python -c "import nltk; nltk.download('stopwords')"
```

4. **To run the project use:"**
  ```bash
   python main.py
```




 
