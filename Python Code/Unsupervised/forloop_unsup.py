class ForLoop:
    def __init__(self):
        self.w_i = 0
        self.w_j = 0
        self.w_k = 0

    def for_until_loop(self):
        self.w_i = 0
        while self.w_i <= 20:
            self.w_j = self.w_i
            self.w_i += 1
            while self.w_j <= 20:
                self.w_k = self.w_j * self.w_i
                print(f'UNTIL: {self.w_i} W-K: {self.w_k} = {self.w_j} * {self.w_i}')
                self.w_j += 1

    def for_varying_loop(self):
        self.w_i = self.w_j = self.w_k = 0
        for self.w_i in range(1, 21):
            self.w_j = self.w_i
            for self.w_j in range(1, 21):
                self.w_k = self.w_j * self.w_i
                print(f'VARYING: {self.w_i} W-K: {self.w_k} = {self.w_j} * {self.w_i}')

if __name__ == "__main__":
    for_loop = ForLoop()
    for_loop.for_until_loop()
    for_loop.for_varying_loop()
