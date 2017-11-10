import sys
import os
import shutil
import logging
import gensim.downloader as api
from gensim.downloader import base_dir

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("test-downloader-api")

logger.info(sys.version)
if os.path.exists(base_dir):
    logger.warning("REMOVE {}".format(base_dir))
    shutil.rmtree(base_dir)

info = api.info()

logger.info("Test models")
failed_models = []
for idx, model_name in enumerate(info["models"]):
    logger.info("{} ({} of {})".format(model_name, idx + 1, len(info["models"])))

    try:
        logger.info(api.load(model_name).most_similar("who"))
    except Exception as e:
        logger.critical(e)
        failed_models.append(model_name)

if failed_models:
    logger.critical("FAILED MODELS: {}".format(", ".join(failed_models)))

logger.info("Test datasets")
failed_datasets = []
for idx, dataset_name in enumerate(info["corpora"]):
    logger.info("{} ({} of {})".format(dataset_name, idx + 1, len(info["corpora"])))
    try:
        res = sum(1 for _ in api.load(dataset_name))
        if res == 0:
            raise Exception("empty dataset")

    except Exception as e:
        logger.critical(e)
        failed_datasets.append(dataset_name)

if failed_datasets:
    logger.critical("FAILED DATASETS: {}".format(", ".join(failed_datasets)))
