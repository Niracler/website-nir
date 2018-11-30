# website_py
web方面的轮子 django + nginx + mysql + docker + gunicorn 

## 目录
 * [IDE部署说明](#IDE部署说明)
 * [docker部署说明](#docker部署说明)
 * [联系](#联系)
 * [参考文章](#参考文章)

## IDE运行说明：    
 - 安装依赖的包
 ```bash
 pip3 install --upgrade pip
 pip3 install -r  requirements.txt
 ```

 - 修改settings.py, 将数据库的host改为127.0.0.1
 - 修改docker-compose.yml, 将3306端口映射出来
 - 启动并建立数据库
```bash
docker-compose up -d db     #启动数据库
python3 manage.py migrate
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser # 创建超级用户
```
 - 启动项目
```bash
python3 manage.py runserver 8000
```

## docker部署说明

* 部署命令

```bash
docker-compose up -d db     #启动数据库
docker-compose up -d web    #启动django
docker-compose up -d nginx  #启动nginx
```
注意:
> 1. 本地调试不需要启动, nginx, 端口号8000, 没有静态文件  
> 2. nginx启用的是https, 要自行添加ssl证书

## 联系
项目需要完善的地方还有很多，如有BUG或者更好的建议欢迎提出

* [issue](https://github.com/Niracler/website-nir/issues)
* mail:niracler@gmail.com

## 参考文章

[docker-compose部署django+nginx+mysql项目](https://blog.csdn.net/bbwangj/article/details/81170010)  
[Docker部署Web应用（Django）](https://blog.csdn.net/hbnn111/article/details/77176629)