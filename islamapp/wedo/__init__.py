# celery 實例初始化 
# __init__.py
from celery import Celery
app = Celery('wedo')  # 創建 Celery 實例
app.config_from_object('wedo.config') 

# 配置 wedo.config
# config.py
BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
CELERY_RESULT_SERIALIZER = 'json' # 結果序列化方案
CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24 # 任務過期時間
CELERY_TIMEZONE='Asia/Shanghai'   # 時區配置
CELERY_IMPORTS = (     # 指定導入的任務模塊,可以指定多個
    'wedo.tasks',
    'wedo.period_task'
)