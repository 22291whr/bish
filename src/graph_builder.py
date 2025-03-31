import networkx as nx
from pyvis.network import Network
from config.settings import Config

class GraphVisualizer:
    def __init__(self, df, relations):
        self.df = df
        self.relations = relations
        self.G = nx.DiGraph()

    def build_graph(self):
        # 添加节点
        for _, row in self.df.iterrows():
            self.G.add_node(
                row['id'],
                label=f"{row['id']}: {row['content'][:20]}...",
                group=row['cluster']
            )
        # 添加边
        for rel in self.relations:
            self.G.add_edge(rel[1], rel[2], label=rel[0])
        return self.G
    # def _get_color(self, cluster_id):
    #     """为不同聚类分配颜色"""
    #     colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4']
    #     return colors[cluster_id % len(colors)]
    #
    # def _get_edge_color(self, rel_type):
    #     """为不同关系类型分配颜色"""
    #     color_map = {
    #         '时序': '#FF9999',
    #         '补充': '#99CC99',
    #         '因果': '#FFD700',
    #         '替代': '#CC99FF'
    #     }
    #     return color_map.get(rel_type, '#666666')

    def visualize(self):
        net = Network(notebook=True, directed=True, height="800px")
        net.from_nx(self.G)

        # # 调整物理引擎参数防止节点重叠
        # net.set_options("""
        # {
        #   "physics": {
        #     "stabilization": {
        #       "enabled": true,
        #       "iterations": 1000
        #     },
        #     "repulsion": {
        #       "nodeDistance": 200
        #     }
        #   }
        # }
        # """)
        net.show_buttons(filter_=['physics', 'nodes', 'edges'])
        net.save_graph(Config.OUTPUT_HTML)