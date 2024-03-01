L1 = list(map(int, input().split()))
L2 = list(map(int, input().split()))

p0 = tuple(L1[:2])
p1 = tuple(L1[2:])
p2 = tuple(L2[:2])
p3 = tuple(L2[2:])

def get_cross_product(p_a, p_b, p_c):
    v_a = (p_b[0]-p_a[0], p_b[1]-p_a[1])
    v_b = (p_c[0]-p_a[0], p_c[1]-p_a[1])
    # print(v_a, v_b)
    v = v_a[0]*v_b[1] - v_a[1]*v_b[0]
    
    if v == 0:
        return '0'
    
    return '+' if v > 0 else '-'

def check_result(v_a, v_b, v_c, v_d):
    if v_a != v_b and v_c != v_d:
        return 1
    
    return 0

v0 = get_cross_product(p0, p2, p3)
v1 = get_cross_product(p1, p2, p3)
v2 = get_cross_product(p2, p0, p1)
v3 = get_cross_product(p3, p0, p1)

# print(v0, v1, v2, v3)
print(check_result(v0, v1, v2, v3))