class SnapshotArray:
    def __init__(self, length: int):
        self.snapshots_idx = []
        self.snapshots = {}
        self.current = {} 
        self.latest_idx = 0

    def set(self, index: int, val: int) -> None:
        self.current[index] = val
        self.latest_idx = len(self.snapshots_idx)

    def snap(self) -> int:
        if self.latest_idx == len(self.snapshots_idx):
            self.snapshots[self.latest_idx] = self.current.copy()

        self.snapshots_idx.append(self.latest_idx)
        return len(self.snapshots_idx) - 1

    def get(self, index: int, snap_id: int) -> int:
        if index in self.snapshots[self.snapshots_idx[snap_id]]:
            return self.snapshots[self.snapshots_idx[snap_id]][index]
        else:
            return 0

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)