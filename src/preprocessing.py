# -*- coding: utf-8 -*-
import jieba
import pandas as pd
from sentence_transformers import SentenceTransformer
from config.settings import Config



class TextPreprocessor:
    def __init__(self):
        self.stopwords = self._load_stopwords(Config.STOPWORDS_PATH)
        self.model = SentenceTransformer(Config.SENTENCE_MODEL_PATH)

    def _load_stopwords(self, path):
        with open(path, 'r', encoding='utf-8') as f:
            return set(f.read().splitlines())

    def process(self, text):
        words = jieba.cut(text)
        return ' '.join([w for w in words if w not in self.stopwords and w.strip()])

    def run(self):
        df = pd.read_csv(Config.DATA_PATH)
        df['processed'] = df['content'].apply(self.process)
        df['embedding'] = self.model.encode(df['processed'].tolist()).tolist()
        return df

