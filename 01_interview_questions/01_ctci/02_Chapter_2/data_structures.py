from typing import Any


class Node:
    def __init__(self, data: Any = None) -> None:
        self.data = data
        self.next: "Node" = None

    def get_data(self) -> Any:
        return self.data

    def get_next(self) -> "Node":
        return self.next

    def set_data(self, data: Any) -> None:
        self.data = data

    def set_next(self, next: "Node") -> None:
        self.next = next

    def __repr__(self):
        return "Node(" + str(self.data) + ")"


class UnorderedList:
    """
    Unordered list (items are not sorted)
    Every element added:
        (self.head = old_head)
        Old head becomes "next" of new element. (new.next = old_head))
        Becomes head (new == self.head)

        Head points to next.
        Last element has no "next".

    """

    def __init__(self) -> None:
        self.head: Node = None

    def is_empty(self) -> bool:
        return self.head == None

    def add(self, item: Any) -> None:
        temp = Node(item)
        old_head = self.head
        temp.set_next(old_head)
        self.head = temp

    def add_to_tail(self, item: Any) -> None:
        temp = Node(item)
        temp_last = self.head
        while temp_last.get_next():
            temp_last = temp_last.get_next()
        temp_last.set_next(temp)

    def length(self) -> int:
        count = 0
        current_node = self.head

        while current_node != None:
            count += 1
            current_node = current_node.get_next()

        return count

    def search(self, item: Any) -> bool:
        current_node = self.head
        found = False

        while not found and current_node != None:
            if current_node.get_data() == item:
                found = True
            else:
                current_node = current_node.get_next()

        return found

    def remove(self, item: Any) -> None:
        """
        Note: item must be a *value* not a "Node"
        """
        current_node = self.head
        previous_node = None
        found = False

        while not found:
            if current_node.get_data() == item:
                found = True
            else:
                previous_node = current_node
                current_node = current_node.get_next()

        if previous_node is None:
            self.head = current_node.get_next()
        else:
            previous_node.set_next(current_node.get_next())

    def __repr__(self) -> str:
        out = [self.head]
        temp_last = self.head
        while temp_last.get_next():
            temp_last = temp_last.get_next()
            out.append(temp_last)
        return "head -> [" + " ".join([str(x) for x in out]) + "]"


if __name__ == "__main__":
    u = UnorderedList()
    u.add(3)
    print(u.head)
    u.add(4)
    print(u.head)
    u.add_to_tail(5)
    print(u.head)
    print(u)
    u.remove(4)
    print(u)
    print(u.search(5))
    print(u.search(4))
