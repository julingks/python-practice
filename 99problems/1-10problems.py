import unittest

class NinetyNineProblemsFixture(unittest.TestCase):
    # 01.Find the last element of a list.
    def test01(self):
        def find_last(l):
            return l[-1]
        l = [1,2,3,4,5,6,7,8,9]
        self.assertEqual(9, find_last(l))


    # 02.Find the last but one element of a list.
    def test02(self):
        def findLastButOne(l):
            return l[-2]
        l = [1,2,3,4,5,6,7,8,9]
        self.assertEqual(8, findLastButOne(l))


    # 03.Find the K'th element of a list
    def test03(self):
        def findKthElement(l, k):
            return l[k-1]
        l = [1,2,3,4,5,6,7,8,9]
        self.assertEqual(3, findKthElement(l,3))


    # 04.Find the number of elements of a list
    def test04(self):
        def findTheNumberOfElements(l):
            return len(l)
        l = [1,2,3,4,5,6,7,8,9]
        self.assertEqual(9, findTheNumberOfElements(l))


    # 05.Reverse a lists
    def test05(self):
        def reverseList(l):
            return list(reversed(l))
        def reverseManual(l):
            return l[::-1]
        l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        reversed_l = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        self.assertEqual(reversed_l, reverseList(l))
        self.assertEqual(reversed_l, reverseManual(l))

if __name__ == '__main__':
      unittest.main()
