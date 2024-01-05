# somente 30 dias

import time

def calcular_diferenca_maior(mensalidade, vencimento_atual, novo_vencimento):
    dias_no_mes = 30  # Considerando sempre 30 dias no mês
    diferenca_dias = novo_vencimento - vencimento_atual if novo_vencimento >= vencimento_atual else dias_no_mes - vencimento_atual + novo_vencimento
    diferenca_reais = (mensalidade / dias_no_mes) * diferenca_dias
    valor_proporcional = mensalidade + diferenca_reais
    return valor_proporcional, diferenca_reais, diferenca_dias

def calcular_diferenca_menor(mensalidade, vencimento_atual, novo_vencimento):
    dias_no_mes = 30  # Considerando sempre 30 dias no mês
    diferenca_dias = vencimento_atual - novo_vencimento if vencimento_atual >= novo_vencimento else dias_no_mes - novo_vencimento + vencimento_atual
    diferenca_reais = (mensalidade / dias_no_mes) * diferenca_dias
    valor_proporcional = mensalidade - diferenca_reais
    return valor_proporcional, diferenca_reais, diferenca_dias

def obter_dias_no_mes():
    return 30  # Considerando sempre 30 dias no mês

def main():
    while True:
        try:
            print("Iniciando programa...")
            time.sleep(1)
            print("==================================")
            print("Programa iniciado :D")
            print("==================================")
            mensalidade = float(input("Informe o valor da mensalidade R$: ").replace(',', '.'))
            vencimento_atual = int(input("Informe o dia do vencimento atual (formato dd): "))
            novo_vencimento = int(input("Informe o dia do novo vencimento desejado (formato dd): "))
            print("==================================")
            
            print("Calculando proporcional. Aguarde...")
            time.sleep(1)
            print("==================================")

            if novo_vencimento >= vencimento_atual:
                valor_proporcional, diferenca_reais, diferenca_dias = calcular_diferenca_maior(
                    mensalidade, vencimento_atual, novo_vencimento
                )
            else:
                valor_proporcional, diferenca_reais, diferenca_dias = calcular_diferenca_menor(
                    mensalidade, vencimento_atual, novo_vencimento
                )

            valor_proporcional_str = '{:,.2f}'.format(valor_proporcional).replace('.', ',')
            diferenca_reais_str = '{:,.2f}'.format(diferenca_reais).replace('.', ',')
            
            print(f"O valor proporcional da próxima mensalidade é: R${valor_proporcional_str}")
            print(f"Valor da diferença em reais: R${diferenca_reais_str}")
            print(f"Diferença de dias: {diferenca_dias} dia(s)")
        except ValueError:
            print("Por favor, insira um valor numérico válido.")

        print("==================================")
        resposta = input("Deseja fazer outro cálculo? (Digite 's' para continuar ou 'n' para encerrar): ")
        if resposta.lower() != 's':
            print("Tudo bem então, até a próxima :)")
            print("Programa finalizado.")
            time.sleep(1)
            break

if __name__ == "__main__":
    main()
