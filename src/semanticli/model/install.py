import os
import sys
from pathlib import Path
import requests
from appdirs import user_data_dir
from shutil import rmtree

DEFAULT_MODEL = "mixedbread-ai/mxbai-embed-large-v1"

MODELS_DIR = Path(user_data_dir("semanticli")) / "models"
HUB_URL = "https://huggingface.co"
HUB_URL_OPTIONS = "/resolve/main/"
CHUNK_SIZE = 8192

# full url example
# "https://huggingface.co/mixedbread-ai/mxbai-embed-large-v1/resolve/main/onnx/model.onnx?download=true"
# model_name = mixedbread-ai/mxbai-embed-large-v1

def download_model(model_name , hub=HUB_URL , url_options = HUB_URL_OPTIONS):
    print("Downloading " + model_name + " from: " + hub)
    model_dir = MODELS_DIR / model_name.replace('/','-')
    print("Model dir: "+str(model_dir))
    model_dir.mkdir(parents=True, exist_ok=True)
    repo_url = hub + "/"  + model_name + url_options
    url_append = "?dowload=true"
    download_file(model_name,"model.onnx",model_dir,repo_url,"onnx/",url_append)
    download_file(model_name,"tokenizer.json",model_dir,repo_url,file_url_append=url_append)
    download_file(model_name,"config.json",model_dir,repo_url,file_url_append=url_append)
    print("Successfully downloaded " + model_name +".")

def download_file(model_name,file_name, model_dir, repo_url, file_url_prepend="", file_url_append=""):
    file_path = model_dir / file_name
    if file_path.exists(): 
        os.remove(str(file_path))
    file_url = repo_url + file_url_prepend + file_name + file_url_append
    print("Downloading {fname}...".format(fname=file_name))
    response = requests.get(file_url, stream=True)
    if not response.ok:
        print("Couldn't find: " + file_url)
        print("Check model name, repo or internet connection.")
        delete_model(model_name)
        sys.exit(1)
        #response.raise_for_status()
    with open(file_path, "wb") as f:
        downloaded_bytes = 0
        for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
            f.write(chunk)
            downloaded_bytes += CHUNK_SIZE
            print(" Downloaded: " + str(downloaded_bytes/1000000) + " MBs.",end='\r')

    print("{fname} downloaded successfully".format(fname=file_name))

def delete_model(model_name):
    model_dir = MODELS_DIR / model_name.replace('/','-')
    print("Removing: "+str(model_dir))
    if not model_dir.exists():
        print("Model doesn't exist")
        sys.exit(1)
    rmtree(MODELS_DIR / model_name, onerror=remove_failed)

def remove_failed():
    print("Failed removing model, check priviliges.")
    sys.exit(1)

def list_models():
    for item in MODELS_DIR.iterdir():
        if item.is_dir():
            print(item.name)

def first_run():
    if not MODELS_DIR.exists():
        print("First time run, Installing default embeddings model...")
        download_model(DEFAULT_MODEL)