import random

class BubbleSort:
    def __init__(self):
        self.len_arr = 10
        self.arr = [0]*self.len_arr
        self.min_num = 1
        self.max_num = 99

    def generate_random_num(self):
        for i in range(self.len_arr):
            self.arr[i] = random.randint(self.min_num, self.max_num)
            print(f'Unsorted: {self.arr[i]}')

    def sorting_array(self):
        for j in range(self.len_arr):
            for k in range(self.len_arr - 1):
                if self.arr[k] > self.arr[k + 1]:
                    self.arr[k], self.arr[k + 1] = self.arr[k + 1], self.arr[k]
        
        for h in range(self.len_arr):
            print(f'Sorted: {self.arr[h]}')

if __name__ == "__main__":
    bubble_sort = BubbleSort()
    bubble_sort.generate_random_num()
    bubble_sort.sorting_array()
