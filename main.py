#**********************Программа******************************************

from serial import Serial,SerialException,EIGHTBITS,PARITY_NONE

import time

import logging

from Compiller import Compiller

from CalcVisitor import *

from arpeggio.cleanpeg import ParserPEG

from arpeggio import visit_parse_tree

logger = logging.getLogger(__name__)
logging.basicConfig(filename='cmplr.log', filemode='w',
                            level=logging.DEBUG)

def serOpen():
    """
     @return ser type Serial
    """

    SERIAL_PORT='COM7'
    SERIAL_SPEED=9600

    ser=Serial()
    ser.port=SERIAL_PORT
    ser.baudrate=SERIAL_SPEED
    ser.bytesize = EIGHTBITS   #number of bits per bytes
    ser.timeout = 1            #non-block read
    ser.writeTimeout = 2       #timeout for write
    ser.xonxoff = False        #disable software flow control
    ser.rtscts = False         #disable hardware (RTS/CTS) flow control
    ser.dsrdtr = False         #disable hardware (DSR/DTR) flow control

    try:
          """
             Пытаемся открыть серийный порт
          """
          ser.open()

    except SerialException as e:

          logger.debug("error open serial port: " + str(e))

          exit(2)

    return ser

def parse(input_expr):
     """
       @param input_expr type str
       @return calcVisitor type CalcVisitor
     """

     parser=ParserPEG(calc_grammar,"calc")

     parse_tree=parser.parse(input_expr)
    
     calcVisitor=CalcVisitor()

     visit_parse_tree(parse_tree,calcVisitor)
                     
     return calcVisitor


def interpret_program():
     """
      Считываем строку пользователя и отправляем бат-код в устройство
     """ 

     ser:Serial=serOpen()

     us_input=input('Ukuvchi>>>') # получаем конкретную строку исходной программы
  
     calcVisitor:CalcVisitor=parse(us_input) # анализируем исходный код программы 

         
     compiller=Compiller()
     ast=calcVisitor.program_ast
     compiller.compille(ast)
     bytecode=compiller.by_co_program

     STOP=32
     bytecode+=[STOP]

     logger.debug("by-co list:%s"%(str(bytecode)))
    
     bytesAmount=ser.write(bytes(bytecode))
     logger.debug("ser r:%d",bytesAmount) 
     time.sleep(0.5)
     
     readDevice(ser) 
     

     ser.close()

def readDevice(ser:Serial):
     """ 
         Считываем то что вернуло устройство
         @param ser type Serial 
     """
     isCmdSessionLasts=True
     while isCmdSessionLasts :
       
       line_out=ser.readline()
       logger.debug(line_out)

       if line_out==b'STOP VM\n':
             
          return
   

if __name__=='__main__':

   interpret_program()

#***********************End Программа****************************


 
