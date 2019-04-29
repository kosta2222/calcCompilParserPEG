"""
  байт-код как перечисления
"""
(   NOOP    ,#0
    IADD    ,#1
    ISUB    ,#2
    IMUL    ,#3
    IDIV    ,#4
    IREM    ,#5
    IPOW    ,#6
    ILT     ,#7
    IEQ     ,#8
    BR      ,#9
    BRT     ,#10
    BRF     ,#11
    ICONST  ,#12
    LOAD    ,#13
    GLOAD   ,#14
    STORE   ,#15
    GSTORE  ,#16
    PRINT   ,#17
    POP     ,#18
    CALL    ,#19
    RET     ,#20
    STORE_RESULT,#21
    LOAD_RESULT,#22
    INVOKE_BY_ORDINAL,#23
    CREATE_STRING,#24
    NEWARRAY,#25
    IASTORE,#26
    IALOAD,#27
    DUP,#28
    ASTORE,#29
    ALOAD,#30
    INVOKE,#31
    STOP,#32

    blink_red_led, #33
    turn_on_relay #34
)=range(35)