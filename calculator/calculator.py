#calculator app

def menu():
    print("""
          0. Exit
          1. Add
          2. Sub
          3. Multiply
          4. Divide
          5. Exponent
          """)
          
while True:
    menu()
    memory = []
    try:
        choice = int(input("Enter your choice ---> "))
    except ValueError:
        print("Enter a valid option.")
        continue

    if choice == 0:
        print("Exiting...")
        break

    elif choice == 1:
        
        while True:
            if not memory:
                num = int(input("Enter the first digit : "))
                if num == 0:
                    memory = []
                    break
                memory.append(num)
            num = int(input("Enter a number to add (or type 0 if u wanna exit) :"))
            if num == 0:
                break
            memory.append(num)
            print("current sum ---> ",memory, "'s total = " ,sum(memory))

    elif choice == 2:
        
        while True:
            if not memory:
                num = int(input("Enter the first didgit : "))
                if num == 0:
                    memory = []
                    break
                memory.append(num)
                diff = num

            num = int(input("Enter a number to sub (or type 0 to exit) : "))
            if num == 0:
                break
            diff -= num
            memory.append(num)
            print(memory, "its difference = ", diff)

    elif choice == 3:
        
        while True:
            if not memory:
                num = int(input("Enter the first digit : "))
                if num == 0:
                    memory = []
                    break
                memory.append(num)
                product = num

            num = int(input("Enter a num to multiply (or enter 0 to exit) : "))
            if num == 0:
                memory = []
                print("dumbo anything x 0 is 0 except for 0")
                break
            memory.append(num)
            product *= num
            print(memory, "its product is", product)

    elif choice == 4:
        
        while True:
            if not memory:
                num = int(input("Enter the first digit : "))
                if num == 0:
                    memory = []
                    break
                memory.append(num)
                quotient = num

            num = int(input("Enter a num to divide (or enter 0 to exit) : "))
            if num == 0:
                print("cant divide by 0.")
                break
            memory.append(num)
            remainder = quotient % num
            quotient /= num
            print(memory, "its quotient is", quotient, "and remainder is ", remainder)

    elif choice == 5:
        
        while True:
            if not memory:
                num = int(input("Enter the base num : "))
                if num == 0:
                    memory = []
                    break
                memory.append(num)
                exponent = num #base

            num = int(input("Enter a num to raise to (or enter 0 to exit) : "))
            if num == 0:
                print("anything power 0 is 1.")
                break
            memory.append(num)
            print(memory)
            print(exponent,"raised to the power", num, "is : ")
            exponent = exponent ** num
            print(exponent)

    else:
        print("try again.")