from math import ceil


def main(H):
    Omax = {n ** 3 - 4 * n for n in H if -41 < n <= 33}
    Theta = {o % 2 - ceil(o / 2) for o in Omax if not (-92 < o <= 74)}
    Delta = H.union(Omax)
    epsilon = len(Delta.union(Theta)) - sum(abs(theta) for theta in Theta)
    return epsilon

print(main({68, -55, 15, -44, 20, 30, 56, -7, -70, -66})) #-19197
print(main({98, 58, -60, -49, 23, 21, -11, -10, 52, 26})) #-20465