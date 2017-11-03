# gensim-data
## How to add new dataset/model?
1. Create the tar.gz file of the dataset/model.
2. Now, find the value of checksum of this tar.gz file. Use the function below : 
```
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
5. Then, upload the model/dataset tar.gz file and ```__init__.py``` files and click on publish release.
6. Lastly, update the list.json file.

