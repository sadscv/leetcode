def get_bit(input):
    return len(str(input))

def str2int(input):
    output = 0
    for i in range(len(input)):
        output += 10**i * int(input[-i-1])
    return output

def test(input):
    input = int(input)
    bit = get_bit(input)
    list = [format(i, 'b').zfill(bit) for i in range(2**bit)]
    # list = [format(i, 'b').zfill(bit) for i in range(2 ** (bit-1), 2**bit)]
    output = [ j for j in list if str2int(j) <= input]
    print(len(output))




if __name__ == '__main__':

    x = input('enter a number:')
    test(x)
