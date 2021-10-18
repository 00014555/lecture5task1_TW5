def biggest(num1, num2, num3):
    if (num1 >= num2) and (num1 >= num3):
        largest = num1
    elif (num2 >= num1) and (num2 >= num3):
        largest = num2
    else:
        largest = num3
        return largest

    def testIsBiggest():
        test1 = biggest(15, 45, 30)
        test2 = biggest(100, 50, 10)
        test3 = biggest(1, 2, 3)
        print(test1, test2, test3)

        testIsBiggest()









# season = input("Enter the season: ")
# if season == "winter":
#     print("dec, jan, feb")
# elif season == "spring":
#     print("mar, apr, may")
# elif season == "summer":
#     print("jun, jul, aug")
# elif season == "autumn":
#     print("sep, oct, nov")
# else:
#     print("wrong input")


















# y = 7
# x = 8
# if x == y:
#     print('x and y are equal')
# else:
#     if x < y:
#         print('x is less than y')
#     else:
#         print('x is greater than y')






# x = int(input("Enter the number"))
# if x > 0:
#    print("x is positive")
# elif x<0:
#    print("x is negative")
# else:
#     print("x is zero")