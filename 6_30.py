{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "783251e0-f9e4-4bf7-b22b-00d90ac2f53f",
   "metadata": {},
   "outputs": [],
   "source": [
    "N = int(input())\n",
    "\n",
    "for i in range(N):\n",
    "    a,b = map(int,input().split())\n",
    "    print(\"Case #{0}: {1}\".format(i+1,a+b))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "91756caf-3ea1-4553-9375-82c7b8231d94",
   "metadata": {},
   "outputs": [],
   "source": [
    "def Answer() :\n",
    "    N = int(input(\"N으로 나눌 때 나머지와 몫이 같은 수의 합 : \"))\n",
    "    N_sum = int((1/2)*N*(N**2-1))\n",
    "    return(N_sum)\n",
    "\n",
    "Answer()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "09db74e4-f8ce-431e-8d9e-14fc07d477f8",
   "metadata": {},
   "outputs": [],
   "source": [
    "def get_same_q_and_r_sum(n):\n",
    "    res = 0\n",
    "    for i in range(1,n):\n",
    "        res += i*(n+1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "77e9442c-a0a0-4bb0-a6b9-12721199e24c",
   "metadata": {},
   "outputs": [],
   "source": [
    "N = int(input())\n",
    "\n",
    "for i in range(N):\n",
    "    a,b = map(int,input().split())\n",
    "    print(\"Case #{0}: {1} + {2} = {3}\".format(i+1,a,b,a+b))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0f4195a0-583b-4a15-89da-69038712891b",
   "metadata": {},
   "outputs": [],
   "source": [
    "N = int(input())\n",
    "for i in range(N):\n",
    "    print(\" \"*(N-i-1)+\"*\"*(i+1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5c1df112-3f7f-4fd9-b986-1bcdf1c6f491",
   "metadata": {},
   "outputs": [],
   "source": [
    "N,X = map(int,input().split())\n",
    "\n",
    "N_list = list(map(int,input().split()))\n",
    "\n",
    "for i in range(N):\n",
    "    if X > N_list[i] :\n",
    "        print(N_list[i],end=' ')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6d1ceb85-5cf4-42f7-8496-f9e1c285b0b7",
   "metadata": {},
   "outputs": [],
   "source": [
    "while True:\n",
    "    a,b = map(int,input().split())\n",
    "    if a > 0 or b > 0 :\n",
    "        print(a+b)\n",
    "    elif a == 0 and b == 0:\n",
    "        break\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "20f94437-7edb-44fd-94ce-bae6c575f06c",
   "metadata": {},
   "outputs": [],
   "source": [
    "while True :\n",
    "    try:\n",
    "        a,b = map(int,input().split())\n",
    "        print(a+b)\n",
    "    except:\n",
    "        break"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8bda2c99-83e8-4f36-9363-995c9e54c904",
   "metadata": {},
   "outputs": [],
   "source": [
    "a = int(input()) # 더하기 사이클\n",
    "x = []\n",
    "x.append(a)\n",
    "i = 0\n",
    "\n",
    "while True :\n",
    "    x_1 = x[i] // 10\n",
    "    x_0 = x[i] % 10\n",
    "    res = ((x_0)*10)+((x_1+x_0)%10)\n",
    "    if res != x[0] :        \n",
    "        i += 1\n",
    "        x.append(res)\n",
    "    else :\n",
    "        break\n",
    "        \n",
    "print(i+1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2a215df3-f0e4-4434-9a14-09639bd5c8e0",
   "metadata": {},
   "outputs": [],
   "source": [
    "import random as rd\n",
    "lotto = []\n",
    "number = list(range(1,46))\n",
    "\n",
    "for i in range(100) :\n",
    "    num = rd.choice(number)\n",
    "    if num in lotto :\n",
    "        num = rd.choice(number)\n",
    "    else :\n",
    "        lotto.append(num)\n",
    "\n",
    "    if len(lotto) == 6 :\n",
    "        break\n",
    "\n",
    "lotto.sort()\n",
    "print(lotto)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6d76aa9c-bb99-4655-ab36-e701682968d0",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "47d6dd5e-28c0-478a-a857-bc0eb79cdc5e",
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
   "version": "3.8.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
