import json
from os import path
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """File Storage class handles serialization and deserialization of data"""
    CLASSES = {
        'BaseModel': BaseModel,
        'User': User,
        'City': City,
        'Amenity': Amenity,
        'State': State,
        'Place': Place,
        'Review': Review
    }
    # This is the path to file storage
    __file_path = "file.json"
    # This dict stores all user records and object by the <class name>.id
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets obj in __objects with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        obj_dict = {}
        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()

        with open(self.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects if it exists"""
        if path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                obj_dict = json.load(f)

            for key, d in obj_dict.items():
                class_name, obj_id = key.split('.')
                obj_class = globals()[class_name]
                obj = obj_class(**d)
                self.__objects[key] = obj
