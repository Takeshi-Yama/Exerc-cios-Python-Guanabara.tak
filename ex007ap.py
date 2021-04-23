numlist=list()
while True:
   inp= input('Digite a nota do aluno: ')
   if inp=='pronto' :break
   valor=float(inp)
   numlist.append(valor)
   Média=sum(numlist)/len(numlist)
print('Média: ',Média)
print(f'A média do aluno foi {Média}.')
