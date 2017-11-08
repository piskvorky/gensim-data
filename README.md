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
  
## How to add new dataset/model?
1. Create the tar.gz file of the dataset/model. In case, dataset/model size is greater than 2Gb, use:
```tar cz data-file-name|split -d -b 2Gib - data-name.tar.gz_```
This will split the dataset/model into files of <=2Gb.
2. Now, find the value of checksum of this tar.gz(in case of multiple parts, find separate checksum of each) file. Use the function below : 
```
import hashlib
def calculate_md5_checksum(tar_file):
    hash_md5 = hashlib.md5()
    with open(tar_file, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()
```
3. After that, create the ```__init__.py``` file for dataset/model. ```__init__.py``` file contains load_data() function. 
For datasets, this function returns the path to dataset file/folder.
For model, load_data() fucntion loads and returns the model.

4. Next, create a new release. Add model/dataset name in the fields: tag version and release title.
5. Then, upload the model/dataset tar.gz file(files in case of multipart) and ```__init__.py``` files and click on publish release.
6. Lastly, update the list.json file.

