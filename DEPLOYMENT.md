# 🚀 AI For Science 网站部署指南

## 📋 部署前准备

### 1. 域名准备
- 购买域名（推荐：阿里云、腾讯云、GoDaddy等）
- 确保域名已实名认证
- 记录域名的DNS服务器信息

### 2. 服务器准备
- 云服务器（推荐：阿里云、腾讯云、AWS、DigitalOcean）
- 操作系统：Ubuntu 20.04+ 或 CentOS 8+
- 至少1GB内存，20GB存储空间

## 🌐 部署方式

### 方式一：免费静态托管（推荐新手）

#### 1. GitHub Pages
```bash
# 1. 创建GitHub仓库
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/你的用户名/aiforscience.git
git push -u origin main

# 2. 启用GitHub Pages
# 进入仓库设置：Settings > Pages
# Source: Deploy from a branch > main > Save
# 获得域名：https://你的用户名.github.io/aiforscience
```

#### 2. Netlify（推荐）
1. 注册 [Netlify](https://netlify.com)
2. 点击 "New site from Git"
3. 连接GitHub仓库或直接拖拽 `Website` 文件夹
4. 自动获得域名：`https://你的项目名.netlify.app`
5. 自定义域名：在Site settings > Domain management中添加

#### 3. Vercel
```bash
# 安装Vercel CLI
npm install -g vercel

# 部署
cd Website
vercel

# 按提示操作，获得域名
```

### 方式二：云服务器部署

#### 步骤1：连接服务器
```bash
ssh root@你的服务器IP
```

#### 步骤2：安装必要软件
```bash
# 更新系统
sudo apt update && sudo apt upgrade -y

# 安装Nginx
sudo apt install -y nginx

# 安装Docker（可选）
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker $USER
```

#### 步骤3：上传网站文件
```bash
# 方法1：使用scp
scp -r Website/* root@你的服务器IP:/var/www/html/

# 方法2：使用Git
git clone https://github.com/你的用户名/aiforscience.git
sudo cp -r aiforscience/Website/* /var/www/html/
```

#### 步骤4：配置域名DNS
在域名管理平台添加A记录：
- 类型：A
- 主机记录：@
- 记录值：你的服务器IP
- 主机记录：www
- 记录值：你的服务器IP

#### 步骤5：使用部署脚本
```bash
# 给脚本执行权限
chmod +x deploy.sh

# 运行部署脚本
./deploy.sh yourdomain.com
```

### 方式三：Docker部署

#### 1. 修改配置文件
编辑 `docker-compose.yml` 和 `nginx.conf`，将 `yourdomain.com` 替换为你的实际域名。

#### 2. 启动服务
```bash
# 创建必要目录
mkdir -p ssl logs webroot

# 启动服务
docker-compose up -d

# 查看日志
docker-compose logs -f
```

## 🔒 SSL证书配置

### Let's Encrypt（免费）
```bash
# 安装Certbot
sudo apt install -y certbot python3-certbot-nginx

# 获取证书
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com

# 测试自动续期
sudo certbot renew --dry-run
```

### 手动配置SSL
```bash
# 生成自签名证书（仅用于测试）
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
-keyout /etc/ssl/private/nginx-selfsigned.key \
-out /etc/ssl/certs/nginx-selfsigned.crt
```

## 📊 性能优化

### 1. 启用Gzip压缩
已在Nginx配置中启用

### 2. 浏览器缓存
```nginx
# 静态资源缓存1年
location ~* \.(css|js|png|jpg|jpeg|gif|ico|svg)$ {
    expires 1y;
    add_header Cache-Control "public, immutable";
}
```

### 3. CDN加速
- 使用阿里云CDN、腾讯云CDN等
- 配置静态资源缓存策略

## 🔧 维护命令

### 更新网站
```bash
# 方法1：直接替换文件
sudo cp -r 新文件/* /var/www/html/

# 方法2：使用Git
cd /var/www/html
git pull origin main
sudo systemctl reload nginx
```

### 查看日志
```bash
# Nginx访问日志
sudo tail -f /var/log/nginx/access.log

# Nginx错误日志
sudo tail -f /var/log/nginx/error.log

# 系统日志
sudo journalctl -u nginx -f
```

### 备份网站
```bash
# 创建备份
sudo tar -czf backup_$(date +%Y%m%d).tar.gz /var/www/html

# 恢复备份
sudo tar -xzf backup_20240101.tar.gz -C /
```

## 🛡️ 安全配置

### 1. 防火墙设置
```bash
# 安装UFW
sudo apt install -y ufw

# 配置防火墙
sudo ufw allow ssh
sudo ufw allow 'Nginx Full'
sudo ufw enable
```

### 2. 安全头配置
已在Nginx配置中添加安全头

### 3. 定期更新
```bash
# 更新系统
sudo apt update && sudo apt upgrade

# 更新Nginx
sudo apt install --only-upgrade nginx
```

## 📈 监控和分析

### 1. 访问统计
```bash
# 安装GoAccess
sudo apt install -y goaccess

# 生成报告
goaccess /var/log/nginx/access.log -o /var/www/html/report.html --log-format=COMBINED
```

### 2. 性能监控
- 使用Google Analytics
- 配置Google Search Console
- 设置Uptime监控

## 🚨 故障排除

### 常见问题

#### 1. 网站无法访问
```bash
# 检查Nginx状态
sudo systemctl status nginx

# 检查端口
sudo netstat -tlnp | grep :80
sudo netstat -tlnp | grep :443

# 检查防火墙
sudo ufw status
```

#### 2. SSL证书问题
```bash
# 检查证书状态
sudo certbot certificates

# 重新获取证书
sudo certbot --nginx -d yourdomain.com
```

#### 3. 性能问题
```bash
# 检查磁盘空间
df -h

# 检查内存使用
free -h

# 检查CPU使用
top
```

## 📞 技术支持

如果遇到问题，可以：
1. 查看Nginx错误日志
2. 检查DNS解析是否正确
3. 确认防火墙设置
4. 验证SSL证书状态

---

**部署完成后，你的AI For Science网站就可以通过 `https://yourdomain.com` 访问了！** 