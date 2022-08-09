#!/usr/bin/python3
"class Base file, that control all"


import uuid
from datetime import datetime


class BaseModel:
    " class base"


    def __init__(self):
        "initialize instance"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        "print name class, id and doc"
        return "[{}] {} {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        "save update"
        self.updated_at = datetime.now()

    def to_dict(self):
        "return dictionnary representation"
        own_dict = self.__dict__.copy()
        own_dict['__class__'] = self.__class__.__name__
        own_dict['created_at'] = own_dict['created_at'].isoformat()
        own_dict['updated_at'] = own_dict['updated_at'].isoformat()
        return own_dict
