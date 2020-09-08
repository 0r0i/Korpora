class Metric:
    name = None

    def evaluate(self, true_values, predicted_values, **kargs):
        raise NotImplementedError('Implement `evaluate` function')

    def multiprocessing(self, true_values, predicted_values, n_jobs=2, chunk_size=100):
        raise NotImplementedError

    def __call__(self, true_values, predicted_values, **kargs):
        return self.evaluate(true_values, predicted_values, **kargs)

    def __str__(self):
        return f'Korporametric.Metric({self.name})'

