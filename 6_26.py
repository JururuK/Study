{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 242,
   "id": "beb709e8-7f71-4f69-9fcb-b1181b68a1c1",
   "metadata": {},
   "outputs": [],
   "source": [
    "with open('myself.csv') as csvfile :\n",
    "    myself = csv.reader(csvfile)\n",
    "    rows = []\n",
    "    for row in myself :\n",
    "        rows.append(row)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 243,
   "id": "077e9b05-d355-4e1d-912b-d40254e38c65",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_myself = pd.read_csv('myself.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 244,
   "id": "5834f01b-49c4-4693-980d-68ceefedcf0e",
   "metadata": {},
   "outputs": [],
   "source": [
    "news_original = \"Junhyeong's major is English education.His career contains as a teacher. His height is 175.\"\n",
    "news_split = news_original.split('.')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 245,
   "id": "72b1c8c3-2954-4bb5-9fdc-85de54ccaf0e",
   "metadata": {},
   "outputs": [],
   "source": [
    "news_split0 = news_split[0].split(' ')\n",
    "news_split1 = news_split[1].split(' ')\n",
    "news_split2 = news_split[2].split(' ')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 246,
   "id": "1830b774-defc-4019-8fa4-31cd2759650d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "판단 보류\n",
      "판단 보류\n",
      "판단 보류\n",
      "major의 내용은 English이고, 일치합니다.\n",
      "판단 보류\n"
     ]
    }
   ],
   "source": [
    "true_0 = 0\n",
    "total = len(news_split)-1\n",
    "\n",
    "for i in range(len(news_split0)) :\n",
    "    if news_split0[i] in rows[0] :\n",
    "        for j in range(len(news_split0)) :\n",
    "            if news_split0[j] in list(df_myself[news_split0[i]]) :\n",
    "                true_topic = news_split0[i]\n",
    "                true_answer = news_split0[j]\n",
    "                print(\"{0}의 내용은 {1}이고, 일치합니다.\".format(true_topic, true_answer))\n",
    "                true_0 += 1\n",
    "            elif news_split0[j] not in list(df_myself[news_split0[i]]) :\n",
    "                print('판단 보류')\n",
    "\n",
    "if true_0 < 1 :\n",
    "    result_0 = \"해당 문장에는 사실을 포함한 내용이 없습니다\"\n",
    "else :\n",
    "    result_0 = \"해당 문장에는 {}내용에 대한 사실을 포함합니다.\".format(true_topic)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 247,
   "id": "200759a7-48f1-46f7-963e-dba7e41b3721",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "판단 보류\n",
      "판단 보류\n",
      "판단 보류\n",
      "판단 보류\n",
      "판단 보류\n",
      "career의 내용은 teacher이고, 일치합니다.\n"
     ]
    }
   ],
   "source": [
    "true_1 = 0\n",
    "for i in range(len(news_split1)) :\n",
    "    if news_split1[i] in rows[0] :\n",
    "        for j in range(len(news_split1)) :\n",
    "            if news_split1[j] in list(df_myself[news_split1[i]]) :\n",
    "                true_topic = news_split1[i]\n",
    "                true_answer = news_split1[j]\n",
    "                print(\"{0}의 내용은 {1}이고, 일치합니다.\".format(true_topic, true_answer))\n",
    "                true_1 += 1\n",
    "            elif news_split1[j] not in list(df_myself[news_split1[i]]) :\n",
    "                print('판단 보류')\n",
    "\n",
    "if true_1 < 1 :\n",
    "    result_1 = \"해당 문장에는 사실을 포함한 내용이 없습니다\"\n",
    "else :\n",
    "    result_1 = \"해당 문장에는 {}내용에 대한 사실을 포함합니다.\".format(true_topic)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 248,
   "id": "8a74d621-bc49-4151-80a3-ca0bfafcdfe7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "판단 보류\n",
      "판단 보류\n",
      "판단 보류\n",
      "판단 보류\n",
      "판단 보류\n"
     ]
    }
   ],
   "source": [
    "true_2 = 0\n",
    "for i in range(len(news_split2)) :\n",
    "    if news_split2[i] in rows[0] :\n",
    "        for j in range(len(news_split2)) :\n",
    "            if news_split2[j] in list(df_myself[news_split2[i]]) :\n",
    "                true_topic = news_split2[i]\n",
    "                true_answer = news_split2[j]\n",
    "                print(\"{0}의 내용은 {1}이고, 일치합니다.\".format(true_topic, true_answer))\n",
    "                true_2 += 1\n",
    "            elif news_split2[j] not in list(df_myself[news_split2[i]]) :\n",
    "                print('판단 보류')\n",
    "accuracy = (true / total) * 100\n",
    "accuracy = round(accuracy)\n",
    "if true_2 < 1 :\n",
    "    result_2 = \"해당 문장에는 사실을 포함한 내용이 없습니다.\"\n",
    "else :\n",
    "    result_2 = \"해당 문장에는 {}내용에 대한 사실을 포함합니다.\".format(true_topic)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 249,
   "id": "b7606375-f120-40f1-9e39-f78bc8839653",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "해당 문장에는 major내용에 대한 사실을 포함합니다.\n",
      "해당 문장에는 career내용에 대한 사실을 포함합니다.\n",
      "해당 문장에는 사실을 포함한 내용이 없습니다\n",
      "해당 뉴스는 67% 만큼 사실을 포함합니다\n"
     ]
    }
   ],
   "source": [
    "def total_accuracy(x) :\n",
    "    print(result_0)\n",
    "    print(result_1)\n",
    "    print(result_2)\n",
    "    print(\"해당 뉴스는 {}% 만큼 사실을 포함합니다.\".format(accuracy))\n",
    "    \n",
    "total_accuracy(news_original)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "965b3556-0e52-4459-a2df-aa01a72eadc2",
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
