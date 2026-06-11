class DynamicArray:
    
    def __init__(self, capacity: int):
        if capacity<=0:
            raise ValueError("capacity should be >0")
        self.capacity=capacity
        self.arraylist=[0]*capacity
        self.size=0
        
    def get(self, i: int) -> int:
        if i<0:
            raise ValueError("i should be non negative integer")
        return self.arraylist[i]

    def set(self, i: int, n: int) -> None:
        if i<0:
            raise ValueError("i should be non negative integer")
        self.arraylist[i]=n  
        # return self.arraylist[i]

    def pushback(self, n: int) -> None:
        if self.getSize() == self.getCapacity():
            self.resize()
        self.arraylist[self.getSize()]=n
        self.size +=1

    def popback(self) -> int:
        val=self.arraylist[self.getSize()-1]
        self.size -=1
        return val
 

    def resize(self) -> None:
        self.capacity=2*self.capacity
        new_arr=[0]*self.capacity
        for i in range(self.size):
            new_arr[i]=self.arraylist[i]
        self.arraylist=new_arr


    def getSize(self) -> int:
        return self.size
        
    
    def getCapacity(self) -> int:
        return self.capacity

###Unit test

# import unittest

# class TestDynamicArray(unittest.TestCase):

#     def test_initial_state(self):
#         arr = DynamicArray(3)
#         self.assertEqual(arr.get(0),0)
#         self.assertEqual(arr.getSize(),0)
#         arr.pushback(55)
#         self.assertEqual(arr.getSize(),1)

# if __name__ == "__main__":
#     unittest.main()
