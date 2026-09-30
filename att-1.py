def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2
print("=== sistema de notas aluco ===")
n1 = float(input("digite a primeira nota: "))
n2 = float(input("digite a segunda nota:"))
media = calcular_media(n1, n2)
print(f"a media final e: {media:.2f}")

if media >= 7.0:
    print("status: aprovado!")

else:
    print("status: reprovado.")
    