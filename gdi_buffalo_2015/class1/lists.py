"""
filename: lists.py
author: wendyjan

This file shows lists in Python using Turtle and printing.
"""
import turtle

if __name__ == "__main__":
    print("List basics!")
    my_list = [1, 1, 2, 3, 5, 8, 13, 21]
    print(my_list)
    for number in my_list: 
        print(number)
    
    print('\n')
    print("List indexing!")
    print("The first element in my list is:", my_list[0])
    print("The last element in my list is:", my_list[-1])
    print("The length of my list is:", len(my_list))
    # TODO Print the second-to-last element in the array.

    print('\n')
    print("Lists and types!")
    my_mixed_list = [1, 1, 2, 3, "shell", "petal", 13, 21.0]
    for thing in my_mixed_list:
	print(thing, "is of type:", type(thing))
    import turtle
    ted = turtle.Turtle()
    ted.speed(1)
    for temp_color in ["red", "blue", "green", "black"]:
        ted.color(temp_color) 
        ted.forward(100)
        ted.right(90)
    for index in range(4):
        ted.forward(50)
        ted.right(90)
    turtle.done()

    print('\n')
    print("List slicing!")
    students = ["Wendy", "Anne", "Ryan", "Lena", "Jess"]
    print ("The first two students to arrive are:",students[0:2])
    print("And the last three are:", students[-3:])
    # Print the last student to arrive in class.
    # Can you do it two different ways?

    print('\n')
    print("List shortcuts!")
    print(list(range(5)))
    for i in range(5):
        print(i)
    print(list(range(1, 6, 1)))
    print(list(range(1, 6, 2)))
    print(list(range(5, 0, -1)))

    print('\n')
    print("Copying a list!")
    list_a = list(range(10))
    print ("list_a:", list_a)
    list_b = list_a
    print ("list_b = list_a")
    print ("Now let's change the first element in list_b")
    print ("We'll change it from", list_b[0], "to 200")
    list_b[0] = 200
    print ("list_b is now:", list_b)
    print ("and list_a is:", list_a)

    print ('\n')
    print ("List Methods!")
    print ("list_a is still", list_a)
    list_a.append(35)
    print (list_a)
    list_a.reverse() 
    print (list_a)
    list_a.remove(1)
    print (list_a)
    print (list_a.pop())
    print (list_a)
