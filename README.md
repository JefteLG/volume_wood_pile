# Calcular o Volume de uma pilha de madeiras

## Primeiros passos
- Projeto foi criado utilizando o `python=3.8.15`.
- Baixe o modelo Mask R-CNN de segmentação no [Link](https://drive.google.com/file/d/1tUuFEsUU21UoIMC42huRqquYUMcq6D4b/view).
- Coloque o modelo no path `/model`.
- Recomendo utilizar um ambiente virtual para instalar o modulos python e executar o script.

> Nota: Eu utilizei o Anaconda para trabalhar com ambiente virtual caso queira usa-lo, siga o [Tutorial](https://github.com/JefteLG/volume_wood_pile#configurando-o-ambiente-virtual).

- Execute o requirements.txt.

```sh
pip install -r requirements.txt
```

## Executar o projeto
- Acesse a raiz do projeto e execute o script python.
```sh
python app.py
```

> Atenção : Cuidado ao executar o script, execute ele na raiz do projeto.

## Configurando o Ambiente virtual

1. Baixe o Anaconda no [link](https://www.anaconda.com/products/distribution#Downloads).
2. Crie o ambiente virtual. No terminal digite o seguite código:

```sh
conda create -n <nome_do_ambiente> python=3.8.15 -y
```

3. Ative o ambiente virtual e execute o `pip install -r requirements.txt` dentro do ambiente virtual:

```sh
conda activate <nome_do_ambiente>
```
