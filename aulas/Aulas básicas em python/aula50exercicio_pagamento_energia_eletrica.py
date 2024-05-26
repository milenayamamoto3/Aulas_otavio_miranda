def cal_valor_pagar(consumo, tipo):
    if tipo == 'R':
        if consumo <= 500:
            preco = 0.40
        else:
            preco = 0.65
    elif tipo == 'I':
        if consumo <= 5000:
            preco = 0.55
        else:
            preco = 0.60
    elif tipo == 'C':
        if consumo <= 1000:
            preco = 0.55
        else:
            preco = 0.60
    else:
        print("Tipo de instalação inválido.")
        return None
    
    valor_pagar = consumo * preco
    return valor_pagar

def main():
    try:
        consumo = float(input("Digite a quantidade consumida em kWh: "))
        tipo = input("Digite o tipo de instalação (R para residencial, I para industrial, C para comercial): ").upper()
    
        valor_pagar = cal_valor_pagar(consumo, tipo)
    
        if valor_pagar is not None:
            print(f"O valor a pagar pela energia é: R$ {valor_pagar:.2f}")
    except:
        print('Digite algo válido')

if __name__ == "__main__":
    main()

