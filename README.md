# Survey_Bot_Mackblasters
It will take survey when we started and detect the gender(Male or Female by using name) and emotional(the feedback is positive or negative)

## Major packages used
- Speech Recognition
- PyTorch
- Pyttsx
- NLTK

## Project requirements
- `Python 3.7-3.9` (Pytorch limitation)
**If virtual environment is not installed on your machine install it using below command.*
```console
  pip install virtualenv
```
Activate **virtualenv**
```console
   virtualenv env
  .\Scripts\activate  
```
Run pip to install all the dependencies
```console
  pip install -r requirements.txt
It will create `data.pth` which is the model data.

```console
  py .\nlp_pipeline\train.py
```
If you get an error during the first run, you also need to install `nltk.tokenize.punkt`:

*Run this once in your terminal:*

```console
  python
  >>> import nltk
  >>> nltk.download('punkt')
```
Finally start main.py
```console
  py main.py
```
