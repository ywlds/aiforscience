#!/bin/bash

echo "🚀 开始设置 GitHub Pages 部署..."

# 检查是否在Website目录中
if [ ! -f "index.html" ]; then
    echo "❌ 请在Website目录中运行此脚本"
    exit 1
fi

# 初始化Git仓库
echo "📁 初始化Git仓库..."
git init

# 添加所有文件
echo "📝 添加文件到Git..."
git add .

# 创建第一次提交
echo "💾 创建初始提交..."
git commit -m "Initial commit: AI For Science website"

echo "✅ Git仓库初始化完成！"
echo ""
echo "📋 接下来的步骤："
echo "1. 在GitHub上创建新仓库"
echo "2. 运行以下命令连接远程仓库："
echo "   git remote add origin https://github.com/你的用户名/仓库名.git"
echo "   git branch -M main"
echo "   git push -u origin main"
echo ""
echo "3. 在GitHub仓库设置中启用Pages："
echo "   Settings > Pages > Source: Deploy from a branch > main"
echo ""
echo "4. 等待几分钟，你的网站就会在以下地址可用："
echo "   https://你的用户名.github.io/仓库名" 