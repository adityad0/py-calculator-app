try:
    from tkinter import *
except ModuleNotFoundError:
    print("Tkinter was not found!")
    quit()

# The value ("expression") of the input box
expression = ""


# Function to update expression in the text box
def press(num):
    global expression

    expression = expression + str(num)

    # Set the value of the input box to that of the equation
    equation.set(expression)


# Function to evaluate the final expression using the eval function
def equalpress():
    try:
        global expression

        answer = str(eval(expression))

        equation.set(answer)

        # Reset the expression to an empty string.
        expression = ""

	# Catch synatx and division by zero errors and show the error message
    except ZeroDivisionError:
        equation.set("Cannot divide by 0")
        expression = ""
    except SyntaxError:
        equation.set("Syntax Error")
        expression = ""

def clear():
    # This function will clear the contents of the input box. (Set the value to and empty string)
	global expression
	expression = ""
	equation.set("")


def main():
    global equation

    # Set colors for the app
    BACKGROUND_COLOR = '#EDEBD7'
    BUTTON_BACKGROUND = '#0000FF'
    BUTTON_FOREGROUND = '#FFFFFF'
    SYMBOLS_BTNS_BG = '#C8961C'
    SYMBOLS_BTNS_FG = '#FFFFFF'
    EQUAL_BTN_BG = '#1B998B'
    EQUAL_BTN_FG = '#FFFFFF'
    CLR_BTN_BG = '#C42847'
    CLR_BTN_FG = '#FFFFFF'

	# Create the GUI window
    gui = Tk()

	# Background color of the root window
    gui.configure(background = BACKGROUND_COLOR)

	# Title of the window
    gui.title("Calculator")

	# Height and width dimentions of the GUI window
    gui.geometry("424x215")

	# StringVar() is the variable class
	# we create an instance of this class
    equation = StringVar()

	# Creating the input box to enter an equation and show the output
    expression_field = Entry(gui, textvariable=equation, width=14)
    expression_field.place(x = 10, y = 10, width=200, height=100)

    # A grid is created with a width of 6 items and each item is placed using a coordinate system like a table
    expression_field.grid(columnspan = 6, ipadx = 70)

    # BUTTON
    # text: The text on the button
    # fg: Foreground (Text) color
    # bg: Background color
    # command: The function that will be called on button click
    # height: The height of the button
    # width: The width of the button
    # border: Thickness of the border around the button
    # font: The name of the font being used and, the font size

    # Lambda function:

    # GRID:
    '''
                     INPUT_BOX(0,0)
    C(1,0)       ()(1,1)      %(1,2)      +(1,3)
    1(2,0)        2(2,1)      3(2,2)      -(2,3)
    4(3,0)        5(3,1)      6(3,2)      *(3,3)
    7(4,0)        8(4,1)      9(4,2)      /(4,3)
    +/-(5,0)      0(5,1)      .(5,2)      =(5,3)
    '''

    clearBtn = Button(gui, text='Clear', fg = CLR_BTN_FG, bg = CLR_BTN_BG, command=clear, height=2, width=14, border=1, font=(("Poppins"),9))
    clearBtn.grid(row=2, column=0)

    parenthesesBtn = Button(gui, text=' ( ) ', fg = SYMBOLS_BTNS_FG, bg = SYMBOLS_BTNS_BG, command=lambda: press(''), height=2, width=14, border=1, font=(("Poppins"),9))
    parenthesesBtn.grid(row=2, column=1)

    # To get the remainder
    percentBtn = Button(gui, text=' % ', fg = SYMBOLS_BTNS_FG, bg = SYMBOLS_BTNS_BG, command=lambda: press('%'), height=2, width=14, border=1, font=(("Poppins"),9))
    percentBtn.grid(row=2, column=2)

    button1 = Button(gui, text=' 1 ', fg = BUTTON_FOREGROUND, bg = BUTTON_BACKGROUND, command=lambda: press(1), height=2, width=14, border=1, font=(("Poppins"),9))
    button1.grid(row=3, column=0)

    button2 = Button(gui, text=' 2 ', fg = BUTTON_FOREGROUND, bg = BUTTON_BACKGROUND, command=lambda: press(2), height=2, width=14, border=1, font=(("Poppins"),9))
    button2.grid(row=3, column=1)

    button3 = Button(gui, text=' 3 ', fg = BUTTON_FOREGROUND, bg = BUTTON_BACKGROUND, command=lambda: press(3), height=2, width=14, border=1, font=(("Poppins"),9))
    button3.grid(row=3, column=2)

    button4 = Button(gui, text=' 4 ', fg = BUTTON_FOREGROUND, bg = BUTTON_BACKGROUND,command=lambda: press(4), height=2, width=14, border=1, font=(("Poppins"),9))
    button4.grid(row=4, column=0)

    button5 = Button(gui, text=' 5 ', fg = BUTTON_FOREGROUND, bg = BUTTON_BACKGROUND,command=lambda: press(5), height=2, width=14, border=1, font=(("Poppins"),9))
    button5.grid(row=4, column=1)

    button6 = Button(gui, text=' 6 ', fg = BUTTON_FOREGROUND, bg = BUTTON_BACKGROUND,command=lambda: press(6), height=2, width=14, border=1, font=(("Poppins"),9))
    button6.grid(row=4, column=2)

    button7 = Button(gui, text=' 7 ', fg = BUTTON_FOREGROUND, bg = BUTTON_BACKGROUND,command=lambda: press(7), height=2, width=14, border=1, font=(("Poppins"),9))
    button7.grid(row=5, column=0)

    button8 = Button(gui, text=' 8 ', fg = BUTTON_FOREGROUND, bg = BUTTON_BACKGROUND, command=lambda: press(8), height=2, width=14, border=1, font=(("Poppins"),9))
    button8.grid(row=5, column=1)

    button9 = Button(gui, text=' 9 ', fg = BUTTON_FOREGROUND, bg = BUTTON_BACKGROUND,command=lambda: press(9), height=2, width=14, border=1, font=(("Poppins"),9))
    button9.grid(row=5, column=2)

    button0 = Button(gui, text=' 0 ', fg = BUTTON_FOREGROUND, bg = BUTTON_BACKGROUND, command=lambda: press(0), height=2, width=14, border=1, font=(("Poppins"),9))
    button0.grid(row=6, column=1)

    plus = Button(gui, text=' + ', fg = SYMBOLS_BTNS_FG, bg = SYMBOLS_BTNS_BG, command=lambda: press("+"), height=2, width=14, border=1, font=(("Poppins"),9))
    plus.grid(row=2, column=3)

    minus = Button(gui, text=' - ', fg = SYMBOLS_BTNS_FG, bg = SYMBOLS_BTNS_BG, command=lambda: press("-"), height=2, width=14, border=1, font=(("Poppins"),9))
    minus.grid(row=3, column=3)

    multiply = Button(gui, text=' * ', fg = SYMBOLS_BTNS_FG, bg = SYMBOLS_BTNS_BG, command=lambda: press("*"), height=2, width=14, border=1, font=(("Poppins"),9))
    multiply.grid(row=4, column=3)

    divide = Button(gui, text=' / ', fg = SYMBOLS_BTNS_FG, bg = SYMBOLS_BTNS_BG, command=lambda: press("/"), height=2, width=14, border=1, font=(("Poppins"),9))
    divide.grid(row=5, column=3)

    equal = Button(gui, text=' = ', fg = EQUAL_BTN_FG, bg = EQUAL_BTN_BG, command=equalpress, height=2, width=14, border=1, font=(("Poppins"),9))
    equal.grid(row=6, column=3)

    change_signBtn = Button(gui, text=' +/- ', fg = BUTTON_FOREGROUND, bg = BUTTON_BACKGROUND, height=2, width=14, border=1, font=(("Poppins"),9))
    change_signBtn.grid(row=6, column=0)

    Decimal= Button(gui, text='.', fg = BUTTON_FOREGROUND, bg = BUTTON_BACKGROUND, command=lambda: press('.'), height=2, width=14, border=1, font=(("Poppins"),9))
    Decimal.grid(row=6, column=2)

	# All objects are placed in the ROOT window i.e, gui

    # Start the gui
    gui.mainloop()

# Call main()
if __name__ == "__main__":
    main()