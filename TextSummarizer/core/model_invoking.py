from TextSummarizer.utils.load_config import LoadConfig

class TextSummarizer:
    def __init__(self):
        self.config_loader = LoadConfig()

        self.tokenizer = self.config_loader.tokenizer
        self.model = self.config_loader.model
        self.max_input_length = self.config_loader.max_input_length
        self.max_summary_length = self.config_loader.max_summary_length
        self.min_summary_length = self.config_loader.min_summary_length
        self.num_beams = self.config_loader.num_beams
        self.length_penalty = self.config_loader.length_penalty
    
    def summarize_text(self, text):
        t5_input = "summarize: " + text

        inputs = self.tokenizer.encode(
            t5_input,
            return_tensors="pt",
            max_length=self.max_input_length,
            truncation=True
        )

        summary_ids = self.model.generate(
            inputs,
            max_length=self.max_summary_length,
            min_length=self.min_summary_length,
            length_penalty=self.length_penalty,
            num_beams=self.num_beams,
            early_stopping=True
        )

        return self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)
