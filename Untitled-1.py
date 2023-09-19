
renda = float(input("Renda Bruta "))
primeira_faixa = 180000.00
segunda_faixa = 360000.00
terceira_faixa = 720000.00
quarta_faixa = 1800000.00
quinta_faixa = 3600000.00
sexta_faixa = 4800000.00



if renda <= primeira_faixa:
   renda = renda*(0.06)

if segunda_faixa >= renda > primeira_faixa:
   renda = (renda*(0.112)) - 9360.00

if terceira_faixa >= renda > segunda_faixa:
   renda = (renda*(0.135)) - 17640.00

if quarta_faixa >= renda > terceira_faixa:
   renda = (renda*(0.16)) - 35640.00

if quinta_faixa >= renda > quarta_faixa:
   renda = (renda*(0.21)) - 125640.00

if sexta_faixa >= renda > quinta_faixa:
    renda = (renda*(0.33)) - 648000.00

if renda > sexta_faixa:
    renda = 0.00
    print("Sua renda não se enquadra no Simples Nacional")




print("Imposto a pagar pelo Simples Nacional: R$ ",renda)