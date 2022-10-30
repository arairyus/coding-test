#!/bin/python3
import sys
import re

def split_ops(array : list):
  format = '([a-z]+)|([A-Z][a-z]+)|([A-Z]+)'
  words = [x.lower() for x in re.split(format, array[-1]) if x != None and x != '']
  result = words[0]
  for word in words[1:]:
    if word != '()':
      result += ' '
      result += word
  
  return result
  
def combine_ops(array : list):
  target_string = array[-1].split()
  for i in range(len(target_string)):
    if i == 0:
      if array[0] == 'C':
        result = target_string[i].capitalize()
      else:
        result = target_string[i].lower()
    else:
      result += target_string[i].capitalize()
    
  if array[0] == 'M':
    result += '()'
  
  return result
  
  
if __name__ == "__main__":
  array = [line.rstrip() for line in sys.stdin.readlines()]
  for element in array:
    data_list = element.split(';')
    if data_list[0] == "S":
      res = split_ops(data_list[1:])
    else:
      res = combine_ops(data_list[1:])
      
    print(res)