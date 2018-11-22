import pymysql

# 打开数据库连接
conn = pymysql.connect(
    host="127.0.0.1",
    port=3333,
    user="root",
    passwd="123456",
    db="dataname",
    charset='utf8'
)  # 要指定编码，否则中文可能乱码

# 获取操作游标
cursor = conn.cursor()

if __name__ == '__main__':
    if cursor:
        command = "INSERT INTO dataname.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES (1, 'pbkdf2_sha256$120000$fNEvAahUVi7V$vC5gL6MN2Su1IMTB25Ukon+AfKt950oNRcqcVKCk49Q=', null, 1, 'niracler', '', '', '1026037967@qq.com', 1, 1, '2018-11-22 14:08:44.200183')"
        # 使用execute方法执行SQL语句
        cursor.execute(command)
        # 提交到数据库执行
        conn.commit()
        # 关闭数据库连接
        conn.close()
