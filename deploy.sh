#!/bin/bash

# AI For Science 网站部署脚本
# 使用方法: ./deploy.sh your-domain.com

DOMAIN=$1

if [ -z "$DOMAIN" ]; then
    echo "使用方法: ./deploy.sh your-domain.com"
    exit 1
fi

echo "🚀 开始部署 AI For Science 网站到 $DOMAIN"

# 1. 创建网站目录
echo "📁 创建网站目录..."
sudo mkdir -p /var/www/$DOMAIN
sudo cp -r . /var/www/$DOMAIN/
sudo chown -R www-data:www-data /var/www/$DOMAIN
sudo chmod -R 755 /var/www/$DOMAIN

# 2. 创建Nginx配置文件
echo "⚙️ 配置Nginx..."
sudo tee /etc/nginx/sites-available/$DOMAIN > /dev/null <<EOF
server {
    listen 80;
    server_name $DOMAIN www.$DOMAIN;
    root /var/www/$DOMAIN;
    index index.html;

    # 启用Gzip压缩
    gzip on;
    gzip_vary on;
    gzip_min_length 1024;
    gzip_types text/plain text/css text/xml text/javascript application/javascript application/xml+rss application/json;

    # 安全头
    add_header X-Frame-Options "SAMEORIGIN" always;
    add_header X-XSS-Protection "1; mode=block" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header Referrer-Policy "no-referrer-when-downgrade" always;
    add_header Content-Security-Policy "default-src 'self' http: https: data: blob: 'unsafe-inline'" always;

    # 缓存设置
    location ~* \.(css|js|png|jpg|jpeg|gif|ico|svg)$ {
        expires 1y;
        add_header Cache-Control "public, immutable";
    }

    location / {
        try_files \$uri \$uri/ /index.html;
    }

    # 错误页面
    error_page 404 /404.html;
    error_page 500 502 503 504 /50x.html;
}
EOF

# 3. 启用站点
echo "🔗 启用Nginx站点..."
sudo ln -sf /etc/nginx/sites-available/$DOMAIN /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx

# 4. 安装SSL证书（Let's Encrypt）
echo "🔒 安装SSL证书..."
sudo apt update
sudo apt install -y certbot python3-certbot-nginx

# 获取SSL证书
sudo certbot --nginx -d $DOMAIN -d www.$DOMAIN --non-interactive --agree-tos --email admin@$DOMAIN

# 5. 设置自动续期
echo "⏰ 设置证书自动续期..."
sudo crontab -l 2>/dev/null | { cat; echo "0 12 * * * /usr/bin/certbot renew --quiet"; } | sudo crontab -

# 6. 创建备份脚本
echo "💾 创建备份脚本..."
sudo tee /var/www/backup.sh > /dev/null <<EOF
#!/bin/bash
BACKUP_DIR="/var/backups/website"
DATE=\$(date +%Y%m%d_%H%M%S)
mkdir -p \$BACKUP_DIR
tar -czf \$BACKUP_DIR/$DOMAIN_\$DATE.tar.gz -C /var/www $DOMAIN
find \$BACKUP_DIR -name "*.tar.gz" -mtime +7 -delete
EOF

sudo chmod +x /var/www/backup.sh

# 7. 创建更新脚本
echo "🔄 创建更新脚本..."
sudo tee /var/www/update.sh > /dev/null <<EOF
#!/bin/bash
cd /var/www/$DOMAIN
git pull origin main
sudo systemctl reload nginx
echo "网站更新完成！"
EOF

sudo chmod +x /var/www/update.sh

echo "✅ 部署完成！"
echo "🌐 网站地址: https://$DOMAIN"
echo "📧 管理邮箱: admin@$DOMAIN"
echo "🔧 更新命令: sudo /var/www/update.sh"
echo "💾 备份命令: sudo /var/www/backup.sh" 