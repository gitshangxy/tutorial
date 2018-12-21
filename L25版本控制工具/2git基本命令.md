git基本命令
===
## 准备工作
打开git bash或cmd终端。cd到项目文件夹根目录下。 cd \pycharm尚小雨\testgit
- git config --global user.email "你的邮箱"
- git config --global user.name "你的名字"
- git init 。初始化本地仓库git，会看到项目文件夹下生成 .git隐藏文件夹，这个文件夹会记录以后的更改和提交。


## 常用命令
- git add 文件名 。跟踪一个文件 。 git add 1.py 。
- git add .  。跟踪当前文件夹下所有文件。
- git commit -m "开发新功能"
- git checkout master
- git checkout newfeature
- git merge 副分支 。合并副分支内容到当前分支。

## 分支
添加新分支
git branch new
  git rebase        提交历史

(*newfeature) git add .         git commit -m ""
(*newfeature) git checkout master 
(*master) git merge newfeature    这样就会把新分支的修改合并到主分支之下

## 撤回
 （用到再百度）
 撤回add  文件
 撤回commit  记录
 
 ## 还原
 git log 查看提交记录


