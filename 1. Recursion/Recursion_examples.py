{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "714d160b",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Sum of n natural numbers\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "b9c21933",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter your number: 4\n",
      "The sum of 4 Natural numbers is: 15\n"
     ]
    }
   ],
   "source": [
    "def sum_rec(n):\n",
    "    if n == 0:\n",
    "        return 0\n",
    "    return sum_rec(n-1)+n\n",
    "n = int(input(\"Enter your number: \"))\n",
    "print(\"The sum of\",n,\"Natural numbers is:\",sum_rec(num))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5e16ff74",
   "metadata": {},
   "outputs": [],
   "source": [
    "#factorial of n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a74b956f",
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
