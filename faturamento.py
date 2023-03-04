import json
from statistics import mean


class Faturamento:  # questao 3
    def __init__(self, filename):
        file = open(filename)
        self.data = json.load(file)

    def max(self):
        values = [k['valor'] for k in self.data]
        return max(values)

    def min(self):
        values = [k['valor'] for k in self.data if k['valor'] > 0.0]
        return min(values)

    def median(self):
        values = [k['valor'] for k in self.data if k['valor'] > 0.0]
        return mean(values)

    def dias_alem_da_media(self):
        media = self.median()
        values = [k['valor'] for k in self.data if k['valor'] > media]
        return len(values)
