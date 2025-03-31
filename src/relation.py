import re
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from config.settings import Config


class RelationAnnotator:
    def __init__(self, df):
        self.df = df
        self.relations = []

    def _extract_time(self, text):
        matches = re.findall(r'\d{4}年\d{1,2}月\d{1,2}日', text)
        return matches[0] if matches else None

    def _add_relation(self, rel_type, source, target):
        if (rel_type, source, target) not in self.relations:
            self.relations.append((rel_type, source, target))

    def _process_pair(self, a, b):
        # 时序关系
        time_a = self._extract_time(a['content'])
        time_b = self._extract_time(b['content'])
        if time_a and time_b:
            if time_a < time_b:
                self._add_relation('时序', a['id'], b['id'])
            else:
                self._add_relation('时序', b['id'], a['id'])

        # 相似度关系
        sim = cosine_similarity([a['embedding']], [b['embedding']])[0][0]
        if sim > Config.SIMILARITY_THRESHOLD:
            self._add_relation('补充', a['id'], b['id'])

    def run(self):
        for cluster_id in self.df['cluster'].unique():
            if cluster_id == -1: continue
            group = self.df[self.df['cluster'] == cluster_id].to_dict('records')
            for i in range(len(group)):
                for j in range(i + 1, len(group)):
                    self._process_pair(group[i], group[j])
        return self.relations