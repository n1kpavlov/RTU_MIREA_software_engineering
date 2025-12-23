class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.length = 0

    def _get_index(self, key):
        return hash(key) % self.size

    def __setitem__(self, key, value):
        index = self._get_index(key)
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))
        self.length += 1

    def __getitem__(self, key):
        index = self._get_index(key)
        bucket = self.table[index]

        for k, v in bucket:
            if k == key:
                return v

        raise KeyError(f"Key '{key}' not found")

    def __len__(self):
        return self.length

    def __str__(self):
        return str(self.table)



ht = HashTable()

ht['name'] = 'Alice'
ht['age'] = 30
ht[42] = 'The answer'

print(ht['name'])
print(ht['age'])
print(ht[42])

try:
    print(ht['unknown'])
except KeyError as e:
    print(e)

print(len(ht))

ht['age'] = 31
print(ht['age'])