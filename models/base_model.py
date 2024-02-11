#!/usr/bin/python3
'''we define a classBase'''
import uuid
from datetime import datetime
import models


class BaseModel:
    '''it s a class parent'''

    def __init__(self, *args, **kwargs):
        '''creat new base'''
        if **kwargs is 0:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for (k, v) in kwargs.items():
                if k == "created_at" or v == "update_at":
                    self.__dict__[k] = datetime.strptime(v,
                            "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[k] = v
    def __str__(self):
        '''the string representation of an instance'''
        return f"[{}] ({}) {}".format(self.__class__.__name__,
                self.id, self.__dict__)

    def save(self):
        '''update the update_at'''
        self.update_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        '''return a dictinary containing keys/values'''
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["created_at"] = self.created_at.isoformat()
        return new_dict
