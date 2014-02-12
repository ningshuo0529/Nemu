#Packgen
import os

opcodes = [
    ("ADC", [
        (0x69, "IMM", 2, 2),
        (0x65, "ZP", 2, 3),
        (0x75, "ZPX", 2, 4),
        (0x60, "ABS", 3, 4),
        (0x70, "ABX", 3, 4),
        (0x79, "ABY", 3, 4),
        (0x61, "IIX", 2, 6),
        (0x71, "IIY", 2, 5)
        ]
     ),
    ("AND", [
        (0x29, "IMM", 2, 2),
        (0x25, "ZP", 2, 3),
        (0x35, "ZPX", 2, 4),
        (0x2D, "ABS", 3, 4),
        (0x3D, "ABX", 3, 4),
        (0x39, "ABY", 3, 4),
        (0x21, "IIX", 2, 6),
        (0x31, "IIY", 2, 5)
        ]
     ),
    ("ASL", [
        (0x0A, "ACC", 1, 2),
        (0x06, "ZP", 2, 5),
        (0x16, "ZPX", 2, 6),
        (0x0E, "ABS", 3, 6),
        (0x1E, "ABX", 3, 7)
        ]
     ),
    ("BCC", [
        (0x90, "REL", 2, 2)
        ]
     ),
    ("BCS", [
        (0xB0, "REL", 2, 2)
        ]
     ),
    ("BEQ", [
        (0xF0, "REL", 2, 2),
        ]
     )
    ,
    ("BIT", [
        (0x24, "ZP", 2, 3),
        (0x2C, "ABS", 3, 4),
        ]
     ),
    ("BMI", [
        (0x30, "REL", 2, 2)
        ]
     ),
    
# start of will's work
	("STA", [
		(0x85, "ZP", 2, 3),
		(0x95, "ZPX", 2, 4),
		(0x80, "ABS", 3, 4),
		(0x90, "ABX", 3, 5),
		(0x99, "ABY", 3, 5),
		(0x81, "IIX", 2, 6),
		(0x91, "IIY", 2, 6)
		]
	 ),
	("STX", [
		(0x86, "ZP", 2, 3),
		(0x96, "ZPY", 2, 4),
		(0x8E, "ABS", 3, 4)
		]
	 ),
	("STY", [
		(0x84, "ZP", 2, 3),
		(0x94, "ZPX", 2, 4),
		(0x8C, "ABS", 3, 4)
		]
	 ),
	("TAX", [
		(0xAA, "IMP", 1, 2)
		]
	 ),
	("TAY", [
		(0xA8, "IMP", 1, 2)
		]
	 ),
	("TSX", [
		(0xBA, "IMP", 1, 2)
		]
	 ),
	("TXA", [
		(0x8A, "IMP", 1, 2)
		]
	 ),
	("TXS", [
		(0x9A, "IMP", 1, 2)
		]
	 ),
	("TYA", [
		(0x98, "IMP", 1, 2)
		]
	 ),
]

table = dict()
fi = open("../src/InstructionTable.inc", "w")

for x in range(0, 255):
    table[x] = ("NOP", "NOP", "NOP")

for op in opcodes:
    for version in op[1]:
        table[version[0]] = (op[0], version[1])

fi.write("const InstructionPack const Table[] = {\n")
for k,v in table.iteritems():
    fi.write("\t{ " + v[1] +  " , " + v[0] + " , NOP }, //" + hex(k) + "\n")
fi.write("};\n")
fi.close()



