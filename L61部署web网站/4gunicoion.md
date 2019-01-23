## 介绍
Gunicorn“绿色独角兽”是一个被广泛使用的高性能的Python WSGI UNIX HTTP服务器，移植自Ruby的独角兽（Unicorn ）项目,使用pre-fork worker模式，具有使用非常简单，轻量级的资源消耗，以及高性能等特点。

Gunicorn 服务器作为wsgi app的容器，能够与各种Web框架兼容（flask，django等）,得益于gevent等技术，使用Gunicorn能够在基本不改变wsgi app代码的前提下，大幅度提高wsgi app的性能。
### (了解)原理
参考 [原理](https://blog.csdn.net/jailman/article/details/78496522)
worker
### (不重要)gunicorn vs uWSGI
https://ivan-site.com/2012/10/gevent-gunicorn-vs-uwsgi/

## 安装
pip install

## 🦄配置

## 启动


