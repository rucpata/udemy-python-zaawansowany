instruction = ['say hello', 'say how are you', 'abort', 'ask for money', 'say thank you', 'say bye']
instructionApprove = []

for instr in instruction:
    print('Adding istruction: ', instr)
    instructionApprove.append(instr)

    if instr == 'abort':
        print('Aborting!!!')
        instructionApprove.clear()
        break
else:
    print('Following actions will be taken: ', instructionApprove)


print('-'*30)
instructionApprove.clear()

i = 0
while i <len(instruction):
    print('Adding istruction: ', instruction[i])
    instructionApprove.append(instruction[i])

    if instruction[i] == 'abort':
        print('Aborting!!!')
        instructionApprove.clear()
    break

    i += 1
else:
    print('Following actions will be taken: ', instructionApprove)