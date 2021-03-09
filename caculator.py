import math
import tkinter as tk
class GUI(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.equation = ""
        self.solution = ""
        self.pack()
        self.create_widgets()
    ############################################# CREATE ALL GUI #############################################################
    def create_widgets(self):
        # Creates the equation and solution text box #
        self.equation_text_box = tk.Label(master=self, text=self.equation)
        self.equation_text_box.pack(side = "top")
        self.solution_text_box = tk.Label(master=self, text=self.solution)
        self.solution_text_box.pack(side = "top")
        # PRIMARY PAD FOR ALL BUTTONS #
        pad = tk.Frame(master=self,width = 300,height = 300)
        pad.pack(side = "bottom")

        ############### SECONDARY PAD FOR BUTTON NUMBERS (1-9) ####################
        number_pad = tk.Frame(master=pad,width=150,height=150)
        number_pad.grid(row=0,column=1)
        self.btn1 = tk.Button(master=number_pad,text="1",width=4,height=3,command=self.np1)
        self.btn1.grid(row=0,column=0)

        self.btn2 = tk.Button(master=number_pad,text="2",width=4,height=3,command=self.np2)
        self.btn2.grid(row=0,column=1)

        self.btn3 = tk.Button(master=number_pad,text="3",width=4,height=3,command=self.np3)
        self.btn3.grid(row=0,column=2)

        self.btn4 = tk.Button(master=number_pad,text="4",width=4,height=3,command=self.np4)
        self.btn4.grid(row=1,column=0)

        self.btn5 = tk.Button(master=number_pad,text="5",width=4,height=3,command=self.np5)
        self.btn5.grid(row=1,column=1)

        self.btn6 = tk.Button(master=number_pad,text="6",width=4,height=3,command=self.np6)
        self.btn6.grid(row=1,column=2)

        self.btn7 = tk.Button(master=number_pad,text="7",width=4,height=3,command=self.np7)
        self.btn7.grid(row=2,column=0)

        self.btn8 = tk.Button(master=number_pad,text="8",width=4,height=3,command=self.np8)
        self.btn8.grid(row=2,column=1)

        self.btn9 = tk.Button(master=number_pad,text="9",width=4,height=3,command=self.np9)
        self.btn9.grid(row=2,column=2)
        #####################################################################################

        ####################### SECONDARY PAD FOR ALL SIGNS (+,-,*,/,^) #################################
        signs_pad = tk.Frame(master=pad,width=150,height=150)
        signs_pad.grid(row=0,column=2)

        self.add_sign = tk.Button(master=signs_pad,text="+",fg="black",width=4,height=3,command=self.add)
        self.add_sign.grid(row=0,column=0)
        self.subtract_sign = tk.Button(master=signs_pad,text="-",fg="black",width=4,height=3,command=self.subtract)
        self.subtract_sign.grid(row=0,column=1)
        self.multiply_sign = tk.Button(master=signs_pad,text="*",fg="black",width=4,height=3,command=self.multiply)
        self.multiply_sign.grid(row=0,column=2)
        self.division_sign = tk.Button(master=signs_pad,text="/",fg="black",width=4,height=3,command=self.devide)
        self.division_sign.grid(row=1,column=0)
        self.exponent_sign = tk.Button(master=signs_pad,text="^",fg="black",width=4,height=3,command=self.exponent)
        self.exponent_sign.grid(row=1,column=1)
        self.decimal_sign = tk.Button(master=signs_pad,text=".",fg="black",width=4,height=3,command=self.decimal)
        self.decimal_sign.grid(row=1,column=2)
        self.leftparen_sign = tk.Button(master=signs_pad,text="(",fg="black",width=4,height=3,command=self.leftparen)
        self.leftparen_sign.grid(row=2,column=0)
        self.rightparen_sign = tk.Button(master=signs_pad,text=")",fg="black",width=4,height=3,command=self.rightparen)
        self.rightparen_sign.grid(row=2,column=1)
        #####################################################################################################################
        ##################### SECONDARY PAD FOR ALL CONFIGURING BUTTONS (ENTER,EXIT,DELETE) #####################################################
        configure_pad = tk.Frame(master=pad,width=150,height=150)
        configure_pad.grid(row=1,column=1)

        ############# Special case : I put numpad-zero here because it would not fit inside the 3x3 numpad ###########
        self.btn10 = tk.Button(master=configure_pad,text="0",width=4,height=3,command=self.np10)
        self.btn10.grid(row=0,column=1)

        self.quit = tk.Button(master=configure_pad,text="<-",fg="red",width=3,height=3,command=self.delete)
        self.quit.grid(row=0,column=0)
        self.enter = tk.Button(master=configure_pad,text="=",fg="green",width=3,height=3,command=self.enter)
        self.enter.grid(row=0,column=2)
        self.delete = tk.Button(master=configure_pad,text="RES",fg="red",width=4,height=3,command=self.delete_all)
        self.delete.grid(row=1,column=1)
        #############################################################################################################
    ############################################# ALL BUTTON EVENTS #####################################################
    def np1(self): 
        self.equation+='1'
        self.update_command_line()
    def np2(self): 
        self.equation+='2'
        self.update_command_line()
    def np3(self): 
        self.equation+='3'
        self.update_command_line()
    def np4(self): 
        self.equation+='4'
        self.update_command_line()
    def np5(self): 
        self.equation+='5'
        self.update_command_line()
    def np6(self): 
        self.equation+='6'
        self.update_command_line()
    def np7(self): 
        self.equation+='7'
        self.update_command_line()
    def np8(self): 
        self.equation+='8'
        self.update_command_line()
    def np9(self): 
        self.equation+='9'
        self.update_command_line()
    def np10(self): 
        self.equation+='0'
        self.update_command_line()
    def add(self):
        # if placed when equation box is empty and solution box is not empty (meaning a problem already has been solved)... re add the solution to the equation. 
        if self.problem_already_answered: self.equation+=self.solution+'+'
        else: self.equation+='+'
        self.update_command_line()
    def subtract(self): 
        if self.problem_already_answered(): self.equation+=self.solution+'-'
        else: self.equation+='-'
        self.update_command_line()
    def multiply(self): 
        if self.problem_already_answered(): self.equation+=self.solution+'*'
        else: self.equation+='*'
        self.update_command_line()
    def devide(self): 
        if self.problem_already_answered(): self.equation+=self.solution+'/'
        else: self.equation+='/'
        self.update_command_line()
    def exponent(self):
        if self.problem_already_answered(): self.equation+=self.solution+'^'
        else: self.equation+='^'
        self.update_command_line()
    def decimal(self):
        self.equation+="."
        self.update_command_line()
    def leftparen(self):
        self.equation+='('
        self.update_command_line()
    def rightparen(self):
        self.equation+=')'
        self.update_command_line()
    def enter(self):
        cac = Caculator(self.equation)
        cac.solve_number_problem()
        self.solution= cac.return_solution()
        self.equation = ""
        self.update_command_line()
    def delete(self):
        self.equation = self.equation[:-1]
        self.update_command_line()
    def delete_all(self):
        self.equation = ""
        self.solution  = ""
        self.update_command_line()
    ###################################### UPDATE BOTH PROBLEM AND SOLUTION LABEL BOXES ####################################
    def update_command_line(self):
        self.equation_text_box["text"] = self.equation
        self.solution_text_box["text"] = self.solution
    ###################################### CHECKS IF THE EQUATION TEXT IS EMPTY AND THE SOLUTION TEXT IS NOT EMPTY OR INF... IF SO RETURN TRUE ######################################
    def problem_already_answered(self):
        return self.equation == "" and self.solution != "" and self.solution != "inf" and self.solution != "-inf" 

class Caculator:
    def __init__(self, problem_input,x=0,y=0):
        print(problem_input)
        self.problem_input = problem_input.strip(" ")
        self.pemdas = {'(':4,')':4,'^':3,'*':2,'/':2,'+':1,'-':1}
        self.signs = ['+','*','-','/','^']
        self.solved_solution = 0

    def solve_number_problem(self):
        c = 0
        problem_list = [""]
        # make string problem into list form
        for char in self.problem_input:
            if char in self.signs:
                problem_list.append(char)
                problem_list.append("")
                c+=2
            else:
                problem_list[c] += char
        # if first list element is a sign return nothing
        if problem_list[0] in self.signs:
            return
        # if not  a complete 3 part problem, exit | example - (['5'] ['+'] ['5']) is length 3 but (['5'], ['+']) is 2 
        while len(problem_list) >= 2:
            sign_value = 0
            # PAMDAS ALGORITHN - Goes through all signs in list and gets the highest ranked sign according to PEMDAS, for example (* is higher ranked than +)
            for l,v in enumerate(problem_list):
                if v in self.signs:
                    if (self.pemdas[v] > sign_value):
                        sign_value = self.pemdas[v]
                        sign = v
                        loc = l
            # get the two numbers beside the highest ranked sign according to PEMDAS...
            # converting it to a float to make it compatiable with float pointing numbers from division | '10' to 10.0
            try:
                num1 = float(problem_list[loc-1])
                num2 = float(problem_list[loc+1])
            # if number cannot be converted change it to inf if positive and -inf if negative instead
            except:
                for char in str(self.solved_solution):
                    if char == "+":
                        self.solved_solution = "inf"
                        return
                    elif char == "-":
                        self.solved_solution = "-inf"
                        return
            # do the operation
            if sign == '+': self.solved_solution = num1 + num2
            elif sign == '*': self.solved_solution = num1 * num2
            elif sign == '-': self.solved_solution = num1 - num2
            elif sign == "/": self.solved_solution = num1 / num2
            elif sign == '^': self.solved_solution = num1 ** num2
            # get the two numbers beside the highest ranked sign according to PEMDAS and the highest ranking sign and remove them (['5','+','5'])...
            for _ in range(3): problem_list.pop(loc-1)
            # readd the solution to those 2 numbers and add it back
            problem_list.insert(loc-1, self.solved_solution)

    def return_solution(self):
        return str(self.solved_solution)
def main():
    root = tk.Tk()
    gui = GUI(master=root)
    gui.mainloop()

if __name__ == '__main__':
    main()
