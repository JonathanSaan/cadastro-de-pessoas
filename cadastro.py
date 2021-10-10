from time import sleep

pessoas_cadastradas = []

def menu():
	while True:
		try:
			print('-'*40)
			print('MENU PRINCIPAL'.center(40))
			print('-'*40)
			print('\033[33m 1 \033[m- \033[1;34mver pessoas cadrastadas \033[m')
			print('\033[33m 2 \033[m- \033[1;34mcadastrar uma nova pessoa\033[m')
			print('\033[33m 3 \033[m- \033[1;34msair do programa\033[m')
			print('-'*40)
			opção = int(input('\033[33mSua opção: \033[m'))
			
			if opção == 1:
				print('-'*40)
				print('PESSOAS CADASTRADAS'.center(37))
				for c in pessoas_cadastradas:
					nome, idade = c		
					print(f'Nome: {nome: <20} Idade: {idade}\n')
				if len(pessoas_cadastradas) == 0:
					print('\nNenhuma pessoa foi cadastrada. \n')
				sleep(1)
				menu()
			
			elif opção == 2:
				while True:
					try:
						print('-'*40)
						nome = str(input('Nome: '))
						if len(nome) < 3:
							nome()
						idade = int(input('Idade: '))
						pessoas_cadastradas.append((nome, idade))
						continuar =str(input('Deseja continuar? [S/N]: ')).lower()[0]
						sleep(0.5)
						if continuar == 's':
							continue
						elif continuar == 'n' or 'ñ':
							menu()
					except:
						print('não entendi. por favor repita novamente.')
					else:
						break
						
			elif opção == 3:
				print('-'*40)
				print('Saindo do sistema... Até logo!'.center(40))
				print('-'*40)
				break
				
			if opção > 3:
				print('\033[31mERRO! digite uma opção válida!\033[m')
				sleep(1)
				menu()
		except(ValueError):
			print('\033[31mERRO! digite apenas um numero inteiro valido.\033[m ')
			sleep(1)
		else:
			break
menu()
