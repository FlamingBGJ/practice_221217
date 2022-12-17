import pandas
import numpy as np
# numpy 를 np라는 이름으로 사용하겠다.

my_arr = np.arange(1000000)
# np.array(range(1000000))

my_list = list(range(1000000))
print(my_arr)
print(type(my_arr))

%time
for _ in range(1000):
    my_arr2 = my_arr*2
my_arr2[:20]

%time 
for _ in range(1000):
    my_list2 = [i*2 for i in my_list]
my_list2[:20]

# array를 랜덤한 숫자로 만든다. 
data_0 = np.random.randn(3)
data_0.shape

#ndarray 생성
data_4 = [6,7,8,3,4,2]
arr_1 = np.array(data_4)
print(arr_1.shape)

data_5 = [[6,7,8,3,4,2]]
arr_2 = np.array(data_5)
print(arr_2.shape)

data_7 = [[[6,7,8,3,4,2]]]
arr_3 = np.array(data_7)
print(arr_3.shape)

# list 를 이용해 array를 만들어 보세요
# 아무 숫자나 넣고 만들면 되요
# 단 4, 2 의 shape으로 만들어 보세요
list_1 = [[1,2,3,4],[4,5,6,7]]
list_2 = [[1,2], [3,4], [4,5], [6,7]]

arr_5 = np.array(list_1)
arr_6 = np.array(list_2)

print(arr_5.shape)
print(arr_6.shape)
print(arr_6.ndim)

# append 함수를 통해 리스트의 요소를 추가할 수 있다.
list_1 = []
list_1.append(1)
print(list_1)

# 0으로 채워진 5,10 행렬
np.zeros((5,10))

# zeros 를 이용해 3,4,5 인 array를 만들어 보세요 
# 모든 숫자가 2로 채워진 3,4인 array를 만들어 보세요 
arr_7 = np.zeros([3,4,5])
print(arr_7.shape)
np.full([3,4], 2)
print(arr_7)

# 데이터 타입 변경
arr_6.astype(dtype="float64")
print(arr_6.dtype)

#numpy 산술연산
arr_1 = np.array([
    [1,2,3],
    [4,5,6]
])

# 요소곱
arr_1 * arr_1

# arr_1과 arr_2의 덧셈, 뺄셈, 곱셈, 나눗셈
arr_2 = np.array([
    [2,3,4],
    [7,6,3]
])

print(arr_1 + arr_2)
print(arr_1 - arr_2)
print(arr_1 * arr_2)
print(arr_1 / arr_2)

# arr_1과 arr_2의 대소비교
print(arr_1 >= arr_2)
print(arr_1 != arr_2)

# 행렬 전치
arr_2.transpose()