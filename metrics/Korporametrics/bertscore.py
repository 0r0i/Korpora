from .metric import Metric


class BERTScore(Metric):
    def __init__(self, bert_model, idf=None):
        super().__init__()
        self.name = 'BERTScore'
        self.bert_model = bert_model

    def evaluate(self, hypotheses, references):
        raise NotImplementedError('Will be implemented')

    def train_idf(self, paths):
        """
        Args:
            paths (list of str or str) file path
        """
        raise NotImplementedError

    def save_model(self, root_dir, model_name):
        raise NotImplementedError

    @classmethod
    def from_pretrained(self, model_name_or_path):
        raise NotImplementedError

