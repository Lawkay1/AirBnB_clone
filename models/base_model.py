#!/usr/bin/python3
"class Base file, that control all"


import uuid
from datetime import datetime
import models
from json import JSONEncoder


class BaseModel:
    " class base"
    def __init__(self, *args, **kwargs):
        "initialize instance"
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(
                            value,
                            '%Y-%m-%dT%H:%M:%S.%f')
                elif key == "__class__":
                    continue

                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        "print name class, id and doc"
        nameClass = self.__class__.__name__
        return "[{}] ({}) {}".format(nameClass, self.id, self.__dict__)

    def save(self):
        "save update"
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        "return dictionnary representation"
        own_dict = dict()
        own_dict['__class__'] = self.__class__.__name__

        for key, value in self.__dict__.items():
            if key in ('created_at', 'updated_at'):
                own_dict[key] = value.isoformat()
            else:
                own_dict[key] = value
        return own_dict

class BaseModelEncoder(JSONEncoder):
    """JSON Encoder BaseModel"""

    def default(self, o):
        """ default instances"""
        if isinstance(o, BaseModel):
            return o.to_dict()
        return super().default(o)
