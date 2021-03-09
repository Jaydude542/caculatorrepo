import math
import tkinter as tk
class GUI(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.equation = ""
        self.solution = ""
        self.equation_text_box = tk.Label(master=self, text=self.equation)
        self.equation_text_box.pack(side = "top")
        self.solution_text_box = tk.Label(master=self, text=self.solution)
        self.solution_text_box.pack(side = "top")
        self.pack()
        self.create_widgets()
    ############################################# CREATE ALL GUI #############################################################
    def create_widgets(self):
        
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
        self.equation+='+'
        self.update_command_line()
    def subtract(self): 
        self.equation+='-'
        self.update_command_line()
    def multiply(self): 
        self.equation+='*'
        self.update_command_line()
    def devide(self): 
        self.equation+='/'
        self.update_command_line()
    def exponent(self):
        self.equation+='^'
        self.update_command_line()
    def decimal(self):
        self.equation+="."
        self.update_command_line()
    def enter(self):
        print(self.equation)
        cac = Caculator(self.equation)
        self.solution= cac.return_solution()
        self.update_command_line()
    def delete(self):
        self.equation = self.equation[:-1]
        self.update_command_line()
    def delete_all(self):
        self.equation = ""
        self.solution  = ""
        self.update_command_line()
    ###################################### CREATE AND UPDATE BOTH PROBLEM AND SOLUTION LABEL BOXES ####################################
    def update_command_line(self):
        self.equation_text_box["text"] = self.equation
        self.solution_text_box["text"] = self.solution

class Caculator:
    def __init__(self, problem_input,x=0,y=0):
        self.problem_input = problem_input.strip(" ")
        self.x,self.y = x,y
        self.pemdas = (('(',')'),('^','^'),('*','/'),('+','-'))
        self.variables = ['x','y']
        self.signs = ['+','*','-','/','^']
        self.inequality_signs = ['<','>','<=','>=']
        self.organized_problem = []
        self.solved_solution = 0
        self.translate_problem()
    def translate_problem(self):
        for char in self.problem_input:
            if char in self.variables[0]:
                self.organized_problem.append(self.x)
            elif char in self.variables[1]:
                self.organized_problem.append(self.y)

        return self._find_type_problem()
    def _find_type_problem(self):
        # Checking what type of problem it is.
        for char in self.inequality_signs: 
            if char in self.organized_problem: self._solve_inequality()
        if '=' in self.organized_problem: self._solve_equation()
        elif (self.x + self.y == 0):
            self.organized_problem = self.problem_input 
            self._solve_number_problem()
        else: self._solve_expression()

    def _solve_number_problem(self):
        c = 0
        str_lst = [""]
        # make string problem into list form
        for char in self.organized_problem:
            if char.isnumeric():
                str_lst[c] += char
            elif char in self.signs:
                str_lst.append(char)
                str_lst.append("")
                c+=2
        # if first list element is a sign return nothing
        if str_lst[0] in self.signs:
            return
        # if not  a complete 3 part problem, exit | example - (['5'] ['+'] ['5']) is length 3 but (['5'], ['+']) is 2 
        while len(str_lst) >= 2:
            # get first sign in list
            for loc,val in enumerate(str_lst):
                if val in self.signs:
                    sign = val
                    break
            # put the two numbers in the front in variables...
            # converting it to a float to make it compatiable with float pointing numbers from division | '10' to 10.0
            num1 = float(str_lst[0])
            num2 = float(str_lst[2])
            # do the operation
            if sign == '+': self.solved_solution = num1 + num2
            elif sign == '*': self.solved_solution = num1 * num2
            elif sign == '-': self.solved_solution = num1 - num2
            elif sign == "/": self.solved_solution = num1 / num2
            elif sign == '^': self.solve_solution = math.pow(num1,num2)
            # remove first two numbers and insert the solved solution at the beginning of the list
            # remove both numbers and sign - the 3 in front
            for _ in range(3): str_lst.pop(0)
            # readd the self.solution to be added to future numbers
            str_lst.insert(0, self.solved_solution)        

            
    def _solve_expression(self):
        print("Solve expression")
        first_var = self._order_first()
        last_var = self._order_last()

        for var in self.organized_problem:
            if var == "+":
                self.solved_solution += first_var + last_var
            elif var == "*":
                self.solved_solution += first_var * last_var
            elif var == "-":
                self.solved_solution += first_var - last_var
            elif var == "^":
                self.solved_solution += first_var ** last_var
            elif var == "/":
                if self.x == 0 or self.y == 0:
                    print("Cant devide by zero!")
                    break
                self.solved_solution += first_var / last_var
    def _solve_equation(self):
        print("Solve equations")
    def _solve_inequality(self):
        print("Solve inequalities")
    def _order_first(self):
        for var in self.organized_problem:
            if var == self.x:
                return self.x
            elif var == self.y:
                return self.y
        return self.x
    def _order_last(self):
        for var in self.organized_problem:
            if var == self.x:
                return self.y
            elif var == self.y:
                return self.x
        return self.y

    def return_solution(self):
        return f"= {self.solved_solution}"

def main():
    root = tk.Tk()
    gui = GUI(master=root)
    gui.mainloop()


if __name__ == '__main__':
    main()
