# Desafio045: Crie um programa que faça o computador jogar Jokenpô com você.
import random
from time import sleep

print('-='*15)
print('        J-O-K-E-N-P-Ô')
print('-='*15)
player = int(input('[1] - PEDRA \n[2] - PAPEL \n[3] - TESOURA \nESCOLHA SUA JOGADA: '))
print('-='*15)
sleep(0.5)
print('\033[1;31mJO')
sleep(0.5)
print('\033[1;33mKEN')
sleep(0.5)
print('\033[1;32mPO!!!\033[m')
sleep(0.5)
cpu = ['PEDRA','PAPEL', 'TESOURA']
cpu = random.choice(cpu)
if player == 1:
    player = 'PEDRA'
    if cpu =='PEDRA':
        resultado = '\033[1;33mEMPATOU'
    elif cpu == 'PAPEL':
        resultado = '\033[1;31mCPU VENCEU'
    elif cpu == 'TESOURA':
        resultado = '\033[1;32mVOCÊ VENCEU'
elif player == 2:
    player = 'PAPEL'
    if cpu =='PEDRA':
        resultado = '\033[1;32mVOCÊ VENCEU'
    elif cpu == 'PAPEL':
        resultado = '\033[1;33mEMPATOU'
    elif cpu == 'TESOURA':
        resultado = '\033[1;31mCPU VENCEU'
elif player == 3:
    player = 'TESOURA'
    if cpu =='PEDRA':
        resultado = '\033[1;31mCPU VENCEU'
    elif cpu == 'PAPEL':
        resultado = '\033[1;32mVOCÊ VENCEU'
    elif cpu == 'TESOURA':
        resultado = '\033[1;33mEMPATOU'
print('-='*15)
print('CPU jogou {}.\nVOCÊ jogou {}.\n{}\033[m!!!' .format(cpu, player, resultado))
print('-='*15)
