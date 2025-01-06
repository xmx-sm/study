TORTOISE_ORM = {
    'connections': {  # 定义数据库连接
        'master': {  # 主数据库连接配置
            # 'engine': 'tortoise.backends.asyncpg',  # 如果使用PostgreSQL，请取消此行注释并注释掉下一行
            'engine': 'tortoise.backends.mysql',  # 使用MySQL或MariaDB作为数据库引擎
            'credentials': {  # 数据库连接凭证
                'host': '127.0.0.1',  # 数据库服务器地址（这里指本地）
                'port': '3306',  # MySQL默认端口
                'user': 'root',  # 数据库用户名
                'password': '000117',  # 数据库密码
                'database': 'cckj',  # 要连接的数据库名称
                'minsize': 1,  # 连接池最小连接数
                'maxsize': 5,  # 连接池最大连接数
                'charset': 'utf8mb4',  # 数据库字符集
                'echo': True  # 是否在控制台打印SQL语句（调试用）
            }
        },
        'slave': {  # 从数据库连接配置（可以用于读取操作的负载均衡）
            'engine': 'tortoise.backends.mysql',  # 使用MySQL或MariaDB作为数据库引擎
            'credentials': {  # 数据库连接凭证
                'host': '127.0.0.1',  # 数据库服务器地址（这里指本地）
                'port': '3306',  # MySQL默认端口
                'user': 'root',  # 数据库用户名
                'password': '000117',  # 数据库密码
                'database': 'cckj',  # 要连接的数据库名称
                # 'minsize': 1,  # 连接池最小连接数
                # 'maxsize': 5,  # 连接池最大连接数
                'charset': 'utf8mb4',  # 数据库字符集
                'echo': True  # 是否在控制台打印SQL语句（调试用）
            }
        },
    },
    'apps': {  # 应用程序定义
        'models': {  # 模型应用程序的配置
            'models': ['models'],  # 包含模型的模块列表(路径)，"aerich.models"是迁移工具Aerich的模型
            'default_connection': 'master',  # 默认使用的数据库连接（主连接）
        }
    },
    # 'routers': ["models"],  # 数据库路由类，用于实现读写分离等高级特性
    'use_tz': False,  # 是否启用时区支持，默认不启用
    'timezone': 'Asia/Shanghai'  # 设置时区为亚洲/上海，当`use_tz`为True时生效
}

# from tortoise import Tortoise, run_async
# async def init():
#     # Here we create a SQLite DB using file "db.sqlite3"
#     #  also specify the app name of "models"
#     #  which contain models from "app.models"
#     await Tortoise.init(
#         # 数据库连接
#         # db_url='sqlite://db.sqlite3',
#         # 连接mysql pip install aiomysql
#         db_url='mysql://root:000117@127.0.0.1:3306/cckj',
#         # 指定管理的models，__main__ 🈯️当前文件的models.Model
#         modules={'models': ['__main__']}
#     )
#     # Generate the schema
#     await Tortoise.generate_schemas()