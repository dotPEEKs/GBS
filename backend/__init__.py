class InvalidDbObject(Exception):
    pass

def extract_class_members(obj) -> str:
    class_members = [member for member in dir(obj) if not member.startswith("_")]
    for member in class_members:
        string+="%s = %s\n" % (member,getattr(obj,member))
    return string
class Repr:
    def __repr__(self):
        repr_str = "<%s " % (self.__class__.__name__) + "\n" + extract_class_members(self) + ">"
        return repr_str