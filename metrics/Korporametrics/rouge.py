from .metric import Metric


class ROUGE(Metric):
    def __init__(self, min_n=1, max_n=5):
        self.n = [n for n in range(min_n, max_n + 1)]
        self.name = 'ROUGE'

    def evaluate(self, references, hypotheses):
        raise NotImplementedError
