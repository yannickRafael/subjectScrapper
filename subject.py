import json

from cachecontrol.serialize import Serializer



class Subject :
    def __init__(self, name, identifier, ref):
        self.name = name
        self.identifier = identifier
        self.ref = ref


class SubjectEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Subject):
            return {"nome": obj.name, "codigo": obj.identifier, "cursoId": obj.ref}
