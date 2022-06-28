# purchase_master

## 常用命令

> 安装 / 管理环境

```shell
# 安装工具 
pip install pip-tools
```
```shell
# 根据 requirement.in 生成依赖txt文件
pip-compile
```
```shell
# 同步环境
pip-sync
```

> 数据库管理
```shell
# 生成migrations文件
python manage.py makemigrations
```
```shell
# 应用迁移
python manage.py migrate
```
```shell
# 创建管理员
python manage.py createsuperuser
```