idade = int(input())
anos = idade // 365
idade = idade - anos* 365
meses = idade // 30
idade = idade - meses*30
dias = idade
print(f'{int(anos)} anos(s)')
print(f'{int(meses)} mes(es)')
print(f'{int(dias)} dia(s)')