#!/usr/bin/python3
"""
base class
"""
import json
import os.path


class Base:
    """A class named Base
    Attributes:
    attr1(__nb_objects): number of objects
    attr2(id): object id
    """
    __nb_object = 0

    def __init__(self, id=None):
        """Initiliazes"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_object += 1
            self.id = Base.__nb_object

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        l = []
        if list_objs is None:
            with open(cls.__name__ + ".json", "w",  encoding='utf-8') as file:
                file.write(Base.to_json_string(l))
            return l
        for model in list_objs:
            list_dictionaries.append(model.to_dictionary())
        with open(cls.__name__ + ".json", "w",  encoding='utf-8') as file:
            file.write(Base.to_json_string(l))

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation json_string
        """
        L = []
        if json_string is None or json_string == "":
            return L
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        create a dummy
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
        def load_from_file_csv(cls):
            """ Deserializes CSV and load """
            filename = cls.__name__ + ".csv"

            try:
                with open(filename, encoding="utf-8") as myfile:
                    r = csv.reader(myfile)
                    if cls.__name__ == "Rectangle":
                        attr = ["id", "width", "height", "x", "y"]
                    elif cls.__name__ == "Square":
                        attr = ["id", "size", "x", "y"]
                    inslist = []
                    for row in r:
                        ct, dic = 0, {}
                        for i in row:
                            dic[attr[ct]] = int(i)
                            ct += 1
                        inslist.append(cls.create(**dic))
                    return inslist
            except IOError:
                return []
