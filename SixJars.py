class SixJars:

    def __init__(self, income):
        self.income = income
        self.cutoff = income * 0.4

    def get_NEC(self): # Necessities Account
        return self.income * 0.6

    def get__FFA(self): # Financial Freedom
        return self.income * 0.2

    def get_GIVE(self):
        return self.cutoff * 0.05

    def get_EDU(self): # Education
        return self.cutoff * 0.2

    def get_PLAY(self):
        return self.cutoff * 0.15

    def get_LTSS_1(self): # Long Term Saving for Spending
        return self.cutoff * 0.20

    def get_LTSS_2(self): # Long Term Saving for Spending
        return self.cutoff * 0.20

    def __str__(self):
        str =  '[Initial]\n'
        str += 'Total income: %.02f\n' % (self.income)
        str += 'NEC: 20%%   --- %.02f x 0.2 = %.02f\n' % (self.cutoff, self.get_NEC())
        str += '\n'

        str += '[HOT]\n'
        str += 'PLAY: 15%%  --- %.02f x 0.15 = %.02f\n' % (self.cutoff, self.get_PLAY())
        str += 'EDU: 20%%   --- %.02f x 0.20 = %.02f\n' % (self.cutoff, self.get_EDU())
        str += 'GIVE: 20%%  --- %.02f x 0.05 = %.02f\n' % (self.cutoff, self.get_GIVE())
        str += '\n'

        str += '[COLD]\n'
        str += 'FFA: 20%%   --- %.02f x 0.2 = %.02f\n' % (self.cutoff, self.get__FFA())
        str += 'LTSS1: 20%% --- %.02f x 0.2 = %.02f\n' % (self.cutoff, self.get_LTSS_1())
        str += 'LTSS2: 20%% --- %.02f x 0.2 = %.02f\n' % (self.cutoff, self.get_LTSS_2())
        str += '\n'
        return str

print SixJars(3201)