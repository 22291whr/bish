from preprocessing import TextPreprocessor
from clustering import TextCluster
from relation import RelationAnnotator
from graph_builder import GraphVisualizer


def main():
    # 数据预处理
    preprocessor = TextPreprocessor()
    df = preprocessor.run()

    # 文本聚类
    cluster_processor = TextCluster(df)
    clustered_df = cluster_processor.run()

    # 关系标注
    annotator = RelationAnnotator(clustered_df)
    relations = annotator.run()

    # 构建与可视化图谱
    visualizer = GraphVisualizer(clustered_df, relations)
    G = visualizer.build_graph()
    visualizer.visualize()


if __name__ == "__main__":
    main()