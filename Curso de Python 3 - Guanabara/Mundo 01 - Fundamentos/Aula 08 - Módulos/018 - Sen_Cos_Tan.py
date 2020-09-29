from math import sin, cos, tan, radians

Ang = float(input("Digite o ângulo que você deseja: "))

sen = sin(radians(Ang))
cos = cos(radians(Ang))
tan = tan(radians(Ang))

print("O ângulo de {} tem o SENO de {:.2f}".format(Ang, sen))
print("O ângulo de {} tem o COSSENO de {:.2f}".format(Ang, cos))
print("O ângulo de {} tem o TANGENTE de {:.2f}".format(Ang, tan))
