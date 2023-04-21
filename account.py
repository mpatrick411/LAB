class Account:
    def __init__(self, name: str) -> None:
        """
        Initialize a new Account object with a given name and zero balance.

        Args:
            name (str): The name of the account holder.
        """
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> bool:
        """
        Deposit the given amount into the account balance.

        Args:
            amount (float): The amount to deposit.

        Returns:
            bool: True if the deposit is successful, False otherwise.
        """
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount: float) -> bool:
        """
        Withdraw the given amount from the account balance.

        Args:
            amount (float): The amount to withdraw.

        Returns:
            bool: True if the withdrawal is successful, False otherwise.
        """
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def get_balance(self) -> float:
        """
        Get the current balance of the account.

        Returns:
            float: The current balance of the account.
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        Get the name of the account holder.

        Returns:
            str: The name of the account holder.
        """
        return self.__account_name