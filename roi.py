class ROI():
    def __init__(self, total_income = 0, total_expenses = 0, down_payment = 0, the_cash_flow = 0, the_roi = 0, total_investment = 0):
        self.total_income = total_income
        self.total_expenses = total_expenses
        self.down_payment = down_payment
        self.the_cash_flow = the_cash_flow
        self.the_roi = the_roi
        self.total_investment = total_investment

    def navigation(self):
        buying = True
        while buying:
            response = input('Welcome to the ROI Calculator! Type start to start or quit to Quit ').lower()
            if response == "start":
                self.income()
            elif response == "quit":
                print('Thanks for using ROI calculator!')
                buying = False
            else:
                print('Invalid Input, please try again.')

    def income(self):
        income = int(input('Please enter the total income for the rental property before any deductions (monthly) '))
        self.total_income = income
        self.expenses()

    def expenses(self):
        costs = int(input('Great, now please enter the total monthly expenses for the property. '))
        self.total_expenses = costs
        self.cash_flow()
    
    def cash_flow(self):
        cashFlow = self.total_income - self.total_expenses
        self.the_cash_flow = cashFlow
        total_investment = int(input('Please enter the down-payment and other up-front costs for the property. '))
        self.total_investment = total_investment
        self.final_roi()
    
    def final_roi(self):
        self.the_cash_flow * 12
        divide_me = self.the_cash_flow / self.total_investment
        self.the_roi = divide_me * 1000
        print(f'With the information provided, your ROI on the property is {self.the_roi} percent.')
        
        
new_roi = ROI()
new_roi.navigation()
