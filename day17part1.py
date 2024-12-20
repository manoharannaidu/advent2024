def run_program(program, A, B, C):
    registers = {'A': A, 'B': B, 'C': C}
    pointer = 0
    output = []

    def get_combo_value(operand):
        if operand <= 3:
            return operand  # literal value
        elif operand == 4:
            return registers['A']
        elif operand == 5:
            return registers['B']
        elif operand == 6:
            return registers['C']
        else:
            raise ValueError("Invalid combo operand: 7 is reserved.")

    while pointer < len(program):
        opcode = program[pointer]  # Current instruction's opcode
        operand = program[pointer + 1]  # Operand for the current instruction

        if opcode == 0:  # adv: Division into register A
            denominator = 2 ** get_combo_value(operand)
            if denominator != 0:
                registers['A'] = registers['A'] // denominator
        elif opcode == 1:  # bxl: Bitwise XOR into register B
            registers['B'] ^= operand
        elif opcode == 2:  # bst: Modulo 8 into register B
            registers['B'] = get_combo_value(operand) % 8
        elif opcode == 3:  # jnz: Jump if A is not 0
            if registers['A'] != 0:
                pointer = operand
                continue  # Skip pointer increment
        elif opcode == 4:  # bxc: Bitwise XOR B and C into register B
            # Operand is ignored
            registers['B'] ^= registers['C']
        elif opcode == 5:  # out: Output value modulo 8
            output.append(get_combo_value(operand) % 8)
        elif opcode == 6:  # bdv: Division into register B
            denominator = 2 ** get_combo_value(operand)
            if denominator != 0:
                registers['B'] = registers['A'] // denominator
        elif opcode == 7:  # cdv: Division into register C
            denominator = 2 ** get_combo_value(operand)
            if denominator != 0:
                registers['C'] = registers['A'] // denominator
        else:
            raise ValueError(f"Unknown opcode: {opcode}")

        pointer += 2

    return ",".join(map(str, output))


initial_A = 64012472
initial_B = 0
initial_C = 0
program = [2,4,1,7,7,5,0,3,1,7,4,1,5,5,3,0]  

result = run_program(program, initial_A, initial_B, initial_C)
print("Output:", result)
