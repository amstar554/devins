#ex1

import itertools
# class Uniquesets:
#     def __init__(self, alist):
#         self.subsetlist = []
#         self.somelist = alist
#
#     def find1subsets(self, alist):
#         self.subsetlist.append((list(itertools.combinations(alist, 1))))
#         return self.subsetlist
#
#     def find2subsets(self, alist):
#         self.subsetlist.append((list(itertools.combinations(alist, 2))))
#         return self.subsetlist
#
#     def find3subsets(self, alist):
#         self.subsetlist.append((list(itertools.combinations(alist, 3))))
#         return self.subsetlist
#
# a = [1, 5, 7]
#
# abc = Uniquesets(a)
# #abc.find1subsets(a)
# #abc.find2subsets(a)
# #abc.find3subsets(a)

#ex2
class Zerodown:
    def __init__(self, alist):
        self.subsetlist = []
        self.somelist = alist

    def find_subsets(self, alist):
        subset_count = 1
        while subset_count != len(alist):
            self.subsetlist.append((list(itertools.combinations(alist, subset_count))))
            subset_count += 1
        return self.subsetlist

    def subset_adder(self):
        print(sum(list(self.subsetlist)))

a = [1,4,6,8,5]
abc = Zerodown(a)
abc.find_subsets(a)

#ask for help!