import math

with open("rosalind_iprb.txt") as file:
    num_AA, num_Aa, num_aa = map(int, file.read().split())

population_size = num_AA + num_Aa + num_aa

"""
num_AA — гомозиготы AA
num_Aa — гетерозиготы Aa
num_aa — гомозиготы aa
population_size — num_AA + num_Aa + num_aa

Ищем вероятность доминантного фенотипа через противоположное событие:

P(dominant) = 1 - P(aa)

Рецессивный потомок aa возможен только при трёх типах пар:

1) Aa × Aa:
   число пар = C(num_Aa, 2)
   вероятность потомка aa = 1/4

2) Aa × aa:
   число пар = num_Aa * num_aa
   вероятность потомка aa = 1/2

3) aa × aa:
   число пар = C(num_aa, 2)
   вероятность потомка aa = 1

Всего возможных пар родителей:
C(N, 2), где N = num_AA + num_Aa + num_aa.

Поэтому:

        C(num_Aa, 2) * 0.25
      + num_Aa * num_aa * 0.5
      + C(num_aa, 2)
P(aa) = --------------------------------
                    C(N, 2)
"""

P = (1 - (math.factorial(num_Aa) / (2 * math.factorial(num_Aa - 2)) * 0.25 + num_Aa * num_aa * 0.5 +
     math.factorial(num_aa) / (2 * math.factorial(num_aa - 2))) /
     (math.factorial(population_size) / (2 * math.factorial(population_size - 2))))

print(P)