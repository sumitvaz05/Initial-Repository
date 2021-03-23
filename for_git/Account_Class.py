{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "pretty-window",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Account:\n",
    "    def __init__(self, owner, balance):\n",
    "        self.owner=owner\n",
    "        self.balance=balance\n",
    "        print(f'Name: {owner}\\nBalance: {balance}')\n",
    "    \n",
    "    def deposit(self,amount):\n",
    "        self.balance+=amount\n",
    "        print(\"Deposit accepted\")\n",
    "        print(f'Current balance:{self.balance}')\n",
    "        \n",
    "    def withdraw(self,amount):\n",
    "        if amount<=self.balance:\n",
    "            self.balance-=amount\n",
    "            print('Withdrawal accepted')\n",
    "            print(f'Current balance:{self.balance}')\n",
    "            \n",
    "        else:\n",
    "            print('Error: Overdraft on account')"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
