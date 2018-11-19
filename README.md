# website_py
web方面的轮子 django + nginx + mysql + docker + gunicorn 

## 目录
 * [IDE部署说明](#IDE部署说明)
 * [docker部署说明](#docker部署说明)
 * [参考文章](#参考文章)

## IDE部署说明：    

## docker部署说明

* 部署命令

```bash
docker-compose up -d db     #启动数据库
docker-compose up -d web    #启动django
docker-compose up -d nginx  #启动nginx
```
注意:
> 1. 本地调试不需要启动nginx, 端口号8000  
> 2. nginx启用的是https, 要自行添加ssl证书

## 参考文章

[docker-compose部署django+nginx+mysql项目](https://blog.csdn.net/bbwangj/article/details/81170010)  
[Docker部署Web应用（Django）](https://blog.csdn.net/hbnn111/article/details/77176629)