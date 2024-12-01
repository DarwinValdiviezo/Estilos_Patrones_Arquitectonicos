class ConfigManager:
    _instance = None
    _config = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def set(self, key, value):
        self._config[key] = value

    def get(self, key):
        return self._config.get(key)
