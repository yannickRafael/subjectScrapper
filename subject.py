import json

from cachecontrol.serialize import Serializer


#subject class
class Subject :
    def __init__(self, name, identifier, ref):
        self.name = name
        self.identifier = identifier
        self.ref = ref

#encoder to transform into json
class SubjectEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Subject):
            return {"nome": obj.name, "codigo": obj.identifier, "cursoId": obj.ref}
