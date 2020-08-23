class Name:

    def __init__(self, fname, lname):
        self.fname = fname.title()
        self.lname = lname.title()
        self.fullname = self.fname +" " +  self.lname
        self.initials = self.fname[0] + "."+ self.lname[0] 


a1 = Name("john", "SMITH")
print(a1.fname)
print(a1.fullname)
print(a1.initials)