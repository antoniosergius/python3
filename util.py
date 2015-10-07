#!/usr/bin/env python3.4
#
#  util.py
#
#  Copyright 2015 Antônio Sérgio Garcia Ferreira <antoniosergio@mail.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#  2015/08/24 20:10:45
#
#  ---
#
import re

def replace(old, new, lst):
   '''
   Substitui old por new na lista lst.
   Raises TypeError se lst não for list.
   '''
   if not isinstance(lst, list):
      raise TypeError("Error: Invalid type. lst must be list.")
   for i, item in enumerate(lst):
      if item == old:
         lst.pop(i)
         lst.insert(i, new)
         break

def flatten(it):
   '''
   flatten(it) -> list

   Recebe uma lista de várias dimensões e retorna uma de dimensão única.
   '''
   if isinstance(it, list):
      ls=[]
      for item in it:
         ls = ls + flatten(item)
      return ls
   else:
      return [it]

def mysort(lst, pos=0, reverse=False):
   '''
   mysort(lst, pos=0, reverse=False) -> list

   Recebe uma lista de dupla dimensão (matriz) e ordena pela posição especificada
   no argumento pos. Se for omitido a list será ordenada com base no primeiro item
   (pos 0).
   '''
   if not isinstance(lst,list) or not list or pos>len(lst[0])-1:
      return None
   def _key(x):
      return x[pos]
   lst.sort(key=_key, reverse=reverse)
   return lst

def stat(dic):
   '''
   stat(dic)

   Imprime a média, soma, variação de um dicionário com valores númericos.
   '''
   if not isinstance(dic, dict) or len(dic) in (0,1):
      return None
   summ = sum(dic.values())
   rate = summ / len(dic)
   variance = max(dic.values())-min(dic.values())
   return summ, rate, variance

def valid(cad):
   '''
   Verifica se cad é um cadastro (cpf/cnpj) válido.
   Retorna True se for válido.
   '''
   def _iscnpj(cnpj):
      '''Função interna que verifica o cnpj.'''
      count, summ, flag = 0, 0, 5
      while flag <= 6:
         summ = 0
         for i in range(flag, 1, -1):
            summ += int(cnpj[count])*i
            count += 1
         for i in range(9, 1, -1):
            summ += int(cnpj[count])*i
            count += 1
         remainder = summ % 11
         if remainder < 2:
            if cnpj[flag+7] != '0': return False
         elif 11 - remainder != int(cnpj[flag+7]): return False
         count = 0
         flag += 1
      else: return True

   def _iscpf(cpf):
      '''Função interna que verifica o cpf.'''
      head,*middle,tail = cpf
      if head==tail and middle.count(head)==9: return False
      count, summ, flag = 0, 0, 10
      while flag <= 11:
         summ = 0
         for i in range(flag, 1, -1):
            summ += int(cpf[count])*i
            count += 1
         remainder = summ % 11
         if remainder < 2:
            if cpf[flag-1]!='0': return False
         elif 11-remainder != int(cpf[flag-1]): return False
         count = 0
         flag += 1
      else: return True

   if not isinstance(cad, str):
      return False
   elif not cad.isdigit():
      return False
   size = len(cad)
   if size==11:
      return _iscpf(cad)
   elif size==14:
      return _iscnpj(cad)
   elif size>=15 and cad[0]=='0':
      head, tail = cad[:size-14], cad[size-14:]
      if head.count('0') == len(head):
         return _iscnpj(tail)
   return False
