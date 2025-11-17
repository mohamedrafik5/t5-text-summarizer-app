import os
import yaml
from transformers import T5ForConditionalGeneration, T5Tokenizer

class LoadConfig:
    def __init__(self):
        self.root_dir = os.path.abspath(
            os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)
        )

        self.config_path = os.path.join(self.root_dir, "TextSummarizer", "config", "config.yaml")

        with open(self.config_path, "r") as file:
            self.config = yaml.safe_load(file)
        self._load_config()
        self.tokenizer, self.model = self._load_model()

    def _load_config(self):
        model_cfg = self.config["model"]
        self.model_name = model_cfg["name"]
        self.max_summary_length = model_cfg["max_summary_length"]
        self.min_summary_length = model_cfg["min_summary_length"]
        self.max_input_length = model_cfg["max_input_length"]
        self.num_beams = model_cfg["num_beams"]
        self.length_penalty = model_cfg["length_penalty"]

    def _load_model(self):
        self.tokenizer = T5Tokenizer.from_pretrained(self.model_name) 
        self.model = T5ForConditionalGeneration.from_pretrained(self.model_name)
        return self.tokenizer, self.model