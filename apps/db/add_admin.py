import pymysql

# 打开数据库连接
conn = pymysql.connect(
    host="db",
    port=3306,
    user="root",
    passwd="123456",
    db="dataname",
    charset='utf8'
)  # 要指定编码，否则中文可能乱码

# 获取操作游标
cursor = conn.cursor()

if __name__ == '__main__':
    if cursor:
        command = "INSERT INTO users_userprofile (id, password, last_login, is_superuser, username, first_name, last_name, is_staff, is_active, date_joined, name, email) VALUES (2, 'pbkdf2_sha256$120000$4GDngwkqLjqB$bImkmCX0dfHUoCpQLOOOJjEI8g9csZ1HN/A0GFahdVM=', null, 1, 'remember', '', '', 1, 1, '2019-02-28 01:57:23.531668', null, '1026037967@qq.com')"
        # 使用execute方法执行SQL语句
        cursor.execute(command)
        # 提交到数据库执行
        conn.commit()
        # 关闭数据库连接
        conn.close()
