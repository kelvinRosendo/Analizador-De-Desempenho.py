#objetivos do codigo:
#    ajudar a melhorar o desempenho em qualquer coisa
#    interagir pelo input com o usuario 
#   mostrar sites que ajudem o usuario em suas duvidas
#através de perguntas simples

nome = input("qual é o seu nome ")

sono = int(input("você tem dormido quantas horas por noite ?"))
if sono < 6:
    print("acho que você deve regular seu sono, aqui isso deve te ajudar: https://www.vigilantesdopeso.com.br/br/artigos/como-regular-sono").format(nome)

alimentação = int(input("quantas refeições você tem feito ?,"))
tempo_para_alimentação = input("você tem tido tempo para se alimentar ?")
if alimentação < 3:
    print (tempo_para_alimentação)
    
if tempo_para_alimentação == ("não"):
    print ("aqui estão receitas rapidas e nutritivas para não ocupar seu tempo: https://www.receiteria.com.br/receitas-saudaveis-rapidas/ ;)")
else :
    print("peocure ter um tempo para se alimentar")

carga_horaria_de_trabalho = int(input("quantas horas você tem trabalhado por dia ? "))
folgas_por_semana = int(input("quantas folgas por semana você tem ?"))
if carga_horaria_de_trabalho > 12:
    print(folgas_por_semana)
else:
    print("okay, sua carga horaria de trabalho não e necessariamente o problema")

if folgas_por_semana < 3:
    print("não há muito a ser feito pois é seu trabalho mas tome cuidado você está trabalhando demais e dê uma olhada nas leis trabalhistas")

descanço = input("você tem arranjado tempo para seu lazer ?")
if descanço == ("sim"):
    print("okay")
else:
    ("é majoriatoriamete necessario que o corpo humano tenha seu tempo de descanso... <-- trecho de um artigo feito por um especialista")      

    print("uma ultima dica faça uma rotina organizadinha, ajuda bastante ;)")