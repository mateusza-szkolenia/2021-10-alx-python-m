#
# A   l   a   _   m   a   _   k   o   t   a   _   a   _   k   o ...
# 0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15 ...
# [4:4]                                   (pusto)
# [4:5]           ^                       (1 znak)
# [4:10]          ^   ^   ^   ^   ^   ^   (6 znaków)

zdanie = "Ala ma kota a kot ma pchły"

print(f"{zdanie[4:4]=}")
print(f"{zdanie[4:5]=}")
print(f"{zdanie[4:10]=}")
print(f"{zdanie[4:11]=}")

# brak drugiej liczby - do końca
print(f"{zdanie[14:]=}")

# brak pierwszej liczby - od początku (od zera)
print(f"{zdanie[:6]=}")

# 5 ostatnich znaków
print(f"{zdanie[-5:]=}")

# nie wiem po co, ale zadziała:
print(f"{zdanie[:]=}")
print(f"{zdanie=}")
