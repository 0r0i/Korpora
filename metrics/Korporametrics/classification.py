from .metric import Metric


class F1(Metric):
    def __init__(self):
        self.name = 'F1'

    def evaluate(self, true_values, predicted_values):
        raise NotImplementedError


class Recall(Metric):
    def __init__(self):
        self.name = 'Recall'

    def evaluate(self, true_values, predicted_values):
        raise NotImplementedError


class Precision(Metric):
    def __init__(self):
        self.name = 'Precision'

    def evaluate(self, true_values, predicted_values):
        raise NotImplementedError


class ClasificationReport(Metric):
    def __init__(self):
        self.name = 'Classification report'

    def evaluate(self, true_values, predicted_values, return_as_dict=False):
        raise NotImplementedError


f1 = F1()
recall = Recall()
precision = Precision()
classification_report = ClassificationReport()

