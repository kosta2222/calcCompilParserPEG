#import pdb
#pdb.set_trace()
from struct import pack, unpack

from bytecodes import *

isa=isinstance
class Compiller:
  """
     РљРѕРјРїРёР»СЏС‚РѕСЂ - СЃРѕР·РґР°РµС‚ Р±Р°Р№С‚-РєРѕРґ
  """
  by_co_program:list=[]
 
  def __init__(self):

    print("Compiller processing...")
  
  # packing
  def shortAsBytes(self, val):
    
      return pack('h',val)

  def gen(self, command):

     self.by_co_program.append(command)

  def compille(self,node):
   """
     @param node type list
   """
   
   print('\n'+str(node))
   if isa(node[0], int):
      
      self.gen(ICONST)
      self.by_co_program.extend(self.shortAsBytes(node[0]))
      
   if node[0]=='>':
         
      for i in node[1:]:

         self.compille(i)
  
   elif node[0]=='+':

      self.gen(IADD)

   elif node[0]=='-':
    
     self.gen(ISUB)

   elif node[0]=='*':
     
      self.gen(IMUL)
   
   elif node[0]=='/':
  
      self.gen(IDIV)

  def __str__(self):

    return 'bytecode:'+str(self.by_co_program)  