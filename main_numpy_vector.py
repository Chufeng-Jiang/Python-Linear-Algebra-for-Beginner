import numpy as np

if __name__ == "__main__":

    print(np.__version__)

    # np.array 基础
    print("========np.array 基础========")
    lst = [1, 2, 3]
    lst[0] = "Linear Algebra"
    print(lst)
    print("========vec = np.array([1, 2, 3])========")
    vec = np.array([1, 2, 3])
    print(vec)
    # vec[0] = "Linear Algebra"
    # vec[0] = 666
    # print(vec)
    print("========np.array的创建========")
    # np.array的创建
    print(np.zeros(5))
    print(np.ones(5))
    print(np.full(5, 666))
    print("========np.array的基本属性========")
    # np.array的基本属性
    print(vec)
    print("size =", vec.size)
    print("size =", len(vec))
    print(vec[0])
    print(vec[-1])
    print(vec[0: 2])
    print(type(vec[0: 2]))
    print("========np.array的基本运算========")
    # np.array的基本运算
    vec2 = np.array([4, 5, 6])
    print("{} + {} = {}".format(vec, vec2, vec + vec2))
    print("{} - {} = {}".format(vec, vec2, vec - vec2))
    print("{} * {} = {}".format(2, vec, 2 * vec))
    print("没有数学意义的乘法：{} * {} = {}".format(vec, vec2, vec * vec2))
    print("{}.dot({}) = {}".format(vec, vec2, vec.dot(vec2)))
    print("========求模========")
    print(np.linalg.norm(vec))
    print("========归一化========")
    print(vec / np.linalg.norm(vec))
    print("========单位向量========")
    print(np.linalg.norm(vec / np.linalg.norm(vec)))
    print("========零向量会报错========")
    zero3 = np.zeros(3)
    print(zero3 / np.linalg.norm(zero3))
