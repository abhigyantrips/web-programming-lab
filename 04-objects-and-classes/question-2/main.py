class PairGetSum:
    """Find a pair of elements from a given array whoose sum equals the specified target number."""
    
    def __init__(self, arr, target):
        self.arr = arr
        self.target = target
    
    def find_pair(self):
        for i in range(0, len(self.arr)-1):
            if self.arr[i] + self.arr[i+1] == self.target:
                print(f"Pair found! {self.arr[i]} + {self.arr[i+1]}")
                return
        
        print("Pair not found!")

def main():
    arr = [int(i) for i in input("Enter numbers for array (spaced separation): ").split()]
    target = int(input("Enter target number: "))
    
    pgs = PairGetSum(arr, target)
    pgs.find_pair()    

if __name__ == '__main__':
    main()