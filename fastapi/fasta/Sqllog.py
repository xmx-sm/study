TORTOISE_ORM = {
    'connections': {
        # 定义了要使用的数据库连接。可以定义多个连接，每个都有自己的别名。
        'default': {
            # 'engine': 'tortoise.backends.asyncpg',  # 如果使用 PostgreSQL，则取消此行注释并指定为 asyncpg 引擎
            'engine': 'tortoise.backends.mysql',  # 使用 MySQL 或 MariaDB 数据库时，指定 MySQL 引擎
            'credentials': {
                'host': '127.0.0.1',  # 数据库服务器的主机地址；这里指本地主机
                'port': '3306',       # 数据库服务器监听的端口；MySQL 默认是 3306
                'user': 'root',       # 登录数据库的用户名
                'password': '000117',  # 用户对应的密码，请确保妥善保管你的密码
                'database': 'cckj',  # 要连接的具体数据库名称
                'minsize': 1,         # 连接池中最小空闲连接数；至少保持 1 个连接
                'maxsize': 15,         # 连接池中最大连接数；最多允许同时有 5 个连接
                'charset': 'utf8mb4', # 字符集编码，确保支持完整的 Unicode 编码，包括表情符号等
                "echo": True          # 是否开启 SQL 查询日志输出，对于调试很有用
            }
        },
    },
    'apps': {
        # 定义了应用程序和它们关联的模型。可以有多个应用程序，每个都有自己的模型集合。
        'models': {
            'models': ['models', "aerich.models"],  # 列出包含模型的所有模块路径。'models' 是用户定义的模型，而 'aerich.models' 是由 Aerich 工具自动生成的迁移模型
            'default_connection': 'default',        # 指定默认使用的数据库连接别名
        }
    },
    'use_tz': False,  # 是否启用时区支持；False 表示不使用时区（即所有时间都是本地时间）
    'timezone': 'Asia/Shanghai'  # 当 use_tz 设置为 True 时，这指定了应用程序应该使用的时区。这里设置为中国上海的时区
}