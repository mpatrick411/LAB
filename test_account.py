from account import *


class Test:
    def setup_method(self):
        self.a1 = Account('John')

    def teardown_method(self):
        del self.a1

    def test_init(self):
        assert self.a1.get_name() == 'John'
        pass

    def test_deposit(self):
        assert self.a1.deposit(-10) == False
        assert self.a1.deposit(0) == False
        assert self.a1.deposit(10) == True
        pass

    def test_withdraw(self):
        self.a1.deposit(5)
        assert self.a1.withdraw(-10) == False
        assert self.a1.withdraw(0) == False
        assert self.a1.withdraw(10) == False
        assert self.a1.withdraw(1) == True
        pass



