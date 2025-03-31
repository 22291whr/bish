import umap
import hdbscan
import pandas as pd
from config.settings import Config

class TextCluster:
    def __init__(self, df):
        self.df = df
        self.embeddings = [eval(e) for e in df['embedding']]  # 从字符串转换回列表

    def reduce_dimension(self):
        reducer = umap.UMAP(random_state=42)
        return reducer.fit_transform(self.embeddings)

    def cluster(self, reduced_embeddings):
        clusterer = hdbscan.HDBSCAN(min_cluster_size=Config.CLUSTER_MIN_SIZE)
        return clusterer.fit_predict(reduced_embeddings)

    def run(self):
        reduced = self.reduce_dimension()
        self.df['cluster'] = self.cluster(reduced)
        return self.df