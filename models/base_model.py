#!usr/bin/python3
import uuid
from datetime import datetime
import models


class BaseModel:
    """"
    This class is used to create instances and managing
    The instances are utilized by other classes
    """
    # global variable for time
    TIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"
    time = datetime.now()

    def __init__(self, *args, **kwargs):
        """
        We use this function to initialize the Base class
        and create new instances of the Base class
        :param args: is not utilized
        :param kwargs:key values arguments (dictionary)
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ["created_at", "updated_at"]:
                        value = datetime.strptime(value, self.TIME_FORMAT)
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self) -> str:
        """
        :return: a str representation of the created instance
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """
        This method is used to update and save updated at datime attribute
        :return: no return
        """
        self.updated_at = datetime.now()
        models.storage.save()
        models.storage.new(self)

    def to_dict(self):
        """
        this function is used to return a dictionary of
        instance attributes
        :return: result
        """
        excluded = ['name', 'my_number']
        result = {k: v for k, v in self.__dict__.items() if k not in excluded}
        result['__class__'] = self.__class__.__name__

        for k, v in result.items():
            if isinstance(v, datetime):
                result[k] = v.isoformat()

        return result
    