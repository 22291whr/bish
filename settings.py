# # -*- coding: utf-8 -*-
# # config/settings.py
# import os
#
#
# class Config:
#     BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # 项目根目录
#
#     DATA_PATH = os.path.join(BASE_DIR, "data/texts.csv")
#     STOPWORDS_PATH = os.path.join(BASE_DIR, "data/stopwords.txt")
#     OUTPUT_HTML = os.path.join(BASE_DIR, "outputs/graph.html")
#     SENTENCE_MODEL_PATH = os.path.join(BASE_DIR, "model")
#

# -*- coding: utf-8 -*-

# Load model directly
# from transformers import AutoModel
#
# model = AutoModel.from_pretrained("THUDM/glm-4-9b-chat", trust_remote_code=True)

class Config:
    # 模型配置
    LOCAL_MODEL_PATH = "./model"
    CLUSTER_MIN_SIZE = 3  # 聚类最小分组大小

    # 路径配置
    STOPWORDS_PATH = "./data/stopwords.txt"  # 停用词表路径
    DATA_PATH = "./data/texts.csv"  # 原始数据路径
    OUTPUT_HTML = "./outputs/graph.html"  # 图谱输出路径

    # 关系标注阈值
    SIMILARITY_THRESHOLD = 0.6  # 补充关系相似度阈值
