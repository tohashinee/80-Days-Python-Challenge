#•	Day 7: Write a script to insert, delete, and slice elements from a dynamic list without using high-level list methods.
class CustomDynamicList:
    def __init__(self, initial_capacity=4):
        self.capacity = initial_capacity
        self.size = 0
        self.array = [None] * self.capacity

    #Method to create a new array
    def _resize(self,new_capacity):
        newarray = [None] * new_capacity
        for i in range (self.size):
            newarray[i] = self.array[i]
        self.array = newarray
        self.initial_capacity = new_capacity

    def display(self):
        """Displays the elements currently stored in the dynamic list."""
        elements = []
        for i in range(self.size):
            elements.append(self.array[i])  # Standard list conversion for easy printing
        return elements

    def append(self,datavalue):
        if self.size == self.capacity:
            self._resize(self.capacity * 2)
        self.array[self.size] = datavalue
        self.size += 1

    #Writing a method for insert
    def insert(self,index,datavalue):
        if index<0 or index >= self.size:
            print("Index Out of Bounds")
        if self.size == self.initial_capacity:
            self._resize(self.initial_capacity*2)

        for i in range(self.size,index,-1):
            self.array[i] = self.array[i-1]

        self.array[index] = datavalue

    def delete(self,datavalue):
        index = -1
        for i in range(self.size):
            if self.array[i] == datavalue:
                index = i
                break

        if index == -1:
            raise ValueError("Data value not found")
        
        for i in range(index,self.size-1):
            self.array[i] = self.array[i+1]

        self.array[self.size-1] = None
        self.size-=1
        if 0 < self.size <= self.capacity //4:
            self._resize(self.capacity//2)

    def slice(self,start,end):
        if start <0: max(0,self.size+start)
        if end <0: end = max(0, self.size+end)

        start = min(start, self.size)
        end = min(end, self.size)
        
        sliced_list = CustomDynamicList(initial_capacity=max(4, end - start))
        
    # Manually extract and append items into the slice
        for i in range(start, end):
            sliced_list.append(self.array[i])
            
        return sliced_list


# --- Demonstration ---
if __name__ == "__main__":
    # Initialize list
    my_list = CustomDynamicList()
    
    # 1. Populate the list
    for x in range(6):
        my_list.append(x)
    print("Initial list:", my_list.display())

    # 2. Insert element at index 2
    my_list.insert(2, 25)
    print("After inserting 25 at index 2:", my_list.display())

    # 3. Delete element at index 1
    my_list.delete(1)
    print("After deleting element - 1:", my_list.display())

    # 4. Slice the list from index 1 to 3
    sliced_result = my_list.slice(1,3)
    print("Sliced list (indices 1 to 3):", sliced_result.display())





        






    
