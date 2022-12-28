    MOV SS, 1
    MOV SP, 0x20; [0, 0xf] -> stack
    jmp start    

show:
    MOV D, 255
    iret; return


start:
    MOV C, 0

increase:
    INC C
    MOV D, C
    JP disable

enable:
    sti;
    jmp interrupt

disable:
    cli;

interrupt:
    int show
    jmp increase


    HLT; stop