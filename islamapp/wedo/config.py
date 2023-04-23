broker_url = 'redis://10.8.238.2:6379/0' # Broker配置，使用Redis作爲消息中間件
result_backend = 'redis://10.8.238.2:6379/0' # BACKEND配置，這裏使用redis
result_serializer = 'json' # 結果序列化方案
result_expires = 60 * 60 * 24 # 任務過期時間
timezone='Asia/Shanghai'   # 時區配置
imports = (     # 指定導入的任務模塊,可以指定多個
    'wedo.tasks',
    'wedo.period_task'
)