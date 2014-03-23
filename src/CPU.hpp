#pragma once

#include <cstdint>
#include <array>

class VMemory;

namespace InstructionTable
{
	class InstructionPack;
};

class CPU
{
public:
	CPU();

	std::array<uint8_t, 0x800> RAM;
	VMemory* Memory;

	uint8_t A, SP, X, Y;
	uint16_t PC;
	uint8_t IR;


	int Addr;

	bool Asserted;

	unsigned CurrentCyle;
	const InstructionTable::InstructionPack* Instruction;

	union
	{
		struct
		{
			uint8_t CarryFlag : 1;
			uint8_t ZeroFlag : 1;
			uint8_t InterruptFlag : 1;
			uint8_t DecimalFlag : 1;

			uint8_t BreakFlag : 1;
			uint8_t __UnusedFlag : 1;
			uint8_t OverflowFlag : 1;
			uint8_t SignFlag : 1;
		};
		uint8_t Status;
	};

	void DumpRegisters();
	void Fetch();

	void Execute();

	uint8_t Read(int addr);

	uint8_t Write(int addr, uint8_t value);

	void Interrupt();

	void Cycle();

	uint8_t Pop();
	void Push(uint8_t value);

	void SoftReset();

	void HardReset();
};

