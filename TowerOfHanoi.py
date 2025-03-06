def TowerOfHanoi(N, src, des, aux):
    if N == 1:
        print("Move disk 1 from rod", src, "to rod", des)
        return
    TowerOfHanoi(N-1, src, aux, des)
    print("Move disk", N, "from rod", src, "to rod", des)
    TowerOfHanoi(N-1, aux, des, src)


TowerOfHanoi(3, "A", "B", "C")
