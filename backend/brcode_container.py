class BRCodeContainer:
    def __init__(self):
        self.container = {}
    def push_back(self,item_name: str,item_brcode_type,item_brcode):
        self.container[item_name] = {"brcode_type":item_brcode_type,"brcode":item_brcode}
    def get(self):
        return self.container
    def __iter__(self):
        for key,value in self.container.items():
            yield key,value["brcode_type"],value["brcode"]
    def __repr__(self):
        repr_string = "<BRCodeContainer("
        for k, v in self.container.items():
            repr_string += f"\t{k}={v},\n"
        repr_string += ")>"
        return repr_string