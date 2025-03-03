def inverter_string(string):
  

    string_invertida = ""
    for i in range(len(string) - 1, -1, -1):
        string_invertida += string[i]
    return string_invertida



string_original = input("Digite uma palavra: ")
string_invertida = inverter_string(string_original)
print(f"String invertida: {string_invertida}")