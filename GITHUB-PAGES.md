# 🌐 GitHub Pages 部署指南

## 📋 步骤详解

### 步骤1：在GitHub上创建仓库

1. 登录 [GitHub](https://github.com)
2. 点击右上角的 "+" 号，选择 "New repository"
3. 填写仓库信息：
   - **Repository name**: `aiforscience` (或你喜欢的名字)
   - **Description**: `AI For Science 官方网站`
   - **Visibility**: 选择 Public (免费) 或 Private
   - **不要**勾选 "Add a README file"
4. 点击 "Create repository"

### 步骤2：上传网站文件

在本地终端中执行以下命令：

```bash
# 进入Website目录
cd Website

# 给脚本执行权限
chmod +x setup-github.sh

# 运行设置脚本
./setup-github.sh
```

### 步骤3：连接GitHub仓库

```bash
# 替换为你的GitHub用户名和仓库名
git remote add origin https://github.com/你的用户名/aiforscience.git

# 设置主分支名称
git branch -M main

# 推送到GitHub
git push -u origin main
```

### 步骤4：启用GitHub Pages

1. 在GitHub仓库页面，点击 "Settings" 标签
2. 在左侧菜单中找到 "Pages"
3. 在 "Source" 部分：
   - 选择 "Deploy from a branch"
   - Branch 选择 "main"
   - Folder 选择 "/ (root)"
4. 点击 "Save"

### 步骤5：等待部署

- GitHub会自动构建和部署你的网站
- 通常需要1-5分钟
- 部署完成后，你会看到绿色的勾号

## 🌐 访问你的网站

### 免费域名格式
```
https://你的用户名.github.io/aiforscience
```

### 示例
- 如果你的GitHub用户名是 `john`
- 仓库名是 `aiforscience`
- 那么你的网站地址就是：`https://john.github.io/aiforscience`

## 🔧 自定义域名（可选）

### 添加自定义域名
1. 在仓库的 "Settings" > "Pages" 中
2. 在 "Custom domain" 部分输入你的域名
3. 点击 "Save"
4. 在你的域名管理平台添加CNAME记录：
   ```
   类型: CNAME
   主机记录: @ (或 www)
   记录值: 你的用户名.github.io
   ```

### 强制HTTPS
- GitHub Pages 自动提供HTTPS
- 在 "Pages" 设置中勾选 "Enforce HTTPS"

## 📝 更新网站

每次修改网站后，需要推送到GitHub：

```bash
# 添加修改的文件
git add .

# 提交修改
git commit -m "更新网站内容"

# 推送到GitHub
git push origin main
```

GitHub会自动重新部署你的网站。

## 🎨 自定义设置

### 修改网站信息
编辑 `index.html` 中的内容：
- 修改标题和描述
- 更新联系信息
- 添加你的个人资料

### 修改样式
编辑 `styles.css`：
- 更改颜色主题
- 调整布局
- 添加新的动画效果

### 添加功能
编辑 `script.js`：
- 添加新的交互功能
- 集成第三方服务
- 添加分析代码

## 📊 监控和统计

### 查看访问统计
1. 在仓库的 "Insights" 标签
2. 查看 "Traffic" 部分
3. 可以看到页面访问量

### 添加Google Analytics
在 `index.html` 的 `<head>` 部分添加：

```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_MEASUREMENT_ID');
</script>
```

## 🚨 常见问题

### 网站无法访问
1. 检查仓库是否为Public
2. 确认Pages设置正确
3. 等待几分钟让部署完成

### 样式不显示
1. 检查CSS文件路径
2. 确认文件已正确上传
3. 清除浏览器缓存

### 更新不生效
1. 确认代码已推送到GitHub
2. 等待自动部署完成
3. 强制刷新浏览器 (Ctrl+F5)

## 🎯 优势

- ✅ **完全免费**
- ✅ **自动HTTPS**
- ✅ **全球CDN**
- ✅ **自动部署**
- ✅ **版本控制**
- ✅ **易于维护**

## 📞 技术支持

如果遇到问题：
1. 检查GitHub Pages文档
2. 查看仓库的 "Actions" 标签了解部署状态
3. 在GitHub社区寻求帮助

---

**恭喜！你的AI For Science网站现在可以通过GitHub Pages访问了！** 