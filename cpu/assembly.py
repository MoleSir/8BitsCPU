import pin

FETCH = [
    pin.PC_OUT | pin.MAR_IN, 
    pin.RAM_OUT | pin.IR_IN | pin.PC_INC,

    pin.PC_OUT | pin.MAR_IN, 
    pin.RAM_OUT | pin.DST_IN | pin.PC_INC,

    pin.PC_OUT | pin.MAR_IN, 
    pin.RAM_OUT | pin.SRC_IN | pin.PC_INC,
]  

MOV = (0 << pin.ADDR2_SHIFT) | pin.ADDR2
ADD = (1 << pin.ADDR2_SHIFT) | pin.ADDR2
SUB = (2 << pin.ADDR2_SHIFT) | pin.ADDR2
CMP = (3 << pin.ADDR2_SHIFT) | pin.ADDR2
AND = (4 << pin.ADDR2_SHIFT) | pin.ADDR2
OR  = (5 << pin.ADDR2_SHIFT) | pin.ADDR2
XOR = (6 << pin.ADDR2_SHIFT) | pin.ADDR2

INC = (0 << pin.ADDR1_SHIFT) | pin.ADDR1
DEC = (1 << pin.ADDR1_SHIFT) | pin.ADDR1
NOT = (2 << pin.ADDR1_SHIFT) | pin.ADDR1
JMP = (3 << pin.ADDR1_SHIFT) | pin.ADDR1

JO  = (4 << pin.ADDR1_SHIFT) | pin.ADDR1
JNO = (5 << pin.ADDR1_SHIFT) | pin.ADDR1
JZ  = (6 << pin.ADDR1_SHIFT) | pin.ADDR1
JNZ = (7 << pin.ADDR1_SHIFT) | pin.ADDR1
JP  = (8 << pin.ADDR1_SHIFT) | pin.ADDR1
JNP = (9 << pin.ADDR1_SHIFT) | pin.ADDR1

PUSH = (10 << pin.ADDR1_SHIFT) | pin.ADDR1
POP = (11 << pin.ADDR1_SHIFT) | pin.ADDR1

CALL = (12 << pin.ADDR1_SHIFT) | pin.ADDR1
INT = (13 << pin.ADDR1_SHIFT) | pin.ADDR1


HLT = 0x3f
NOP = 0x0
RET = 1
IRET = 2
STI = 3
CLI = 4

