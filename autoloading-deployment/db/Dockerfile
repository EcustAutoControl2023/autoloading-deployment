FROM mysql:latest

# 解决中文编码问题
COPY ./hmy.cnf /etc/mysql/conf.d/hmy.cnf

# 修改权限
RUN chmod 644 /etc/mysql/conf.d/hmy.cnf
