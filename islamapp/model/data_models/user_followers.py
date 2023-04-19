from mongoengine import fields, Document

class UserFollowers(Document):
    # TODO
    # task_id:
    # user_id:
    # user_ig_id:
    # ...

    def to_json(self):
        returnDict = {}
        for key in self.__iter__():
            try:
                val = self.__getattribute__(key)
                returnDict[key] = val
            except:
                pass
        return returnDict