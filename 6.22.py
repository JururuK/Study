{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "fa75f05a-233f-41ca-8f5c-81d488ea2d26",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "신성검사 님이 아덴 월드에 로그인 하였습니다.\n",
      "hp : 2000, damage : 45 입니다.\n",
      "요정 님이 아덴 월드에 로그인 하였습니다.\n",
      "hp : 1500, damage : 55 입니다.\n",
      "신성검사님이 공격하였습니다. 데미지를 왼방향으로 45입혔습니다.\n",
      "요정님이 공격하였습니다. 데미지를 오른방향으로 55입혔습니다.\n"
     ]
    }
   ],
   "source": [
    "# Lineage\n",
    "name = \"신성검사\"\n",
    "hp = 2000\n",
    "dam = 45\n",
    "\n",
    "print(\"{0} 님이 아덴 월드에 로그인 하였습니다.\".format(name))\n",
    "print(\"hp : {0}, damage : {1} 입니다.\".format(hp,dam))\n",
    "E_name = \"요정\"\n",
    "E_hp = 1500\n",
    "E_dam = 55\n",
    "\n",
    "print(\"{0} 님이 아덴 월드에 로그인 하였습니다.\".format(E_name))\n",
    "print(\"hp : {0}, damage : {1} 입니다.\".format(E_hp,E_dam))\n",
    "\n",
    "def attack(name, loc, dam) :\n",
    "    print(\"{0}님이 공격하였습니다. 데미지를 {1}방향으로 {2}입혔습니다.\"\\\n",
    "          .format(name,loc,dam))\n",
    "      \n",
    "attack(name,\"왼\",dam)\n",
    "attack(E_name,\"오른\",E_dam)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "5a4f8b97-225d-448b-aca7-b0ed9b1ca053",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Unit : \n",
    "    def __init__(self, name, hp, dam) :\n",
    "        self.name = name\n",
    "        self.hp = hp\n",
    "        self.dam = dam\n",
    "        print(\"{0} 님이 아덴 월드에 로그인 하였습니다.\".format(self.name))\n",
    "        print(\"hp : {0}, damage : {1} 입니다.\".format(self.hp,self.dam))\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "66007d0d-64be-424a-beb6-d00bb6b6cab9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "기사 님이 아덴 월드에 로그인 하였습니다.\n",
      "hp : 1000, damage : 100 입니다.\n",
      "암기 님이 아덴 월드에 로그인 하였습니다.\n",
      "hp : 800, damage : 80 입니다.\n",
      "다엘 님이 아덴 월드에 로그인 하였습니다.\n",
      "hp : 600, damage : 110 입니다.\n",
      "멈춘 상태\n"
     ]
    }
   ],
   "source": [
    "Unit_1 = Unit(\"기사\",1000,100)\n",
    "Unit_2 = Unit(\"암기\",800,80)\n",
    "Unit_3 = Unit(\"다엘\",600,110)\n",
    "Unit_1.stop = True\n",
    "\n",
    "if Unit_1.stop == True:\n",
    "    print(\"멈춘 상태\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 137,
   "id": "a14be3c9-5680-400a-af7e-850bb95e6942",
   "metadata": {},
   "outputs": [],
   "source": [
    "import random\n",
    "import numpy as np\n",
    "class AttackUnit :\n",
    "    def __init__(self, name, hp, dam) :\n",
    "        self.name = name\n",
    "        self.hp = hp\n",
    "        self.dam = dam\n",
    "    \n",
    "    def attack(self, tar) :\n",
    "        print(\"{0}님이 {1}에 {2}의 피해를 입혔습니다\"\\\n",
    "             .format(self.name, tar, self.dam))\n",
    "    \n",
    "    def damaged(self, dam) :\n",
    "        print(\"{0}님이 {1}의 피해를 받았습니다\"\\\n",
    "             .format(self.name, dam))\n",
    "        self.hp -= dam\n",
    "        print(\"{0}님의 잔여 hp는 {1}입니다.\"\\\n",
    "             .format(self.name, self.hp))\n",
    "        \n",
    "        if self.hp <= 0 :\n",
    "            print(\"{}님의 잔여 hp가 0이 되어 사망하였습니다.\"\\\n",
    "                 .format(self.name))\n",
    "    \n",
    "    def enchant(self, sword) :\n",
    "        \n",
    "        pos = np.random.choice(100)\n",
    "        print(pos)\n",
    "        if pos >= 80 :\n",
    "            self.hp += 100\n",
    "            print(\"{0}님의 {1}가 한순간 파랗게 빛납니다.\"\\\n",
    "                 .format(self.name, sword),\\\n",
    "                 \"{0}님이 기뻐하여 hp가 100 증가하였습니다 현재 hp는 {1}입니다.\"\\\n",
    "                 .format(self.name, self.hp),sep=\"\\n\")\n",
    "        else :\n",
    "            self.hp -= 100\n",
    "            print(\"{0}님의 {1}이(가) 파랗게 빛나더니 증발되어 사라집니다.\\\n",
    "            \\n{2}님이 실망하여 hp가 100 감소하였습니다 현재 hp는 {3}입니다.\"\\\n",
    "                 .format(self.name, sword, self.name, self.hp))\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 138,
   "id": "51b85a8c-c606-43f7-b059-8478b26a0d96",
   "metadata": {},
   "outputs": [],
   "source": [
    "Unit_1 = AttackUnit(\"기사\",1000,90)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 139,
   "id": "e3c6a827-8753-47ab-861f-2f65ee115194",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "21\n",
      "기사님의 마족검이(가) 파랗게 빛나더니 증발되어 사라집니다.            \n",
      "기사님이 실망하여 hp가 100 감소하였습니다 현재 hp는 900입니다.\n"
     ]
    }
   ],
   "source": [
    "Unit_1.enchant(\"마족검\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "256f40f9-9db9-478f-867f-e5875fffe055",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 152,
   "id": "ba425ab4-8bd1-47be-81b5-4d7610a507d8",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Unit :\n",
    "    def __init__(self,ID,HP) :\n",
    "        self.ID = ID\n",
    "        self.HP = HP\n",
    "\n",
    "class Attack_Unit(Unit):\n",
    "    def __init__(self,ID,HP,damage):\n",
    "        Unit.__init__(self,ID,HP) #상속 방법\n",
    "        self.damage = damage\n",
    "\n",
    "    def attack(self, tar) :\n",
    "        print(\"{0}님이 {1}에 {2}의 피해를 입혔습니다\"\\\n",
    "             .format(self.ID, tar, self.damage))\n",
    "    \n",
    "    def damaged(self, damage) :\n",
    "        print(\"{0}님이 {1}의 피해를 받았습니다\"\\\n",
    "             .format(self.ID, damage))\n",
    "        self.HP -= damage\n",
    "        print(\"{0}님의 잔여 hp는 {1}입니다.\"\\\n",
    "             .format(self.ID, self.HP))\n",
    "        \n",
    "        if self.HP <= 0 :\n",
    "            print(\"{}님의 잔여 hp가 0이 되어 사망하였습니다.\"\\\n",
    "                 .format(self.HP))\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 153,
   "id": "0e6aa83b-de0d-40b3-b5f7-665ca4aadf0b",
   "metadata": {},
   "outputs": [],
   "source": [
    "Unit_3 = Attack_Unit(\"나\",100,10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 154,
   "id": "f378bf4b-aefe-40c2-a699-63cad65ba24a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "나님이 너에 10의 피해를 입혔습니다\n"
     ]
    }
   ],
   "source": [
    "Unit_3.attack(\"너\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 155,
   "id": "c444e072-6c89-41cc-832f-e81422e91a91",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Jungle :\n",
    "    def __init__(self, dash_speed) :\n",
    "        self.dash_speed = dash_speed\n",
    "    def dash(self,ID,loc) :\n",
    "        print(\"{0}님이 {1}을 향해 {2}의 속도로 회피!!\"\\\n",
    "             .format(ID,loc,self.dash_speed))\n",
    "\n",
    "NPC_1 = Jungle(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 156,
   "id": "dc4a53fd-245e-4c54-8557-a6a593fe2145",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "경비병님이 동쪽을 향해 10의 속도로 회피!!\n"
     ]
    }
   ],
   "source": [
    "NPC_1.dash(\"경비병\",\"동쪽\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 157,
   "id": "3d84c6ad-2871-4022-9754-aefe1d2c6da9",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Jungle_Unit(Attack_Unit,Jungle) :\n",
    "    def __init__(self,ID,HP,damage,dash_speed) :\n",
    "        Attack_Unit.__init__(self,ID,HP,damage)\n",
    "        Jungle.__init__(self,dash_speed)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 158,
   "id": "2b2f97f9-2f26-4b7d-a842-68c59692aa3a",
   "metadata": {},
   "outputs": [],
   "source": [
    "Metis = Jungle_Unit(\"운영자\", 9999, 1000, 10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 164,
   "id": "29d4b2f2-8e2c-4d93-9af6-10a65afab70e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "운영자님이 오른쪽을 향해 10의 속도로 회피!!\n"
     ]
    }
   ],
   "source": [
    "Metis.dash(Metis.ID,\"오른쪽\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 163,
   "id": "e4822094-e875-421c-98e0-4ab4656e41b4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "운영자님이 왼쪽에 1000의 피해를 입혔습니다\n"
     ]
    }
   ],
   "source": [
    "Metis.attack(\"왼쪽\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 162,
   "id": "bffbfec0-04b3-4487-b1b2-809e3f0fae78",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "운영자님이 2000의 피해를 받았습니다\n",
      "운영자님의 잔여 hp는 1999입니다.\n",
      "운영자님이 2000의 피해를 받았습니다\n",
      "운영자님의 잔여 hp는 -1입니다.\n",
      "-1님의 잔여 hp가 0이 되어 사망하였습니다.\n",
      "운영자님이 2000의 피해를 받았습니다\n",
      "운영자님의 잔여 hp는 -2001입니다.\n",
      "-2001님의 잔여 hp가 0이 되어 사망하였습니다.\n"
     ]
    }
   ],
   "source": [
    "Metis.damaged(2000)\n",
    "Metis.damaged(2000)\n",
    "Metis.damaged(2000)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 162,
   "id": "3465f49f",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "운영자님이 2000의 피해를 받았습니다\n",
      "운영자님의 잔여 hp는 1999입니다.\n",
      "운영자님이 2000의 피해를 받았습니다\n",
      "운영자님의 잔여 hp는 -1입니다.\n",
      "-1님의 잔여 hp가 0이 되어 사망하였습니다.\n",
      "운영자님이 2000의 피해를 받았습니다\n",
      "운영자님의 잔여 hp는 -2001입니다.\n",
      "-2001님의 잔여 hp가 0이 되어 사망하였습니다.\n"
     ]
    }
   ],
   "source": [
    "Metis.damaged(2000)\n",
    "Metis.damaged(2000)\n",
    "Metis.damaged(2000)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 163,
   "id": "e4822094-e875-421c-98e0-4ab4656e41b4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "운영자님이 왼쪽에 1000의 피해를 입혔습니다\n"
     ]
    }
   ],
   "source": [
    "Metis.attack(\"왼쪽\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 164,
   "id": "29d4b2f2-8e2c-4d93-9af6-10a65afab70e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "운영자님이 오른쪽을 향해 10의 속도로 회피!!\n"
     ]
    }
   ],
   "source": [
    "Metis.dash(Metis.ID,\"오른쪽\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 158,
   "id": "2b2f97f9-2f26-4b7d-a842-68c59692aa3a",
   "metadata": {},
   "outputs": [],
   "source": [
    "Metis = Jungle_Unit(\"운영자\", 9999, 1000, 10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 157,
   "id": "3d84c6ad-2871-4022-9754-aefe1d2c6da9",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Jungle_Unit(Attack_Unit,Jungle) :\n",
    "    def __init__(self,ID,HP,damage,dash_speed) :\n",
    "        Attack_Unit.__init__(self,ID,HP,damage)\n",
    "        Jungle.__init__(self,dash_speed)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d1d3e5bd-6a9b-46db-9c74-7b57432a2e54",
   "metadata": {},
   "source": [
    "# ERROR"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 184,
   "id": "dfa0cc19-5f91-4182-a3ba-0cd6229a3695",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "나눗셈 계산기\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "첫 번째 값 : 10\n",
      "두 번째 값 : 0\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "====================\n",
      "0으로 나누면 야레야레\n"
     ]
    }
   ],
   "source": [
    "try :\n",
    "    print(\"나눗셈 계산기\")\n",
    "    num1 = int(input(\"첫 번째 값 :\"))\n",
    "    num2 = int(input(\"두 번째 값 :\"))\n",
    "\n",
    "    print(\"{0}/{1} = {2}\".format(num1, num2, int(num1/num2)))\n",
    "except ZeroDivisionError as zero_e:\n",
    "    print(\"=\"*20)\n",
    "    print(\"0으로 나누면 야레야레\")\n",
    "except ValueError as val_e :\n",
    "    print(\"=\"*20)\n",
    "    print(\"숫자가 아니면 야레야레\")\n",
    "except Exception as all_e :\n",
    "    print(\"===알림===\")\n",
    "    print(\"알 수 없는 에러 발생\")\n",
    "    print(\"슬랙에 올려주세요!\")\n",
    "    print(\"에러 코드\")\n",
    "    print(type(all_e)) #에러의 타입을 알려줌\n",
    "                       #type 안쓰면 에러 내용도 알려줌"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "77f6dab1-c3ab-4b74-a7d2-6474692f81f0",
   "metadata": {},
   "source": [
    "# 카카오 계산기(v0.0.2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 224,
   "id": "07169302-b918-48db-a599-0c834f620fc1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "카톡카톡카톡카톡카톡카톡카톡카톡카톡카톡카톡카\n",
      "*** You can be the CEO of the KAKAO!! ***\n",
      "톡카톡카톡카톡카톡카톡카톡카톡카톡카톡카톡카톡\n",
      "=========================================\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "지금 카카오 몇 주를 가지고 있나요? 133\n",
      "월급에서 주식에 얼마나 구매할 건가요? 19999910\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "과연~~~ 결과는!!! 5\n",
      "과연~~~ 결과는!!! 4\n",
      "과연~~~ 결과는!!! 3\n",
      "과연~~~ 결과는!!! 2\n",
      "과연~~~ 결과는!!! 1\n",
      "19999910만큼 카카오 주식을 구매시 당신은 카카오 주식을 321주 가지게 됩니다.\n",
      "CEO로 한걸음 더 나아갑니다\n",
      "===============================================\n",
      "난 한가지만 살거다!! 하시는분은 운영자에 문의주세요.\n"
     ]
    }
   ],
   "source": [
    "import time\n",
    "try :\n",
    "    print(\"카톡카톡카톡카톡카톡카톡카톡카톡카톡카톡카톡카\")\n",
    "    print(\"*** You can be the CEO of the KAKAO!! ***\")\n",
    "    print(\"톡카톡카톡카톡카톡카톡카톡카톡카톡카톡카톡카톡\")\n",
    "    print(\"=========================================\")\n",
    "    now_kakao = int(input(\"지금 카카오 몇 주를 가지고 있나요?\"))\n",
    "    \n",
    "    if now_kakao > 60000000 :\n",
    "        print(\"정말이라면 당신은 이미 대표이사 입니다. 사회에 환원하시는게 어떨까요?\")\n",
    "        raise ValueError\n",
    "\n",
    "    salary = int(input(\"월급에서 주식에 얼마나 구매할 건가요?\"))\n",
    "    for i in range(5) :\n",
    "        time.sleep(1)\n",
    "        print(\"과연~~~ 결과는!!!\",5-i)\n",
    "        \n",
    "    kakao = 159000\n",
    "    div = salary // kakao\n",
    "    new_kakao = now_kakao + ans\n",
    "\n",
    "    if salary % 10 > 0 :\n",
    "        print(\"장난하세요??? 1원 단위를 번다고요??\")\n",
    "        raise ValueError \n",
    "        \n",
    "    if ans < 1 :\n",
    "        print(\"이걸로는 더 못사겠네요..아직 {}주 있으니 다음달에는 더 사봅시다. 점점 더 멀어져간다\".format(now_kakao))\n",
    "    else : \n",
    "        print(\"{}만큼 카카오 주식을 구매시 당신은 카카오 주식을 {}주 가지게 됩니다.\\nCEO로 한걸음 더 나아갑니다\".format(salary,new_kakao))\n",
    "    \n",
    "\n",
    "except ValueError as val_e :\n",
    "    \n",
    "    print(\"X\"*40)\n",
    "    print(\"입력이 잘못되었습니다\")\n",
    "    print(type(val_e))\n",
    "    \n",
    "except Exception as all_e :\n",
    "    \n",
    "    print(\"X\"*40)\n",
    "    print(\"알 수 없는 에러가 발생하였습니다\")\n",
    "    print(\"에러 코드\",type(all_e))\n",
    "    print(\"지금 운영자에게 문의하세요!!!\")\n",
    "    print(\"X\"*16,\"에러내용\",\"X\"*16)\n",
    "    print(all_e)\n",
    "    \n",
    "finally :\n",
    "    \n",
    "    print(\"===============================================\")\n",
    "    print(\"난 한가지만 살거다!! 하시는분은 운영자에 문의주세요.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 208,
   "id": "9fe26586-df46-4fd9-929d-2b9cae03b696",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "인공지능 모델 V 0.0.1\n",
      "==============================\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "학습률을 입력하세요.(※ 4이하 값) :  3\n",
      "학습 횟수를 입력하세요.(※ 10 이하의 값) : 10\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "값이 잘못되었습니다. 다시 확인해주세요\n",
      "※type : <class 'ValueError'>\n",
      "한번 더 제대로 실행해보세요!!! 할 수 있드아~!\n"
     ]
    }
   ],
   "source": [
    "import time\n",
    "try :\n",
    "    print(\"인공지능 모델 V 0.0.1\")\n",
    "    print(\"=\"*30)\n",
    "    \n",
    "    num1 = float(input(\"학습률을 입력하세요.(※ 4이하 값) : \"))\n",
    "    num2 = int(input(\"학습 횟수를 입력하세요.(※ 10 이하의 값) :\"))\n",
    "    \n",
    "    if num1 >= 4 or num2 >= 10 :\n",
    "        raise ValueError\n",
    "    print(\"학습 알고리즘을 실행하겠습니다.\")\n",
    "    \n",
    "    for i in range(num2) :\n",
    "        time.sleep(1)\n",
    "        print(\"Epoch - {0} lr - {1}\".format(i,num1))\n",
    "        \n",
    "    print(\"학습이 완료되었습니다.\")\n",
    "\n",
    "except ValueError as val_e:\n",
    "    print(\"값이 잘못되었습니다. 다시 확인해주세요\")\n",
    "    print(\"※type :\",type(val_e))\n",
    "\n",
    "finally :\n",
    "    print(\"한번 더 제대로 실행해보세요!!! 할 수 있드아~!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 223,
   "id": "60f3b2c2-b548-42f8-8653-b9f43025903f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 223,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "5//2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "960e23f2-0be8-43cf-82cd-ccd5d5f8ea34",
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
