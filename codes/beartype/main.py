# pip install beartype

from beartype import beartype

@beartype
def greet(name: str) -> str:
    return f'Hello, {name}!'

# 正确使用 
greet('Alice')

# 如果试图传入一个非字符串类型的参数，beartype  会立即抛出类型错误。
try:
    greet(123)
except TypeError as error:
    print(error)
    
    
from typing import List, TypeVar

T = TypeVar('T')

class Stack:
    def __init__(self):
        self._container: List[T] = []

    @beartype
    def push(self, item: T) -> None:
        self._container.append(item)

    @beartype
    def pop(self) -> T:
        return self._container.pop()

# 实例化一个整数类型的栈，并尝试进行类型安全操作 
int_stack = Stack[int]()
int_stack.push(1)
int_stack.push(2)
print(int_stack.pop())  # 输出: 2