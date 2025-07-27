import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib.patches import Rectangle, Circle, FancyBboxPatch
import matplotlib.patches as mpatches

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 设置样式
sns.set_style("whitegrid")
plt.style.use('seaborn-v0_8')

def create_ml_diagram():
    """创建机器学习示意图"""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # 数据点
    x = np.random.normal(0, 1, 50)
    y = 2 * x + np.random.normal(0, 0.5, 50)
    
    # 绘制数据点
    ax.scatter(x, y, alpha=0.6, s=50, color='#3B82F6')
    
    # 绘制拟合线
    z = np.polyfit(x, y, 1)
    p = np.poly1d(z)
    ax.plot(x, p(x), "r--", linewidth=2, color='#EF4444')
    
    # 添加标签
    ax.set_xlabel('输入特征', fontsize=12)
    ax.set_ylabel('预测输出', fontsize=12)
    ax.set_title('机器学习：监督学习示例', fontsize=14, fontweight='bold')
    
    # 添加图例
    ax.legend(['拟合线', '训练数据'], loc='upper left')
    
    plt.tight_layout()
    plt.savefig('ml_diagram.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_deep_learning_diagram():
    """创建深度学习示意图"""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # 定义网络层
    layers = ['输入层', '隐藏层1', '隐藏层2', '输出层']
    neurons = [4, 6, 4, 1]
    
    # 绘制网络结构
    y_positions = np.linspace(0, 1, max(neurons))
    
    for i, (layer, n_neurons) in enumerate(zip(layers, neurons)):
        x_pos = i * 2
        for j in range(n_neurons):
            y_pos = y_positions[j] if j < len(y_positions) else 0.5
            circle = Circle((x_pos, y_pos), 0.1, color='#3B82F6', alpha=0.7)
            ax.add_patch(circle)
            
            # 连接到下一层
            if i < len(layers) - 1:
                next_n = neurons[i + 1]
                for k in range(next_n):
                    next_y = y_positions[k] if k < len(y_positions) else 0.5
                    ax.plot([x_pos + 0.1, x_pos + 1.9], [y_pos, next_y], 
                           'gray', alpha=0.3, linewidth=0.5)
        
        # 添加层标签
        ax.text(x_pos, -0.1, layer, ha='center', va='top', fontsize=10, fontweight='bold')
    
    ax.set_xlim(-0.5, 6.5)
    ax.set_ylim(-0.2, 1.2)
    ax.set_title('深度学习：神经网络结构', fontsize=14, fontweight='bold')
    ax.axis('off')
    
    plt.tight_layout()
    plt.savefig('deep_learning.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_gnn_diagram():
    """创建图神经网络示意图"""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # 定义节点位置
    nodes = {
        'A': (1, 3), 'B': (2, 4), 'C': (3, 3),
        'D': (1, 2), 'E': (2, 1), 'F': (3, 2)
    }
    
    # 定义边
    edges = [('A', 'B'), ('B', 'C'), ('A', 'D'), ('B', 'E'), ('C', 'F'), ('D', 'E'), ('E', 'F')]
    
    # 绘制边
    for edge in edges:
        x1, y1 = nodes[edge[0]]
        x2, y2 = nodes[edge[1]]
        ax.plot([x1, x2], [y1, y2], 'gray', alpha=0.6, linewidth=2)
    
    # 绘制节点
    for node, (x, y) in nodes.items():
        circle = Circle((x, y), 0.2, color='#10B981', alpha=0.8)
        ax.add_patch(circle)
        ax.text(x, y, node, ha='center', va='center', fontsize=12, fontweight='bold', color='white')
    
    ax.set_xlim(0, 4)
    ax.set_ylim(0, 5)
    ax.set_title('图神经网络：分子图结构', fontsize=14, fontweight='bold')
    ax.axis('off')
    
    plt.tight_layout()
    plt.savefig('gnn_diagram.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_automation_lab_diagram():
    """创建自动化实验示意图"""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # 绘制实验台
    lab_bench = Rectangle((0, 0), 8, 1, color='#6B7280', alpha=0.3)
    ax.add_patch(lab_bench)
    
    # 绘制机器人臂
    robot_arm = Rectangle((1, 1), 0.2, 2, color='#374151', alpha=0.8)
    ax.add_patch(robot_arm)
    
    # 绘制实验设备
    equipment_positions = [(2, 0.2), (4, 0.2), (6, 0.2)]
    for i, (x, y) in enumerate(equipment_positions):
        equipment = Rectangle((x, y), 0.8, 0.6, color='#3B82F6', alpha=0.7)
        ax.add_patch(equipment)
        ax.text(x + 0.4, y + 0.3, f'设备{i+1}', ha='center', va='center', fontsize=8)
    
    # 绘制数据流
    for i in range(3):
        ax.arrow(2.5 + i*2, 1.5, 0, -0.5, head_width=0.1, head_length=0.1, 
                fc='#EF4444', ec='#EF4444', alpha=0.7)
    
    ax.set_xlim(0, 8)
    ax.set_ylim(0, 4)
    ax.set_title('自动化实验：机器人实验平台', fontsize=14, fontweight='bold')
    ax.axis('off')
    
    plt.tight_layout()
    plt.savefig('automation_lab.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_active_learning_diagram():
    """创建主动学习示意图"""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # 绘制数据点
    x1 = np.random.normal(0, 1, 30)
    y1 = np.random.normal(0, 1, 30)
    x2 = np.random.normal(3, 1, 20)
    y2 = np.random.normal(3, 1, 20)
    
    # 已标记数据
    ax.scatter(x1, y1, c='#3B82F6', s=50, alpha=0.7, label='已标记数据')
    ax.scatter(x2, y2, c='#3B82F6', s=50, alpha=0.7)
    
    # 未标记数据
    x_unlabeled = np.random.uniform(-2, 5, 50)
    y_unlabeled = np.random.uniform(-2, 5, 50)
    ax.scatter(x_unlabeled, y_unlabeled, c='#9CA3AF', s=30, alpha=0.5, label='未标记数据')
    
    # 高价值样本（主动学习选择）
    high_value_x = np.random.uniform(1, 2, 5)
    high_value_y = np.random.uniform(1, 2, 5)
    ax.scatter(high_value_x, high_value_y, c='#EF4444', s=100, alpha=0.8, 
               marker='*', label='主动学习选择')
    
    ax.set_xlabel('特征1', fontsize=12)
    ax.set_ylabel('特征2', fontsize=12)
    ax.set_title('主动学习：智能样本选择', fontsize=14, fontweight='bold')
    ax.legend()
    
    plt.tight_layout()
    plt.savefig('active_learning.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_generative_model_diagram():
    """创建生成模型示意图"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # GAN示意图
    ax1.set_title('生成对抗网络 (GAN)', fontsize=12, fontweight='bold')
    
    # 生成器
    generator = Rectangle((0.5, 0.3), 1, 0.4, color='#3B82F6', alpha=0.7)
    ax1.add_patch(generator)
    ax1.text(1, 0.5, '生成器', ha='center', va='center', fontsize=10, fontweight='bold')
    
    # 判别器
    discriminator = Rectangle((2.5, 0.3), 1, 0.4, color='#EF4444', alpha=0.7)
    ax1.add_patch(discriminator)
    ax1.text(3, 0.5, '判别器', ha='center', va='center', fontsize=10, fontweight='bold')
    
    # 箭头
    ax1.arrow(1.5, 0.5, 0.8, 0, head_width=0.05, head_length=0.05, fc='black', ec='black')
    ax1.arrow(2.5, 0.5, -0.8, 0, head_width=0.05, head_length=0.05, fc='black', ec='black')
    
    ax1.set_xlim(0, 4)
    ax1.set_ylim(0, 1)
    ax1.axis('off')
    
    # VAE示意图
    ax2.set_title('变分自编码器 (VAE)', fontsize=12, fontweight='bold')
    
    # 编码器
    encoder = Rectangle((0.5, 0.3), 1, 0.4, color='#10B981', alpha=0.7)
    ax2.add_patch(encoder)
    ax2.text(1, 0.5, '编码器', ha='center', va='center', fontsize=10, fontweight='bold')
    
    # 潜在空间
    latent = Rectangle((2, 0.3), 1, 0.4, color='#F59E0B', alpha=0.7)
    ax2.add_patch(latent)
    ax2.text(2.5, 0.5, '潜在空间', ha='center', va='center', fontsize=10, fontweight='bold')
    
    # 解码器
    decoder = Rectangle((3.5, 0.3), 1, 0.4, color='#8B5CF6', alpha=0.7)
    ax2.add_patch(decoder)
    ax2.text(4, 0.5, '解码器', ha='center', va='center', fontsize=10, fontweight='bold')
    
    # 箭头
    ax2.arrow(1.5, 0.5, 0.3, 0, head_width=0.05, head_length=0.05, fc='black', ec='black')
    ax2.arrow(3, 0.5, 0.3, 0, head_width=0.05, head_length=0.05, fc='black', ec='black')
    
    ax2.set_xlim(0, 5)
    ax2.set_ylim(0, 1)
    ax2.axis('off')
    
    plt.tight_layout()
    plt.savefig('generative_model.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_quantum_algorithm_diagram():
    """创建量子算法示意图"""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # 绘制量子比特
    qubit_positions = [(1, 3), (2, 3), (3, 3), (4, 3)]
    for i, (x, y) in enumerate(qubit_positions):
        circle = Circle((x, y), 0.2, color='#8B5CF6', alpha=0.8)
        ax.add_patch(circle)
        ax.text(x, y, f'Q{i+1}', ha='center', va='center', fontsize=10, fontweight='bold', color='white')
    
    # 绘制量子门
    gate_positions = [(1.5, 2), (2.5, 2), (3.5, 2)]
    gate_names = ['H', 'CNOT', 'RZ']
    for i, ((x, y), name) in enumerate(zip(gate_positions, gate_names)):
        gate = Rectangle((x-0.2, y-0.1), 0.4, 0.2, color='#EF4444', alpha=0.7)
        ax.add_patch(gate)
        ax.text(x, y, name, ha='center', va='center', fontsize=10, fontweight='bold', color='white')
    
    # 绘制量子电路线
    for i in range(4):
        ax.plot([1, 4], [3-i*0.1, 3-i*0.1], 'gray', alpha=0.6, linewidth=2)
    
    # 添加标签
    ax.text(0.5, 3, '输入', ha='right', va='center', fontsize=10, fontweight='bold')
    ax.text(4.5, 3, '输出', ha='left', va='center', fontsize=10, fontweight='bold')
    
    ax.set_xlim(0, 5)
    ax.set_ylim(1.5, 3.5)
    ax.set_title('量子算法：量子电路', fontsize=14, fontweight='bold')
    ax.axis('off')
    
    plt.tight_layout()
    plt.savefig('quantum_algorithm.png', dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    print("正在生成核心技术示意图...")
    
    create_ml_diagram()
    print("✓ 机器学习示意图已生成")
    
    create_deep_learning_diagram()
    print("✓ 深度学习示意图已生成")
    
    create_gnn_diagram()
    print("✓ 图神经网络示意图已生成")
    
    create_automation_lab_diagram()
    print("✓ 自动化实验示意图已生成")
    
    create_active_learning_diagram()
    print("✓ 主动学习示意图已生成")
    
    create_generative_model_diagram()
    print("✓ 生成模型示意图已生成")
    
    create_quantum_algorithm_diagram()
    print("✓ 量子算法示意图已生成")
    
    print("\n所有技术示意图已生成完成！") 