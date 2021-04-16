import os
from uuid import uuid4

class ErogakiWrapperRedisConfig:
    def __init__(self):
        self.hostname = os.environ["REDIS_HOSTNAME"] if "REDIS_HOSTNAME" in os.environ else "localhost"
        self.port = int(os.environ["REDIS_PORT"]) if "REDIS_PORT" in os.environ else 6379
        self.db = int(os.environ["REDIS_DB"]) if "REDIS_DB" in os.environ else 0

class ErogakiWrapperConfig:
    def __init__(self):
        self.instance = uuid4()
        self.redis = ErogakiWrapperRedisConfig()
