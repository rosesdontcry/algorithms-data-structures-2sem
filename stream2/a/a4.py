def search_answer(k_temp, barrels_temp):
    max_value = sum(barrels_temp)
    min_value = max(barrels_temp)
    while  min_value < max_value:
        probable_weight = (max_value + min_value) // 2
        weight_barrels = 0
        count_ships = 1

        for barrel in barrels_temp:
            if weight_barrels + barrel > probable_weight:
                weight_barrels = barrel

                count_ships += 1
                if count_ships > k_temp:
                    min_value = probable_weight + 1
                    break

            else:
                weight_barrels += barrel

        else:
            max_value = probable_weight

    print(max_value)
    return -1

n, k = [int(i) for i in input().split()]
barrels = [int(i) for i in input().split()]

search_answer(k, barrels)
