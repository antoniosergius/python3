#!/usr/bin/env python3.4
#
#  2015/09/25 13:43:29
#
import sys

def isprime(n):
   '''
   isprime(n) -> bool

   Verifica se o número é primo. O método utilizado é o seguinte: inicialmente
   é considerado -1,0,1 como não primos e o módulo de dois como primo. Em seguida é feita
   uma lista começando de 3 até a raiz quadrada do módulo do número fornecido, sem
   os pares que são compostos. O dois é inserido para para saber se n é par.

   '''
   if type(n)!=int or n in {-1, 0, 1}: return False
   if abs(n)==2: return True
   divisors = list(range(3,int(abs(n)**0.5+1),2))
   divisors.insert(0, 2)
   count = 0
   for num in divisors:
      if abs(n)%num==0:
         count+=1
   return count==0

def flatten_list_old(lst):
   new=[]
   if type(lst)!=list or not lst:
      return new
   for inside_list in lst:
      for elem in inside_list:
         new.append(elem)
   return new

def flatten_list(lst):
   '''
   flatten_list(lst) -> list

   Recebe uma lista de duas dimensões e retorna uma de dimensão única.
   A técnica usada é conhecida como list comprehension
   '''
   if type(lst)!=list or not lst:
      return -1
   else:
      return [num for elem in lst for num in elem]

def dict_statistics(dic):
   '''
   dict_statistics(dic)

   Imprime a média, soma, variância e o desvio padrão de um dicionário com
   valores númericos.
   '''
   if type(dic)!=dict or len(dic) in (0,1):
      return -1
   summ = 0.0
   for value in dic.values():
      summ += value
   rate = summ / len(dic)
   variance = 0.0
   for value in dic.values():
      variance += (value - rate)**2
   statistics='''
      Rate = %.2f
      Summ = %.2f
      Data Variance    = %.2f
      Stand. Deviation = %.2f
   ''' %(rate, summ, variance/(len(dic)-1), variance**0.5)
   print(statistics)


#if __name__=="__main__":
   #if len(sys.argv)!=2:
      #sys.exit(-1)
   #n=int(sys.argv[1])
   #if isprime(n):
      #print("%d é primo" %n)
   #else:
      #print("%d não é primo" %n)
