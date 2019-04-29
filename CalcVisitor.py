
from arpeggio import PTNodeVisitor

# РћРїРёСЃС‹РІР°РЅРёРµ РіСЂР°РјРјР°С‚РёРєРё
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
 РЎРѕР·РґР°РЅРёРµ РєР»Р°СЃСЃР° С‚РёРїР° Visitor
 РћР±СЂР°Р±Р°С‚С‹РІР°РµРј AST - СЃРѕР·РґР°РµРј РґСЂСѓРіРѕРµ AST РґР»СЏ РЅР°С€РµРіРѕ РєРѕРјРїРёР»СЏС‚РѕСЂР°
 Р РµР·СѓР»СЊС‚Р°С‚ Р·Р°РїРёСЃС‹РІР°РµРј РІ РіР»РѕР±Р°Р»СЊРЅС‹Р№ program_ast СЃРїРёСЃРѕРє
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
      # РІС‹СЂР°Р¶РµРёРµ СЃРѕСЃС‚РѕРёС‚ РёР· 2-С… С‡Р»РµРЅРѕРІ Рё РѕРґРЅРѕР№ РѕРїРµСЂР°С†РёРё
      # С‚.Рµ. РІ children РёРјРµРµРј 1 СЌР»РµРјРµРЅС‚ - СѓРјРЅРѕР¶РёС‚СЊ РёР»Рё СЂР°Р·РґРµР»РёС‚СЊ
      if len(children)==1:

           self.program_ast.append([children[0]])
       
      # РІС‹СЂР°Р¶РµРЅРёРµ СЃРѕСЃС‚РѕРёС‚ РёР· Р±РѕР»РµРµ 2 С‡Р»РµРЅРѕРІ Р°СЂРёС„РјРµС‚РёС‡РµСЃРєРѕР№ РѕРїРµСЂР°С†РёРё 
      else:
       
          self.program_ast.append(children[0])

          for i in range(int(len(children) / 2)):

             self.program_ast.append([children[2*i + 1]])

     
  def visit_stmt(self,node,children):

    if len(children)>0:   
      # РІС‹СЂР°Р¶РµРёРµ СЃРѕСЃС‚РѕРёС‚ РёР· 2-С… С‡Р»РµРЅРѕРІ Рё РѕРґРЅРѕР№ РѕРїРµСЂР°С†РёРё
      # С‚.Рµ. РІ children РёРјРµРµРј 1 СЌР»РµРјРµРЅС‚ - СЃР»РѕР¶РёС‚СЊ РёР»Рё РѕС‚РЅСЏС‚СЊ
      if len(children)==1:

           self. program_ast.append([children[0]])
       
      # РІС‹СЂР°Р¶РµРЅРёРµ СЃРѕСЃС‚РѕРёС‚ РёР· Р±РѕР»РµРµ 2 С‡Р»РµРЅРѕРІ Р°СЂРёС„РјРµС‚РёС‡РµСЃРєРѕР№ РѕРїРµСЂР°С†РёРё 
      else:
       
         self.program_ast.append(children[0])
        
         for i in range(int(len(children) / 2)):

            self.program_ast.append([children[2*i + 1]])