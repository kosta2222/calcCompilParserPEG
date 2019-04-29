
from arpeggio import PTNodeVisitor

# Описывание грамматики
calc_grammar="""
number=r'\d+(\.\d+)?'

factor=number/"(" stmt ")"
term=factor(mulop factor)*
stmt=term(addop term)*

addop="+" / "-"
mulop="*" / "/"

calc=stmt EOF
"""

""" 
 Создание класса типа Visitor
 Обрабатываем AST - создаем другое AST для нашего компилятора
 Результат записываем в глобальный program_ast список
"""
class CalcVisitor(PTNodeVisitor):

  program_ast=['>']

  def visit_number(self,node,children):
   
      self.program_ast.append([int(node.value)])
   
  def visit_factor(self,node,children):
   
    if len(children)>0:
       
         self.program_ast.append([children[0]])
      
  def visit_term(self,node,children):
    
    if len(children)>0:   
      # выражеие состоит из 2-х членов и одной операции
      # т.е. в children имеем 1 элемент - умножить или разделить
      if len(children)==1:

           self.program_ast.append([children[0]])
       
      # выражение состоит из более 2 членов арифметической операции 
      else:
       
          self.program_ast.append(children[0])

          for i in range(int(len(children) / 2)):

             self.program_ast.append([children[2*i + 1]])

     
  def visit_stmt(self,node,children):

    if len(children)>0:   
      # выражеие состоит из 2-х членов и одной операции
      # т.е. в children имеем 1 элемент - сложить или отнять
      if len(children)==1:

           self. program_ast.append([children[0]])
       
      # выражение состоит из более 2 членов арифметической операции 
      else:
       
         self.program_ast.append(children[0])
        
         for i in range(int(len(children) / 2)):

            self.program_ast.append([children[2*i + 1]])