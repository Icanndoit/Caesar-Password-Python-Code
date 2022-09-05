# 함수 선언
def power(item):
    return item * item

def under_3(item):
    return item < 3

# 변수 선언
list_input_a = [1, 2, 3, 4, 5]

# map() 함수 사용
output_a = map(power, list_input_a)
print("# map() 함수의 실행결과")
print("map(power, list_input_a) :", output_a, type(output_a))
print("map(power, list_input_a) :", list(output_a), "\n")

# filter() 함수 사용
output_b = filter(under_3, list_input_a)
print("# filter() 함수의 실행결과")
print("map(power, list_input_b) :", output_b, type(output_b))
print("map(power, list_input_b) :", list(output_b), "\n")

# map() 함수의 선언법 : map(함수, 리스트)
# map() 함수는 리스트를 요소에 넣고 리턴된 값으로 새로운 리스트를 구성해 주는 함수이다.

# filter() 함수 선언법 : filter(함수, 리스트)
# filter() 함수는 리스트의 요소를 함수에 넣고 리턴된 값이 True인 것으로, 
# 새로운 리스트를 구성해 주는 함수이다.