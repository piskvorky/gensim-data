# Gensim data
This repository contains models and dataset that available through gensim download api. This repo used as storage.

## Quickstart
To load model/dataset you can use 2 types of API:
- CLI
  ```bash
  python -m gensim.downloader --catalogue  # show info about available models/datasets
  python -m gensim.downloader --download glove-twitter-50  # download model, will be stored in ~/gensim-data/glove-twitter-50/
  ```
- Python API

  Example: load pre-trained vectors
  ```python
  import gensim.downloader as api

  info = api.info()  # show info about available models/datasets
  model = api.load("glove-twitter-50")  # download model and load it to memory
  model.most_similar("cat")
  
  """
  Output:

  [(u'dog', 0.9429584741592407),
   (u'pet', 0.8726721405982971),
   (u'kitty', 0.8676421046257019),
   (u'bear', 0.8655619621276855),
   (u'monkey', 0.8506731390953064),
   (u'pig', 0.8369913101196289),
   (u'puppy', 0.8335512280464172),
   (u'kitten', 0.829558789730072),
   (u'cats', 0.8218453526496887),
   (u'dogs', 0.8203402757644653)] 
  """
  ```
  
  Example: load dataset and train Word2Vec
  ```python
  from gensim.models.word2vec import Text8Corpus
  from gensim.models.word2vec import Word2Vec
  import gensim.downloader as api

  corpus_path = api.load('text8')  # download dataset
  corpus = Text8Corpus(corpus_path)  # load text8 as corpus
  model = Word2Vec(corpus)  # train model

  ```
  
## Available data
### Datasets
| name | source | description |
|------|--------|-------------|
| 20-newsgroups | http://qwone.com/~jason/20Newsgroups/ | The 20 Newsgroups data set is a collection of approximately 20,000 newsgroup documents, partitioned (nearly) evenly across 20 different newsgroups |
| fake-news | Kaggle | It contains text and metadata scraped from 244 websites tagged as 'bullshit' here by the BS Detector Chrome Extension by Daniel Sieradski. |
| text8 | http://mattmahoney.net/dc/text8.zip | Cleaned small sample from wikipedia |

### Models
| name | description | papers | preprocessing | parameters |
|------|-------------|------------|--------|---------------|
| glove-twitter-100 | Pre-trained vectors, 2B tweets, 27B tokens, 1.2M vocab, uncased. https://nlp.stanford.edu/projects/glove/ | https://nlp.stanford.edu/pubs/glove.pdf | Converted to w2v format with `python -m gensim.scripts.glove2word2vec -i <fname> -o glove-twitter-100.txt` | dimensions = 100 |
| glove-twitter-200 | Pre-trained vectors, 2B tweets, 27B tokens, 1.2M vocab, uncased. https://nlp.stanford.edu/projects/glove/ | https://nlp.stanford.edu/pubs/glove.pdf | Converted to w2v format with `python -m gensim.scripts.glove2word2vec -i <fname> -o glove-twitter-200.txt` | dimensions = 200 |
| glove-twitter-25 | Pre-trained vectors, 2B tweets, 27B tokens, 1.2M vocab, uncased. https://nlp.stanford.edu/projects/glove/ | https://nlp.stanford.edu/pubs/glove.pdf | Converted to w2v format with `python -m gensim.scripts.glove2word2vec -i <fname> -o glove-twitter-25.txt` | dimensions = 25 |
| glove-twitter-50 | Pre-trained vectors, 2B tweets, 27B tokens, 1.2M vocab, uncased. https://nlp.stanford.edu/projects/glove/ | https://nlp.stanford.edu/pubs/glove.pdf | Converted to w2v format with `python -m gensim.scripts.glove2word2vec -i <fname> -o glove-twitter-50.txt` | dimensions = 50 |
| glove-wiki-gigaword-100 | Pre-trained vectors ,Wikipedia 2014 + Gigaword 5,6B tokens, 400K vocab, uncased. https://nlp.stanford.edu/projects/glove/ | https://nlp.stanford.edu/pubs/glove.pdf | Converted to w2v format with `python -m gensim.scripts.glove2word2vec -i <fname> -o glove-wiki-gigaword-100.txt` | dimensions = 100 |
| glove-wiki-gigaword-200 | Pre-trained vectors ,Wikipedia 2014 + Gigaword 5,6B tokens, 400K vocab, uncased. https://nlp.stanford.edu/projects/glove/ | https://nlp.stanford.edu/pubs/glove.pdf | Converted to w2v format with `python -m gensim.scripts.glove2word2vec -i <fname> -o glove-wiki-gigaword-200.txt` | dimentions = 200 |
| glove-wiki-gigaword-300 | Pre-trained vectors, Wikipedia 2014 + Gigaword 5, 6B tokens, 400K vocab, uncased. https://nlp.stanford.edu/projects/glove/ | https://nlp.stanford.edu/pubs/glove.pdf | Converted to w2v format with `python -m gensim.scripts.glove2word2vec -i <fname> -o glove-wiki-gigaword-300.txt` | dimensions = 300 |
| glove-wiki-gigaword-50 | Pre-trained vectors ,Wikipedia 2014 + Gigaword 5,6B tokens, 400K vocab, uncased. https://nlp.stanford.edu/projects/glove/ | https://nlp.stanford.edu/pubs/glove.pdf | Converted to w2v format with `python -m gensim.scripts.glove2word2vec -i <fname> -o glove-wiki-gigaword-50.txt` | dimension = 50 |
(generated by generate_table.py based on lists.json)
  
## How to add new dataset/model?
1. Create the `tar.gz` file of the dataset/model. 
   ```bash
   tar -cvzf - filename > filename.tar.gz
   ```
   Attention, if your dataset/model size is greater than **1800MB**, use `split` after:
   ```bash
   tar -cvzf - filename | split -d -b 1800m - filename.tar.gz_
   ```
2. Calculate checksum of your archive (or parts), you can use `md5sum filename.tar.gz` or this python function: 
   ```python
   import hashlib
   
   def calculate_md5_checksum(tar_file):
       hash_md5 = hashlib.md5()
       with open(tar_file, "rb") as f:
           for chunk in iter(lambda: f.read(4096), b""):
               hash_md5.update(chunk)
       return hash_md5.hexdigest()
    
   print(calculate_md5_checksum("filename.tar.gz"))
   ```
3. After that, create the ```__init__.py``` file for dataset/model. ```__init__.py``` file contains load_data() function. 
For datasets, this function returns the path to dataset file/folder.
For model, load_data() fucntion loads and returns the model.

4. Next, create a new release. Add model/dataset name in the fields: tag version and release title.
5. Then, upload the model/dataset tar.gz file(files in case of multipart) and ```__init__.py``` files and click on publish release.
6. Lastly, update the list.json file.

