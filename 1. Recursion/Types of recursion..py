{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "92eb44f6",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Types of recursion\n",
    "# 1.Tail recursion\n",
    "# 2.head recursion\n",
    "# 3.Tree recursion\n",
    "# 4.Indirect recursion\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f2cbb929",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 1.Tail recursion"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "68215c08",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter your number: 4\n",
      "1\n",
      "4\n",
      "9\n",
      "16\n"
     ]
    }
   ],
   "source": [
    "def cal_rec(n):\n",
    "    if n > 0:\n",
    "        cal_rec(n-1)\n",
    "        k = n**2\n",
    "        print(k)\n",
    "        \n",
    "cal_rec(int(input(\"Enter your number: \")))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f080e9d1",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Head recursion"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "7fce7315",
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
    "def cal_rec(n):\n",
    "    if n > 0:\n",
    "        k = n**2\n",
    "        print(k)\n",
    "        cal_rec(n-1)\n",
    "\n",
    "cal_rec(int(input(\"Enter your number: \")))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "196e8b5f",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Tree recursion :: calling function itself more than once"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "b44258b8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter your number:3\n",
      "1\n",
      "4\n",
      "1\n",
      "9\n",
      "1\n",
      "4\n",
      "1\n"
     ]
    }
   ],
   "source": [
    "def cal_rec(n):\n",
    "    if n > 0:\n",
    "        cal_rec(n-1)\n",
    "        k = n**2\n",
    "        print(k)\n",
    "        cal_rec(n-1)\n",
    "        \n",
    "cal_rec(int(input(\"Enter your number:\")))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a6ce8b75",
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
