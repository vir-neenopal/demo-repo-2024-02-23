# sample_class.py
import pandas as pd

class SampleClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}!", f"{pd.DataFrame(data = {'col1': [1, 2], 'col2': [3, 4]})}"
