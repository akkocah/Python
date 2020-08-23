class Pagination:
    def __init__(self, items=[], pageSize=10):
        self.items = items
        self.pageSize = int(pageSize)
        self.totalPages = (len(items)//pageSize) + \
                           (1 if len(items) % pageSize else 0)
        self.currentPage = 1
    def getItems(self):
        return self.items
    def getPageSize(self):
        return self.pageSize
    def getCurrentPage(self):
        return self.currentPage
    def prevPage(self):
        if self.currentPage != 1:
            self.currentPage -= 1
        return self
    def nextPage(self):
        if self.currentPage != self.totalPages:
            self.currentPage += 1
        return self
    def firstPage(self):
        self.currentPage = 1
        return self
    def lastPage(self):
        self.currentPage = self.totalPages
        return self
    def goToPage(self, pageNum):
        if 1 < int(pageNum) <= self.totalPages:
            self.currentPage = int(pageNum)
        elif int(pageNum) <= 1:
            self.currentPage = 1
        else:
            self.currentPage = self.totalPages
        return self
    def getVisibleItems(self):
        return self.items[(self.currentPage-1)*self.pageSize:self.currentPage*self.pageSize]
alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 9)
print(p.getVisibleItems())  # ["a", "b", "c", "d"]
p.nextPage()
print(p.getVisibleItems())  # ['e', 'f', 'g', 'h']
p.lastPage()
print(p.getVisibleItems())  # ["y", "z"]
print(p.getCurrentPage())

###########################################################3333
class Pagination:
    def __init__(self, items, pageSize):
        self.items = items
        self.pageSize = pageSize
        self.totalPage = len(self.items)//self.pageSize + (1 if len(self.items) % self.pageSize != 0 else 0)
        self.defaultPage = 1
    def goToPage(self, page):
        self.defaultPage = page
        return self
    def firstPage(self):
        self.defaultPage = 1
        return self
    def nextPage(self):
        if self.defaultPage != self.totalPage:
            self.defaultPage += 1
        return self
    def prevPage(self):
        if self.defaultPage != 1:
            self.defaultPage -= 1
        return self
    def lastPage(self):
        self.defaultPage = self.TotalPage
        return self
    def getVisibleItems(self):
        return self.items[(self.defaultPage-1) * self.pageSize : self.defaultPage * self.pageSize]
alphabetList = list("abcdefghijklmnopqrstuvwxyz")
s = Pagination(alphabetList, 5)
print(s.getVisibleItems())
s.nextPage()
print(s.getVisibleItems())
s.nextPage().nextPage().nextPage()
print(s.getVisibleItems())
s.goToPage(3)
print(s.getVisibleItems())
s.goToPage(3).nextPage()
print(s.getVisibleItems())