class PowerSetClass:
    """Get all possible unique subsets from a set of distinct integers."""
    
    def __init__(self, arr):
        self.arr = arr
    
    def power_set_generator(self):
        power_set = []
        
        for i in range(2**(len(self.arr))):
            subset = []
            for j in range(len(self.arr)):
                if (i & (1<<j)):
                    subset.append(self.arr[j])
            
            if subset not in power_set:
                power_set.append(subset)
        
        return power_set

def main():
    arr = [int(i) for i in input("Enter numbers for array (spaced separation): ").split()]
    psc = PowerSetClass(arr)
    power_set = psc.power_set_generator()
    
    print(power_set)

if __name__ == '__main__':
    main()