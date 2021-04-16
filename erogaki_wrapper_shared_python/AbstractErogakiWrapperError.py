from json import JSONEncoder
from erogaki_wrapper_shared_python.ErogakiWrapperConfig import config

class AbstractErogakiWrapperErrorJsonEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, AbstractErogakiWrapperError):
            return {
                "component": obj.component,
                "instance": obj.instance,
                "name": obj.__class__.__name__,
                "description": obj.description
            }

class AbstractErogakiWrapperError(Exception):
    def __init__(self, description):
        self.description = description
        self.instance = config.instance
        self.json = AbstractErogakiWrapperErrorJsonEncoder().encode(self)
