L1 = list(map(int, input().split()))
L2 = list(map(int, input().split()))

x1, y1, x2, y2 = L1
x3, y3, x4, y4 = L2

mx1, my1, mx2, my2 = min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)
mx3, my3, mx4, my4 = min(x3, x4), min(y3, y4), max(x3, x4), max(y3, y4)

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
    elif v_a != v_b and (v_c == '0' or v_d == '0'):
        return 1
    elif v_c != v_d and (v_a == '0' or v_b == '0'):
        return 1
    elif v_a == v_b == v_c == v_d == '0':
        if mx1 <= mx4 and mx3 <= mx2 and my1 <= my4 and my3 <= my2:
            return 1
    
    return 0

v0 = get_cross_product(p0, p2, p3)
v1 = get_cross_product(p1, p2, p3)
v2 = get_cross_product(p2, p0, p1)
v3 = get_cross_product(p3, p0, p1)

# print(v0, v1, v2, v3)
print(check_result(v0, v1, v2, v3))