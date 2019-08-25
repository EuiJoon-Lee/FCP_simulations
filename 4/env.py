class Env:
    def __init__(self, default_pool, pool, rate, tobin, name):
        self.default_pool = default_pool
        self.pool = pool
        self.rate = rate
        self.tobin = tobin
        self.name = name

    def change_rate(self, rate):
        self.rate = rate

    def change_tobin(self, tobin):
        self.tobin = tobin

    def change_pool(self, amount, add=True):
        if add:
            self.pool=self.pool + amount
        else: 
            self.pool=self.pool - amount

    def reg_pool(self, target):
        if self.pool < self.default_pool:
            self.pool=self.pool + target
            if self.pool > self.default_pool:
                self.pool=self.default_pool
        elif self.pool > self.default_pool:
            self.pool=self.pool - target
            if self.pool < self.default_pool:
                self.pool=self.default_pool
        return self.pool
