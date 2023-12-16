# Implement every design pattern possible, even if unnecessary 
class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class DataProcessor(metaclass=SingletonMeta):
    def process(self, data):
        return data[::-1]

class Factory:
    @staticmethod
    def get_processor():
        return DataProcessor()

class Adapter:
    def __init__(self, processor):
        self.processor = processor
    def process(self, data):
        return ''.join(self.processor.process(data))

factory = Factory()
processor = factory.get_processor()
adapter = Adapter(processor)
result = adapter.process("DesignPatterns")