class VectorClock:
    def __init__(self):
        self.timestamps = {}

    def increment(self, node):
        if node not in self.timestamps:
            self.timestamps[node] = 0
        self.timestamps[node] += 1

    def set(self, node, value):
        self.timestamps[node] = value

    def __add__(self, other):
        result = VectorClock()
        for node in set(self.timestamps) | set(other.timestamps):
            result.timestamps[node] = max(
                self.timestamps.get(node, 0), other.timestamps.get(node, 0)
            )
        return result

    def __eq__(self, other):
        return self.timestamps == other.timestamps

    def __ne__(self, other):
        return self.timestamps != other.timestamps

    def __lt__(self, other):
        return self.is_before(other)

    def __floordiv__(self, other):
        return not self.is_before(other) and not other.is_before(self)

    def is_before(self, other):
        for node, timestamp in self.timestamps.items():
            if timestamp > other.timestamps.get(node, 0):
                return False
        for node, timestamp in other.timestamps.items():
            if timestamp > self.timestamps.get(node, 0):
                return True
        return False

    def __repr__(self):
        return str(sorted(self.timestamps.items()))


if __name__ == "__main__":
    v1 = VectorClock()
    v1.increment("A")
    v1.increment("B")

    v2 = VectorClock()
    v2.increment("C")
    v2.set("B", 2)

    print(v1, v2)
    v3 = v1 + v2
    print(v3)

    print("Equal:       v1 == v1 \t", v1 == v1)
    print("Not equal:   v1 != v2 \t", v1 != v2)
    print("Before:      v1 < v2 \t", v1 < v2)
    print("Concurrent:  v1 // v2 \t", v1 // v2)
