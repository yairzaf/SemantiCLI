import numpy as np
import onnxruntime as ort
from tokenizers import Tokenizer
import json
from pathlib import Path
from appdirs import user_data_dir
from typing import List, Optional

from semanticli.model.install import MODELS_DIR

class Model():
    def __init__(self, model_name: str):
        model_dir = MODELS_DIR / model_name.replace('/','-')
        if not model_dir.exists():
            print("Model {modname} doesn't exist, please install using --im model-name.".format(modnam = model_name))

        self.session = ort.InferenceSession(str(model_dir / "model.onnx"))

        self.model_inputs = [input.name for input in self.session.get_inputs()]

        self.tokenizer = Tokenizer.from_file(str(model_dir / "tokenizer.json"))

        self.config = {}
        if (model_dir / "config.json").exists():
            with open(model_dir / "config.json") as f:
                self.config = json.load(f)
        
        self.max_length = self.config.get("max_position_embeddings", 512)
        
        self.tokenizer.enable_padding(
            pad_id=0,  # Default pad token id
            pad_token="[PAD]",
            length=self.max_length
        )
        
        self.tokenizer.enable_truncation(max_length=self.max_length)

    def __call__(self, texts: List[str]) -> np.ndarray:
        
        encoded = self.tokenizer.encode_batch(texts)
        
        model_inputs = {}
        
        model_inputs['input_ids'] = np.array([e.ids for e in encoded], dtype=np.int64)
        model_inputs['attention_mask'] = np.array([e.attention_mask for e in encoded], dtype=np.int64)
        
        if 'token_type_ids' in self.model_inputs:
            model_inputs['token_type_ids'] = np.zeros_like(model_inputs['input_ids'], dtype=np.int64)
        
        outputs = self.session.run(None, model_inputs)
        embeddings = outputs[0]
        
        return embeddings