i = 0
while i < 10:
    i += 1

    if i == 2:
        continue  # kończy obecną iterację (obrót) pętli i wraca do sprawdzenia warunku

    print(i)
    if i == 7:
        break  # przerywa najbardziej wewnętrzną pętlę

print("koniec")
