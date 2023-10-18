import math
from ._globals import EPSILON
class Vector:

    def __init__(self, lst):
        """
        __init__ 代表类的构造函数
        双下划线开头的变量 例如_values,代表类的私有成员
        lst是个引用，list(lst)将值复制一遍，防止用户修改值
        """
        self._values = list(lst)

    def dot(self, another):
        """向量点乘，返回结果标量"""
        assert len(self) == len(another), \
            "Error in dot product. Length of vectors must be same."
        return sum(a * b for a, b in zip(self, another))

    def norm(self):
        """返回向量的模"""
        return math.sqrt(sum(e**2 for e in self))

    def normalize(self):
        """
        归一化，规范化
        返回向量的单位向量
        此处设计到了除法: def __truediv__(self, k):
        """
        if self.norm() < EPSILON:
            raise ZeroDivisionError("Normalize error! norm is zero.")
        return Vector(self._values) / self.norm()
        # return 1 / self.norm() * Vector(self._values)
        # return Vector([e / self.norm() for e in self])

    def __truediv__(self, k):
        """返回数量除法的结果向量：self / k"""
        return (1 / k) * self

    @classmethod
    def zero(cls, dim):
        """返回一个dim维的零向量
        @classmethod 修饰符对应的函数不需要实例化，不需要 self 参数，但第一个参数需要是表示自身类的cls参数，可以来调用类的属性，类的方法，实例化对象等。
        """
        return cls([0] * dim)

    def __add__(self, another):
        """向量加法，返回结果向量"""
        assert len(self) == len(another), \
            "Error in adding. Length of vectors must be same."
        # return Vector([a + b for a, b in zip(self._values, another._values)])
        return Vector([a + b for a, b in zip(self, another)])

    def __sub__(self, another):
        """向量减法，返回结果向量"""
        assert len(self) == len(another), \
            "Error in subtracting. Length of vectors must be same."
        return Vector([a - b for a, b in zip(self, another)])

    def __mul__(self, k):
        """返回数量乘法的结果向量：self * k"""
        return Vector([k * e for e in self])

    def __rmul__(self, k):
        """
        返回数量乘法的结果向量：k * self
        self本身就是一个列表
        """
        return self * k

    def __pos__(self):
        """返回向量取正的结果向量"""
        return 1 * self

    def __neg__(self):
        """返回向量取负的结果向量"""
        return -1 * self

    def __iter__(self):
        """返回向量的迭代器"""
        return self._values.__iter__()

    def __getitem__(self, index):
        """取向量的第index个元素"""
        return self._values[index]

    def __len__(self):
        """返回向量长度（有多少个元素）"""
        return len(self._values)

    def __repr__(self):
        """打印显示：Vector([5, 2])"""
        return "Vector({})".format(self._values)

    def __str__(self):
        """打印显示：(5, 2)"""
        return "({})".format(", ".join(str(e) for e in self._values))