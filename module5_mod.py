class NumberCollection:
    def __init__(self):
        self.numbers = []

    def insert_number(self, num):
        self.numbers.append(num)

    def search_number(self, x):
        # Return 1-based index if found, else -1
        for i, num in enumerate(self.numbers):
            if num == x:
                return i + 1  # 1-based index
        return -1
