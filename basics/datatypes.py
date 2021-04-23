

def datatypes_analysis():
    numeric_pure = '123'
    numeric_signed = '+12'
    numeric_signed_wrong = '+-12'
    alphanumeric_pure = '123abc'
    just_math_op = '+'


    print(f'{numeric_pure} isnumeric ? {numeric_pure.isnumeric()}')
    print(f'{numeric_signed} isnumeric ? {numeric_pure.isnumeric()}')
    print(f'{numeric_signed_wrong} isnumeric ? {numeric_pure.isnumeric()}')
    print(f'{alphanumeric_pure} isnumeric ? {alphanumeric_pure.isnumeric()}')
    print(f'{just_math_op} isnumeric ? {just_math_op.isnumeric()}')


def main():
    datatypes_analysis()


if __name__ == '__main__':
    main()