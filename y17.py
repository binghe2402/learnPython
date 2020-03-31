class Tree(object):
    def __init__(self,name):
        self.name = name
        self.cate = "plant"
    def __getattribute__(self,*args,**kwargs):
        if args[0] == "大树":
            print("log 大树")
            return "我爱大树"
        else:
            return object.__getattribute__(self,*args,**kwargs)
aa = Tree("大树")
print(aa.大树)
print(aa.cate)
