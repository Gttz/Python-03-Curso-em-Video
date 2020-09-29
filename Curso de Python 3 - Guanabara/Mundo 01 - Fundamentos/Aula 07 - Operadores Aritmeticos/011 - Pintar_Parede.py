Largura = float(input("Digite a Largura da parede:"))
Altura = float(input("Digite a Altura da parede: "))

área = Largura * Altura

print("Sua parede tem a dimensão de {}x{} e sua área é de: {}m²".format(Largura, Altura, área))
tinta = área / 2

print("Para pintar a parede, você precisará de {}l de tinta.".format(tinta))