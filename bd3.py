def calcular_salario_com_comissao():
    """
    Calcula o salário final de um funcionário com base no salário base
    e no total de vendas realizadas no mês, adicionando uma comissão.
    """
    print("--- Calculadora de Salário com Comissão ---")

    
    while True:
        try:
            salario_base_str = input("Digite o salário base do funcionário (ex: 2000.50): R$ ")
            salario_base = float(salario_base_str.replace(',', '.')) # Troca vírgula por ponto para float
            if salario_base < 0:
                print("O salário base não pode ser negativo. Por favor, tente novamente.")
            else:
                break
        except ValueError:
            print("Entrada inválida para o salário. Por favor, digite um número.")

    
    while True:
        try:
            total_vendas_str = input("Digite o total de vendas realizadas no mês (ex: 1500.75): R$ ")
            total_vendas = float(total_vendas_str.replace(',', '.')) # Troca vírgula por ponto para float
            if total_vendas < 0:
                print("O total de vendas não pode ser negativo. Por favor, tente novamente.")
            else:
                break
        except ValueError:
            print("Entrada inválida para o total de vendas. Por favor, digite um número.")

    
    porcentagem_comissao = 0.03  

    
    valor_comissao = total_vendas * porcentagem_comissao

    
    novo_salario = salario_base + valor_comissao

   
    print("\n--- Resumo do Cálculo ---")
    print(f"Salário Base Informado: R${salario_base:.2f}")
    print(f"Total de Vendas do Mês: R${total_vendas:.2f}")
    print(f"Porcentagem da Comissão: {porcentagem_comissao * 100:.0f}%")
    print(f"Valor da Comissão: R${valor_comissao:.2f}")
    print(f"**Salário Final (Salário Base + Comissão): R${novo_salario:.2f}**")


if __name__ == "__main__":
    calcular_salario_com_comissao()