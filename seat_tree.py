

from collections import deque

class SeatNode:
    def __init__(self, seat_no):
        self.seat_no = seat_no
        self.booked = False
        self.passenger = None
        self.left = None
        self.right = None


class SeatTree:
    def __init__(self, total_seats):
        self.root = self._build_tree(1, total_seats)

    def _build_tree(self, start, end):
        if start > end:
            return None
        mid = (start + end) // 2
        node = SeatNode(mid)
        node.left = self._build_tree(start, mid - 1)
        node.right = self._build_tree(mid + 1, end)
        return node

    # -------- Seat Allocation (DFS) --------
    def allocate_seat(self, passenger_name=None):
        return self._dfs_allocate(self.root, passenger_name)

    def _dfs_allocate(self, node, passenger_name):
        if not node:
            return None
        if not node.booked:
            node.booked = True
            node.passenger = passenger_name
            return node.seat_no
        left = self._dfs_allocate(node.left, passenger_name)
        if left:
            return left
        return self._dfs_allocate(node.right, passenger_name)

    def free_seat(self, seat_no):
        self._dfs_free(self.root, seat_no)

    def _dfs_free(self, node, seat_no):
        if not node:
            return
        if node.seat_no == seat_no:
            node.booked = False
            node.passenger = None
            return
        self._dfs_free(node.left, seat_no)
        self._dfs_free(node.right, seat_no)

    def count_available(self):
        return self._count(self.root)

    def _count(self, node):
        if not node:
            return 0
        return (0 if node.booked else 1) + self._count(node.left) + self._count(node.right)

    # -------- Admin Traversals --------
    def _traverse_with_passenger(self, node, res, order):
        if not node:
            return
        if order == "pre":
            res.append((node.seat_no, node.passenger))
        self._traverse_with_passenger(node.left, res, order)
        if order == "in":
            res.append((node.seat_no, node.passenger))
        self._traverse_with_passenger(node.right, res, order)
        if order == "post":
            res.append((node.seat_no, node.passenger))

    def preorder(self):
        res = []
        self._traverse_with_passenger(self.root, res, "pre")
        return res

    def inorder(self):
        res = []
        self._traverse_with_passenger(self.root, res, "in")
        return res

    def postorder(self):
        res = []
        self._traverse_with_passenger(self.root, res, "post")
        return res

    def level_order(self):
        if not self.root:
            return []
        q = deque([self.root])
        res = []
        while q:
            node = q.popleft()
            res.append((node.seat_no, node.passenger))
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return res

