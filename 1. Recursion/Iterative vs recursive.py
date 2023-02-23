{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1534e3b4",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Iterative method"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "8d041129",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter your number: 4\n",
      "16\n",
      "9\n",
      "4\n",
      "1\n"
     ]
    }
   ],
   "source": [
    "def calculate_itr(n):\n",
    "    while n > 0:\n",
    "        k = n**2\n",
    "        print(k)\n",
    "        n = n-1\n",
    "calculate_itr(int(input(\"Enter your number: \")))        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "b0160969",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The number: 4\n",
      "1 16\n",
      "2 9\n",
      "3 4\n",
      "4 1\n"
     ]
    }
   ],
   "source": [
    "\n",
    "def calculate_itr(n,i):\n",
    "    \n",
    "    while n > 0 and i >= 1:\n",
    "        k = n**2\n",
    "        print(i, k)\n",
    "        n = n-1 #to terminate the code\n",
    "        i = i+1\n",
    "        \n",
    "calculate_itr(int(input(\"The number: \")),1)        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ee4a5064",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "91da2d12",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Recursive method"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "ffc16975",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter your number: 4\n",
      "16\n",
      "9\n",
      "4\n",
      "1\n"
     ]
    }
   ],
   "source": [
    "def calculate_rec(n):\n",
    "    if n > 0:\n",
    "        k = n**2\n",
    "        print(k)\n",
    "        calculate_rec(n-1)\n",
    "\n",
    "calculate_rec(int(input(\"Enter your number: \")))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "ad6b1426",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter no: 4\n",
      "enter i1\n",
      "1 16\n",
      "2 9\n",
      "3 4\n",
      "4 1\n"
     ]
    }
   ],
   "source": [
    "def calculate_rec(n,i):\n",
    "    if n > 0 and i >= 1:\n",
    "        k = n ** 2\n",
    "        print(i,k)\n",
    "        i = i+1\n",
    "        calculate_rec(n-1,i)\n",
    "        \n",
    "\n",
    "calculate_rec(int(input('Enter no: ')),int(input(\"enter i\")))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d2ed0de9",
   "metadata": {},
   "outputs": [],
   "source": []
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