INSTRUCTIONS = {
    2 : {
        MOV : {
            (pin.AM_REG, pin.AM_INS) : [
                pin.DST_W | pin.SRC_OUT,
            ],
            (pin.AM_REG, pin.AM_REG) : [
                pin.DST_W | pin.SRC_R,  
            ],
            (pin.AM_REG, pin.AM_DIR) : [
                pin.SRC_OUT | pin.MAR_IN,
                pin.DST_W | pin.RAM_OUT
            ],
            (pin.AM_REG, pin.AM_RAM) : [
                pin.SRC_R | pin.MAR_IN,
                pin.DST_W | pin.RAM_OUT
            ],
            (pin.AM_DIR, pin.AM_INS) : [
                pin.DST_OUT | pin.MAR_IN,
                pin.RAM_IN | pin.SRC_OUT
            ],
            (pin.AM_DIR, pin.AM_REG) : [
                pin.DST_OUT | pin.MAR_IN,
                pin.RAM_IN | pin.SRC_R
            ],
            (pin.AM_DIR, pin.AM_DIR) : [
                pin.SRC_OUT | pin.MAR_IN,
                pin.RAM_OUT | pin.T1_IN,
                pin.DST_OUT | pin.MAR_IN,
                pin.RAM_IN | pin.T1_OUT
            ],
            (pin.AM_DIR, pin.AM_RAM) : [
                pin.SRC_R | pin.MAR_IN,
                pin.RAM_OUT | pin.T1_IN,
                pin.DST_OUT | pin.MAR_IN,
                pin.RAM_IN | pin.T1_OUT
            ],
            (pin.AM_RAM, pin.AM_INS) : [
                pin.DST_R | pin.MAR_IN,
                pin.RAM_IN | pin.SRC_OUT
            ],
            (pin.AM_RAM, pin.AM_REG) : [
                pin.DST_R | pin.MAR_IN,
                pin.RAM_IN | pin.SRC_R
            ],
            (pin.AM_RAM, pin.AM_DIR) : [
                pin.SRC_OUT | pin.MAR_IN,
                pin.RAM_OUT | pin.T1_IN,
                pin.DST_R | pin.MAR_IN,
                pin.RAM_IN | pin.T1_OUT
            ],
            (pin.AM_RAM, pin.AM_RAM) : [
                pin.SRC_R | pin.MAR_IN,
                pin.RAM_OUT | pin.T1_IN,
                pin.DST_R | pin.MAR_IN,
                pin.RAM_IN | pin.T1_OUT
            ],
        },
        ADD : {
            (pin.AM_REG, pin.AM_INS): [
                pin.DST_R | pin.A_IN,
                pin.SRC_OUT | pin.B_IN,
                pin.OP_ADD | pin.ALU_OUT | pin.DST_W | pin.ALU_PSW,
            ],
            (pin.AM_REG, pin.AM_REG): [
                pin.DST_R | pin.A_IN,
                pin.SRC_R | pin.B_IN,
                pin.OP_ADD | pin.ALU_OUT | pin.DST_W | pin.ALU_PSW,
            ],
        },
        SUB : {
            (pin.AM_REG, pin.AM_INS): [
                pin.DST_R | pin.A_IN,
                pin.SRC_OUT | pin.B_IN,
                pin.OP_SUB | pin.ALU_OUT | pin.DST_W | pin.ALU_PSW,
            ],
            (pin.AM_REG, pin.AM_REG): [
                pin.DST_R | pin.A_IN,
                pin.SRC_R | pin.B_IN,
                pin.OP_SUB | pin.ALU_OUT | pin.DST_W | pin.ALU_PSW,
            ],
        },
        CMP : {
            (pin.AM_REG, pin.AM_INS): [
                pin.DST_R | pin.A_IN,
                pin.SRC_OUT | pin.B_IN,
                pin.OP_SUB | pin.ALU_PSW,
            ],
            (pin.AM_REG, pin.AM_REG): [
                pin.DST_R | pin.A_IN,
                pin.SRC_R | pin.B_IN,
                pin.OP_SUB | pin.ALU_PSW,
            ],
        },
        AND : {
            (pin.AM_REG, pin.AM_INS): [
                pin.DST_R | pin.A_IN,
                pin.SRC_OUT | pin.B_IN,
                pin.OP_AND | pin.ALU_OUT | pin.DST_W | pin.ALU_PSW,
            ],
            (pin.AM_REG, pin.AM_REG): [
                pin.DST_R | pin.A_IN,
                pin.SRC_R | pin.B_IN,
                pin.OP_AND | pin.ALU_OUT | pin.DST_W | pin.ALU_PSW,
            ],
        },
        OR : {
            (pin.AM_REG, pin.AM_INS): [
                pin.DST_R | pin.A_IN,
                pin.SRC_OUT | pin.B_IN,
                pin.OP_OR | pin.ALU_OUT | pin.DST_W | pin.ALU_PSW,
            ],
            (pin.AM_REG, pin.AM_REG): [
                pin.DST_R | pin.A_IN,
                pin.SRC_R | pin.B_IN,
                pin.OP_OR | pin.ALU_OUT | pin.DST_W | pin.ALU_PSW,
            ],
        },
        XOR : {
            (pin.AM_REG, pin.AM_INS): [
                pin.DST_R | pin.A_IN,
                pin.SRC_OUT | pin.B_IN,
                pin.OP_XOR | pin.ALU_OUT | pin.DST_W | pin.ALU_PSW,
            ],
            (pin.AM_REG, pin.AM_REG): [
                pin.DST_R | pin.A_IN,
                pin.SRC_R | pin.B_IN,
                pin.OP_XOR | pin.ALU_OUT | pin.DST_W | pin.ALU_PSW,
            ],
        },
    },
    1 : {
        INC : {
            pin.AM_REG: [
                pin.DST_R | pin.A_IN,
                pin.OP_INC | pin.ALU_OUT | pin.DST_W | pin.ALU_PSW
            ],
        },
        DEC : {
            pin.AM_REG: [
                pin.DST_R | pin.A_IN,
                pin.OP_DEC | pin.ALU_OUT | pin.DST_W | pin.ALU_PSW
            ],
        },
        NOT : {
            pin.AM_REG: [
                pin.DST_R | pin.A_IN,
                pin.OP_NOT | pin.ALU_OUT | pin.DST_W | pin.ALU_PSW
            ],
        },
        JMP : {
            pin.AM_INS: [   
                pin.PC_IN | pin.DST_OUT,
            ],
        },
        # 调节跳转与无条件跳转的微操作完全一样，但 JMP 不管 PSW 是什么，在 ROM 里面，都会把这个微操作写上
        # 即，把 DST 的值放入 PC，完成跳转
        # 但是条件跳转不一样，会根据不同的 PSW 来到不同的 ROM 输入，虽然 ROM 输入最高 8 位都是一样的
        # 但 ROM 输出不一定是有这俩个微操作，可能就是继续下一条指令
        # 写 ROM 的时候就会根据 PSW 的值与不同的条件跳转进行判断，把 ROM 对应位置写下不同的微操作
        JO : {
            pin.AM_INS: [   
                pin.PC_IN | pin.DST_OUT,
            ],
        },
        JNO : {
            pin.AM_INS: [   
                pin.PC_IN | pin.DST_OUT,
            ],
        },
        JZ : {
            pin.AM_INS: [   
                pin.PC_IN | pin.DST_OUT,
            ],
        },
        JNZ : {
            pin.AM_INS: [   
                pin.PC_IN | pin.DST_OUT,
            ],
        },
        JP : {
            pin.AM_INS: [   
                pin.PC_IN | pin.DST_OUT,
            ],
        },
        JNP : {
            pin.AM_INS: [   
                pin.PC_IN | pin.DST_OUT,
            ],
        },
        PUSH : {
            pin.AM_REG: [
                pin.SP_OUT | pin.A_IN,
                pin.OP_DEC | pin.SP_IN | pin.ALU_OUT,
                pin.SP_OUT | pin.MAR_IN,
                pin.SS_OUT | pin.MSR_IN,
                pin.DST_R | pin.RAM_IN,
                pin.CS_OUT | pin.MSR_IN,
            ],
            pin.AM_INS: [
                pin.SP_OUT | pin.A_IN,
                pin.OP_DEC | pin.SP_IN | pin.ALU_OUT,
                pin.SP_OUT | pin.MAR_IN,
                pin.SS_OUT | pin.MSR_IN,
                pin.DST_OUT | pin.RAM_IN,
                pin.CS_OUT | pin.MSR_IN,
            ],
        },
        POP : {
            pin.AM_REG: [
                pin.SP_OUT | pin.MAR_IN,
                pin.SS_OUT | pin.MSR_IN,
                pin.DST_W | pin.RAM_OUT,
                pin.SP_OUT | pin.A_IN,
                pin.OP_INC | pin.SP_IN | pin.ALU_OUT,
                pin.CS_OUT | pin.MSR_IN,
            ],
        },
        CALL : {
            pin.AM_INS: [
                pin.SP_OUT | pin.A_IN,
                pin.OP_DEC | pin.SP_IN | pin.ALU_OUT,
                pin.SP_OUT | pin.MAR_IN,
                pin.SS_OUT | pin.MSR_IN,
                pin.PC_OUT | pin.RAM_IN,
                pin.DST_OUT | pin.PC_IN,
                pin.CS_OUT | pin.MSR_IN,
            ],
            pin.AM_REG: [
                pin.SP_OUT | pin.A_IN,
                pin.OP_DEC | pin.SP_IN | pin.ALU_OUT,
                pin.SP_OUT | pin.MAR_IN,
                pin.SS_OUT | pin.MSR_IN,
                pin.PC_OUT | pin.RAM_IN,
                pin.DST_R | pin.PC_IN,
                pin.CS_OUT | pin.MSR_IN,
            ],
        },
        INT : {
            pin.AM_INS: [
                pin.SP_OUT | pin.A_IN,
                pin.OP_DEC | pin.SP_IN | pin.ALU_OUT,
                pin.SP_OUT | pin.MAR_IN,
                pin.SS_OUT | pin.MSR_IN,
                pin.PC_OUT | pin.RAM_IN,
                pin.DST_OUT | pin.PC_IN,
                pin.CS_OUT | pin.MSR_IN | pin.ALU_PSW | pin.ALU_CLI,
            ],
            pin.AM_REG: [
                pin.SP_OUT | pin.A_IN,
                pin.OP_DEC | pin.SP_IN | pin.ALU_OUT,
                pin.SP_OUT | pin.MAR_IN,
                pin.SS_OUT | pin.MSR_IN,
                pin.PC_OUT | pin.RAM_IN,
                pin.DST_R | pin.PC_IN,
                pin.CS_OUT | pin.MSR_IN | pin.ALU_PSW | pin.ALU_CLI,
            ],
        },
    },
    0 : {
        NOP : [
            pin.CYC,
        ],
        HLT : [
            pin.HLT
        ],
        RET : [
            pin.SP_OUT | pin.MAR_IN,
            pin.SS_OUT | pin.MSR_IN,
            pin.PC_IN | pin.RAM_OUT,
            pin.SP_OUT | pin.A_IN,
            pin.OP_INC | pin.SP_IN | pin.ALU_OUT,
            pin.CS_OUT | pin.MSR_IN,
        ],
        IRET : [
            pin.SP_OUT | pin.MAR_IN,
            pin.SS_OUT | pin.MSR_IN,
            pin.PC_IN | pin.RAM_OUT,
            pin.SP_OUT | pin.A_IN,
            pin.OP_INC | pin.SP_IN | pin.ALU_OUT,
            pin.CS_OUT | pin.MSR_IN | pin.ALU_PSW | pin.ALU_STI,
        ],
        STI : [
            pin.ALU_PSW | pin.ALU_STI,
        ],
        CLI : [
            pin.ALU_PSW | pin.ALU_CLI,
        ]

    },
}