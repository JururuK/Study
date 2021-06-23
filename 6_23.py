{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "f0085bf2-4bf4-4745-8110-28fb71d462e9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'C:\\\\Users\\\\JH\\\\GJ_AI'"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import os\n",
    "os.getcwd()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "0d7ec19f-8486-4cfc-bc75-fee872db20f7",
   "metadata": {},
   "outputs": [],
   "source": [
    "import csv\n",
    "\n",
    "with open('dataset/copy of gapminder.tsv') as csvfile:\n",
    "    csvreader = csv.reader(csvfile)\n",
    "    rows = []\n",
    "    for row in csvreader:\n",
    "        rows.append(row)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "6cf67050-9721-4023-af88-16d8a905e532",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[['country\\tcontinent\\tyear\\tlifeExp\\tpop\\tgdpPercap'], ['Afghanistan\\tAsia\\t1952\\t28.801\\t8425333\\t779.4453145'], ['Afghanistan\\tAsia\\t1957\\t30.332\\t9240934\\t820.8530296'], ['Afghanistan\\tAsia\\t1962\\t31.997\\t10267083\\t853.10071'], ['Afghanistan\\tAsia\\t1967\\t34.02\\t11537966\\t836.1971382'], ['Afghanistan\\tAsia\\t1972\\t36.088\\t13079460\\t739.9811058'], ['Afghanistan\\tAsia\\t1977\\t38.438\\t14880372\\t786.11336'], ['Afghanistan\\tAsia\\t1982\\t39.854\\t12881816\\t978.0114388'], ['Afghanistan\\tAsia\\t1987\\t40.822\\t13867957\\t852.3959448'], ['Afghanistan\\tAsia\\t1992\\t41.674\\t16317921\\t649.3413952']]\n"
     ]
    }
   ],
   "source": [
    "print(rows[0:10])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "1795742c-440c-4867-b7b8-087c979b1286",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_csv('dataset/copy of gapminder.tsv',sep='\\t')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "0312d8df-a082-446b-9375-81a363826eaa",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>country</th>\n",
       "      <th>continent</th>\n",
       "      <th>year</th>\n",
       "      <th>lifeExp</th>\n",
       "      <th>pop</th>\n",
       "      <th>gdpPercap</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Afghanistan</td>\n",
       "      <td>Asia</td>\n",
       "      <td>1952</td>\n",
       "      <td>28.801</td>\n",
       "      <td>8425333</td>\n",
       "      <td>779.445314</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Afghanistan</td>\n",
       "      <td>Asia</td>\n",
       "      <td>1957</td>\n",
       "      <td>30.332</td>\n",
       "      <td>9240934</td>\n",
       "      <td>820.853030</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Afghanistan</td>\n",
       "      <td>Asia</td>\n",
       "      <td>1962</td>\n",
       "      <td>31.997</td>\n",
       "      <td>10267083</td>\n",
       "      <td>853.100710</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Afghanistan</td>\n",
       "      <td>Asia</td>\n",
       "      <td>1967</td>\n",
       "      <td>34.020</td>\n",
       "      <td>11537966</td>\n",
       "      <td>836.197138</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Afghanistan</td>\n",
       "      <td>Asia</td>\n",
       "      <td>1972</td>\n",
       "      <td>36.088</td>\n",
       "      <td>13079460</td>\n",
       "      <td>739.981106</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1699</th>\n",
       "      <td>Zimbabwe</td>\n",
       "      <td>Africa</td>\n",
       "      <td>1987</td>\n",
       "      <td>62.351</td>\n",
       "      <td>9216418</td>\n",
       "      <td>706.157306</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1700</th>\n",
       "      <td>Zimbabwe</td>\n",
       "      <td>Africa</td>\n",
       "      <td>1992</td>\n",
       "      <td>60.377</td>\n",
       "      <td>10704340</td>\n",
       "      <td>693.420786</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1701</th>\n",
       "      <td>Zimbabwe</td>\n",
       "      <td>Africa</td>\n",
       "      <td>1997</td>\n",
       "      <td>46.809</td>\n",
       "      <td>11404948</td>\n",
       "      <td>792.449960</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1702</th>\n",
       "      <td>Zimbabwe</td>\n",
       "      <td>Africa</td>\n",
       "      <td>2002</td>\n",
       "      <td>39.989</td>\n",
       "      <td>11926563</td>\n",
       "      <td>672.038623</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1703</th>\n",
       "      <td>Zimbabwe</td>\n",
       "      <td>Africa</td>\n",
       "      <td>2007</td>\n",
       "      <td>43.487</td>\n",
       "      <td>12311143</td>\n",
       "      <td>469.709298</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>1704 rows × 6 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "          country continent  year  lifeExp       pop   gdpPercap\n",
       "0     Afghanistan      Asia  1952   28.801   8425333  779.445314\n",
       "1     Afghanistan      Asia  1957   30.332   9240934  820.853030\n",
       "2     Afghanistan      Asia  1962   31.997  10267083  853.100710\n",
       "3     Afghanistan      Asia  1967   34.020  11537966  836.197138\n",
       "4     Afghanistan      Asia  1972   36.088  13079460  739.981106\n",
       "...           ...       ...   ...      ...       ...         ...\n",
       "1699     Zimbabwe    Africa  1987   62.351   9216418  706.157306\n",
       "1700     Zimbabwe    Africa  1992   60.377  10704340  693.420786\n",
       "1701     Zimbabwe    Africa  1997   46.809  11404948  792.449960\n",
       "1702     Zimbabwe    Africa  2002   39.989  11926563  672.038623\n",
       "1703     Zimbabwe    Africa  2007   43.487  12311143  469.709298\n",
       "\n",
       "[1704 rows x 6 columns]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "display(df)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f7ec9e34-dc50-4054-b59d-bda39ce2eb9e",
   "metadata": {},
   "source": [
    "## 1.2.1 Series & Dataframe"
   ]
  },
  {
   "attachments": {
    "9d29a26b-8f96-4145-bf30-d99c6e472a0e.png": {
     "image/png": "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7GjadWw2Scsmxidp2SNsdyb4urizD52h7GOL8FVPDkbQ8TYwcRGPVVlcYjZJyybGJ2nZI2yHJvhM8FmEr40+8PTTT7uLL764MozDBh8eG0HHE3QniYvRo0e7yy+/3P3444/u22+/dUcffbR7++23Mz/95ptv3EUXXeR22GEHh4+EfpPKcSfZJBVMp6UefZVPbrnlFnfrrbcm6+fTYhN9rwm+Nnb2Gui++H3SpEk1nUCrn6HTInx0nq+++qrvQAWrsWPHussuu6w0Ivnhhx/c888/777//vuoMvsqQQu+Ze47SVxcd9117sADD/SC77vvvnMnn3yye+uttzKfOeigg9z666/v9thjD/fpp59m54vwXnnlld10002XfRZaaKGo+4ryiz3fSTaJfeaU0/VVPjn99NPdmWee2dDPBXvazDLLLJP5+9JLL+3OPvtsx3lJk+LeBJ8JvkIHJQJAR9Aux+00wUfHSKf3/vvvtw2zRragbOoQ00mTV18l6EY4tON6J4kLLfjysNpiiy3ce++9F+3H/fv3dx999FF0+rwye3Ouk2zSm+dP7Z6+yie9EXw77rij++qrr7zPjx8/3m288cbuyCOP9IOo1Owi9THBZ4KvkKRN8MVP99GgTPA1h5eQUF/Zd5K4qCf4iFJsttlmTQk4E3yd7fuxbbRbBR/4vPLKK27uued2n3/+eWGfGotju9KZ4EtY8NF4TjrpJEe4eI455nD77rtvNl342muvuX322cfNM8882TXOiaMMGTLE3Xjjjdkx55mmue222/y5J554wo9IHnroIdevX78sD8qcPHmy22qrrbJwNREjOghGM6S977773NZbb+2/77333u6CCy6oKQfHp6wpU6bUnJe6yb6KCB8jMeq24IILuvnnn99deeWVWR2feeYZt9tuu7lZZ53VXz/ssMOyTk8wueuuuxznSbPaaqu5u+++O8NTT2kxxcVzgjflyTMfcMAB7tlnn3XYZ6655nKrrLKKu/fee7PrTMWCNecpY9CgQVnEUPB/4IEHvO0pb91113WPP/54VpauwzrrrJPlK+WH+5QJ+vrrr/dTinp6mgjmtttu66esf/rpJ4f/brLJJm7GGWd0m2++uXvuuecc53lOptOJVIHjwgsv7M4555xsykX8H+wXXXRRv54txCY87lTBJ341btw4x5pT7UPwAL7/xRdfuLPO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xOFUVSoTfFUhb+Wa4EvAB4yg441g4iIeq7JSmk3KQjquHOOTOJyqSmWCryrkrVwTfAn4gBF0vBFMXMRjVVZKs0lZSMeVY3wSh1NVqUzwVYW8lWuCLwEfMIKON4KJi3isykppNikL6bhyjE/icKoqlQm+qpC3ck3wJeADRtDxRjBxEY9VWSnNJmUhHVeO8UkcTlWlSlbw8T92P/vsMzdx4kT3zTffuJ9++sk1+o8bZf2u27/+9S9fl//+97+5dnv//ffd2muv7bbddlv3z3/+MzeNPnnHHXe4oUOH6lMt/T5mzBi31157ub///e8tzXdaMyvLXtNaz3bf/7e//c37UzPlnHzyye7+++9v5pbctCkTNP/4O2/j/JQpUzxmtEW9/f777z3+P/e///1vnyTvGjzz888/6ywKv3eSuICX4FOen/+3mcdl4Mz1X375xQmGeeD84x//8HlhE/wpzAv/hr+5nmdT8qYMysq7P69MOZeyTfA3nhn/CvEDI3AXfP/zn//II/XYgwlpw03aQV7+gqnYJO/eH3/80fGp1y9QT9Jg45itHXxC/agDPpRXD8EBf87rb7kfHLg/5IvwmeqVRd7YS380duSNLbj+66+/9mgHlKXrEtYVrLlP7g99gmO5XtRmdRpsEW5JCr7x48e7DTfc0M0555xuxhlndEsttZR78MEHPanUE31lCYhbbrnFLbDAAl6MhoDimFtssYW755573IQJE3KNHt7TbsEHZh999JELHSisBw543333NWwU4X29PS7LXr2tX1n3nXnmmW6FFVZwdIyx26RJk9z3338fm7wwXTsIurCwyAsQ3/XXX++23nrrHnc8/vjjbtlll/W8MPfcc7s999wz60zx7+OPP95NN910NZ9PPvnE53POOefUnJd0O+ywQ5TPpywuegBV58Rf//pXN3DgQAd+M8wwg1tsscXcFVdckeHIrY8++qjHGYzmm28+d+qpp+bmiA/269cv4+ollljC3X333Vnar776yq288spu9tlndzPPPLP382effTa7jjA58MAD3fzzz+9tQ12GDx+eXW/0JUWb4L/33nuvW2aZZbyfzjvvvO7oo4/OxAh+esEFF7hFFlnE409fcthhhznsEm7kRX9y+OGH11wCw+WXXz7L/6yzzsr4HR4/7rjjvN3oP8Um5MVGv0TdZpllFjfrrLO6tdZayxGk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8QiauIjHqqyUZpOykI4rx/gkDqeqUiUv+L744gu39dZbuyeeeMLV+y8bXCtLQHz00Udu3333dQi1cPvPf/7jTjrpJDf77LO7bbfd1iH+Gm133HGHGzp0aKNkvb4+ZswYN2jQIPe3v/2t13m048ay7NWOurcyz0ceecTts88+TWV58sknuzvvvLOpe/ISp0rQ//rXv3Kfj/O3336722ijjdz+++/v+FdO4cY/DL/qqqvcGmus4Y466ij3888/+yTXXXedP8d5/RkyZIgj30ZbN4mLF154we21114epxEjRhTyGJxywAEHuNGjRxfCR5rLLrvMbbDBBu6UU07pwUMMRo855hhf1kUXXeQYoMZuVdvkH//4h7v11lsLq8u/trrkkksc/YLebrrpphofxB8///zzLEk9/IcNG9bjXu4/9NBDs/u//fZbd+SRR/p2cuWVV/Yon4QJ12h+AAAgAElEQVT8n9WDDz7YbbjhhrltjX6O6+Q9atSoqIBBq/mEgMmzzz7rBgwY4HbbbTf3yiuvZM/IF/A9/vjj3dprr+2fl+cON7C/+eab3RZbbOEGDx7sAzFhGn1M+htvvDGXE+677z6vR3beeWf3wQcfZLfdf//9uTbZY489HHyktzyfoUz+TeCee+7pbXb55Zf3aCfojXPPPde3ozPOOKPH9Zh2lLzgozFNN910DqBTEHx0DDSklVZayf/TeW1IviNQ11tvvaYidu0WfGEdi45prBByjEgtyqOZ8yb4/kCLDnP99df3vtMMfq1I22qCntY6IQ6eeuopT86rrbZaTXaQP+Jsyy23dGeddZbv4EhDm5Ptxx9/9Pfuvvvu7uyzz3bHHnusu+eee/zl5557zp/jvHx23HFHnybskCU/va9aXOi6tPM7NjjssMMcncqZZ57p8WaAm7eBKfwMh+VtdHYHHnig23XXXX1eAwcO9B0WXM5GpHqHHXZwJ5xwgrfp9ttv77DJv//977zsepyryia//vqru+2223w/gDAONwYZ11xzjVtmmWXc4Ycf3uN5ECngIn7IHizYGuHPAF7fx/eNN97YnX766f5+hBp9EIMd7LfNNts42oMWHnfffbej7QjutBPKZaMtPPjgg2711Vf3bYP8eQbEVaOt1XwChghOfPHEE0/0dX766ad9NRBOCFLOwweHHHKIW3PNNd2XX36ZVfOHH35wm2++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ScH3pz/9qX8wjQeePwY+BcGno7ztbW/rXv/613fDTqTROKBXvepVfcdsDWHZ500LvmVlt9cY3Pvf//491b29f6+fI/jOzwbf+c53dm984xu7U6dOzTrvXlnuN/06HfR+69Dex+ma/Dz72c/uLr/88jkenOWVV17ZffzjH+9FgwHLxIpokwf71f/aPwPZ5z73uf465/+Wt7yl4/SJju9973v9gLYq98MUFy2jg34mAm677bY+Qmxg/9KXvtQ97WlP6x588MEZ73vuuacf1H74wx/2rAjr3/72t7PrVYd//vOfvb/7zGc+04sEKwkvetGL+nukOXPmTPfKV76y+9a3vtWfc3zqU5/a8fGu//vf/+6vG0jx/cY3vtG9/OUv7x566KEdZVWZ7fGw2uSBBx7oPvCBD3QXXXRRL7zaOrHDT33qU71wNcH46le/2r32ta+dPRNBSETdeOON/dj24x//uHvKU57S/eY3v+mfmZ22Nuwzm//BD37Qi5k///nP3dOf/vTORFH7ER76gfNtPXy2ykQMDccqfUK7EEz6ggnAf/7zn/7+P/zhD30baXv1/+hHP9q99a1v3SFuhmX5vk5/oj5DDp6D8HWN+MXZBMMz4PiCF7xgNmFQlze/+c3dpz/96f45+At2ft999+3gpO6EuTbBlP0L6vz85z/v0/I9gibS8BcENn4m3sWBTVx//fU9uze84Q2z8+31RTazWz/yrO9+97t7X9cyUS/5r9qPJin4GJzZEfW6m8hrrz8eAoJhqRsH+I53vGNHoxKpbUShGnvZcSqCj5PliBjXsvqu69rj0V7rquum8vnLX/7SO9Sf/exn3XXXXbdSRHiddVmng15HvThtEY7777+/Ew1q8xRxes973jMXqf7Rj37Uz3zHoteEjT5a0Qnf2xmxSJfZ/3AwbMtsP3O07fcL5TORbaA00Hkmg4hBtQa7Zc95991395NfdlTpiJNbbrml/85PmhzXNb7FCshdd93Vn/vd737Xvetd75pFUkQyDLqESN2z7HhYbfL5z3++f0Yi+IMf/OCudX3FK14xi/L9+te/7q644oqZn2WHX//613tRN/asxPHb3/72md0TxSYyNdi7h6gh3Nv7rUDx5x/+8IfnbPxvf/tbHxX761//Ope+7iXejx07NmsTbSYSaGyrNIuOm/QnxvoPfehDM45jdWBLfIhrRBsf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"
    }
   },
   "cell_type": "markdown",
   "id": "f50df19d-6f77-47ad-98c2-79e69bc42fe5",
   "metadata": {},
   "source": [
    "![image.png](attachment:9d29a26b-8f96-4145-bf30-d99c6e472a0e.png)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "8be5e1c9-d33f-4134-9630-d5cc43f5bf9a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>country</th>\n",
       "      <th>continent</th>\n",
       "      <th>year</th>\n",
       "      <th>lifeExp</th>\n",
       "      <th>pop</th>\n",
       "      <th>gdpPercap</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Afghanistan</td>\n",
       "      <td>Asia</td>\n",
       "      <td>1952</td>\n",
       "      <td>28.801</td>\n",
       "      <td>8425333</td>\n",
       "      <td>779.445314</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Afghanistan</td>\n",
       "      <td>Asia</td>\n",
       "      <td>1957</td>\n",
       "      <td>30.332</td>\n",
       "      <td>9240934</td>\n",
       "      <td>820.853030</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Afghanistan</td>\n",
       "      <td>Asia</td>\n",
       "      <td>1962</td>\n",
       "      <td>31.997</td>\n",
       "      <td>10267083</td>\n",
       "      <td>853.100710</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Afghanistan</td>\n",
       "      <td>Asia</td>\n",
       "      <td>1967</td>\n",
       "      <td>34.020</td>\n",
       "      <td>11537966</td>\n",
       "      <td>836.197138</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Afghanistan</td>\n",
       "      <td>Asia</td>\n",
       "      <td>1972</td>\n",
       "      <td>36.088</td>\n",
       "      <td>13079460</td>\n",
       "      <td>739.981106</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Afghanistan</td>\n",
       "      <td>Asia</td>\n",
       "      <td>1977</td>\n",
       "      <td>38.438</td>\n",
       "      <td>14880372</td>\n",
       "      <td>786.113360</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Afghanistan</td>\n",
       "      <td>Asia</td>\n",
       "      <td>1982</td>\n",
       "      <td>39.854</td>\n",
       "      <td>12881816</td>\n",
       "      <td>978.011439</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       country continent  year  lifeExp       pop   gdpPercap\n",
       "0  Afghanistan      Asia  1952   28.801   8425333  779.445314\n",
       "1  Afghanistan      Asia  1957   30.332   9240934  820.853030\n",
       "2  Afghanistan      Asia  1962   31.997  10267083  853.100710\n",
       "3  Afghanistan      Asia  1967   34.020  11537966  836.197138\n",
       "4  Afghanistan      Asia  1972   36.088  13079460  739.981106\n",
       "5  Afghanistan      Asia  1977   38.438  14880372  786.113360\n",
       "6  Afghanistan      Asia  1982   39.854  12881816  978.011439"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head(7)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "a0d93650-ab73-4222-ae88-b4b9a97a6aa0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>country</th>\n",
       "      <th>continent</th>\n",
       "      <th>year</th>\n",
       "      <th>lifeExp</th>\n",
       "      <th>pop</th>\n",
       "      <th>gdpPercap</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Afghanistan</td>\n",
       "      <td>Asia</td>\n",
       "      <td>1952</td>\n",
       "      <td>28.801</td>\n",
       "      <td>8425333</td>\n",
       "      <td>779.445314</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Afghanistan</td>\n",
       "      <td>Asia</td>\n",
       "      <td>1957</td>\n",
       "      <td>30.332</td>\n",
       "      <td>9240934</td>\n",
       "      <td>820.853030</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Afghanistan</td>\n",
       "      <td>Asia</td>\n",
       "      <td>1962</td>\n",
       "      <td>31.997</td>\n",
       "      <td>10267083</td>\n",
       "      <td>853.100710</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Afghanistan</td>\n",
       "      <td>Asia</td>\n",
       "      <td>1967</td>\n",
       "      <td>34.020</td>\n",
       "      <td>11537966</td>\n",
       "      <td>836.197138</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Afghanistan</td>\n",
       "      <td>Asia</td>\n",
       "      <td>1972</td>\n",
       "      <td>36.088</td>\n",
       "      <td>13079460</td>\n",
       "      <td>739.981106</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Afghanistan</td>\n",
       "      <td>Asia</td>\n",
       "      <td>1977</td>\n",
       "      <td>38.438</td>\n",
       "      <td>14880372</td>\n",
       "      <td>786.113360</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Afghanistan</td>\n",
       "      <td>Asia</td>\n",
       "      <td>1982</td>\n",
       "      <td>39.854</td>\n",
       "      <td>12881816</td>\n",
       "      <td>978.011439</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>Afghanistan</td>\n",
       "      <td>Asia</td>\n",
       "      <td>1987</td>\n",
       "      <td>40.822</td>\n",
       "      <td>13867957</td>\n",
       "      <td>852.395945</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       country continent  year  lifeExp       pop   gdpPercap\n",
       "0  Afghanistan      Asia  1952   28.801   8425333  779.445314\n",
       "1  Afghanistan      Asia  1957   30.332   9240934  820.853030\n",
       "2  Afghanistan      Asia  1962   31.997  10267083  853.100710\n",
       "3  Afghanistan      Asia  1967   34.020  11537966  836.197138\n",
       "4  Afghanistan      Asia  1972   36.088  13079460  739.981106\n",
       "5  Afghanistan      Asia  1977   38.438  14880372  786.113360\n",
       "6  Afghanistan      Asia  1982   39.854  12881816  978.011439\n",
       "7  Afghanistan      Asia  1987   40.822  13867957  852.395945"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[:8]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "f078ca64-89f5-4358-980f-11a42c86b5d3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "pandas.core.frame.DataFrame"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "75312aad-3b4f-4082-af6e-55bccfd96bc2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(1704, 6)"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "df796191-c8f9-483a-9f27-c3ed6354b0c3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "tuple"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_shape = df.shape\n",
    "type(df_shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "c235c39f-bb59-4e67-b8fe-f713bed67202",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "6"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_shape[1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "1a887099-68ea-4d7e-93ef-8bd0130a3fc5",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "\n",
    "input_cnt = df_shape[1] # = 6\n",
    "output_cnt = 1\n",
    "\n",
    "theta_1 = np.random.normal(0, 1, [input_cnt, output_cnt])\n",
    "theta_0 = np.random.normal(0, 1, [output_cnt])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "b17c3240-7b12-461e-8bce-2b903000d8e7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['country', 'continent', 'year', 'lifeExp', 'pop', 'gdpPercap'], dtype='object')"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "c940320c-0d1d-4fa6-8ae7-134cb53fdd9c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "country       object\n",
       "continent     object\n",
       "year           int64\n",
       "lifeExp      float64\n",
       "pop            int64\n",
       "gdpPercap    float64\n",
       "dtype: object"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "6cedf461-c6b7-48d5-a3b0-1271497f896c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 1704 entries, 0 to 1703\n",
      "Data columns (total 6 columns):\n",
      " #   Column     Non-Null Count  Dtype  \n",
      "---  ------     --------------  -----  \n",
      " 0   country    1704 non-null   object \n",
      " 1   continent  1704 non-null   object \n",
      " 2   year       1704 non-null   int64  \n",
      " 3   lifeExp    1704 non-null   float64\n",
      " 4   pop        1704 non-null   int64  \n",
      " 5   gdpPercap  1704 non-null   float64\n",
      "dtypes: float64(2), int64(2), object(2)\n",
      "memory usage: 80.0+ KB\n",
      "None\n"
     ]
    }
   ],
   "source": [
    "print(df.info()) #info 많이 사용"
   ]
  },
  {
   "attachments": {
    "e637b6ff-d5b6-446f-bb91-3561caebaf3d.png": {
     "image/png": "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mgeMHBSJyumTDzFUenvDLrKV1JjqySmWi7DjzoW2A8vYb64OcdO03UC12WTJz8831tRNN91krKEffvhBb731lq644godcsghGj58uLxeb5v1x3+d8/LyNHToUB144IE644wzdO+99xrr7JVXXtGNN96oY445RiNGjJDT6Wzzvvn7GO97XmGdlp7ymgEM6PHkdVGGJCMruvGuvCxFXV+M7t5COaPv4P21ZNXzTcdHyBdVjXjPq9X2D7S2KBJpypYMkYOyJfscoczDzvGVLbnwSXmve1t5d3yh/Pt/MLEtA1rGRfi9YRgS+8q54Alln0hxyHPlmnaUEeS19xqh1IqusnlxEWb7CCC4JjvhvW+dU8T3TMQbWhOlFW+UkpISLVu2TI8//rgAKlx4GzduNC66srL4E2Jb64YAQMeOHasVK1YY1yIg9uyzz+q8887TlClTlJubm3TzBgAZMe4orTrvsyYAweqZvfBW9R92oPIKals8p0iBC6FdRHup1RWoQH/6hh81acY5Qjuxta5d/O36hXRDlC3ZY54yDjxpW9mSjS+bWlrU1DKxLSwtypVs/XFbcchLnlP2GXcZ9qFr/+Pk3P0AY7mZ4pAFgcUhrXIl8V+7pF/3k/4EOvCN3fzYEquaPn26tmzZop9++knvvfeezj77bGO12O3cnKH357fi4mL17NnTEC/GjBmjCRMmaJ999ml67bnnntptt900ePBgEw8rKioK216448TyPUDGsXExPvnkk8a1iaXId+HclrEcpy32IcY0cvzROvLkl5sAzF+DCwV34k+Ay7Axi9Wtz54qr9pFhSXdjL5h3cYMdX/RLgpO8uL7Lj3Gm/ImE6at1pxFt5laXP72/O/ITlH+pCX1+bY4/xaPYawth69oY06hbGVdZO9B2ZJpck0/SpmLzlP2Kbcq56Jfy3v9O8q780sVbA2wtnARBhaHXPug3CuuVsb805W+50I5hu4pe9eBspXUmthZCiBuFYdsk/u4xWsfZm1qw/1CL45t2IGd7kJUV1dr9erVhkjx5z//2bgAYf6lEitonBCQIHbZZRfNmTPHuOU2b95syBcQKv7617+aF2DH68cff9Q333wjP9kCaw0yxvfff29iYd9++614ffDBB7r//vt1/vnn69BDDzUsQ4/H03RM/7ET9Z6WlmZiYMcff7yxJB977DGtXLlS3bt3b7Vj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"
    }
   },
   "cell_type": "markdown",
   "id": "222cd6a2-2132-4be9-9d76-2d232422dcba",
   "metadata": {},
   "source": [
    "### Ex) pulsar_stars.csv\n",
    "![image.png](attachment:e637b6ff-d5b6-446f-bb91-3561caebaf3d.png)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "8ba518ff-13b9-4bf4-b7b7-da79c0be1ac9",
   "metadata": {},
   "outputs": [],
   "source": [
    "stars = pd.read_csv('dataset/copy of pulsar_stars.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "f4cdc528-83b0-49dd-9cd2-11fae9bf5d55",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Mean of the integrated profile</th>\n",
       "      <th>Standard deviation of the integrated profile</th>\n",
       "      <th>Excess kurtosis of the integrated profile</th>\n",
       "      <th>Skewness of the integrated profile</th>\n",
       "      <th>Mean of the DM-SNR curve</th>\n",
       "      <th>Standard deviation of the DM-SNR curve</th>\n",
       "      <th>Excess kurtosis of the DM-SNR curve</th>\n",
       "      <th>Skewness of the DM-SNR curve</th>\n",
       "      <th>target_class</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>140.562500</td>\n",
       "      <td>55.683782</td>\n",
       "      <td>-0.234571</td>\n",
       "      <td>-0.699648</td>\n",
       "      <td>3.199833</td>\n",
       "      <td>19.110426</td>\n",
       "      <td>7.975532</td>\n",
       "      <td>74.242225</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>102.507812</td>\n",
       "      <td>58.882430</td>\n",
       "      <td>0.465318</td>\n",
       "      <td>-0.515088</td>\n",
       "      <td>1.677258</td>\n",
       "      <td>14.860146</td>\n",
       "      <td>10.576487</td>\n",
       "      <td>127.393580</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>103.015625</td>\n",
       "      <td>39.341649</td>\n",
       "      <td>0.323328</td>\n",
       "      <td>1.051164</td>\n",
       "      <td>3.121237</td>\n",
       "      <td>21.744669</td>\n",
       "      <td>7.735822</td>\n",
       "      <td>63.171909</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>136.750000</td>\n",
       "      <td>57.178449</td>\n",
       "      <td>-0.068415</td>\n",
       "      <td>-0.636238</td>\n",
       "      <td>3.642977</td>\n",
       "      <td>20.959280</td>\n",
       "      <td>6.896499</td>\n",
       "      <td>53.593661</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>88.726562</td>\n",
       "      <td>40.672225</td>\n",
       "      <td>0.600866</td>\n",
       "      <td>1.123492</td>\n",
       "      <td>1.178930</td>\n",
       "      <td>11.468720</td>\n",
       "      <td>14.269573</td>\n",
       "      <td>252.567306</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    Mean of the integrated profile  \\\n",
       "0                       140.562500   \n",
       "1                       102.507812   \n",
       "2                       103.015625   \n",
       "3                       136.750000   \n",
       "4                        88.726562   \n",
       "\n",
       "    Standard deviation of the integrated profile  \\\n",
       "0                                      55.683782   \n",
       "1                                      58.882430   \n",
       "2                                      39.341649   \n",
       "3                                      57.178449   \n",
       "4                                      40.672225   \n",
       "\n",
       "    Excess kurtosis of the integrated profile  \\\n",
       "0                                   -0.234571   \n",
       "1                                    0.465318   \n",
       "2                                    0.323328   \n",
       "3                                   -0.068415   \n",
       "4                                    0.600866   \n",
       "\n",
       "    Skewness of the integrated profile   Mean of the DM-SNR curve  \\\n",
       "0                            -0.699648                   3.199833   \n",
       "1                            -0.515088                   1.677258   \n",
       "2                             1.051164                   3.121237   \n",
       "3                            -0.636238                   3.642977   \n",
       "4                             1.123492                   1.178930   \n",
       "\n",
       "    Standard deviation of the DM-SNR curve  \\\n",
       "0                                19.110426   \n",
       "1                                14.860146   \n",
       "2                                21.744669   \n",
       "3                                20.959280   \n",
       "4                                11.468720   \n",
       "\n",
       "    Excess kurtosis of the DM-SNR curve   Skewness of the DM-SNR curve  \\\n",
       "0                              7.975532                      74.242225   \n",
       "1                             10.576487                     127.393580   \n",
       "2                              7.735822                      63.171909   \n",
       "3                              6.896499                      53.593661   \n",
       "4                             14.269573                     252.567306   \n",
       "\n",
       "   target_class  \n",
       "0             0  \n",
       "1             0  \n",
       "2             0  \n",
       "3             0  \n",
       "4             0  "
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "stars.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "5cc012d1-1dd5-4709-bec9-0e423601ef52",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(17898, 9)"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "stars.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "3ff4c24e-4760-4aa6-a4f1-6dc5140987ca",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      " Mean of the integrated profile                  float64\n",
      " Standard deviation of the integrated profile    float64\n",
      " Excess kurtosis of the integrated profile       float64\n",
      " Skewness of the integrated profile              float64\n",
      " Mean of the DM-SNR curve                        float64\n",
      " Standard deviation of the DM-SNR curve          float64\n",
      " Excess kurtosis of the DM-SNR curve             float64\n",
      " Skewness of the DM-SNR curve                    float64\n",
      "target_class                                       int64\n",
      "dtype: object\n"
     ]
    }
   ],
   "source": [
    "print(type(stars))\n",
    "print(stars.dtypes)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "81682cca-d664-4e0e-83b7-bcb345311bea",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 17898 entries, 0 to 17897\n",
      "Data columns (total 9 columns):\n",
      " #   Column                                         Non-Null Count  Dtype  \n",
      "---  ------                                         --------------  -----  \n",
      " 0    Mean of the integrated profile                17898 non-null  float64\n",
      " 1    Standard deviation of the integrated profile  17898 non-null  float64\n",
      " 2    Excess kurtosis of the integrated profile     17898 non-null  float64\n",
      " 3    Skewness of the integrated profile            17898 non-null  float64\n",
      " 4    Mean of the DM-SNR curve                      17898 non-null  float64\n",
      " 5    Standard deviation of the DM-SNR curve        17898 non-null  float64\n",
      " 6    Excess kurtosis of the DM-SNR curve           17898 non-null  float64\n",
      " 7    Skewness of the DM-SNR curve                  17898 non-null  float64\n",
      " 8   target_class                                   17898 non-null  int64  \n",
      "dtypes: float64(8), int64(1)\n",
      "memory usage: 1.2 MB\n"
     ]
    }
   ],
   "source": [
    "stars.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "1b1b6c96-07f7-425d-bc3a-bbc6a0599ba5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0        0\n",
       "1        0\n",
       "2        0\n",
       "3        0\n",
       "4        0\n",
       "        ..\n",
       "17893    0\n",
       "17894    0\n",
       "17895    0\n",
       "17896    0\n",
       "17897    0\n",
       "Name: target_class, Length: 17898, dtype: int64"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "stars_target = stars['target_class']\n",
    "stars_target"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "e16621a8-05d0-4e63-8897-fc804ab4c58f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{0, 1}"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "set(stars_target)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "bc544fa1-481f-40fd-9161-0ab0d6d504e6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    16259\n",
       "1     1639\n",
       "Name: target_class, dtype: int64"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "stars_target.value_counts(0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "b87cbcc7-2761-4dc9-b677-86d38fb36555",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.series.Series'>\n"
     ]
    }
   ],
   "source": [
    "country_df = df['country']\n",
    "print(type(country_df))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "d5d02bae-fb3e-4d19-bf93-d368a0725138",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0    Afghanistan\n",
      "1    Afghanistan\n",
      "2    Afghanistan\n",
      "3    Afghanistan\n",
      "4    Afghanistan\n",
      "Name: country, dtype: object\n",
      "1699    Zimbabwe\n",
      "1700    Zimbabwe\n",
      "1701    Zimbabwe\n",
      "1702    Zimbabwe\n",
      "1703    Zimbabwe\n",
      "Name: country, dtype: object\n"
     ]
    }
   ],
   "source": [
    "print(country_df.head())\n",
    "print(country_df.tail())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "a9155ebe-dc3c-4c44-96e8-7cd8673624ef",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0       Afghanistan\n",
       "1       Afghanistan\n",
       "2       Afghanistan\n",
       "3       Afghanistan\n",
       "4       Afghanistan\n",
       "           ...     \n",
       "1699       Zimbabwe\n",
       "1700       Zimbabwe\n",
       "1701       Zimbabwe\n",
       "1702       Zimbabwe\n",
       "1703       Zimbabwe\n",
       "Name: country, Length: 1704, dtype: object"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "country_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "5684c44e-a4bc-4ff8-9b4b-31707141130b",
   "metadata": {},
   "outputs": [],
   "source": [
    "subset = df[['country','continent','year']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "5081b24b-5acb-4be4-8dae-e93bd2852661",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>country</th>\n",
       "      <th>continent</th>\n",
       "      <th>year</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Afghanistan</td>\n",
       "      <td>Asia</td>\n",
       "      <td>1952</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Afghanistan</td>\n",
       "      <td>Asia</td>\n",
       "      <td>1957</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Afghanistan</td>\n",
       "      <td>Asia</td>\n",
       "      <td>1962</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Afghanistan</td>\n",
       "      <td>Asia</td>\n",
       "      <td>1967</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Afghanistan</td>\n",
       "      <td>Asia</td>\n",
       "      <td>1972</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1699</th>\n",
       "      <td>Zimbabwe</td>\n",
       "      <td>Africa</td>\n",
       "      <td>1987</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1700</th>\n",
       "      <td>Zimbabwe</td>\n",
       "      <td>Africa</td>\n",
       "      <td>1992</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1701</th>\n",
       "      <td>Zimbabwe</td>\n",
       "      <td>Africa</td>\n",
       "      <td>1997</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1702</th>\n",
       "      <td>Zimbabwe</td>\n",
       "      <td>Africa</td>\n",
       "      <td>2002</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1703</th>\n",
       "      <td>Zimbabwe</td>\n",
       "      <td>Africa</td>\n",
       "      <td>2007</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>1704 rows × 3 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "          country continent  year\n",
       "0     Afghanistan      Asia  1952\n",
       "1     Afghanistan      Asia  1957\n",
       "2     Afghanistan      Asia  1962\n",
       "3     Afghanistan      Asia  1967\n",
       "4     Afghanistan      Asia  1972\n",
       "...           ...       ...   ...\n",
       "1699     Zimbabwe    Africa  1987\n",
       "1700     Zimbabwe    Africa  1992\n",
       "1701     Zimbabwe    Africa  1997\n",
       "1702     Zimbabwe    Africa  2002\n",
       "1703     Zimbabwe    Africa  2007\n",
       "\n",
       "[1704 rows x 3 columns]"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "subset"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "43c3572b-f015-4c88-930f-46f181091120",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "pandas.core.frame.DataFrame"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(subset)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "32d224a2-fc83-425b-94d4-bc876209c81c",
   "metadata": {},
   "source": [
    "## 1.2.2 loc(index) & iloc(row number)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "23f80d51-210e-4f7f-8df3-38a1c5f83c9e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>country</th>\n",
       "      <th>continent</th>\n",
       "      <th>year</th>\n",
       "      <th>lifeExp</th>\n",
       "      <th>pop</th>\n",
       "      <th>gdpPercap</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Afghanistan</td>\n",
       "      <td>Asia</td>\n",
       "      <td>1952</td>\n",
       "      <td>28.801</td>\n",
       "      <td>8425333</td>\n",
       "      <td>779.445314</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Afghanistan</td>\n",
       "      <td>Asia</td>\n",
       "      <td>1957</td>\n",
       "      <td>30.332</td>\n",
       "      <td>9240934</td>\n",
       "      <td>820.853030</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Afghanistan</td>\n",
       "      <td>Asia</td>\n",
       "      <td>1962</td>\n",
       "      <td>31.997</td>\n",
       "      <td>10267083</td>\n",
       "      <td>853.100710</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Afghanistan</td>\n",
       "      <td>Asia</td>\n",
       "      <td>1967</td>\n",
       "      <td>34.020</td>\n",
       "      <td>11537966</td>\n",
       "      <td>836.197138</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Afghanistan</td>\n",
       "      <td>Asia</td>\n",
       "      <td>1972</td>\n",
       "      <td>36.088</td>\n",
       "      <td>13079460</td>\n",
       "      <td>739.981106</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       country continent  year  lifeExp       pop   gdpPercap\n",
       "0  Afghanistan      Asia  1952   28.801   8425333  779.445314\n",
       "1  Afghanistan      Asia  1957   30.332   9240934  820.853030\n",
       "2  Afghanistan      Asia  1962   31.997  10267083  853.100710\n",
       "3  Afghanistan      Asia  1967   34.020  11537966  836.197138\n",
       "4  Afghanistan      Asia  1972   36.088  13079460  739.981106"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "61e62345-d73e-4234-9763-3794212f1c5d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "country      Afghanistan\n",
      "continent           Asia\n",
      "year                1952\n",
      "lifeExp           28.801\n",
      "pop              8425333\n",
      "gdpPercap     779.445314\n",
      "Name: 0, dtype: object\n",
      "\n",
      "\n",
      "country      Bangladesh\n",
      "continent          Asia\n",
      "year               1967\n",
      "lifeExp          43.453\n",
      "pop            62821884\n",
      "gdpPercap    721.186086\n",
      "Name: 99, dtype: object\n"
     ]
    }
   ],
   "source": [
    "print(df.loc[0])\n",
    "print(\"\\n\")\n",
    "print(df.loc[99])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "ff2218ed-849d-4eca-8696-817d8e8707f3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'KeyError'>\n",
      "Thank you.\n"
     ]
    }
   ],
   "source": [
    "try:\n",
    "    df.loc[2000] # 범위를 벗어남\n",
    "except Exception as all_e:\n",
    "    print(type(all_e))\n",
    "finally:\n",
    "    print(\"Thank you.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "b1f73fc1-2954-45a9-a9ec-aa8ef25dbfff",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>country</th>\n",
       "      <th>continent</th>\n",
       "      <th>year</th>\n",
       "      <th>lifeExp</th>\n",
       "      <th>pop</th>\n",
       "      <th>gdpPercap</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>Afghanistan</td>\n",
       "      <td>Asia</td>\n",
       "      <td>2002</td>\n",
       "      <td>42.129</td>\n",
       "      <td>25268405</td>\n",
       "      <td>726.734055</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>100</th>\n",
       "      <td>Bangladesh</td>\n",
       "      <td>Asia</td>\n",
       "      <td>1972</td>\n",
       "      <td>45.252</td>\n",
       "      <td>70759295</td>\n",
       "      <td>630.233627</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1000</th>\n",
       "      <td>Mongolia</td>\n",
       "      <td>Asia</td>\n",
       "      <td>1972</td>\n",
       "      <td>53.754</td>\n",
       "      <td>1320500</td>\n",
       "      <td>1421.741975</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          country continent  year  lifeExp       pop    gdpPercap\n",
       "10    Afghanistan      Asia  2002   42.129  25268405   726.734055\n",
       "100    Bangladesh      Asia  1972   45.252  70759295   630.233627\n",
       "1000     Mongolia      Asia  1972   53.754   1320500  1421.741975"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.loc[[10,100,1000]]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ca605352-cfbf-4a32-93da-4fd4f98ddee5",
   "metadata": {},
   "source": [
    "### ▶ df.loc[[low],[col]]\n",
    "### ▶ df.iloc[[low],[col]]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "848b1929-9b57-49bb-81eb-596460c7b703",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   year       pop\n",
      "0  1952   8425333\n",
      "1  1957   9240934\n",
      "2  1962  10267083\n",
      "3  1967  11537966\n",
      "4  1972  13079460\n"
     ]
    }
   ],
   "source": [
    "subset = df.loc[:,['year','pop']] #문자로 뽑기(변수가 많을때는 인덱스를 찾기 힘듦)\n",
    "print(subset.head())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "3e93c84b-f9f5-4670-b6ff-4ecef485d390",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\"None of [Int64Index([2, 4], dtype='int64')] are in the [columns]\"\n",
      "<class 'KeyError'>\n"
     ]
    }
   ],
   "source": [
    "try:\n",
    "    subset = df.loc[:,[2,4]]\n",
    "except Exception as all_e:\n",
    "    print(all_e)\n",
    "    print(type(all_e))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "f9ab88ff-f8aa-4d5e-82f4-bc1ae26c2419",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   year       pop   gdpPercap\n",
      "0  1952   8425333  779.445314\n",
      "1  1957   9240934  820.853030\n",
      "2  1962  10267083  853.100710\n",
      "3  1967  11537966  836.197138\n",
      "4  1972  13079460  739.981106\n"
     ]
    }
   ],
   "source": [
    "subset = df.iloc[:,[2,4,-1]] #숫자(인덱스)로 뽑기\n",
    "print(subset.head())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "fb463923-2b6f-46f1-873a-ec38e750addd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      ".iloc requires numeric indexers, got ['year' 'pop']\n",
      "<class 'IndexError'>\n"
     ]
    }
   ],
   "source": [
    "try:\n",
    "    subset = df.iloc[:,['year','pop']] \n",
    "except Exception as all_e:\n",
    "    print(all_e)\n",
    "    print(type(all_e))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "6b928d67-f3e6-479a-b97a-537c4b672994",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "range(0, 10)"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "range(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "ea4a3623-e93f-4f8a-baca-19b9b2fff502",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "          country continent  year\n",
      "0     Afghanistan      Asia  1952\n",
      "1     Afghanistan      Asia  1957\n",
      "2     Afghanistan      Asia  1962\n",
      "3     Afghanistan      Asia  1967\n",
      "4     Afghanistan      Asia  1972\n",
      "...           ...       ...   ...\n",
      "1699     Zimbabwe    Africa  1987\n",
      "1700     Zimbabwe    Africa  1992\n",
      "1701     Zimbabwe    Africa  1997\n",
      "1702     Zimbabwe    Africa  2002\n",
      "1703     Zimbabwe    Africa  2007\n",
      "\n",
      "[1704 rows x 3 columns]\n"
     ]
    }
   ],
   "source": [
    "small_range = list(range(3))\n",
    "subset = df.iloc[:,small_range]\n",
    "print(subset)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "c657c433-0cdf-426b-b4a0-59ef9c477ae3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "          country continent  year\n",
      "0     Afghanistan      Asia  1952\n",
      "1     Afghanistan      Asia  1957\n",
      "2     Afghanistan      Asia  1962\n",
      "3     Afghanistan      Asia  1967\n",
      "4     Afghanistan      Asia  1972\n",
      "...           ...       ...   ...\n",
      "1699     Zimbabwe    Africa  1987\n",
      "1700     Zimbabwe    Africa  1992\n",
      "1701     Zimbabwe    Africa  1997\n",
      "1702     Zimbabwe    Africa  2002\n",
      "1703     Zimbabwe    Africa  2007\n",
      "\n",
      "[1704 rows x 3 columns]\n"
     ]
    }
   ],
   "source": [
    "subset = df.iloc[:,range(3)]\n",
    "print(subset)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "ddd1510e-24b2-4db7-aa97-94dda88c33d9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "         country  lifeExp    gdpPercap\n",
      "0    Afghanistan   28.801   779.445314\n",
      "99    Bangladesh   43.453   721.186086\n",
      "999     Mongolia   51.253  1226.041130\n"
     ]
    }
   ],
   "source": [
    "print(df.iloc[[0,99,999],[0,3,5]])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "fb81a141-234e-457c-9990-ec96cc35ad6b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "     year       pop\n",
      "0    1952   8425333\n",
      "99   1967  62821884\n",
      "999  1967   1149500\n"
     ]
    }
   ],
   "source": [
    "print(df.loc[[0,99,999],['year','pop']])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "f8c2b655-a314-4ebe-b4bb-204e111a2e9c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "        country  lifeExp    gdpPercap\n",
      "10  Afghanistan   42.129   726.734055\n",
      "11  Afghanistan   43.828   974.580338\n",
      "12      Albania   55.230  1601.056136\n",
      "13      Albania   59.280  1942.284244\n"
     ]
    }
   ],
   "source": [
    "print(df.loc[10:13,['country','lifeExp','gdpPercap']])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3c069667-73ca-4a4c-ad25-a1d43dc03d8b",
   "metadata": {},
   "source": [
    "### Ex) pulsar_stars.csv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "1c86f9ce-5a4f-4592-bc8a-1ee34eb70afe",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 17898 entries, 0 to 17897\n",
      "Data columns (total 9 columns):\n",
      " #   Column                                         Non-Null Count  Dtype  \n",
      "---  ------                                         --------------  -----  \n",
      " 0    Mean of the integrated profile                17898 non-null  float64\n",
      " 1    Standard deviation of the integrated profile  17898 non-null  float64\n",
      " 2    Excess kurtosis of the integrated profile     17898 non-null  float64\n",
      " 3    Skewness of the integrated profile            17898 non-null  float64\n",
      " 4    Mean of the DM-SNR curve                      17898 non-null  float64\n",
      " 5    Standard deviation of the DM-SNR curve        17898 non-null  float64\n",
      " 6    Excess kurtosis of the DM-SNR curve           17898 non-null  float64\n",
      " 7    Skewness of the DM-SNR curve                  17898 non-null  float64\n",
      " 8   target_class                                   17898 non-null  int64  \n",
      "dtypes: float64(8), int64(1)\n",
      "memory usage: 1.2 MB\n"
     ]
    }
   ],
   "source": [
    "stars.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "1fff8a0d-81d5-4a33-a7a1-545e5cbf1504",
   "metadata": {},
   "outputs": [],
   "source": [
    "stars_mean_df = stars[[' Mean of the DM-SNR curve',' Mean of the integrated profile']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "e23c4ab0-2b77-4c52-9f3f-b8d617ddcf8e",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'stars_df' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-46-544b90f1535a>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mstars_df\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m: name 'stars_df' is not defined"
     ]
    }
   ],
   "source": [
    "stars_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f1611a27-4ff4-4a24-93ad-70cffda7b198",
   "metadata": {},
   "outputs": [],
   "source": [
    "stars.loc[[1, 10,100, 1000, 10000],\n",
    "          [' Mean of the DM-SNR curve',' Mean of the integrated profile']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "3e3709a8-4948-4eaf-8286-743ac7acabc6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Mean of the integrated profile</th>\n",
       "      <th>Mean of the DM-SNR curve</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>102.507812</td>\n",
       "      <td>1.677258</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>142.078125</td>\n",
       "      <td>5.376254</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>100</th>\n",
       "      <td>123.468750</td>\n",
       "      <td>32.919732</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1000</th>\n",
       "      <td>90.367188</td>\n",
       "      <td>5.459866</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10000</th>\n",
       "      <td>130.898438</td>\n",
       "      <td>2.078595</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        Mean of the integrated profile   Mean of the DM-SNR curve\n",
       "1                           102.507812                   1.677258\n",
       "10                          142.078125                   5.376254\n",
       "100                         123.468750                  32.919732\n",
       "1000                         90.367188                   5.459866\n",
       "10000                       130.898438                   2.078595"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "stars.iloc[[1, 10,100, 1000, 10000],\n",
    "          [0,4]]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "7bbf9e85-bcaf-4226-a55d-54349cc163d7",
   "metadata": {},
   "outputs": [],
   "source": [
    "stars_target_class = stars.loc[:,'target_class']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "15d85ba5-327e-4e89-8b33-3c600eb1d9b4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{0, 1}\n"
     ]
    }
   ],
   "source": [
    "print(set(stars_target_class))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "47ae8eed-2f14-46de-abf5-6280b4799896",
   "metadata": {},
   "source": [
    "# Basic Pandas for Artificial Intelligence\n",
    "## 1.3.1 Basic Statistics"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "29506953-12c4-484a-ba61-f949c08da415",
   "metadata": {},
   "source": [
    "### Ex) Gapminder Dataset(0~9)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "33bf8759-08bc-4d4a-b39f-a0d7428d4f4a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>country</th>\n",
       "      <th>continent</th>\n",
       "      <th>year</th>\n",
       "      <th>lifeExp</th>\n",
       "      <th>pop</th>\n",
       "      <th>gdpPercap</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Afghanistan</td>\n",
       "      <td>Asia</td>\n",
       "      <td>1952</td>\n",
       "      <td>28.801</td>\n",
       "      <td>8425333</td>\n",
       "      <td>779.445314</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Afghanistan</td>\n",
       "      <td>Asia</td>\n",
       "      <td>1957</td>\n",
       "      <td>30.332</td>\n",
       "      <td>9240934</td>\n",
       "      <td>820.853030</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Afghanistan</td>\n",
       "      <td>Asia</td>\n",
       "      <td>1962</td>\n",
       "      <td>31.997</td>\n",
       "      <td>10267083</td>\n",
       "      <td>853.100710</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Afghanistan</td>\n",
       "      <td>Asia</td>\n",
       "      <td>1967</td>\n",
       "      <td>34.020</td>\n",
       "      <td>11537966</td>\n",
       "      <td>836.197138</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Afghanistan</td>\n",
       "      <td>Asia</td>\n",
       "      <td>1972</td>\n",
       "      <td>36.088</td>\n",
       "      <td>13079460</td>\n",
       "      <td>739.981106</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Afghanistan</td>\n",
       "      <td>Asia</td>\n",
       "      <td>1977</td>\n",
       "      <td>38.438</td>\n",
       "      <td>14880372</td>\n",
       "      <td>786.113360</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Afghanistan</td>\n",
       "      <td>Asia</td>\n",
       "      <td>1982</td>\n",
       "      <td>39.854</td>\n",
       "      <td>12881816</td>\n",
       "      <td>978.011439</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>Afghanistan</td>\n",
       "      <td>Asia</td>\n",
       "      <td>1987</td>\n",
       "      <td>40.822</td>\n",
       "      <td>13867957</td>\n",
       "      <td>852.395945</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>Afghanistan</td>\n",
       "      <td>Asia</td>\n",
       "      <td>1992</td>\n",
       "      <td>41.674</td>\n",
       "      <td>16317921</td>\n",
       "      <td>649.341395</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       country continent  year  lifeExp       pop   gdpPercap\n",
       "0  Afghanistan      Asia  1952   28.801   8425333  779.445314\n",
       "1  Afghanistan      Asia  1957   30.332   9240934  820.853030\n",
       "2  Afghanistan      Asia  1962   31.997  10267083  853.100710\n",
       "3  Afghanistan      Asia  1967   34.020  11537966  836.197138\n",
       "4  Afghanistan      Asia  1972   36.088  13079460  739.981106\n",
       "5  Afghanistan      Asia  1977   38.438  14880372  786.113360\n",
       "6  Afghanistan      Asia  1982   39.854  12881816  978.011439\n",
       "7  Afghanistan      Asia  1987   40.822  13867957  852.395945\n",
       "8  Afghanistan      Asia  1992   41.674  16317921  649.341395"
      ]
     },
     "execution_count": 50,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[0:9]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "f73c9f37-a79c-4b31-a005-ef3695af3217",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_lifeExp = df['lifeExp']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "eec5825a-d3c7-4bf0-a60f-05d8e5c8f167",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "df_lifeExp_sum :  101344.44467999993\n",
      "df_lifeExp_mean :  59.47443936619714\n"
     ]
    }
   ],
   "source": [
    "df_lifeExp_sum = 0\n",
    "\n",
    "for i in range(len(df_lifeExp)):\n",
    "    df_lifeExp_sum += df_lifeExp[i]\n",
    "\n",
    "print(\"df_lifeExp_sum : \", df_lifeExp_sum)\n",
    "    \n",
    "df_lifeExp_mean = df_lifeExp_sum/len(df_lifeExp)\n",
    "print(\"df_lifeExp_mean : \", df_lifeExp_mean)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "bcc509e2-a19a-49fc-8195-6e378e4bfdf4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1952, 1987, 1957, 1992, 1962, 1997, 1967, 2002, 1972, 2007, 1977, 1982]\n"
     ]
    }
   ],
   "source": [
    "df_year_set = list(set(df['year']))\n",
    "print(df_year_set)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "43253c13-daac-4072-95ef-6c54d15ff9c9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>year</th>\n",
       "      <th>lifeExp</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1952</td>\n",
       "      <td>28.801</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1957</td>\n",
       "      <td>30.332</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1962</td>\n",
       "      <td>31.997</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1967</td>\n",
       "      <td>34.020</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1972</td>\n",
       "      <td>36.088</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1699</th>\n",
       "      <td>1987</td>\n",
       "      <td>62.351</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1700</th>\n",
       "      <td>1992</td>\n",
       "      <td>60.377</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1701</th>\n",
       "      <td>1997</td>\n",
       "      <td>46.809</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1702</th>\n",
       "      <td>2002</td>\n",
       "      <td>39.989</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1703</th>\n",
       "      <td>2007</td>\n",
       "      <td>43.487</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>1704 rows × 2 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "      year  lifeExp\n",
       "0     1952   28.801\n",
       "1     1957   30.332\n",
       "2     1962   31.997\n",
       "3     1967   34.020\n",
       "4     1972   36.088\n",
       "...    ...      ...\n",
       "1699  1987   62.351\n",
       "1700  1992   60.377\n",
       "1701  1997   46.809\n",
       "1702  2002   39.989\n",
       "1703  2007   43.487\n",
       "\n",
       "[1704 rows x 2 columns]"
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_year_lifeExp = df[['year','lifeExp']]\n",
    "df_year_lifeExp"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "85ae20bd-08b5-4b5d-94df-577bed97f625",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 1704 entries, 0 to 1703\n",
      "Data columns (total 2 columns):\n",
      " #   Column   Non-Null Count  Dtype  \n",
      "---  ------   --------------  -----  \n",
      " 0   year     1704 non-null   int64  \n",
      " 1   lifeExp  1704 non-null   float64\n",
      "dtypes: float64(1), int64(1)\n",
      "memory usage: 26.8 KB\n"
     ]
    }
   ],
   "source": [
    "df_year_lifeExp.info() #count 값이 나오므로 결측값 확인 가능"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "b204b093-1b4b-418e-a891-a30cee354047",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_year_lifeExp_1952 = []\n",
    "\n",
    "for i in range(len(df_year_lifeExp)):\n",
    "    \n",
    "    if df_year_lifeExp['year'][i] == 1952 :\n",
    "        df_year_lifeExp_1952.append(df_year_lifeExp['lifeExp'][i])\n",
    "        \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "6c3e2436-e9e9-4d13-bae6-d1736ad4004c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[28.801, 55.23, 43.077, 30.015, 62.485]\n"
     ]
    }
   ],
   "source": [
    "print(df_year_lifeExp_1952[0:5])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "2f5ee459-a52b-413d-826c-d634796f5c7d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "df_lifeExp_sum :  6966.182000000002\n",
      "df_lifeExp_mean :  49.05761971830987\n"
     ]
    }
   ],
   "source": [
    "df_lifeExp_sum = 0\n",
    "\n",
    "for i in range(len(df_year_lifeExp_1952)) :\n",
    "    df_lifeExp_sum += df_year_lifeExp_1952[i]\n",
    "print(\"df_lifeExp_sum : \", df_lifeExp_sum)\n",
    "df_lifeExp_mean = df_lifeExp_sum/len(df_year_lifeExp_1952)\n",
    "print(\"df_lifeExp_mean : \", df_lifeExp_mean)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "id": "d5e8458e-5ad3-43de-a272-e41be162c8eb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "         gdpPercap    lifeExp\n",
      "year                         \n",
      "1952   3725.276046  49.057620\n",
      "1957   4299.408345  51.507401\n",
      "1962   4725.812342  53.609249\n",
      "1967   5483.653047  55.678290\n",
      "1972   6770.082815  57.647386\n",
      "1977   7313.166421  59.570157\n",
      "1982   7518.901673  61.533197\n",
      "1987   7900.920218  63.212613\n",
      "1992   8158.608521  64.160338\n",
      "1997   9090.175363  65.014676\n",
      "2002   9917.848365  65.694923\n",
      "2007  11680.071820  67.007423\n"
     ]
    }
   ],
   "source": [
    "print(df.groupby('year')[['gdpPercap','lifeExp']].mean()) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "0de6c021-87b5-4f33-b399-41bdfd1c939e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.groupby.generic.DataFrameGroupBy'>\n"
     ]
    }
   ],
   "source": [
    "groupby_year_df = df.groupby('year')\n",
    "print(type(groupby_year_df))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "id": "64737dbe-04c7-4088-8696-288f1e8053f1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "year\n",
      "1952     3725.276046\n",
      "1957     4299.408345\n",
      "1962     4725.812342\n",
      "1967     5483.653047\n",
      "1972     6770.082815\n",
      "1977     7313.166421\n",
      "1982     7518.901673\n",
      "1987     7900.920218\n",
      "1992     8158.608521\n",
      "1997     9090.175363\n",
      "2002     9917.848365\n",
      "2007    11680.071820\n",
      "Name: gdpPercap, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "print(df.groupby('year')['gdpPercap'].mean())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "198a1b43-b5ae-4f41-ae33-3c337d09b7d6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 1704 entries, 0 to 1703\n",
      "Data columns (total 6 columns):\n",
      " #   Column     Non-Null Count  Dtype  \n",
      "---  ------     --------------  -----  \n",
      " 0   country    1704 non-null   object \n",
      " 1   continent  1704 non-null   object \n",
      " 2   year       1704 non-null   int64  \n",
      " 3   lifeExp    1704 non-null   float64\n",
      " 4   pop        1704 non-null   int64  \n",
      " 5   gdpPercap  1704 non-null   float64\n",
      "dtypes: float64(2), int64(2), object(2)\n",
      "memory usage: 80.0+ KB\n"
     ]
    }
   ],
   "source": [
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "id": "0f3cec69-af71-449a-aecd-f30b20f02cb8",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_continent = df['continent']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "id": "472517d4-57e7-46a2-8911-015773c53f99",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'Africa', 'Americas', 'Asia', 'Europe', 'Oceania'}"
      ]
     },
     "execution_count": 69,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "set(df_continent)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "id": "fcc91329-83ef-4337-94f9-74ba5011721c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>year</th>\n",
       "      <th>continent</th>\n",
       "      <th>lifeExp</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1952</td>\n",
       "      <td>Asia</td>\n",
       "      <td>28.801</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1957</td>\n",
       "      <td>Asia</td>\n",
       "      <td>30.332</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1962</td>\n",
       "      <td>Asia</td>\n",
       "      <td>31.997</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1967</td>\n",
       "      <td>Asia</td>\n",
       "      <td>34.020</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1972</td>\n",
       "      <td>Asia</td>\n",
       "      <td>36.088</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1699</th>\n",
       "      <td>1987</td>\n",
       "      <td>Africa</td>\n",
       "      <td>62.351</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1700</th>\n",
       "      <td>1992</td>\n",
       "      <td>Africa</td>\n",
       "      <td>60.377</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1701</th>\n",
       "      <td>1997</td>\n",
       "      <td>Africa</td>\n",
       "      <td>46.809</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1702</th>\n",
       "      <td>2002</td>\n",
       "      <td>Africa</td>\n",
       "      <td>39.989</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1703</th>\n",
       "      <td>2007</td>\n",
       "      <td>Africa</td>\n",
       "      <td>43.487</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>1704 rows × 3 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "      year continent  lifeExp\n",
       "0     1952      Asia   28.801\n",
       "1     1957      Asia   30.332\n",
       "2     1962      Asia   31.997\n",
       "3     1967      Asia   34.020\n",
       "4     1972      Asia   36.088\n",
       "...    ...       ...      ...\n",
       "1699  1987    Africa   62.351\n",
       "1700  1992    Africa   60.377\n",
       "1701  1997    Africa   46.809\n",
       "1702  2002    Africa   39.989\n",
       "1703  2007    Africa   43.487\n",
       "\n",
       "[1704 rows x 3 columns]"
      ]
     },
     "execution_count": 77,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_year_continent_lifeExp = df[['year','continent','lifeExp']]\n",
    "df_year_continent_lifeExp"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "id": "7a75883f-c331-4d7e-af4d-41735b4203c0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "df_year_continent_lifeExp_sum :  1627.5119600000003\n",
      "df_year_continent_lifeExp_mean :  49.31854424242425\n"
     ]
    }
   ],
   "source": [
    "df_year_continent_lifeExp_row = []\n",
    "df_year_continent_lifeExp_sum = 0\n",
    "\n",
    "for i in range(len(df_year_continent_lifeExp)):\n",
    "    if df_year_continent_lifeExp['year'][i] == 1957 and \\\n",
    "       df_year_continent_lifeExp['continent'][i] == 'Asia' :\n",
    "        df_year_continent_lifeExp_sum += df_year_continent_lifeExp['lifeExp'][i]\n",
    "        df_year_continent_lifeExp_row.append(df_year_continent_lifeExp['lifeExp'][i])\n",
    "\n",
    "print(\"df_year_continent_lifeExp_sum : \", df_year_continent_lifeExp_sum)\n",
    "df_year_continent_lifeExp_mean = df_year_continent_lifeExp_sum/len(df_year_continent_lifeExp_row)\n",
    "print(\"df_year_continent_lifeExp_mean : \", df_year_continent_lifeExp_mean)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dae126f4-a517-4c45-9a9b-3b3818fbd75e",
   "metadata": {},
   "outputs": [],
   "source": [
    "multi_dataset = df.groupby(['year','continent'])[['lifeExp','gdpPercap']].mean() #두개이상도 가능\n",
    "multi_dataset"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "id": "11a1a524-561e-4ed5-8094-64f7959d6f28",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "year\n",
       "1952    142\n",
       "1957    142\n",
       "1962    142\n",
       "1967    142\n",
       "1972    142\n",
       "1977    142\n",
       "1982    142\n",
       "1987    142\n",
       "1992    142\n",
       "1997    142\n",
       "2002    142\n",
       "2007    142\n",
       "Name: gdpPercap, dtype: int64"
      ]
     },
     "execution_count": 85,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.groupby('year')['gdpPercap'].nunique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "id": "bf040d73-1f34-4f0e-8bd0-b2b72f9e303d",
   "metadata": {},
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt # 그리기!\n",
    "import seaborn as sns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "id": "b5ad9c6d-aa0f-4d9c-88aa-2cae98e62f90",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "df_year_lifeExp_mean = df.groupby('year')['lifeExp'].mean()\n",
    "list_year_life = list(year_life)\n",
    "plt.plot(list_year_life, '--d',color = 'red')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 111,
   "id": "0c2b8b84-24fe-4f38-8432-00b973165b10",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "df_year_gdp_mean = df.groupby('year')['gdpPercap'].mean()\n",
    "list_year_gdp = list(df_year_gdp)\n",
    "plt.plot(list_year_life, '--o',color = 'skyblue')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 112,
   "id": "3f5be37e-788e-4420-82aa-6275355994d3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "df_year_gdp_mean.plot()\n",
    "df_year_lifeExp_mean.plot()\n",
    "plt.grid()\n",
    "plt.show() # 값에 너무 차이가 크다"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 117,
   "id": "327c8634-7d28-4cc6-bef5-56ef2694d09e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 8 entries, 0 to 7\n",
      "Data columns (total 8 columns):\n",
      " #   Column      Non-Null Count  Dtype \n",
      "---  ------      --------------  ----- \n",
      " 0   Unnamed: 0  8 non-null      int64 \n",
      " 1   Name        8 non-null      object\n",
      " 2   Born        8 non-null      object\n",
      " 3   Died        8 non-null      object\n",
      " 4   Occupation  8 non-null      object\n",
      " 5   born_dt     8 non-null      object\n",
      " 6   died_dt     8 non-null      object\n",
      " 7   age_dt      8 non-null      object\n",
      "dtypes: int64(1), object(7)\n",
      "memory usage: 640.0+ bytes\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "scientists = pd.read_csv('dataset/copy of scientists_drop_csv.csv')\n",
    "scientists.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 119,
   "id": "a68b4b7f-fb67-4d83-858b-1ff0dd82654a",
   "metadata": {},
   "outputs": [],
   "source": [
    "ages = scientists['age_dt']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 121,
   "id": "6d9b7ba7-7203-4d13-b88f-cf7eedeec4ac",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0   1920-07-25\n",
       "1   1876-06-13\n",
       "2   1820-05-12\n",
       "3   1867-11-07\n",
       "4   1907-05-27\n",
       "5   1813-03-15\n",
       "6   1912-06-23\n",
       "7   1777-04-30\n",
       "Name: born_dt, dtype: datetime64[ns]"
      ]
     },
     "execution_count": 121,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "born_datetime = pd.to_datetime(scientists['born_dt'],format = '%Y-%m-%d')\n",
    "born_datetime"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 126,
   "id": "22bb6e65-e06b-4b7a-892e-0499e4fbbf1d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "no shuffle : \n",
      " 0    13779 days\n",
      "1    22404 days\n",
      "2    32964 days\n",
      "3    24345 days\n",
      "4    20777 days\n",
      "5    16529 days\n",
      "6    15324 days\n",
      "7    28422 days\n",
      "Name: age_dt, dtype: object\n",
      "shuffle : \n",
      " 0    28422 days\n",
      "1    32964 days\n",
      "2    24345 days\n",
      "3    22404 days\n",
      "4    20777 days\n",
      "5    15324 days\n",
      "6    16529 days\n",
      "7    13779 days\n",
      "Name: age_dt, dtype: object\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\JH\\anaconda3\\lib\\random.py:307: SettingWithCopyWarning: \n",
      "A value is trying to be set on a copy of a slice from a DataFrame\n",
      "\n",
      "See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
      "  x[i], x[j] = x[j], x[i]\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "\n",
    "print(\"no shuffle : \\n\", scientists['age_dt'])\n",
    "random.shuffle(scientists['age_dt'])\n",
    "print(\"shuffle : \\n\", scientists['age_dt'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 128,
   "id": "c20f51bf-9471-41a5-b1fb-d41b5f175e44",
   "metadata": {},
   "outputs": [],
   "source": [
    "import csv\n",
    "import numpy as np\n",
    "with open('dataset/copy of pulsar_stars.csv') as csvfile:\n",
    "    csvreader = csv.reader(csvfile)\n",
    "    rows = []\n",
    "    for row in csvreader :\n",
    "        rows.append(row)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 131,
   "id": "7d03787e-53dd-4e77-ad67-d24f52490555",
   "metadata": {},
   "outputs": [],
   "source": [
    "type(rows)\n",
    "data = np.asarray(rows)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 130,
   "id": "e03b7583-68d4-42d8-a94f-2364296334df",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "numpy.ndarray"
      ]
     },
     "execution_count": 130,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 133,
   "id": "1d009dff-7192-43d4-9fa9-6e5993a41ff0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(17899, 9)"
      ]
     },
     "execution_count": 133,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.shape"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "26185fbb-19bd-47dd-9293-b15838d5938f",
   "metadata": {},
   "source": [
    "##### 데이터를 80(학습용) : 20(테스트용) 으로 나눠주는 과정\n",
    "##### 검증데이터는 나중에."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 137,
   "id": "0331548b-286a-4904-b0a8-0d6fb7e13790",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "shuffle_map :  [    0     1     2 ... 17896 17897 17898]\n"
     ]
    }
   ],
   "source": [
    "shuffle_map = np.arange(data.shape[0])\n",
    "print(\"shuffle_map : \", shuffle_map)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 139,
   "id": "809b12f6-654d-4dba-8bab-479e0d9fe1c7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "shuffle_map :  [ 3515 12114   472 ... 15854  3712  8183]\n"
     ]
    }
   ],
   "source": [
    "np.random.shuffle(shuffle_map)\n",
    "print(\"shuffle_map : \", shuffle_map)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 141,
   "id": "843c4746-f003-42d2-8365-d1415b56682e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "14319\n"
     ]
    }
   ],
   "source": [
    "train_rate = 0.8\n",
    "train_dataset_count = int(data.shape[0] * train_rate)\n",
    "print(train_dataset_count)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 142,
   "id": "1e22ca99-f7a8-42ed-a515-22d16c6da991",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   dataset     x      y\n",
      "0        I  10.0   8.04\n",
      "1        I   8.0   6.95\n",
      "2        I  13.0   7.58\n",
      "3        I   9.0   8.81\n",
      "4        I  11.0   8.33\n",
      "5        I  14.0   9.96\n",
      "6        I   6.0   7.24\n",
      "7        I   4.0   4.26\n",
      "8        I  12.0  10.84\n",
      "9        I   7.0   4.82\n",
      "10       I   5.0   5.68\n",
      "11      II  10.0   9.14\n",
      "12      II   8.0   8.14\n",
      "13      II  13.0   8.74\n",
      "14      II   9.0   8.77\n",
      "15      II  11.0   9.26\n",
      "16      II  14.0   8.10\n",
      "17      II   6.0   6.13\n",
      "18      II   4.0   3.10\n",
      "19      II  12.0   9.13\n",
      "20      II   7.0   7.26\n",
      "21      II   5.0   4.74\n",
      "22     III  10.0   7.46\n",
      "23     III   8.0   6.77\n",
      "24     III  13.0  12.74\n",
      "25     III   9.0   7.11\n",
      "26     III  11.0   7.81\n",
      "27     III  14.0   8.84\n",
      "28     III   6.0   6.08\n",
      "29     III   4.0   5.39\n",
      "30     III  12.0   8.15\n",
      "31     III   7.0   6.42\n",
      "32     III   5.0   5.73\n",
      "33      IV   8.0   6.58\n",
      "34      IV   8.0   5.76\n",
      "35      IV   8.0   7.71\n",
      "36      IV   8.0   8.84\n",
      "37      IV   8.0   8.47\n",
      "38      IV   8.0   7.04\n",
      "39      IV   8.0   5.25\n",
      "40      IV  19.0  12.50\n",
      "41      IV   8.0   5.56\n",
      "42      IV   8.0   7.91\n",
      "43      IV   8.0   6.89\n"
     ]
    }
   ],
   "source": [
    "import seaborn as sns\n",
    "\n",
    "anscombe = sns.load_dataset(\"anscombe\")\n",
    "print(anscombe[:])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 143,
   "id": "61e95af6-a1f1-42cd-ae5e-e8e1e2e5e3d5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "x    9.000000\n",
      "y    7.500909\n",
      "dtype: float64\n",
      "x    9.000000\n",
      "y    7.500909\n",
      "dtype: float64\n",
      "x    9.0\n",
      "y    7.5\n",
      "dtype: float64\n",
      "x    9.000000\n",
      "y    7.500909\n",
      "dtype: float64\n"
     ]
    }
   ],
   "source": [
    "anscombe_1 = anscombe[0:11]\n",
    "anscombe_2 = anscombe[11:22]\n",
    "anscombe_3 = anscombe[22:33]\n",
    "anscombe_4 = anscombe[33:44]\n",
    "print(anscombe_1.mean())\n",
    "print(anscombe_2.mean())\n",
    "print(anscombe_3.mean())\n",
    "print(anscombe_4.mean())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 151,
   "id": "292055b4-254f-44df-9d24-dba4a336d993",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "dataset_1 = anscombe[anscombe['dataset'] == 'I']\n",
    "plt.plot(dataset_1['x'],dataset_1['y'],'o')\n",
    "plt.grid()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 152,
   "id": "dc77e9bc-5a41-47ca-a8e3-42feadbe98cf",
   "metadata": {},
   "outputs": [],
   "source": [
    "dataset_2 = anscombe[anscombe['dataset'] == 'II']\n",
    "dataset_3 = anscombe[anscombe['dataset'] == 'III']\n",
    "dataset_4 = anscombe[anscombe['dataset'] == 'IV']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 154,
   "id": "ce7b73cb-5c57-41c1-96ec-529f4dcb3429",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 4 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "fig = plt.figure() # 그래프를 그릴 준비\n",
    "axis1 = fig.add_subplot(2,2,1)\n",
    "axis2 = fig.add_subplot(2,2,2)\n",
    "axis3 = fig.add_subplot(2,2,3)\n",
    "axis4 = fig.add_subplot(2,2,4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 163,
   "id": "cf16f5c5-0d41-4b0f-8d0b-fec77fba778a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 4 Axes>"
      ]
     },
     "execution_count": 163,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "axis1.plot(dataset_1['x'],dataset_1['y'],'o',color ='black')\n",
    "axis2.plot(dataset_2['x'],dataset_2['y'],'o')\n",
    "axis3.plot(dataset_3['x'],dataset_3['y'],'o')\n",
    "axis4.plot(dataset_4['x'],dataset_4['y'],'o')\n",
    "fig"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 161,
   "id": "95f829fb-0e30-4da3-806a-ab82526bc27f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 4 Axes>"
      ]
     },
     "execution_count": 161,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "axis1.set_title(\"dataset_1\")\n",
    "axis2.set_title(\"dataset_2\")\n",
    "axis3.set_title(\"dataset_3\")\n",
    "axis4.set_title(\"dataset_4\")\n",
    "fig"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 158,
   "id": "20f40f5e-4cf6-4577-a917-161273a8cd8f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 4 Axes>"
      ]
     },
     "execution_count": 158,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fig.suptitle(\"Anscombe Data\")\n",
    "fig"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 164,
   "id": "8dee43a0-3000-4d4a-b66c-768939f904f5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   total_bill   tip     sex smoker  day    time  size\n",
      "0       16.99  1.01  Female     No  Sun  Dinner     2\n",
      "1       10.34  1.66    Male     No  Sun  Dinner     3\n",
      "2       21.01  3.50    Male     No  Sun  Dinner     3\n",
      "3       23.68  3.31    Male     No  Sun  Dinner     2\n",
      "4       24.59  3.61  Female     No  Sun  Dinner     4\n",
      "<class 'pandas.core.frame.DataFrame'>\n"
     ]
    }
   ],
   "source": [
    "tips = sns.load_dataset('tips')\n",
    "print(tips.head())\n",
    "print(type(tips))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 165,
   "id": "5212cd2f-0fea-40c6-b696-3df5ad1f5ef4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>total_bill</th>\n",
       "      <th>tip</th>\n",
       "      <th>sex</th>\n",
       "      <th>smoker</th>\n",
       "      <th>day</th>\n",
       "      <th>time</th>\n",
       "      <th>size</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>16.99</td>\n",
       "      <td>1.01</td>\n",
       "      <td>Female</td>\n",
       "      <td>No</td>\n",
       "      <td>Sun</td>\n",
       "      <td>Dinner</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>10.34</td>\n",
       "      <td>1.66</td>\n",
       "      <td>Male</td>\n",
       "      <td>No</td>\n",
       "      <td>Sun</td>\n",
       "      <td>Dinner</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>21.01</td>\n",
       "      <td>3.50</td>\n",
       "      <td>Male</td>\n",
       "      <td>No</td>\n",
       "      <td>Sun</td>\n",
       "      <td>Dinner</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>23.68</td>\n",
       "      <td>3.31</td>\n",
       "      <td>Male</td>\n",
       "      <td>No</td>\n",
       "      <td>Sun</td>\n",
       "      <td>Dinner</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>24.59</td>\n",
       "      <td>3.61</td>\n",
       "      <td>Female</td>\n",
       "      <td>No</td>\n",
       "      <td>Sun</td>\n",
       "      <td>Dinner</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>239</th>\n",
       "      <td>29.03</td>\n",
       "      <td>5.92</td>\n",
       "      <td>Male</td>\n",
       "      <td>No</td>\n",
       "      <td>Sat</td>\n",
       "      <td>Dinner</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>240</th>\n",
       "      <td>27.18</td>\n",
       "      <td>2.00</td>\n",
       "      <td>Female</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Sat</td>\n",
       "      <td>Dinner</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>241</th>\n",
       "      <td>22.67</td>\n",
       "      <td>2.00</td>\n",
       "      <td>Male</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Sat</td>\n",
       "      <td>Dinner</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>242</th>\n",
       "      <td>17.82</td>\n",
       "      <td>1.75</td>\n",
       "      <td>Male</td>\n",
       "      <td>No</td>\n",
       "      <td>Sat</td>\n",
       "      <td>Dinner</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>243</th>\n",
       "      <td>18.78</td>\n",
       "      <td>3.00</td>\n",
       "      <td>Female</td>\n",
       "      <td>No</td>\n",
       "      <td>Thur</td>\n",
       "      <td>Dinner</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>244 rows × 7 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "     total_bill   tip     sex smoker   day    time  size\n",
       "0         16.99  1.01  Female     No   Sun  Dinner     2\n",
       "1         10.34  1.66    Male     No   Sun  Dinner     3\n",
       "2         21.01  3.50    Male     No   Sun  Dinner     3\n",
       "3         23.68  3.31    Male     No   Sun  Dinner     2\n",
       "4         24.59  3.61  Female     No   Sun  Dinner     4\n",
       "..          ...   ...     ...    ...   ...     ...   ...\n",
       "239       29.03  5.92    Male     No   Sat  Dinner     3\n",
       "240       27.18  2.00  Female    Yes   Sat  Dinner     2\n",
       "241       22.67  2.00    Male    Yes   Sat  Dinner     2\n",
       "242       17.82  1.75    Male     No   Sat  Dinner     2\n",
       "243       18.78  3.00  Female     No  Thur  Dinner     2\n",
       "\n",
       "[244 rows x 7 columns]"
      ]
     },
     "execution_count": 165,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tips"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 166,
   "id": "47a74aab-75e3-4a11-8f00-1623ca113d3a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 244 entries, 0 to 243\n",
      "Data columns (total 7 columns):\n",
      " #   Column      Non-Null Count  Dtype   \n",
      "---  ------      --------------  -----   \n",
      " 0   total_bill  244 non-null    float64 \n",
      " 1   tip         244 non-null    float64 \n",
      " 2   sex         244 non-null    category\n",
      " 3   smoker      244 non-null    category\n",
      " 4   day         244 non-null    category\n",
      " 5   time        244 non-null    category\n",
      " 6   size        244 non-null    int64   \n",
      "dtypes: category(4), float64(2), int64(1)\n",
      "memory usage: 7.4 KB\n"
     ]
    }
   ],
   "source": [
    "tips.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 167,
   "id": "2b6d0301-1f66-4c14-a2bb-e7927700b69b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>total_bill</th>\n",
       "      <th>tip</th>\n",
       "      <th>size</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>244.000000</td>\n",
       "      <td>244.000000</td>\n",
       "      <td>244.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>19.785943</td>\n",
       "      <td>2.998279</td>\n",
       "      <td>2.569672</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>8.902412</td>\n",
       "      <td>1.383638</td>\n",
       "      <td>0.951100</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>3.070000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>13.347500</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>2.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>17.795000</td>\n",
       "      <td>2.900000</td>\n",
       "      <td>2.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>24.127500</td>\n",
       "      <td>3.562500</td>\n",
       "      <td>3.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>50.810000</td>\n",
       "      <td>10.000000</td>\n",
       "      <td>6.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       total_bill         tip        size\n",
       "count  244.000000  244.000000  244.000000\n",
       "mean    19.785943    2.998279    2.569672\n",
       "std      8.902412    1.383638    0.951100\n",
       "min      3.070000    1.000000    1.000000\n",
       "25%     13.347500    2.000000    2.000000\n",
       "50%     17.795000    2.900000    2.000000\n",
       "75%     24.127500    3.562500    3.000000\n",
       "max     50.810000   10.000000    6.000000"
      ]
     },
     "execution_count": 167,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tips.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 169,
   "id": "3e468119-5828-44b5-9cdb-3d0b5d24d4c5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count     244\n",
       "unique      4\n",
       "top       Sat\n",
       "freq       87\n",
       "Name: day, dtype: object"
      ]
     },
     "execution_count": 169,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tips['day'].describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 203,
   "id": "4d9c702f-adea-46a2-827f-67a152bec701",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "fig = plt.figure()\n",
    "axis1 = fig.add_subplot(1,1,1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 212,
   "id": "59a9ee33-830c-4f3b-b6c1-b8f9cdb52d69",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "19.785942622950824"
      ]
     },
     "execution_count": 212,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tips['total_bill'].mean()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 213,
   "id": "c174fc89-5618-4f94-ad24-7f25ca80dc16",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "fig = plt.figure()\n",
    "axes1 = fig.add_subplot(1,1,1)\n",
    "\n",
    "axes1.hist(tips['size'], bins = 11)\n",
    "axes1.set_title('History of size')\n",
    "axes1.set_xlabel('Frequency')\n",
    "axes1.grid()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 214,
   "id": "33d9c792-dbcd-4292-bc1d-267f951b21e8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "execution_count": 214,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "axes1.hist(tips['total_bill'], bins = 'auto')\n",
    "axes1.set_title('History of Total Bill')\n",
    "axes1.set_xlabel('Frequency')\n",
    "axes1.grid()\n",
    "fig"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 215,
   "id": "c659aeb4-5b8d-4317-a447-284dfadac2a1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "fig = plt.figure()\n",
    "axes1 = fig.add_subplot(1,1,1)\n",
    "\n",
    "axes1.hist(tips['day'], bins = 7)\n",
    "\n",
    "axes1.set_title('History of day')\n",
    "axes1.set_xlabel('Frequency')\n",
    "axes1.grid()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 218,
   "id": "1116b3aa-caf0-4e45-87b0-5df9ff4280d8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'Thur', 'Sun', 'Sat', 'Fri'}\n",
      "4\n"
     ]
    }
   ],
   "source": [
    "print(set(tips['day']))\n",
    "print(tips['day'].nunique())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 219,
   "id": "3b5155d9-7021-4330-8964-4fab739e8746",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "fri_count :  19\n"
     ]
    }
   ],
   "source": [
    "fri_count = []\n",
    "for i in range(len(tips['day'])):\n",
    "    if tips['day'][i] == 'Fri' :\n",
    "        fri_count.append(i)\n",
    "print(\"fri_count : \", len(fri_count))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 220,
   "id": "e3b88222-548a-4a35-9386-a9e1cb7a6488",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "19\n"
     ]
    }
   ],
   "source": [
    "fri_count = 0\n",
    "for i in range(len(tips['day'])):\n",
    "    if tips['day'][i] == 'Fri' :\n",
    "        fri_count += 1\n",
    "print(fri_count)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 230,
   "id": "50b220f7-e986-40de-81b6-730bae81041a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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6Tj+a0qpVQDm76FKdRwdHOTKwYOcfeYZrhw8eN2+ss997nOcP3+e3bt389nPfpZLly7R1WVUzHvqqaf42Z/9Wd7//vdzww038IUvfMGQIRrlgx/8ILfccgtdXV18+9vTK8u9/vrr3HLLLdx55538+Z//eeH4pUuX2LdvH7fddhu33XYbr7zySkGOI0eOsHv3br785S/Pet7AwADvec972L17N11dXRw5cgSAAwcOcOedd3Lbbbfx0EMPEYlE+NM//VP6+/u59957uffee69rnARBWDjNXV2kJyZIRyLoXI50JEJ6YoLmrkVV5ZzOTHeDcv0wfcb//wKfM//+HPC/Smnnemf8kYEBfXr/fuOOefCgvvDd7+rT+/fryMBAyW1MZepsvPj1k08+qTs7O/XIyIiOxWL6pptu0q+99pp+7rnn9C/90i8VrhkbG5vW7k033aQPHz6stdb6iSeeKLQZjUZ1PB7XWmt95swZnR+TqTP+2c77gz/4A/3FL35Ra611JpPR4XBYDw8P63379ulIJKK11vr3f//39Re+8AWttcz4q4Xo/2K1RagaU3WPDAzo3hde0Ge+/W3d+8ILi7JXzDLjX8pwzm8B9wCtSqk+4HeA3weeUUr9ItALPLRU/RdTvFACFH4He3rKFh41lfe97320tLQA8NGPfpSXXnqJn/mZn+GJJ57gN37jN/jQhz7Evn37Jl0zPj7O+Pg4733vewF49NFH+ad/+ifA2LD2q7/6q7zxxhtYrVbOnDkzY7+znbd3714+8YlPkE6nefDBB9m9ezc/+tGPOHnyJHfddRcAqVSKO++8c0nGQxCEheHt7Fwy+7Rkhl9r/fOzvPXTS9XnbCSCQVymEc5j83hIjI4uWZ9Twx6VUmzfvp1jx47x/e9/n89//vM88MAD/PZv/3bhHK31rOGSX/7yl+no6ODNN98kl8vhcrkWdN573vMefvzjH/O9732PRx99lM9+9rM0NTXxvve9j29961tl0loQhOVAXeTqcTU3k4nFJh3LxGK4mpsX3abP52NiYmLW91944QWCwSDxeJznn3+eu+66i/7+fjweD7/wC7/AE088wfHjxydd09jYiN/v56WXXgJg//79hffGx8dZtWoVFouFb3zjG2Sz2RnlmO28y5cv097ezic/+Ul+8Rd/kePHj3PHHXfw8ssvc+7cOQBisVjhCWE+/QRBWL7UheFfioWSlpYW7rrrLrq6uvjsZz877f27776bRx99lN27d/NzP/dz7Nmzh+7ubt71rnexe/duvvSlL/Fbv/Vb0677yle+wq/8yq9w55134na7C8d/+Zd/ma9//evccccdnDlzplCw4eabb8Zms3HLLbfw5S9/edbzDh8+zO7du7n11lv5zne+w6c//Wna2tp46qmn+Pmf/3luvvlm7rjjDt5++20AHn/8cT7wgQ/I4q4grECWRc3dPXv26KmFWE6dOsWNN95YchtLuf15Kk899RRHjx7lz/7szxZ8bS3n6smz0LFfCPVciANE/3rWf4kKscwYx79sk7QtlKVcKBEEQVhO1I3hryQf//jH+fjHP15tMQRBEGZkWfv4l4ObaqUhYy4Iy59la/hdLhejo6NiiCqINvPxzxZKKgjC8mDZunrWrl1LX1/fissNn0gkatqw5itwCYKwfFm2ht9ut6/IKlCHDx/m1ltvrbYYgiCsYJatq0cQBEFYHGL4BUEQ6gwx/IIgCHWGGH5BEIQ6Y9ku7gqCINQylUwTs1Bkxi8IglBmooODXD10iEw8jqulhUw8ztVDh6678l+5EMMvCIJQZoqLPymLBXtDA3afj2BPT7VFA8TwC4IglJ1EMIjN45l0zObxkAgGqyTRZMTwC4IglJmlKP5UTsTwC4IglJmlKP5UTsTwC4IglBlvZydr7rsPm9tNYnQUm9vNmvvuq5moHgnnFARBWAJqufiTzPgFQRDqDDH8giAIdYYYfkEQhDpDDL8gCEKdIYZfEAShzhDDLwiCUGeI4RcEQagzxPALgiDUGWL4BUEQ6gwx/IIgCHWGGH5BEIQ6Qwy/IAhCnSGGXxAEoc4Qwy8IglBnVMXwK6X+q1LqLaVUj1LqW0opVzXkEARBqEcqbviVUmuA/wLs0Vp3AVbgY5WWQxAEoV6plqvHBriVUjbAA/RXSQ5BEIS6Q2mtK9+pUp8GvgTEgQNa60dmOOdx4HGAjo6O259++unKClklIpEIDQ0N1Rajaoj+on+96r8Uut97773HtNZ7ph6vuOFXSjUB3wH+PTAGPAs8p7X+5mzX7NmzRx89erQyAlaZw4cPc88991RbjKoh+ov+9ar/UuiulJrR8FfD1XM/cFFrPay1TgN/C7y7CnIIgiDUJdUw/L3AHUopj1JKAT8NnKqCHIIgCHVJxQ2/1vpV4DngONBtyvDVSsshCIJQr9iq0anW+neA36lG34IgCPVOVQy/IAj1TXRwkGBPD4lgEFdzM81dXXg7O6stVt0gKRsEQago0cFBrh46RCYex9XSQiYe5+qhQ0QHB6stWt0gM35BECpKsKcHu8+H3YxZz/8O9vSATUxSJZAZvyAIFSURDGLzeCYds3k8JILBKklUf4jhFwShoriam8nEYpOOZWIxXM3NVZKo/hDDLwhCRWnu6iI9MUE6EkHncqQjEdITEzR3dVVbtLpBDL8gCBXF29nJmvvuw+Z2kxgdxeZ2s+a++ySqp4LISoogCBXH29kphr6KyIxfEAShzhDDLwiCUGeI4RcEQagzxPALgiDUGWL4BUEQ6gwx/IIgCHWGGH5BEIQ6Qwy/IAhCnSGGXxAEoc4Qwy8IglBniOEXBEGoMyRXjyAIQpmp9dKSYvgFoc6odaO03MmXlrT7fEZpyViMq4cO1VQGUnH1CEIdIfVul57i0pLKYsHe0IDd5zNKS9YIYvgFoY5YDkZpubMcSkuK4ReEOmI5GKXlznIoLSk+fmFFUm0/drX7n428UbI3NBSO1ZpRWu40d3Vx9dAhwLipZmIx0hMTtO/dW2XJ3kFm/MKKo9p+7Gr3PxdS73bpWQ6lJWXGL6w4iv3YQOF3sKenIl++avc/F3mjFOzpITE6iqu5mfa9e6su10qj1ktLiuEXVhyJYBBXS8ukYzaPh8ToaF30Px+1bpSEpUdcPcKKo9qLa9XuXxDmQwy/sOKoth+72v0LwnyI4RdWHNVeXKt2/4IwH+LjF1Yk1fZjV7t/QZgLmfELgiDUGWL4BUEQ6gwx/IIgCHVGVXz8SqlG4GtAF6CBT2it/6UasgjCcqdW00MItUu1Zvx/Avyz1noHcAtwqkpyCMKyppbTQwi1S8Vn/EopP/Ae4OMAWusUkKq0HIJQDco9O6/l9BBC7aK01pXtUKndwFeBkxiz/WPAp7XW0SnnPQ48DtDR0XH7008/XVE5q0UkEqGhKHNivVFp/XOZDNl4nFwmg8Vmw+p2Y7EtzXwol8mQDodRVivKYkHncuhsFrvfX+hzofonQ6EZ5c1lMjibmsome6Wo5///pdD93nvvPaa13jP1eDUM/x7gX4G7tNavKqX+BAhrrf/7bNfs2bNHHz16tGIyVpPDhw9zzz33VFuMqlFJ/YtL5BWnz12qzVZXDh4kE49PSomcjkSwud2su/9+YOH6l9LmcqKe//+XQnel1IyGvxo+/j6gT2v9qvn6OeC2Ksgh1DmVrka1FEVQJD2EsBgqbvi11oPAFaXUDeahn8Zw+whCRal0NaqlSN4m6SGExVCtlA3/GdivlHIAF4DHqiSHUMdUuhrVUlVmkvQQwkIpyfArpTqBd2HE3L9mztoXjdb6DWCa30kQysl8ETSVLpEnRVCEWmFew6+U+iXgt4FDgAL+t1Lq97TWf7XUwgnCYileuHW1tJCJxbh66NAkN0g1DPF8s/NcJsOVgwdlM5awpJQy4/8scKvWehRAKdUCvAKI4RdqllLj22vJTRIdHCQdDpOx22e9WQlCOShlcbcPmCh6PQFcWRpxBKE8VHrhthwEe3pQVmvFooyE+qWUGf9V4FWl1N9j+Ph/FviJUuq/AWit/2gJ5ROERVHphdtykAgGUW73pGO1VKtXWDmUMuM/DzyPYfQB/h4YAHzmjyDUHMsxvt3V3IzO5SYdq/WblbA8mXfGr7X+QiUEEYRyshwjaJq7utCvvGLsvK1AlJFQv8xq+JVSf6a1/lWl1D/wzmy/gNb6I0sqmSBcJ7W0cFsK3s5O7H4/Nlg2NytheTLXjP8/AL8K/EGFZBGEusdis7GuTnPVCJVjLsN/HkBr/aMKySIIgiBUgLkMf1s+cmcmJJpHEFYGw93d9B04QOzaNTwdHax94AHadu2qtljCEjKX4bcCDRi7dYU5kNJ3K5dKfLbFfaTdbqKDgxX7/xnu7ub0k09iDwTwrFpFKhzm9JNPwmOPifFfwcxl+Ae01r9XMUmWKaWkBhCWJ5X4bKf2oSORiv7/9B04gD0QwGUWbcn/7jtwQAz/CmauOH6Z6ZdApXO6C5WjEp9tsKeHXDbL+PnzDL7yCtlkklw2W7H/n9i1azj8/knHHH4/sWvXKtK/UB3mmvH/dMWkWMYkgkFcLS2Tjsluy/JQipul3K6Y4vZCp07RfNNNk3b/Fn+25eg7fOkSkStXsHk82H0+dC7H+LlzZJPJBeu5GHk8HR2kwmFcTU2kIxHiw8MkRkdxBAIVdTnNxUL1qgXXay3IMBezzvi11rWb1KSGWIriGsI7LpBMPG64WeJxrh46RHRwcEHnXE+fFoeD4WPHSIZChXPyn225+k6Nj4PFgs3tRlksKIsFLBbjeAXGYu0DD5AeHydy9SrjFy6QHB8nl83SuGPHdY1luVioXuX+n6iEzNWgGqUXVxTLMTXAcqAUN0u5XTFT22u8wSgSFzpzZtpnW66+7X4/5HJk4nG01kbKhlzOOF6BsWjbtYsbHnuMTCxm1O71+Vh7//207NxZEy7LhepVC67XWpBhPsTwXydS+m5pKCW7ZrkzcE5tz9XUROvtt5NNJqd9tuXqO7BpE4GtW7E4naTDYZTFQmDrVgKbNs0q10x9XY88bbt2sXrfPnZ+4hNsefBBAhs3LlqfcrNQvWohK2styDAf1Sq9uKJYbqkBlgOlZNcsdwbOmdqzOZ2svusu1t1//4LlK4Xmri7iQ0M0btmCzeMhFIlgyWQmPTFWYixqNZvpQuWqBT1qQYb5kBm/UJOU4kIrt5ttIe2Vq++pT4zKYpn2xFiJsahVl+VC5aoFPWpBhvkQwy/UJKW40MrtZvN2dtK0axdjZ87Q+4MfMHbmDE27ds3YXjn79nZ2su7++9n28MPYfb5pbVRiLGrBZRkdHCQ9McHZZ57hysGDhaiihchVC3rUggzzIa4eoWYpxYVWTjdbdHCQUHc3jdu307p7N5lYjFB3N562tlmNf6W+zJUYi6nXRwcHK1b/Nx8Jo73eGTfLLaTfWnC91oIMcyEzfkEwWQ7RGJWi0iGJ+bHPh7TW89hXAjH8gmCyHKIxKkWlb4Iy9pVFDL8gmMhmvHeotCGWsa8sYvgFwWQ5RGPAO7734kXQclNpQ5wfe53L1fTYrxTE8AuCyXKIxqiU773SN8H82CuLpWbHfiUhUT2CUEStR2MU+96Bwu9gT09Z5a5GsXpvZyd2n49tH/7wkvUhGIjhF4RlRCWzwdb6TVBYPGL4hZKplVSzla6KVUtpdZdDOgCh9hEfv1AStZJqdinlyC+avvW1r9Hzla8QHRioubS6y2UBWqhtxPALJVErm5uWSo7iG0pqYgKsVsJmfvpa2ky0HBaghdpHXD1CSSylb3khxcaXSo7iG0omEsEZCJBNJpno7cXV1LSkVdUWWmxdfO/C9SIzfqEklique6rrRudyc7pVlkqO4g1Ldp+PbDKJ1eUiMzFRtj5mYqH6C0I5kBm/UBLNXV1cPXQIMGbYmViM9MQE7Xv3Tjt3IQujU8MTlcVScKt4OzunteXq6CDU3V2SHAuheNHUt349oydOkEkkcPh8BT/69fYxE/PpLwhLgcz4hZIo1be80MXXmVIDZJNJBl5+ecZF1lB3N027dpXdx128aOoIBPBv2WKUQPT5ltSPLjlqhGpQtRm/UsoKHAWuaq0/VC05qs3UGW2uSv2WEq6Yfz/Y00P40iVG3nwTu99PYNOmwvXFM9hEKMREby+JkRFCZ8/SvHMnaD2pv6nhiblslv4jR8imUkSuXkVrTSaZxOb14mpqAiBx7dq0iljXq9/UDUveVato2b2bxLVrJILBwsLuTDe6/iNHCJ48iQKadu5k9b59Jd8kVmJ4Zq2GwgrvUM0Z/6eBU1Xsv+rMNDtOh8NL7t9dbEhk/rrowACRK1dIRSJE+/qIDgwUrs/PYBOhEMHubnLJJBank7HTpxk5fhxlsUzqb2p4YiYWIz44iLutDZTC6nAQHxpi9ORJoLTZ8GL1Ky6I0tzVRai7e842ooODXHj+eUaOH8fqdGJxOhk5fpwLzz9f8mc4VX+dyy3r8MxaCfsV5qYqhl8ptRb4IPC1avRfK8wUmqis1iUPG1xsSGT+usToKDaPpxDtEh8dLVyfn8FO9PZidbmwud3EBwZwNjXhaGwk0tc3qb+pLqRcOk1g+3bcra3YPR6UUti8XqK9vQBE+/uJXLkyZ4KycoR8ltJGsKeHZCiEo7ERu8eD3ePB0dhIcmys5L5KKb24nKiVsF9hbpTWuvKdKvUc8P8APuCJmVw9SqnHgccBOjo6bn/66acrK2QFSIZCWGyTvW2JXA5HLofTdGtUql+AXCYzZ7/569KRCMpqLRzX2Sz2hgZymQx2n490OEwmkcBis6FzObLxOFa3G2WxFM6drb9wMIgtlTLOzeXIJpOF9+w+H5lYDJvHg9VuN2bI2Sx2v3+SPovVb6FjlAyFyCYSk8YiPx5Wl2tRn2EkEqGhyO2z3LjesV/u+l8PS6H7vffee0xrvWfq8Yr7+JVSHwKGtNbHlFL3zHae1vqrwFcB9uzZo++5Z9ZTly1XDh4kE49P8u+eDIe50edj3RLqO1O/6UgE2zz95q8bv3aNbDKJze0mE49jcTppbGgwrr//fqKDg5zZv59kKISrtZV0JILFbgfA6nTS2tk5a38/+Lu/w//mmzgaG7E6nSSCQSK9vbg7OvC0t+Nub6ehyICkIxFsMKmdxeq30DG6cvAg195+G2WxYHO7AcjE42it6dizZ1Gf4eHDh1nO/+vXO/bLXf/roZK6V8PVcxfwEaXUJeBp4D6l1DerIEfVmWn7vc5ml9y/u9ht//nr8jVRE6EQmVgMd0vLpOu9nZ1sf+QR7IEAodOnGenuZuCVVxi/eJGGtWvn7M/u89GwYQNaa1LhMDaPh4477mD3f/2vNKxbh3f16knnz+TzL0dag1LaaO7qwtnURGpsjHQsRjoWIzU2hrOxcdn66K8XSSmxPKj4jF9r/Xng8wDmjP8JrfUvVFqOWmCm1Ld2t3vJ/buLSbmbj9RIRaOkw2HsjY2oXA6734931appkRux4WHCFy8aj/iBAGmHg8ToKOErV2jbtWvW/iw2G5sffHDGqJBSI2CuR7/iPudrw9vZyeYHH5wU1dN6220LiupZaVQjnbOwcGQDV5WZuv3+/OHDVel3LvKRGnafj8DmzYVNU3MtQvYdOICno6MQggmQCIVQudy8oZizybaQTWSL1S//NHP10CHW3HdfSbJue+ihkvqpRZYi9FJSStQ+Vd3ApbU+XM8x/MuFxURqxK5dw+H3Tzrm8PuJXbu2aDmWKkFZvUaiSOhl/SIzfmFeFpMYzdPRQSocnjTjT4XDeDo6rkuW651NFs9wUQqAoddew7NqFf4NGwqRJ0uZlK1WqFQ1L6H2kJQNwrwsJjHa2gceID0+TiIUIpfNkgiFSI+Ps/aBB5Za3FkpnuEqi4WR48cZOX4cW0MDqXCY0RMnSIZCwPLfPVsK4UuXGDt3joGXXmLkzTdJhkKSLqJOkBn/CqccPtzZfOsNGzdy5eBBxi9eJNrfb4Txud007dxJ444dNN10E9f+9V8ZTyQIbN3KDY89RtuuXXPKNpP8/UeOEDp5Eg1416zBGQhMS/0w3N1N34EDxK5dw9PRwdoHHpjUF0ye4Y6fPw92O8mREVIDA1jtdpzNzYQvX6bRbl+ypGy1QnRwkEhvL1ithRTUoydO4N+yBe+qVdUWr2rUS7oJmfGvYMrlw53Jt960axeh7m6iAwOMnTnD2LlzxAcHyWYyDLz0Ej1/8RdYHQ62fexjbHv4YZq2bcPT1javbLlMZtI5+ZQIFqcTnclw9YUXGHjppUmpH3oPH+b0k0+SikTwrFpFKhLh9JNPMmxm8cxTnBAtNjhIfHAQLBZsTifeVatIjo4yfuFCXRQ3Cfb0ENi2DQWFFNRaKcbPnavb0Mt6WvOQGf8ypNRZSTl9uMW+9fwGrUQoRGpigkwkgisQACATiZBLp8ml0yRGR2lYu3bGfmeTLRuPT5I/OTaGo7ERm9tN7No17IEAuXSaSF8frbfcAsDF73wHV2trYT0h/7vvwIFJs/7icNCM2Y/CeIpxt7airFYcDQ1zRvKslBlhIhjEu3o1Nq+Xid5e0uEwDp8Pu8+3LPUpB/W05iEz/mXGQmYlS5HyN99/MhQy+o9EiA8Pk81msdjtZOJxctksSinSZhGTmfqdTbb8jD86OMjAyy8TPHmS6MAAqUiEbDyOzesll80W2rZ5PMSHhkqKICreXGRzu8mlUmSiUdytrcaNIJfDYd7A5tJ9JcwI8zdBV1MTbbfcwqq776Zx2zYCmzZVW7SqUU8pssXwLzMWEnq4FNWq8v27WlvJpVI4/H6UzUYyGCSXTmNzu7FYrWitsft8s/Y7m2wWm61gYC0OR2F2Hrl8GZQiE41isVoLbWdiMdzt7aTC4UltTY0gKt6ANnbmDBpoWLeukHff6nQS2LoV/8aN8+q+EsI+ZYftdJaqulstIoZ/mbGQWclSfLnz/fvWrzdm4D4fNq+X1Pg46UgErFYSoRDxoSEmenvpf+kl+n74Q4aOHsVVZIhnk83qdhcMbOMNN+BoaECnUuS0JptMkh4fx2K3T0r9sOnnfq4QQZQMhxnp7ma0pwd7IEB0cHDSTD2weTON27fj37gR75o1tN5yC53vfjeBLVuwWK1zjs1KmhFK0fbp1NPNUHz8y4yFFO4odfv8gvzWSnHtJz9BZzIomw0r4Glrw+ZyYfV4iA8OEtiyBWdrK8E33iA2MEDTjTfi37SJUHc3nra2wnrBTLL19fTQ//LLKKWw+/003ngjMb+fid5esuk0a973PpyBADqXw+Z2F/Rxt7Rw4W//ltETJ3C1tLDh/e/H097O1UOHUHb7NN9tw5o1ZBKJguErJbXASiuaIjtsJ1NP6SbE8C8zFpK2AOb/cs+VrgCYVu82MTpq5OrJL+aOj9O4fXshv04+M+Pwm2/SdOONgJGRMz9DL14oy8uWv/Fc/Id/IO714slksHq95JJJor29NO/aRestt2Bzu2ddeG3btYvEtWu033bbJMMMMHT8OKvvvnvSMZvHQyYenzclQzELHfulZKUsMtca9XIzFFfPMqPcj+iz+a37jxyZtpB54dlnsXu9tO/di83lQqfT2AMBXC0teDs7J7lCMhMTWF0urE7npIXYqW6RYjdMdGCAXDrN2JkzBE+eJBWNFqp3lfLIPZsrRkFZfLfFYz984gS9Bw7Q/y//wpn9+6eFji4lK2mRWagOMuNfhpRzVjJbOoah48cnzZ7tDQ3kcjniIyM0rF2Ls6mJZChE+PJlhl57zQihVIpMLEY2nSY2MkLm0iWsLldhQ9BMxjZ/48mm04TPnkVt2oSrtZVsMkl8cJBcUxN2j6ekm9tsrpimnTsn3XyuZ6bu7ewkNjxM7Pvfx9XaisPvJxUOc/rJJ2HKBrWFEh0cJD0xwdlnnll0mG7+tzwJCHMhhr+OmMk9MJuxzMe3F+NqbiZp5q9JhkKMnjiBVgpPZyeZeJzE6CipiQlSwSAOv5/0+Djp8XGSXi+Rvj4sVus0Y5u/8Yx1d2Pz+0kCVocDnc3i37QJncvRUaKfdTZXzCS3VRl8t30HDhhPOvPsG1gI+Vm89nqnudymyjnbzXr8wgXiQ0Mzuu3E+AvFiOGvE/KGJZfNEh8eZuTECfp//GNW3XcfkatXSYZCJMfGSIXDZNNpsskkI93dZFMpFOBobMTV2orFaiUdiRC+fJl0PE4iFMLd3EwqFiOXSDDR24vd68XicJDTmkQwSLivj5ETJ2jbvZt0LIZ/48aC2yZ46hQTly6RGB3F3txsyGeGhoZOnyaXSuHfsYPX//AP50zHAMZsvGnXrmmpG4rXFMpB7No1PFPSGjj8fmIDA5PGe6Z0FLPNxvOzeAUFl1v++FS5Z7tZp8NhvJ2dVd+AtFDdS7leblzlRXz8dUKwp4dcNkv4wgVy6TTutjawWun93vdITUyQjsWI9veTikSIj4yQDIWIXL1KIhg0jg0PE7l4EWtDA5lEgvCFCyRGRvB0dmLz+Zg4f55oXx/ZVAp3ayuxwUEysRjWfCx+JEL4wgVCZ84QHRjgwvPP8/Y3vkFybAy0RtlspEZG0JkM8WvXsFgsRrF2v59z+/cTHRqaMx0DGAYj1N1N4/btrP83/4bG7duNtBJl9n3nM48WU7xvYCYf/IXnn+fC88/P6pcvR5iuIxCoerjpYnQvJpfJyPpFBRDDXyckgkHiw8OGMXW7UUrhDARIjo6iMxlcLS20dHXhaW3FYrGgMxnsHg8WqxWrzQZa42xuxu5w4Gpqwr9xIw3r1+NpbSU5MmLM8p1OlFIkgkF0JmPE5btc6Gz2nUXWaJTE6CjJsTHCFy7g7eykcft2PB0dRvH0XI6GNWto2bULb3s7ZLM4/H50KoXFasXV1IQ9EKDvwIFpOpaywSo6OMiVgwc5+8wzXDl4cFEGZb7MozPJkRwbIxkKzSrbQjYPzbbA79+4seobkGbU3XyaLGXjWzYeXzGb5GoZcfXUCa7mZkZOnDBm+ibZZBJsNnLptGHo/X4jZbFSZNNpLFYrNpvNSGmQTKLsdiMHTzCIIxAgFQ6TicdJmztuyeXwmCGfOpsll0qB1uRSKZxNTeS0LtwQtNZkolGsTifKYqH5xhvxrl3LgMVCNp3G6nTSuG0b4xcv4mhsLOTWgclulWK3QPDUKZpvummSC6Q4r/5coasLcSW07doFjz1muJQGBvB0dLD5ox8tuJ9m8sHnUqlp7RTLll+f0F4vOpdbdJhutcNNZ9Q9nZ523mz1DnKZDLYp6TfqoTZCpRHDXyc0d3XR/+MfkxwbK6ThzcbjeDs6sNjtWN1usuaGJq01VrsdcjmUxUIum8VitWKxWLDY7UZMf3MzVqfT+EJqDYBn1Spczc24W1sZOn4clEJDobiJRSmUzYbd5zM2T3m9ZJNJbG43AFabDYvdjt3rJT0xwURvL1aXi/TEhJGK2STvVplqyK1OJyPHjtG2d29hwbV4xlvOJFxtu3bNupA7kw/e4nAUxilPsWz5Wfzl115b9AJ0LWxAmlF3u71Q9CbPbE8iFpttRW2Sq1XE8K9QZlog2/zQQ1x47jkSIyM4W1rwrl5NOhoFwO71Mn7uHMrhQFmtWD0eMubMPB2N4vD5sNjtOJuaCot18aEhAlu24F27lpFjx9DpNA1r1xq5dfr7cbe3k0skyGazhjvITO/gamkhHY2irFZSwSDaNIixgQF0ezup8XHCySQWl4tsOk1ydBRXWxu5bJZUOEx6fJzNH/3oNEPetH07Q6+9xtjp03S8613TZryLqSS2GGaKLnI2NgIYCeJmmY17Ozux+3xs+/CHF913tTcgzai7eROeS/c8Vreb9NDQpOtXem2EaiCGfwUyWwTP5oceoutTn5o14iKTSBQiQ1LhMIlgsFCRyrNqFR179rB6376CYcnPLkNnzxIbGSE9MUF8ZISOO+6g61OfYuzttxk6etRwDW3bhqelhYY1a/CuWlXot7jIitXtxmK349+61QgFjURQuRyte/fidLunuVXOnjo1yZA7m5pou/12gm+9NeOMt1IpF2aaeW9+8MHCOK/kdADXq7vFZqv6U0s9IIZ/BVIcwWN1uXC3tZEcG+PCc8/R9alPzZimwNvZyboF9lPYzNTXR8PatYXNTKG33qL9Xe9i20MPse2hh+Zso/j9n3zhC1hsNjytrdDaCkA6FiOXTHLrZz4z7dqZDLnV6WTVXXfNqGMlUy7MNvOuBwN2vbpX+6mlHpConhXIbBE8Opste3RE8WambDxOamyM+MgIJ7/61QVHzOgFHl9oNkXJSCkIBjLjrzFymQxXDh68rs0rxRE8+Rj8dDiMzeslfOlSWeXNb2ZKRyJMXLqExeHA0dREYmRkwREzzTt3MpJKkYnHsbpcZBMJ0uPjtN5224znL2YxU2aTgiCGv6aIDg6SDofJ2O3XFW6Yj+CJ9veTDAbBYkFZLNjcbiK9vUQHB8tm/PKbmWKDgyTHxwux+K7W1kL8dal9rd63j3NHjqBzOVL5vPsbNrB6375Zr1mIIa/GjlDZhSrUImL4a4hgTw/Kap013HAuIxIdHOTiP/4j1159lWwyiaOxkUhfH2QyKLsdV1MTWmtcHR2c2b/fiMMfH8fu9xPYtGlegxQdHJy0ENu8cyer9+1j7QMP0PMXf0H44kWjKpYZg25xOMgmk8SuXSv5Ccbb2YmzqYmOvXvLbijLFcNf630K8yM3YzH8NUUiGESZMe158uGG8+XNf/sb32Dk6FFsfj/2hgbiAwMkhobwbdiA3efDYrGQiceZuHQJnc3iCIfBYiEVDmNzuYgPDc1qkKKDg1x4/nlCp0+TTSaNnDwXLxK+dIkdjz5K2223ER8aIhuP4/D7adyxA6ffz8ibb6KUwtPRUbLhs9hsrLvnnkK/wZ4e+n/84+v+glajkHY9Fe9eLsjN2EAWd2sIV3MzOpebdCwfbjhXOoJgTw/hCxewBwI4fT7sLhdYLFidTnLpNC07d9K0YwfkciTHxgopFFxNTUax8tHRObfFB3t6iF69SnpsDIvFgiMQwOJwEHrrLfqPHMHp97PtYx+jY+9eWm+5BU97O1prwpcuEdi2bVHb78udc74aZRNXUqnGlcJKqpt8PYjhryGau7rQ2eyMUSpzGZFEMEgmGp30vs7lsHq9pCYmyMTjRhqAeNyok+t2Y3U6AbC6XGQmJuY0SIlgkNi1a1g9HqwOh1EW0esFi4XQyZO4mpuxOZ0079pFLp0mePIk42ZBc9tMTzAlGL5yf0GrUUi7nop3LxfkZmwghr+G8HZ2Yvf7Zww3LDYiiVCI4TffpO/FF4lcuQJKYfN6JxkZZbFgUQrf+vWFKlhWpxPfxo14OjuNPD1gpGnw+eY0SK7mZnKZDNlkkui1a0xcuUKkvx+FEWqZD6vMRKPk0mm8q1fTsG4d/g0bGD52jGQoNE3m+Wbu5f6CVqOQdj0V714uyM3YQHz8NUaxj7uY/Oaj5NgY4+fOgcWCxWrF3d5uhDJ2dhI+eRKttZEbxXQZtd5yC0033GD8c5sJ2vLpGTKJBORyBFavnnMjU3NXl1Ho48wZbD4fFpuNbDRKMpWi493vLoRVntm/n1w2i6upCd/69QAMv/YaQ6+/jsVimSTzfH7Vcu+yrUYem1rInSNMppbqJlcTMfzLhGLjqouMq7OpiXQkgqulBd+aNVz90Y9IDQ7ibGqi8667cLe1zbh1PptMFqJ68ikUphqk/OLq+MWLJMfHyWYy5MbHsXs8uNrbcfh8heRp3s5OGtato3X3bpTlnQfJ1ttvp/cHP8Db0TFN5rkWOZu7urjw/PMkQyFy6XQhT1Beh8WOYaWNruwbqC3kZmwghn8ZMZNxTYRCTFy6RGxwkPa9e1l91100rFkzrfRg8T/2bAa+OHoGKOT7ifb1oZTCu2YNNoeDbCpFYPNmmnbsmLQYPdMs3eZ04lu7llV33z3phlBycrR8Vscp2R1nQ0L1hPmQm7EY/mVHsXFNhEIEu7vRGEnUxs+fJz0+jru9Hfs85fvyzBbepux27D4fY+fPY/N4cJsZNe1eL57OTqxOJ1anc9Li7WyP0U07dy7YbRPs6aFhzRqabrihcGy+pwQJ1ROE0pDF3WVG8YLhxKVLaEBpjX/DBnQ6jT0QYKK3t3D+fAui+eiZXDrNaHc3I2+8Qbi3l6GjRw3jbVbRyq8PpMJhLA4HCTMbZ/FC5Wy5cFbv27fgRc7FLO5KqJ4glIbM+JcZxT7K2OAgnlWr8G/YgLOpqVDgJDMxUTh/vpl1IhhEWSwEe3qwut2FNqJXrxLt7yenFGOnT6NzOXLmLuDE6CiupqYZZ9KzPUYv1K+6mMXdUvPtV9odJO4nodaouOFXSq0D/hroBHLAV7XWf1JpOcpNKV/u+c6JDg6SDIV4+Td+g+jAAGiNd80aAlu3GvVxx8ZIh8M4AgH8GzfSvncvNpeLXDrNyJtvEr50idCZM2STSS6/8ALZRMKoU9vRwfnvfteoeWuWMLS5XFi8XiIXLxpVufx+Atu34+3oMEopOhxc/Id/IGdu+sqlUmQTCZTFwnhDA807d9J/5Mik/Pzz6TmXiyZ/ftJu5+yzz5IcGyPa10dg61a8q1eXFn2hFNd+8hN0JoPN5zNCWc2KYXmGu7u58Oyz5HI5rA4H2XSay//8z3T81E/NqMv1fu6lup/y7SQnJjj77LPGQa3lRiEsCdWY8WeAz2itjyulfMAxpdQLWuuTVZClLJTy5Z7vnHxahHRDAxNXrpCemACtScfjjJ89i6utDYfpxkiFw1idTqKDg0xcvmy4VTwekuEwKdONQi4HVivZTIbslSvEhoexOxxY7HYjxt/pJDEygrutrRDXPPjKK9j9flQ2S+CGG0jHYmTCYTLRqFFDN5eDdBpltZIcGWHgpZdIjI6y+cEHS9ZzrrFTFguZWIyRnh5ab78dm8vF+NmzZJPJwo1urptHYnSUdDiMPRAgm0gw/NprNGzYUIgEig4OcuG558BqxeZ0Ej53Dg14165l/Nw5dDq9oPWAUnQtJW1DcTsAI8ePA0ZEVH7HsqxTCOWk4j5+rfWA1vq4+fcEcApYU2k5ysl8vuXo4CBn9u9n9ORJxs6fJzk+Pu2cYE8PybExyOXQ2Sx2rxd7QwOZSASgsDs3n2Zh4vJlUsEg6WgUZ2MjydFRUqOjRtlEux2by2UYekBZreTicXKZDBarFczsl1anE51O42xsLPSTGhvD2dJCKhgkE4vh8Ptx+HzY3G4cXi8Onw+lFLlsllw6TXJsbJIPfaF+9uLzI319KKu1kGCuYe1a2vfuxb9xI+vuv39Ow5dfDM4/BeXXO1wtLZOMsM5mcQYCJEZGsHm9hfq+OpNZ8HpAKbqWslZR3E4uncbR2FgYA1mnEJYCpfVsZS4q0LlSG4EfA11a6/CU9x4HHgfo6Oi4/emnn668gCWSDIWw2KY/POVMY5IOh8kkElhsNiP8UWujzKDVSi6TwdnURDIUMvLPOxyo8fFC+GIuncZitRobsxwObC4XAJlEwnBVJBLGImwiQS6dJpfJGLP9fPij1kbR81wOZRZM14DOZgvyWGw246Zg/ra5XAWffv5ancuRD6jUgNVuR9lsWO12rC5Xoa7qXGORP2e2sUtHImRcLuzptHHzM2fHs11b6mdQLFsunUbncmRTqUJ4qc5msbnd2NzukvpaSJ/piQlj7IpCWfOv8zP84nbi6TT2TKYg10LGYCUQiURoKFrXqSeWQvd77733mNZ6z9TjVVvcVUo1AN8Bfm2q0QfQWn8V+CrAnj179D0z7GatFa4cPEgmHp+0EJmORLCZX+yM3c54by/ZZBKb200mHsfidNK4ZQs2n49199zDlYMHuXr8OEObNpH9m78xZu1uN+lYDJvXC1YrntZWmnbsIBOPE75wAd+mTUQHBmhYvZrwpUuEL14kOTyM1hqrzYayWAwDZxp0u9eLtaEBslmyqRTaYsGez9tjtRoGMRzGu307DatXM3b2LKmxMVITE+QyGeOmlcsZTyNNTbhbWmhYv56OPXsKu43nGouZdiQXnz9y/jz9nZ20X76MxemkrbNzzmtL/QyKZYsODBA+f57Y8DBg3Fi11mz4wAewQkl9LaTPYjdOIcQ1Gp3kuilup3t4mPaLFwEWPAYrgcOHD1PL3/WlpJK6VyWcUyllxzD6+7XWf1sNGcrJXDlZ8o/6vvXrycbjhtGfIRzS1dFB3Iw+sTocZOJx4iMjWMxkanaPh+TEBENHjzJ29iy2hgajOtXu3cRHR0mNjxtPBS4XSikyySSZTAZtsRize7fbmNFns2Bm2Mwmk1g9HjRgcTiwezxs/NCH8La3k8tkCGzZgruzE2WxoMwZqYZC6gWL3Y6zsXFSWKaro4Oh117jyg9/yPDrrxPp65szdLN47BrWrkVns6TGxmhYu3ZBuW1KyYvT3NWFxWrFv2ULns5OEsEguVSKjjvuwGq3LziPTil9llLusbgdi91u3GwXMQaCUCrViOpRwF8Cp7TWf1Tp/peCubaB58MSnU1NtNx8MxO9vSRGRiaFQ0YHB+k7cACry4WyWMhpjTZdNDa3m8477iDa10cul0ObLhllseBobsbT2kqkoQGb14srm8XT2UlqYoLk8DDZdBq7z4ezqQlPZ+e0qJ7GG28kF42STSbR2Sytt91G844dRPv7GT97Fu+aNTTt2EFyzx7Gzp4lNjBg3CycTryrVtG+Z8+kSJjo4CCh7m4C27YRHxkx1h3Gx9n87/7dnMVX8mOXicexeTxGqcVcDpvbXfJ2+lK24hefY3U6jVTVAFovqK+F9Jk/b75ykPl2mJh4p9TkAsdAEEqlGq6eu4BHgW6l1Bvmsd/UWn+/CrKUjdm+3MW7WR2BAIEtW/C0t08y+lcPHSIZCuFqbmZM63dy3lssoDUOn4/G9753mkshk0gYrqNIhOadOwvx/GD4kROjo6x+z3tKiiEvhCWOjuJdtYp173vfgo1N8SJlw9q1BTkT167Brl0ljd3Vw4fZtsjH3VK24pd7u3652su3c/469BeEUqm44ddavwSUlnhlBTDfrDBvLF2trYz29KA7O8nF4yiHA6vXSzoapfcHP2Dbww9P3syUTBI8eZLmG2/E09GBu7V10uJfJhYDpUoOrSw2YIutfFXqBipBEKqL7NytAHPNCvPG0rd+PVd++EPDxWPWq9W5HBaHg/joKMNvvsk6s8xiIhRi5NixQrhiNplk5PXXjb6KNjspu51cNsvY+fNGsRWfD3dLy7z5bi48/3xh05bF4WDs3LlJsfqzUe5UyoIgLA2Sq6fKTC0MobNZUuPjZJNJI4bb48HqdBJ6+20ifX3oXI6x06cBaNq+HWWx0LB2La233kp8aGjSAmI+d38umcTu95NLJhk/d45xM2pkJvqPHCFy+TJKKRx+P0opIpcv03/kyLy6SOERQVgeyIx/iYkODtJ/5AihkyeNalU7d05aEM3nnY9cvoy7vZ2IxWL4waxWIwY8m8URCOBqazPSEQDRvj58GzYQNNtUWqMx/OkN69YV+k6bBdXzGTRtbjeZRMI4PguhkyexBwLY3G5SkQiJ4WGS4+PEDhyYN6VBKYudyzlvzXKWXRCKEcNfRvJGPnjyJAojFUAiGCQVDGI3C5aMHD9eSHMAFAqdpMNhHH4/FrsdrRQ6lSKVzWJ1OEiFw6RjMbyrV+Nfv55sIkFsaIj48DBWhwPPqlVEe3tRZrRPfpu/tljArLVrdTqNcou5HA5TlpnIb+dLRSJELl3C4nBgdbnIJhIlpQ6YLyfPck2bvJxlF4SpiKunTOR94yPHj2N1OrE4nQwcOWL43u127B4Pdo8HR2MjyVCI/iNHuHroEJl4HIfXi2/DBlyBAA6zIpbV6USZSbqczc1Gbp6+PnJa49+0iWwsZuza9XoZO3cOZbfjXb9+0jZ/lcsR2Lp1Us3dwNat+DdunFWP5p07SY+PG8VXHA4AcvE4gc2brzt1wHJOm7ycZReEqYjhLxPBnh6SoRCOxsaCkVdWK+lYjPT4eOE8q5lNM3TyZMGQ2E1futXtRmezNG3bhqux0Zjhb9wI2ayRIsFiMZ4MGhpwNDaCUkaahkQC/9atuJubjQRtGNE0dr8fi9VKYMsWOt/9bgJbtmCxWuf0ua/et4+GDRvIxOPkUim01rja22neuXPRxc6jg4NcOXiQ3gMHGDt7lkQoVHjvegqoV5JyF38XhGoirp4ykQgGjQRbRW4Uu89HfHSUtJkADTBSJdvtZFMpw3CEQqQiEcKnT2Pz+citXWvE8NvtuMzMmRaXC4vDgcXhKBh2u5lgzLd+PVaXC6vNZiwI59NExGIENm2iuatrQXnwvZ2dbH7wQTLRqLG3oLV1cm3fBUboFLtIPKtWkQqHCXZ307xrF66mpmUT9SMRS8JKQgx/mXA1NxsG3dxUBeDw+7F5PKTjcYJvv00ukUDncjTddBPNW7cS7e8nfOECNpeLwI4dhN5+m0w8TnRgAGWzkY5GcZhPD6lwGM+qVWQiERKhEDavl1w6TWpszNgRfO4cAG23316Ipskb+YX6oL2dnWx/5JFJOWaK21wIxS4S/4YNjJ44gVaKiUuXCmkSFtpmNZitrORykF0QpiKGv0w0d3Uxdu4ckcuXyWc81ek0jTt2EB8aIhuLoWw2vB0dxk7cHTu48OyzYLVidTpJRaMoM3WAu62NbCpF5PJlaG7GEQgYfn6HA99NN6G0pmHNmneeLrTGaW7z12Xa5l9qOoL5KN7UlU9bEb58mdjAAK0337xs0hGUazwEoRYQw18m8i6S4qiefM4V2623Tku3kLh2jYb160lNTBix7+PjBDZvJmi3E+nrI7B5M572dpLj43haW1E2G4GtW9n20EMV1el6DdtUF4mzqYlGu53WXbtYd//95RCzYpQ73cNSICGnQimI4S8j3s7OaYb57DPPzLwoODqKf+PGQjregZdewu73F/LeW51Ow3dvt7Pq7rsLuXeWG+IiqRwSciqUikT1LDFTd+bCO4uCxTtdbV6vUYFLaxrWrSObTBrrBUWLtaUuJOajaM4+84yRg35wsNxqlUwpaYmF8iAhp0KpiOFfYuZKY1BsFO0+H+RyWMx0wYvNyZ6f9WXicWPWZ27mqrbxX3f//Wx7+OF5SygKi0dCToVSWbGunnL4OkttY67z5lsUzPuN15ntvPLaa+h4fFE52fO1fRNFYZguM2PnXInZFov4k2sLCTkVSmVFGv5y+DpLbaOU80pdFPR2dmL3+dj24Q8vWudkKISrpYVcMlmIl3cGAmVfHxB/cu0h6ylCqaxIV085fJ2ltlErftXivP65VAqb243V5WKit3dJZn21orfwDrKeIpTKipzxl6MgSKlt1ErxkeK8/qMnTgC8U9u3vb3ss75a0VuYzHIIORWqz4qc8c8VSVPuNsrRVzmYWtvX6nSSHB2dVNt3KforRvzJgrA8WJGGvxwFQUpto1aKjxTLka/t27xzJ9sfeWRJZoC1orcgCAtnRRr+cvg6S22jVvyqlZajVvQWBGHhrEgfP5TH17mQaJxaMHiVlqNW9BYEYWGsyBm/IAiCMDti+AVBEOoMMfyCIAh1hhh+QRCEOkMMvyAIQp2h8tWiahml1DBwudpyVIhWYKTaQlQR0V/0r1f9l0L3DVrrtqkHl4XhryeUUke11nuqLUe1EP1F/3rVv5K6i6tHEAShzhDDLwiCUGeI4a89vlptAaqM6F/f1LP+FdNdfPyCIAh1hsz4BUEQ6gwx/IIgCHWGGP4qopT6K6XUkFKqp+hYs1LqBaXUWfN3UzVlXCqUUuuUUi8qpU4ppd5SSn3aPF4v+ruUUj9RSr1p6v8F83hd6J9HKWVVSr2ulPpH83Xd6K+UuqSU6lZKvaGUOmoeq4j+Yviry1PA+6cc+xzwQ631NuCH5uuVSAb4jNb6RuAO4FeUUjupH/2TwH1a61uA3cD7lVJ3UD/65/k0cKrodb3pf6/WendR/H5F9BfDX0W01j8GglMO/yzwdfPvrwMPVlKmSqG1HtBaHzf/nsD48q+hfvTXWuuI+dJu/mjqRH8ApdRa4IPA14oO143+s1AR/cXw1x4dWusBMIwj0F5leZYcpdRG4FbgVepIf9PN8QYwBLygta4r/YE/Bn4dyBUdqyf9NXBAKXVMKfW4eawi+q/YClzC8kAp1QB8B/g1rXVYKVVtkSqG1joL7FZKNQJ/p5Sqm4LFSqkPAUNa62NKqXuqLE61uEtr3a+UagdeUEq9XamOZcZfe1xTSq0CMH8PVVmeJUMpZccw+vu11n9rHq4b/fNorceAwxjrPfWi/13AR5RSl4CngfuUUt+kfvRHa91v/h4C/g54FxXSXwx/7fFd4D+af/9H4O+rKMuSoYyp/V8Cp7TWf1T0Vr3o32bO9FFKuYH7gbepE/211p/XWq/VWm8EPgYc0lr/AnWiv1LKq5Ty5f8GHgB6qJD+snO3iiilvgXcg5GO9RrwO8DzwDPAeqAXeEhrPXUBeNmjlLobOAJ0846P9zcx/Pz1oP/NGIt3VowJ2DNa699TSrVQB/oXY7p6ntBaf6he9FdKbcaY5YPhcv8brfWXKqW/GH5BEIQ6Q1w9giAIdYYYfkEQhDpDDL8gCEKdIYZfEAShzhDDLwiCUGeI4RfqBqVUi5kJ8Q2l1KBS6mrRa8eUc39NKeUpoc3DSqlpBbLN46fNtk8VbclHKfX9ohj+iPl7Y3GWVkFYSiRlg1A3aK1HMTJhopT6XSCitf6DWU7/NeCbQOw6unxEa31UKdUMnFdKPaW1Tmmtf+Y62hSE60Zm/EJdo5T6aTMffLdZH8GplPovwGrgRaXUi+Z5f6GUOlqcO38BNABRIGu2dUkp1VpWRQRhAYjhF+oZF0ZNhH+vtd6F8QT8Ka31nwL9GLnS7zXP/b/NnOk3A+81d97Ox36l1AngNPA/zKRsglB1xPAL9YwVuKi1PmO+/jrwnlnOfVgpdRx4HbgJ2FlC+49orW/G2H7/hFJqw/UKLAjlQAy/UM9ESzlJKbUJeAL4adOQfw/jaaEktNbDwHHgpxYjpCCUGzH8Qj3jAjYqpbaarx8FfmT+PQH4zL/9GDeJcaVUB/CBhXRiRgfdCpy/bokFoQxIVI9QzySAx4BnlVI24DXg/5jvfRX4J6XUgNb6XqXU68BbwAXg5RLb36+UigNO4Cmt9bHyii8Ii0OycwqCINQZ4uoRBEGoM8TwC4Ig1Bli+AVBEOoMMfyCIAh1hhh+QRCEOkMMvyAIQp0hhl8QBKHO+P8BM+HtIWsGvucAAAAASUVORK5CYII=\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "<Figure size 432x288 with 0 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "scatter_plot = plt.figure()\n",
    "plt.figure()\n",
    "\n",
    "axes1 = scatter_plot.add_subplot(1,1,1)\n",
    "axes1.scatter(tips['total_bill'],\n",
    "                   tips['tip'],\n",
    "                   color = 'brown',\n",
    "                   label = 'tips dataset',\n",
    "                   alpha = 0.3)\n",
    "\n",
    "axes1.set_title(\"Scatterplot of Total Bill vs Tip\")\n",
    "axes1.set_xlabel(\"Total Bill\")\n",
    "axes1.set_ylabel(\"Tip\")\n",
    "axes1.legend()\n",
    "axes1.grid()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 226,
   "id": "58edc04c-b6a5-4056-9db8-1e16edb31710",
   "metadata": {},
   "outputs": [],
   "source": [
    "total_bill_row = []\n",
    "tip_row = []\n",
    "for i in range(len(tips['total_bill'])):\n",
    "    if tips['total_bill'][i] >= 40 :\n",
    "        total_bill_row.append(tips['total_bill'][i])\n",
    "    if tips['total_bill'][i] >= 40 :\n",
    "        tip_row.append(tips['tip'][i])\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 227,
   "id": "d6e4bfcb-3308-4222-bac6-1916b9561796",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "total_bill_row :  [48.27, 40.17, 44.3, 41.19, 48.17, 50.81, 45.35, 40.55, 43.11, 48.33]\n",
      "tip_row :  [6.73, 4.73, 2.5, 5.0, 5.0, 10.0, 3.5, 3.0, 5.0, 9.0]\n"
     ]
    }
   ],
   "source": [
    "print(\"total_bill_row : \",total_bill_row)\n",
    "print(\"tip_row : \",tip_row)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 232,
   "id": "c5b20f61-28b0-474a-8c68-f25d160262e2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.plot(total_bill_row,tip_row,'d')\n",
    "plt.suptitle('Tips Dataset(total bill > 40)')\n",
    "plt.xlabel(\"Total Bill\")\n",
    "plt.ylabel(\"Tip\")\n",
    "plt.grid()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 233,
   "id": "39249206-5e9d-43c3-9495-13d39ee83886",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "ax = sns.regplot(x=total_bill_row, y=tip_row)\n",
    "ax.grid()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 234,
   "id": "ea487fe0-d0c3-47f8-89a1-7bb1097c46ae",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "ax = plt.subplots()\n",
    "ax = sns.regplot(x = tips['total_bill'],y=tips['tip'])\n",
    "\n",
    "ax.set_xlabel(\"Total_bill\")\n",
    "ax.set_ylabel(\"Tip\")\n",
    "ax.grid()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "28dda75e-3044-4e86-b76f-62145a40b96e",
   "metadata": {},
   "source": [
    "# box plot"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 236,
   "id": "64cf6228-a34e-474e-a4aa-20fdc1e917e0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAX4AAAEWCAYAAABhffzLAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjMuNCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8QVMy6AAAACXBIWXMAAAsTAAALEwEAmpwYAAAaUUlEQVR4nO3df3Qd9Xnn8fcHYSSMzQ8XQ+0CcdM4rLACTlDSpnW7OIQ2ZGnhbEnOekliGq2dbovabraLfaKeQLoVJTS4yXFDjVMnmASrsCQpJJQWji0nVckmmJQFUzUly9rFtfEPMMUYbIx59o8ZmWv53usr6c6dezWf1zn33Jm5M/N9NLYezX3mO99RRGBmZsVxQt4BmJlZYznxm5kVjBO/mVnBOPGbmRWME7+ZWcE48ZuZFYwTvzWcpJD0tga0I0lfkbRX0g+ybq9M+3PSn/XECp9vkfT+Cp/9oqQflVtX0o2SvjaOeCq2N1GN+je1+nDiL7A0Ebwq6eU0OT4g6dy84xoh6VpJQxPYxQLgMuCciHjPRPdfh3hqFhF/FxHnN6ItKx4nfvvViJgGzAJ2Aitzjqee3gJsiYj9eQdi1kyc+A2AiDgA3AtcMLJM0mmS7pS0W9JWSX8g6QRJMyRtk/Sr6XrTJP1Y0sfS+TskrZL0sKR9kr4j6S3l2q3SRiewCnhv+o3kxQrbz5Z0v6QX0hiWpMt7gL8o2f4zo7Yru/+xxiPpP0j6B0kvSXpW0o1jPPTvlvSP6Teur0jqSPd7iaRtx9tYUoekr0l6XtKLkh6VdPY42ts88u+Zzk+RtEfS/Art/g9JOyRtl/TxUZ9VPCbpt8reUes/Iemq4/2sVkcR4VdBX8AW4P3p9FRgLXBnyed3AvcB04E5wD8DPelnvww8B5wFfAm4t2S7O4B9wC8B7cAXgKGSzwN4Ww1tXFu6XYWf4TvAbUAHMB/YDVxay/blPh9rPMAlwDtITqIuJPnWdFX62Zz0Zz2xyvHfDJwLzAD+Hvijkv1uq/BvdSPwtXT6E8C30n+/NuBi4NRxtHc9cHfJulcCT1bYzwfSn7MLOAVYN+rftNox+TDw/ZJ9XQQ8D5yU9+9DkV65B+BXjv/4SSJ4GXgReB3YDrwj/awNOAhcULL+J4CNJfMrgSfT7X6iZPkdwF+WzE8DDgPnpvMBvO14bZRLtKPiPzfd7/SSZX8M3FHj9kd9PtF40nU+D/xpOj2H4yf+3yyZ/yDwf9PpS6gt8X8ceAS4sMZ/70rtzSb5Y31qOn8vcH2F/XwZuLlk/u2UJP7jHJN24AVgbjr/OeC2vH8XivZyqceuiojTSX4hrwO+I+kngTOBk4CtJetuBX6qZH41yVnfVyLi+VH7fXZkIiJeJvllnz1qnVraqGY28EJE7Bvn9qONOR5JPytpMC0N/Rvwm+l+avVsyfRWjj1Gx/NV4G+Bv0zLLrdImjLW9iJiO8k3gF+XdDpwOXBXhX3MLrOfI6odk4g4CNwDfETSCcCi9GewBnLiNwAi4nBEfIPkDHoBsAc4RHKBdMR5wL8CSGoDbicpjfzXMl35jvQOkjSNpLSwfdQ6VdsgOYusZjswQ9L0Ctsfz+j9jyeedcD9JN9mTiO5DqAa24eS45S2NfoYVRURhyLiMxFxAfDzwBXAx8bZ3lrgI8CHgO9FRKXjuKPMfkod75isBa4BLgVeiYjvVYnXMuDEb8CRPu9XAmcAwxFxmOTMrF/S9PTi7CeBkf7jn0rfP07ydf3O9I/BiA9KWiDpJOB/ktR1S88SqaGNncA56T6Oke7vEeCP04ucFwI9VD5THe2o/Y8znukk3zoOSHoP8J9rbHvEb0s6R9IMkmN691g2lrRQ0jvSY/8SyR+uw+Ns76+AdwG/S/IHvZJ7gGslXSBpKnDDqM+rHpM00b8B3IrP9nPhxG/fkvQySdLoBxZHxFPpZ73AfuAZYIjkTO7Lki4mSYgfS5PlZ0nOhpeX7HcdSUJ4geSC4zUV2i/bRvrZBuAp4DlJeypsv4iklr4d+CZwQ0Q8XOPPXm7/Y43nt4A/lLQP+DRJUhyLdcBDaXvPAH80xu1/kqQe/xIwTHKxu9rNXRXbi4hXga8DPw18o9IOIuJBkrr9BuDH6XupWo7JnSQXgMd8I5pNnNILLGZ1I+kOkguTf5B3LDY2kj4NvD0iPpJxOx8DlkbEgizbsfLK3kpuZsWTln96gI9m3M5Ukm8Ft2XZjlXmUo+Zkd749izwYER8N8N2foXkXoudJGUny4FLPWZmBeMzfjOzgmmJGv+ZZ54Zc+bMyTsMM7OW8thjj+2JiJmjl7dE4p8zZw6bNm3KOwwzs5YiaWu55S71mJkVjBO/mVnBOPGbmRWME7+ZWcE48ZuZFYwTv9kkNjAwQFdXF21tbXR1dTEwMJB3SNYEWqI7p5mN3cDAAH19faxZs4YFCxYwNDRET08PAIsWLco5OstTSwzZ0N3dHe7HbzY2XV1drFy5koULFx5ZNjg4SG9vL5s3b84xMmsUSY9FRPcxy7NM/JK2kDzH8zDwekR0pyMA3k0yhvoW4MMRsbfafpz4zcaura2NAwcOMGXKm09iPHToEB0dHRw+XO1ZLTZZVEr8jajxL4yI+SWNLwfWR8RcYD1HP7zDzOqks7OToaGho5YNDQ3R2dmZU0TWLPK4uHslyTM3Sd+vyiEGs0mvr6+Pnp4eBgcHOXToEIODg/T09NDX15d3aJazrC/uBvCQpABuj4jVwNkRsQMgInZIOivjGMwKaeQCbm9vL8PDw3R2dtLf3+8Lu5Z5jX92RGxPk/vDJM8zvT8iTi9ZZ29EnFFm26XAUoDzzjvv4q1by441ZGZmFeRS44+I7en7LpIHYb8H2ClpVhrULGBXhW1XR0R3RHTPnHnMqKJmZjZOmSV+SadImj4yDfwysBm4H1icrrYYuC+rGMzM7FhZ1vjPBr4paaSddRHxN5IeBe6R1AP8C/ChDGMwM7NRMjvjj4hnIuKi9DUvIvrT5c9HxKURMTd9fyGrGMyKrre3l46ODiTR0dFBb29v3iG1tMkyBIbH6jGbpHp7e1m1ahU33XQT+/fv56abbmLVqlVO/uM0MgTGypUrOXDgACtXrqSvr681k39ENP3r4osvDjMbm/b29rj11luPWnbrrbdGe3t7ThG1tnnz5sWGDRuOWrZhw4aYN29eThEdH7ApyuRUj9VjNklJYv/+/UydOvXIsldeeYVTTjmFVvi9bzatOARGnkM2mFkO2tvbWbVq1VHLVq1aRXt7e04RtbbJNASGE7/ZJLVkyRKWLVvGihUreOWVV1ixYgXLli1jyZIleYfWkibVEBjl6j/N9nKN32x8rrvuumhvbw8g2tvb47rrrss7pJa2bt26mDdvXpxwwgkxb968WLduXd4hVYVr/GZmxeIav5mZAU78ZmaF48RvZlYwTvxmZgXjxG9mVqPJMlZP1k/gMjObFEbG6lmzZg0LFixgaGiInp4egJZ7qpm7c5qZ1aCrq4uVK1eycOHCI8sGBwfp7e1l8+bNOUZWWaXunE78ZmY18Fg9ZtYSJktNuhl4rB4za3qTavz4JuCxejxWj1nTa8Xx45udx+ppINf4zcauFWvSVl+u8ZsVzGSqSVt9OfHXgS+gWTOaVDVpqyvfwDVBk+mmDptcRv7/9fb2Mjw8TGdnJ/39/f5/aa7xT1Qr3tRhZsXgG7gy4gtoZtasfHE3I76AZmatxol/gnwBzcxajS/uTpAvoJlZq3GN38xsknKNP0Pux29mrcSlnglyP34zazUu9UyQ+/GbWbNyP/6MuB+/mTUr1/gz4n789edrJmbZyjzxS2qT9A+Svp3Oz5D0sKSn0/czso4hS+7HX19+eIhZA5QbpL+eL+CTwDrg2+n8LcDydHo58Nnj7aPZH8TSag9naGZ+eIjlCajrK2/k8SAWSecAa4F+4JMRcYWkHwGXRMQOSbOAjRFxfrX9NHON3+rL10ysFUgiy9xZL3nV+D8PXA+8UbLs7IjYAZC+n1VuQ0lLJW2StGn37t0Zh2nNwtdMzLKXWeKXdAWwKyIeG8/2EbE6IrojonvmzJl1js6ala+ZmGUvyxu4fgH4NUkfBDqAUyV9DdgpaVZJqWdXhjFYi/HYR2Mnqa77a4UShk1MQ/rxS7oE+P20xv8nwPMRcbOk5cCMiLi+2vau8ZtNTKvUpFtFqxzPZurHfzNwmaSngcvSeTMza5CGjNUTERuBjen088CljWjXzMyO5Tt3zcwKxonfzKxgnPjNzArGid/MrGCc+M3MCsaJ38ysYJz4zcwKxonfzKxgnPjNzArGid/MrGCc+M3MCsaJ38ysYJz462BgYICuri7a2tro6uryg8HNrKk1ZHTOyWxgYIC+vj7WrFnDggULGBoaoqenB8APDzGzpuQz/gnq7+9nzZo1LFy4kClTprBw4ULWrFlDf39/3qGZmZXlxD9Bw8PDbNu27ahSz7Zt2xgeHs47NDOzslzqmaDZs2ezbNky7rrrriOlnmuuuYbZs2fnHZqZWVk+46+D0c/ebIVncZpZcTnxT9D27du55ZZb6O3tpaOjg97eXm655Ra2b9+ed2hmZmW51DNBnZ2dnHPOOWzevPnIssHBQTo7O3OMysysMp/xT1BfXx89PT0MDg5y6NAhBgcH6enpoa+vL+/QzMzK8hn/BC1atIhHHnmEyy+/nIMHD9Le3s6SJUvch9/MmpbP+CdoYGCABx54gAcffJDXXnuNBx98kAceeMB375pZ03LinyDfwGVmrUat0PWwu7s7Nm3alHcYZbW1tXHgwAGmTJlyZNmhQ4fo6Ojg8OHDOUZm9iZJ7mZcR61yPCU9FhHdo5f7jH+COjs7GRoaOmrZ0NCQe/WYWdNy4p8g9+oxs1bjXj0TNNJ7p7e3l+HhYTo7O+nv73evHjNrWq7xmxVAq9SkW0WrHE/X+M3MDKhS6pH0JFDuT5qAiIgLM4vKzMwyU63Gf0XDojAzs4apmPgjYutEdiypA/gu0J62c29E3CBpBnA3MAfYAnw4IvZOpC0zM6tdxRq/pH2SXirz2ifppRr2fRB4X0RcBMwHPiDp54DlwPqImAusT+fNzKxBqp3xT5/IjiO55P1yOjslfQVwJXBJunwtsBFYNpG2zMysdtXO+E9N32eUe9Wyc0ltkh4HdgEPR8T3gbMjYgdA+n5WhW2XStokadPu3bvH+GOZmVkl1S7uriO5wPsYyZm6Sj4L4K3H23lEHAbmSzod+KakrloDi4jVwGpI+vHXul0WJB1/pTFohf6/ZjZ5VSv1XJG+//REG4mIFyVtBD4A7JQ0KyJ2SJpF8m2gqdWaqFvlpg4zK7aqN3BJOlHp6a6kcyVdLWl+LTuWNDM900fSycD7gX8C7gcWp6stBu4bX+hmZjYe1Wr8S0jOxrem0+uBq4G7JdVyMXYWMCjpCeBRkhr/t4GbgcskPQ1cls6bmVmDVKvx/x7wM8B0YBh4S0TskTSVJJF/ttqOI+IJ4J1llj8PXDregK31+ZqJWb6qJf7X0hur9kr6cUTsAYiIVyS91pjwbDLyNROzfFVL/CdLeidJOeikdFrpq6MRwZmZWf1VS/w7gBXp9HMl0yPzZmbWgqp151zYyEDMzKwxPB6/mVnBOPGbmRWME7+ZWcFUewLXu6ptGBE/rH84ZmaWtWq9em6t8lkA76tzLGZm1gDu1WNmVjDVzviPSIdTvoCSG7ci4s6sgjIzs+wcN/FLuoHkiVkXAH8NXA4MAU78ZmYtqJZePVeTDKr2XET8BnARyQPUzcysBdWS+F+NiDeA19PHMe6ihqdvmZk1kxkzZiCpLi+gbvuaMaOmJ9nWVS01/k3pA1W+RPIYxpeBH2QZlJlZve3du7cpR3ut9zDltThu4o+I30onV0n6G+DUdKx9MzNrQcct9UhaPzIdEVsi4onSZWaWDZcmLCvV7tztAKYCZ0o6g2QcfoBTgdkNiM2s0FyasKxUK/V8guTxi7OB0uEZXgK+mGFMZmaWoWp37n4B+IKk3ohY2cCYzMwsQ7X06rld0u8Av5TObwRuj4hDmUVlZmaZqSXx3wZMSd8BPgr8OfBfsgrKzMyyU+3i7okR8Trw7oi4qOSjDZL+T/ahmZlZFqp15xy5SeuwpJ8ZWSjprcDhTKMyM7PMVCv1jPTZ+n1gUNIz6fwc4DeyDMrMzLJTLfHPlPTJdPp2oA3YTzI08zuBwYxjMzOzDFRL/G3ANN488yedB5ieWURmZpapaol/R0T8YcMiMTOzhqh2cdf3ZZuZTULVEv+lDYvCJo1mHFjMg4qZHa3akA0vNDIQmxyacWAxDypmdrRansBlZmaTiBO/mVnBZJb4JZ0raVDSsKSnJP1uunyGpIclPZ2+n5FVDGZmdqwsz/hfB/57RHQCPwf8tqQLgOXA+oiYC6xP583MrEEyS/wRsSMifphO7wOGgZ8CrgTWpqutBa7KKoZaNGMvFPdEMbMs1TIs84RJmkMyzMP3gbMjYgckfxwknVVhm6XAUoDzzjsvs9iasRcKuCeKmWUn88QvaRrwdeD3IuKlWhNaRKwGVgN0d3c3X2Y2s5YSN5wKN56WdxjHiBtObXibmSZ+SVNIkv5dEfGNdPFOSbPSs/1ZwK4sYzAzA9BnXmrab/dxY2PbzLJXj4A1wHBErCj56H5gcTq9GLgvqxjMzOxYWZ7x/wLJYxqflPR4uuxTwM3APZJ6gH8BPpRhDGZmNkpmiT8ihqg80JvHATIzy4nv3DUzK5iGdOc0s7FzLxTLihO/WZNyLxTLiks9ZmYF48RvZlYwTvxmZgXjxG9mVjBO/GZmBePEb2ZWME78ZmYFU/h+/L5JxsyKpvCJ3zfJmFnRuNRjZlYwhT/jt/pqxtKZy2ZmR3Pit7pqxtKZy2ZmR3PiN7PCqPWZ3410xhlnNLxNJ34zK4R6fhOV1HTfbMfCF3fNzArGid/MrGBc6jFrYq5JWxac+M2alGvSlhWXeszMCsaJ38ysYJz4zcwKxonfzKxgfHEX95wws2IpfOJ3zwkzK5rCJ36rv2b7BuVvT2ZHc+K3uvI3KLPm54u7ZmYF48RvZlYwTvxmZgWTWeKX9GVJuyRtLlk2Q9LDkp5O333VzcyswbI8478D+MCoZcuB9RExF1ifzpuZWQNllvgj4rvAC6MWXwmsTafXAldl1b6ZmZXX6Br/2RGxAyB9P6vSipKWStokadPu3bsbFqCZ2WTXtBd3I2J1RHRHRPfMmTPzDsfMbNJodOLfKWkWQPq+q8Htm5kVXqMT//3A4nR6MXBfg9s3Myu8LLtzDgDfA86XtE1SD3AzcJmkp4HL0nkzM2ugzMbqiYhFFT66NKs2zczs+Jr24q6ZmWXDid/MrGCc+M3MCsaJ38ysYJz4zcwKxk/gqsFYHiVYy7p+qpSZ5cmJvwZO1GbFUJSTPCd+M7NUsybqenON38ysYJz4zcwKxonfzKxgnPjNzArGF3et4YrSc8KsWTnxW8M5UZvly6UeM7OCceI3MysYJ34zs4Jx4jczKxgnfjOzgnHiNzMrGCd+M7OCceI3MysYJ34zs4LxnbtmLa7WITBqXc93Vk9+TvxmLc6J2sbKpR4zs4Jx4jczKxgnfjOzgnHiNzMrGCd+M7OCceI3MysYJ34zs4Jx4jczKxi1ws0fknYDW/OOowZnAnvyDmIS8fGsHx/L+mqV4/mWiJg5emFLJP5WIWlTRHTnHcdk4eNZPz6W9dXqx9OlHjOzgnHiNzMrGCf++lqddwCTjI9n/fhY1ldLH0/X+M3MCsZn/GZmBePEb2ZWME78VUj6CUmPp6/nJP1rOv2ipH/MO77JRNLhkmP9uKQ5Zdb5a0mnNz661iGpT9JTkp5Ij+PPVln3WkmzGxlfqxjLcWxFfgJXFRHxPDAfQNKNwMsR8bk0KX17vPuVdGJEvF6PGCeRVyNifrkPlDwzUBHxwcaG1FokvRe4AnhXRByUdCZwUpVNrgU2A9sbEF7LGMdxbDk+4x+/NklfSs8KHpJ0MoCkjZK60+kzJW1Jp6+V9L8kfQt4KL+wW4OkOZKGJd0G/BA4V9KW9JfQypsF7ImIgwARsScitkv6tKRHJW2WtFqJq4Fu4K70jPbkXCNvLpWO45H/f5K6JW1Mp2+U9OX0d/8ZSb+TX+i1ceIfv7nAFyNiHvAi8Os1bPNeYHFEvC/LwFrUySVlnm+my84H7oyId0ZEKwzZkbeHSP5A/rOk2yT9+3T5n0XEuyOiCzgZuCIi7gU2AddExPyIeDWvoJtQpeNYzb8DfgV4D3CDpCmZRjhBLvWM3/+LiMfT6ceAOTVs83BEvJBZRK3tqFJPWk7bGhH/O7eIWkxEvCzpYuAXgYXA3ZKWA/skXQ9MBWYATwHfyi/S5lblOFbzQPoN4aCkXcDZwLaMQx03J/7xO1gyfZjkTArgdd78JtUxapv9WQc1yfh4jVFEHAY2AhslPQl8ArgQ6I6IZ9NrVaP/X9ooZY7jYqr/bo/OB02dW13qqb8twMXp9NU5xmEFI+l8SXNLFs0HfpRO75E0jaP/T+4DpjcovJZR4Thu5ejf7VpKu02rqf8qtajPAfdI+iiwIe9grFCmASvTLq+vAz8GlpJcg3qSJHE9WrL+HcAqSa8C73Wd/4hKx7ETWCPpU8D38wtv4jxkg5lZwbjUY2ZWME78ZmYF48RvZlYwTvxmZgXjxG9mVjDuzmlWgaTDJN0gp5B061sLfD4i3sg1MLMJcuI3q+zIMBKSzgLWAacBN+QZlNlEudRjVoOI2EVyE8916eiWcyT9naQfpq+fB5D0VUlXjmwn6S5Jv5ZX3Gbl+AYuswokvRwR00Yt20syEuM+4I2IOJDe3j8QEd3pSI7/LSKuknQa8Dgw189fsGbiUo/Z2Ch9nwL8maT5JINyvR0gIr4j6Ytpaeg/Al930rdm48RvViNJbyVJ8rtI6vw7gYtISqYHSlb9KnAN8J+Ajzc4TLPjcuI3q4GkmcAqkoeaRFrG2RYRb0haDLSVrH4H8APguYh4qvHRmlXnxG9W2cmSHufN7pxfBVakn90GfF3Sh4BBSp4dEBE7JQ0Df9XQaM1q5Iu7ZnUmaSpJ//93RcS/5R2P2WjuzmlWR5LeD/wTsNJJ35qVz/jNzArGZ/xmZgXjxG9mVjBO/GZmBePEb2ZWME78ZmYF8/8BM3Jvdi94GZ0AAAAASUVORK5CYII=\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "boxplot = plt.figure()\n",
    "axes1 = boxplot.add_subplot(1,1,1)\n",
    "\n",
    "axes1.boxplot([tips[tips['day']=='Thur']['total_bill'],\n",
    "               tips[tips['day']=='Fri']['total_bill'],\n",
    "               tips[tips['day']=='Sat']['total_bill'],\n",
    "              tips[tips['day']=='Sun']['total_bill']],\n",
    "              labels = ['Thur', 'Fri','Sat','Sun'])\n",
    "               \n",
    "axes1.set_xlabel('Day')\n",
    "axes1.set_ylabel('Total Bill')\n",
    "\n",
    "axes1.set_title('Boxplot of total bills by day')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 241,
   "id": "5e4f7105-185c-4044-a8ed-7521423ccb82",
   "metadata": {},
   "outputs": [],
   "source": [
    "def recode_sex(sex) :\n",
    "    if sex == 'Female':\n",
    "        return 0\n",
    "    else:\n",
    "        return 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 242,
   "id": "c31ab9fb-8f43-47b1-8028-9f855398313b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>sex</th>\n",
       "      <th>sex_color</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Female</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Male</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Male</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Male</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Female</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      sex sex_color\n",
       "0  Female         0\n",
       "1    Male         1\n",
       "2    Male         1\n",
       "3    Male         1\n",
       "4  Female         0"
      ]
     },
     "execution_count": 242,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tips['sex_color']=tips['sex'].apply(recode_sex) #숫자로 바꾼 sex 적용\n",
    "tips[['sex','sex_color']].head(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 243,
   "id": "2fe20a16-48b7-40d1-a93c-8b8d4c2e2639",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[['Sex', 'Length', 'Diameter', 'Height', 'Whole weight', 'Shucked weight', 'Viscera weight', 'Shell weight', 'Rings'], ['M', '0.455', '0.365', '0.095', '0.514', '0.2245', '0.101', '0.15', '15'], ['M', '0.35', '0.265', '0.09', '0.2255', '0.0995', '0.0485', '0.07', '7'], ['F', '0.53', '0.42', '0.135', '0.677', '0.2565', '0.1415', '0.21', '9'], ['M', '0.44', '0.365', '0.125', '0.516', '0.2155', '0.114', '0.155', '10']]\n"
     ]
    }
   ],
   "source": [
    "import csv\n",
    "\n",
    "with open('dataset/abalone.csv') as csvfile:\n",
    "    csvreader = csv.reader(csvfile)\n",
    "    rows = []\n",
    "    for row in csvreader:\n",
    "        rows.append(row)\n",
    "print(rows[0:5])    \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 245,
   "id": "1236c663-56c0-46a4-8506-edbf37ee8b1e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Sex</th>\n",
       "      <th>Length</th>\n",
       "      <th>Diameter</th>\n",
       "      <th>Height</th>\n",
       "      <th>Whole weight</th>\n",
       "      <th>Shucked weight</th>\n",
       "      <th>Viscera weight</th>\n",
       "      <th>Shell weight</th>\n",
       "      <th>Rings</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>M</td>\n",
       "      <td>0.455</td>\n",
       "      <td>0.365</td>\n",
       "      <td>0.095</td>\n",
       "      <td>0.514</td>\n",
       "      <td>0.2245</td>\n",
       "      <td>0.101</td>\n",
       "      <td>0.15</td>\n",
       "      <td>15</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>M</td>\n",
       "      <td>0.35</td>\n",
       "      <td>0.265</td>\n",
       "      <td>0.09</td>\n",
       "      <td>0.2255</td>\n",
       "      <td>0.0995</td>\n",
       "      <td>0.0485</td>\n",
       "      <td>0.07</td>\n",
       "      <td>7</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>F</td>\n",
       "      <td>0.53</td>\n",
       "      <td>0.42</td>\n",
       "      <td>0.135</td>\n",
       "      <td>0.677</td>\n",
       "      <td>0.2565</td>\n",
       "      <td>0.1415</td>\n",
       "      <td>0.21</td>\n",
       "      <td>9</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>M</td>\n",
       "      <td>0.44</td>\n",
       "      <td>0.365</td>\n",
       "      <td>0.125</td>\n",
       "      <td>0.516</td>\n",
       "      <td>0.2155</td>\n",
       "      <td>0.114</td>\n",
       "      <td>0.155</td>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>I</td>\n",
       "      <td>0.33</td>\n",
       "      <td>0.255</td>\n",
       "      <td>0.08</td>\n",
       "      <td>0.205</td>\n",
       "      <td>0.0895</td>\n",
       "      <td>0.0395</td>\n",
       "      <td>0.055</td>\n",
       "      <td>7</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  Sex Length Diameter Height Whole weight Shucked weight Viscera weight  \\\n",
       "0   M  0.455    0.365  0.095        0.514         0.2245          0.101   \n",
       "1   M   0.35    0.265   0.09       0.2255         0.0995         0.0485   \n",
       "2   F   0.53     0.42  0.135        0.677         0.2565         0.1415   \n",
       "3   M   0.44    0.365  0.125        0.516         0.2155          0.114   \n",
       "4   I   0.33    0.255   0.08        0.205         0.0895         0.0395   \n",
       "\n",
       "  Shell weight Rings  \n",
       "0         0.15    15  \n",
       "1         0.07     7  \n",
       "2         0.21     9  \n",
       "3        0.155    10  \n",
       "4        0.055     7  "
      ]
     },
     "execution_count": 245,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "rows_df = pd.DataFrame(data=rows[1:],columns=rows[0])\n",
    "rows_df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 246,
   "id": "3f3ef761-7da8-46ce-a586-0ab7d2b3e97f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "\n",
    "fig = plt.figure()\n",
    "axis1 = fig.add_subplot(1,1,1)\n",
    "axis1.hist(rows_df['Sex'],7)\n",
    "axis1.set_title('Sex of Abalone')\n",
    "axis1.set_xlabel('Sex')\n",
    "axis1.set_ylabel('Frequency')\n",
    "axis1.grid()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 247,
   "id": "44bc8582-7caf-478a-8a32-09396f7e3969",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0       15\n",
      "1        7\n",
      "2        9\n",
      "3       10\n",
      "4        7\n",
      "        ..\n",
      "4172    11\n",
      "4173    10\n",
      "4174     9\n",
      "4175    10\n",
      "4176    12\n",
      "Name: Rings, Length: 4177, dtype: object\n"
     ]
    }
   ],
   "source": [
    "print(rows_df[\"Rings\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 250,
   "id": "9edd2fb7-3e4c-4237-9081-e633400b454c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0       15\n",
       "1        7\n",
       "2        9\n",
       "3       10\n",
       "4        7\n",
       "        ..\n",
       "4172    11\n",
       "4173    10\n",
       "4174     9\n",
       "4175    10\n",
       "4176    12\n",
       "Name: Rings, Length: 4177, dtype: int64"
      ]
     },
     "execution_count": 250,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "rows_df['Rings'] = pd.to_numeric(rows_df['Rings'])\n",
    "rows_df['Rings']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 253,
   "id": "4ed2814a-bfcc-4ab0-a942-f89570235e06",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "fig = plt.figure()\n",
    "axis1 = fig.add_subplot(1,1,1)\n",
    "axis1.hist(rows_df['Rings'],'auto')\n",
    "axis1.set_title(\"Rings of abalone\")\n",
    "axis1.set_xlabel(\"RIngs\")\n",
    "axis1.set_ylabel(\"Frequency\")\n",
    "axis1.grid()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 254,
   "id": "4d1bec50-b83f-4928-8e46-44a753950f34",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "count    4177.000000\n",
      "mean        9.933684\n",
      "std         3.224169\n",
      "min         1.000000\n",
      "25%         8.000000\n",
      "50%         9.000000\n",
      "75%        11.000000\n",
      "max        29.000000\n",
      "Name: Rings, dtype: float64\n",
      "==============================\n",
      "9     689\n",
      "10    634\n",
      "8     568\n",
      "11    487\n",
      "7     391\n",
      "12    267\n",
      "6     259\n",
      "13    203\n",
      "14    126\n",
      "5     115\n",
      "15    103\n",
      "16     67\n",
      "17     58\n",
      "4      57\n",
      "18     42\n",
      "19     32\n",
      "20     26\n",
      "3      15\n",
      "21     14\n",
      "23      9\n",
      "22      6\n",
      "27      2\n",
      "24      2\n",
      "26      1\n",
      "29      1\n",
      "25      1\n",
      "1       1\n",
      "2       1\n",
      "Name: Rings, dtype: int64\n"
     ]
    }
   ],
   "source": [
    "print(rows_df['Rings'].describe())\n",
    "print(\"=\"*30)\n",
    "print(rows_df['Rings'].value_counts())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 256,
   "id": "b18f7fef-0dc6-4ba8-a88f-be5135e4f80e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "import warnings\n",
    "warnings.filterwarnings('ignore')\n",
    "ax = plt.subplots()\n",
    "ax = sns.countplot(rows_df[\"Rings\"])\n",
    "ax.set_title('Count of Rings')\n",
    "ax.set_xlabel(\"Rings\")\n",
    "ax.set_ylabel(\"Frequency\")\n",
    "ax.grid()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 259,
   "id": "2b4b697e-dc66-4be5-931d-833fe472d40a",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[' Mean of the integrated profile', ' Standard deviation of the integrated profile', ' Excess kurtosis of the integrated profile', ' Skewness of the integrated profile', ' Mean of the DM-SNR curve', ' Standard deviation of the DM-SNR curve', ' Excess kurtosis of the DM-SNR curve', ' Skewness of the DM-SNR curve', 'target_class'], ['140.5625', '55.68378214', '-0.234571412', '-0.699648398', '3.199832776', '19.11042633', '7.975531794', '74.24222492', '0'], ['102.5078125', '58.88243001', '0.465318154', '-0.515087909', '1.677257525', '14.86014572', '10.57648674', '127.3935796', '0'], ['103.015625', '39.34164944', '0.323328365', '1.051164429', '3.121237458', '21.74466875', '7.735822015', '63.17190911', '0'], ['136.75', '57.17844874', '-0.068414638', '-0.636238369', '3.642976589', '20.9592803', '6.89649891', '53.59366067', '0']]\n"
     ]
    }
   ],
   "source": [
    "with open('dataset/pulsar_stars.csv') as csvfile:\n",
    "    csvreader = csv.reader(csvfile)\n",
    "    rows = []\n",
    "    for row in csvreader:\n",
    "        rows.append(row)\n",
    "print(rows[0:5])        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 261,
   "id": "0d7a23a1-aa3e-42da-8deb-2b262ec9b1ac",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Mean of the integrated profile</th>\n",
       "      <th>Standard deviation of the integrated profile</th>\n",
       "      <th>Excess kurtosis of the integrated profile</th>\n",
       "      <th>Skewness of the integrated profile</th>\n",
       "      <th>Mean of the DM-SNR curve</th>\n",
       "      <th>Standard deviation of the DM-SNR curve</th>\n",
       "      <th>Excess kurtosis of the DM-SNR curve</th>\n",
       "      <th>Skewness of the DM-SNR curve</th>\n",
       "      <th>target_class</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>140.5625</td>\n",
       "      <td>55.68378214</td>\n",
       "      <td>-0.234571412</td>\n",
       "      <td>-0.699648398</td>\n",
       "      <td>3.199832776</td>\n",
       "      <td>19.11042633</td>\n",
       "      <td>7.975531794</td>\n",
       "      <td>74.24222492</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>102.5078125</td>\n",
       "      <td>58.88243001</td>\n",
       "      <td>0.465318154</td>\n",
       "      <td>-0.515087909</td>\n",
       "      <td>1.677257525</td>\n",
       "      <td>14.86014572</td>\n",
       "      <td>10.57648674</td>\n",
       "      <td>127.3935796</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>103.015625</td>\n",
       "      <td>39.34164944</td>\n",
       "      <td>0.323328365</td>\n",
       "      <td>1.051164429</td>\n",
       "      <td>3.121237458</td>\n",
       "      <td>21.74466875</td>\n",
       "      <td>7.735822015</td>\n",
       "      <td>63.17190911</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>136.75</td>\n",
       "      <td>57.17844874</td>\n",
       "      <td>-0.068414638</td>\n",
       "      <td>-0.636238369</td>\n",
       "      <td>3.642976589</td>\n",
       "      <td>20.9592803</td>\n",
       "      <td>6.89649891</td>\n",
       "      <td>53.59366067</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>88.7265625</td>\n",
       "      <td>40.67222541</td>\n",
       "      <td>0.600866079</td>\n",
       "      <td>1.123491692</td>\n",
       "      <td>1.178929766</td>\n",
       "      <td>11.4687196</td>\n",
       "      <td>14.26957284</td>\n",
       "      <td>252.5673058</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Mean of the integrated profile  \\\n",
       "0                        140.5625   \n",
       "1                     102.5078125   \n",
       "2                      103.015625   \n",
       "3                          136.75   \n",
       "4                      88.7265625   \n",
       "\n",
       "   Standard deviation of the integrated profile  \\\n",
       "0                                   55.68378214   \n",
       "1                                   58.88243001   \n",
       "2                                   39.34164944   \n",
       "3                                   57.17844874   \n",
       "4                                   40.67222541   \n",
       "\n",
       "   Excess kurtosis of the integrated profile  \\\n",
       "0                               -0.234571412   \n",
       "1                                0.465318154   \n",
       "2                                0.323328365   \n",
       "3                               -0.068414638   \n",
       "4                                0.600866079   \n",
       "\n",
       "   Skewness of the integrated profile  Mean of the DM-SNR curve  \\\n",
       "0                        -0.699648398               3.199832776   \n",
       "1                        -0.515087909               1.677257525   \n",
       "2                         1.051164429               3.121237458   \n",
       "3                        -0.636238369               3.642976589   \n",
       "4                         1.123491692               1.178929766   \n",
       "\n",
       "   Standard deviation of the DM-SNR curve  \\\n",
       "0                             19.11042633   \n",
       "1                             14.86014572   \n",
       "2                             21.74466875   \n",
       "3                              20.9592803   \n",
       "4                              11.4687196   \n",
       "\n",
       "   Excess kurtosis of the DM-SNR curve  Skewness of the DM-SNR curve  \\\n",
       "0                          7.975531794                   74.24222492   \n",
       "1                          10.57648674                   127.3935796   \n",
       "2                          7.735822015                   63.17190911   \n",
       "3                           6.89649891                   53.59366067   \n",
       "4                          14.26957284                   252.5673058   \n",
       "\n",
       "  target_class  \n",
       "0            0  \n",
       "1            0  \n",
       "2            0  \n",
       "3            0  \n",
       "4            0  "
      ]
     },
     "execution_count": 261,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "rows_df = pd.DataFrame(data=rows[1:],columns=rows[0])\n",
    "rows_df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 262,
   "id": "aa05a226-8e75-4212-8dc8-7e0fac9a19ee",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "ax = plt.subplots()\n",
    "ax = sns.countplot(rows_df['target_class'])\n",
    "ax.set_title('Target_class')\n",
    "ax.set_ylabel('Frequency')\n",
    "ax.grid()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 263,
   "id": "59c20659-6e73-49d4-86ea-9a9aa3ea9c6d",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns \n",
    "\n",
    "ebola = pd.read_csv('dataset/country_timeseries.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 264,
   "id": "7f749bbf-a196-4e9b-9493-e1fa5087ec97",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Day</th>\n",
       "      <th>Cases_Guinea</th>\n",
       "      <th>Cases_Liberia</th>\n",
       "      <th>Cases_SierraLeone</th>\n",
       "      <th>Cases_Nigeria</th>\n",
       "      <th>Cases_Senegal</th>\n",
       "      <th>Cases_UnitedStates</th>\n",
       "      <th>Cases_Spain</th>\n",
       "      <th>Cases_Mali</th>\n",
       "      <th>Deaths_Guinea</th>\n",
       "      <th>Deaths_Liberia</th>\n",
       "      <th>Deaths_SierraLeone</th>\n",
       "      <th>Deaths_Nigeria</th>\n",
       "      <th>Deaths_Senegal</th>\n",
       "      <th>Deaths_UnitedStates</th>\n",
       "      <th>Deaths_Spain</th>\n",
       "      <th>Deaths_Mali</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>122.000000</td>\n",
       "      <td>93.000000</td>\n",
       "      <td>83.000000</td>\n",
       "      <td>87.000000</td>\n",
       "      <td>38.000000</td>\n",
       "      <td>25.00</td>\n",
       "      <td>18.000000</td>\n",
       "      <td>16.0</td>\n",
       "      <td>12.000000</td>\n",
       "      <td>92.000000</td>\n",
       "      <td>81.000000</td>\n",
       "      <td>87.000000</td>\n",
       "      <td>38.000000</td>\n",
       "      <td>22.0</td>\n",
       "      <td>18.000000</td>\n",
       "      <td>16.000000</td>\n",
       "      <td>12.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>144.778689</td>\n",
       "      <td>911.064516</td>\n",
       "      <td>2335.337349</td>\n",
       "      <td>2427.367816</td>\n",
       "      <td>16.736842</td>\n",
       "      <td>1.08</td>\n",
       "      <td>3.277778</td>\n",
       "      <td>1.0</td>\n",
       "      <td>3.500000</td>\n",
       "      <td>563.239130</td>\n",
       "      <td>1101.209877</td>\n",
       "      <td>693.701149</td>\n",
       "      <td>6.131579</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.833333</td>\n",
       "      <td>0.187500</td>\n",
       "      <td>3.166667</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>89.316460</td>\n",
       "      <td>849.108801</td>\n",
       "      <td>2987.966721</td>\n",
       "      <td>3184.803996</td>\n",
       "      <td>5.998577</td>\n",
       "      <td>0.40</td>\n",
       "      <td>1.178511</td>\n",
       "      <td>0.0</td>\n",
       "      <td>2.746899</td>\n",
       "      <td>508.511345</td>\n",
       "      <td>1297.208568</td>\n",
       "      <td>869.947073</td>\n",
       "      <td>2.781901</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.383482</td>\n",
       "      <td>0.403113</td>\n",
       "      <td>2.405801</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>0.000000</td>\n",
       "      <td>49.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1.00</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>29.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>66.250000</td>\n",
       "      <td>236.000000</td>\n",
       "      <td>25.500000</td>\n",
       "      <td>64.500000</td>\n",
       "      <td>15.000000</td>\n",
       "      <td>1.00</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>157.750000</td>\n",
       "      <td>12.000000</td>\n",
       "      <td>6.000000</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>150.000000</td>\n",
       "      <td>495.000000</td>\n",
       "      <td>516.000000</td>\n",
       "      <td>783.000000</td>\n",
       "      <td>20.000000</td>\n",
       "      <td>1.00</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2.500000</td>\n",
       "      <td>360.500000</td>\n",
       "      <td>294.000000</td>\n",
       "      <td>334.000000</td>\n",
       "      <td>8.000000</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>2.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>219.500000</td>\n",
       "      <td>1519.000000</td>\n",
       "      <td>4162.500000</td>\n",
       "      <td>3801.000000</td>\n",
       "      <td>20.000000</td>\n",
       "      <td>1.00</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>1.0</td>\n",
       "      <td>6.250000</td>\n",
       "      <td>847.750000</td>\n",
       "      <td>2413.000000</td>\n",
       "      <td>1176.000000</td>\n",
       "      <td>8.000000</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>6.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>289.000000</td>\n",
       "      <td>2776.000000</td>\n",
       "      <td>8166.000000</td>\n",
       "      <td>10030.000000</td>\n",
       "      <td>22.000000</td>\n",
       "      <td>3.00</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>1.0</td>\n",
       "      <td>7.000000</td>\n",
       "      <td>1786.000000</td>\n",
       "      <td>3496.000000</td>\n",
       "      <td>2977.000000</td>\n",
       "      <td>8.000000</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>6.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "              Day  Cases_Guinea  Cases_Liberia  Cases_SierraLeone  \\\n",
       "count  122.000000     93.000000      83.000000          87.000000   \n",
       "mean   144.778689    911.064516    2335.337349        2427.367816   \n",
       "std     89.316460    849.108801    2987.966721        3184.803996   \n",
       "min      0.000000     49.000000       3.000000           0.000000   \n",
       "25%     66.250000    236.000000      25.500000          64.500000   \n",
       "50%    150.000000    495.000000     516.000000         783.000000   \n",
       "75%    219.500000   1519.000000    4162.500000        3801.000000   \n",
       "max    289.000000   2776.000000    8166.000000       10030.000000   \n",
       "\n",
       "       Cases_Nigeria  Cases_Senegal  Cases_UnitedStates  Cases_Spain  \\\n",
       "count      38.000000          25.00           18.000000         16.0   \n",
       "mean       16.736842           1.08            3.277778          1.0   \n",
       "std         5.998577           0.40            1.178511          0.0   \n",
       "min         0.000000           1.00            1.000000          1.0   \n",
       "25%        15.000000           1.00            3.000000          1.0   \n",
       "50%        20.000000           1.00            4.000000          1.0   \n",
       "75%        20.000000           1.00            4.000000          1.0   \n",
       "max        22.000000           3.00            4.000000          1.0   \n",
       "\n",
       "       Cases_Mali  Deaths_Guinea  Deaths_Liberia  Deaths_SierraLeone  \\\n",
       "count   12.000000      92.000000       81.000000           87.000000   \n",
       "mean     3.500000     563.239130     1101.209877          693.701149   \n",
       "std      2.746899     508.511345     1297.208568          869.947073   \n",
       "min      1.000000      29.000000        2.000000            0.000000   \n",
       "25%      1.000000     157.750000       12.000000            6.000000   \n",
       "50%      2.500000     360.500000      294.000000          334.000000   \n",
       "75%      6.250000     847.750000     2413.000000         1176.000000   \n",
       "max      7.000000    1786.000000     3496.000000         2977.000000   \n",
       "\n",
       "       Deaths_Nigeria  Deaths_Senegal  Deaths_UnitedStates  Deaths_Spain  \\\n",
       "count       38.000000            22.0            18.000000     16.000000   \n",
       "mean         6.131579             0.0             0.833333      0.187500   \n",
       "std          2.781901             0.0             0.383482      0.403113   \n",
       "min          0.000000             0.0             0.000000      0.000000   \n",
       "25%          4.000000             0.0             1.000000      0.000000   \n",
       "50%          8.000000             0.0             1.000000      0.000000   \n",
       "75%          8.000000             0.0             1.000000      0.000000   \n",
       "max          8.000000             0.0             1.000000      1.000000   \n",
       "\n",
       "       Deaths_Mali  \n",
       "count    12.000000  \n",
       "mean      3.166667  \n",
       "std       2.405801  \n",
       "min       1.000000  \n",
       "25%       1.000000  \n",
       "50%       2.000000  \n",
       "75%       6.000000  \n",
       "max       6.000000  "
      ]
     },
     "execution_count": 264,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ebola.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 267,
   "id": "ac0d7abe-d4d4-4e8b-9cb3-a578c3578032",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "6"
      ]
     },
     "execution_count": 267,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.count_nonzero([0,0,1,1,1,15,189,1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 269,
   "id": "8d42b4ec-64bd-4245-90fb-c1e3bc42304d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Date</th>\n",
       "      <th>Day</th>\n",
       "      <th>Cases_Guinea</th>\n",
       "      <th>Cases_Liberia</th>\n",
       "      <th>Cases_SierraLeone</th>\n",
       "      <th>Cases_Nigeria</th>\n",
       "      <th>Cases_Senegal</th>\n",
       "      <th>Cases_UnitedStates</th>\n",
       "      <th>Cases_Spain</th>\n",
       "      <th>Cases_Mali</th>\n",
       "      <th>Deaths_Guinea</th>\n",
       "      <th>Deaths_Liberia</th>\n",
       "      <th>Deaths_SierraLeone</th>\n",
       "      <th>Deaths_Nigeria</th>\n",
       "      <th>Deaths_Senegal</th>\n",
       "      <th>Deaths_UnitedStates</th>\n",
       "      <th>Deaths_Spain</th>\n",
       "      <th>Deaths_Mali</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>117</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>118</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>119</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>120</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>121</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>122 rows × 18 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "      Date    Day  Cases_Guinea  Cases_Liberia  Cases_SierraLeone  \\\n",
       "0    False  False         False           True              False   \n",
       "1    False  False         False           True              False   \n",
       "2    False  False         False          False              False   \n",
       "3    False  False          True          False               True   \n",
       "4    False  False         False          False              False   \n",
       "..     ...    ...           ...            ...                ...   \n",
       "117  False  False         False          False              False   \n",
       "118  False  False         False           True               True   \n",
       "119  False  False         False           True               True   \n",
       "120  False  False         False           True               True   \n",
       "121  False  False         False           True               True   \n",
       "\n",
       "     Cases_Nigeria  Cases_Senegal  Cases_UnitedStates  Cases_Spain  \\\n",
       "0             True           True                True         True   \n",
       "1             True           True                True         True   \n",
       "2             True           True                True         True   \n",
       "3             True           True                True         True   \n",
       "4             True           True                True         True   \n",
       "..             ...            ...                 ...          ...   \n",
       "117           True           True                True         True   \n",
       "118           True           True                True         True   \n",
       "119           True           True                True         True   \n",
       "120           True           True                True         True   \n",
       "121           True           True                True         True   \n",
       "\n",
       "     Cases_Mali  Deaths_Guinea  Deaths_Liberia  Deaths_SierraLeone  \\\n",
       "0          True          False            True               False   \n",
       "1          True          False            True               False   \n",
       "2          True          False           False               False   \n",
       "3          True           True           False                True   \n",
       "4          True          False           False               False   \n",
       "..          ...            ...             ...                 ...   \n",
       "117        True          False           False               False   \n",
       "118        True          False            True                True   \n",
       "119        True          False            True                True   \n",
       "120        True          False            True                True   \n",
       "121        True          False            True                True   \n",
       "\n",
       "     Deaths_Nigeria  Deaths_Senegal  Deaths_UnitedStates  Deaths_Spain  \\\n",
       "0              True            True                 True          True   \n",
       "1              True            True                 True          True   \n",
       "2              True            True                 True          True   \n",
       "3              True            True                 True          True   \n",
       "4              True            True                 True          True   \n",
       "..              ...             ...                  ...           ...   \n",
       "117            True            True                 True          True   \n",
       "118            True            True                 True          True   \n",
       "119            True            True                 True          True   \n",
       "120            True            True                 True          True   \n",
       "121            True            True                 True          True   \n",
       "\n",
       "     Deaths_Mali  \n",
       "0           True  \n",
       "1           True  \n",
       "2           True  \n",
       "3           True  \n",
       "4           True  \n",
       "..           ...  \n",
       "117         True  \n",
       "118         True  \n",
       "119         True  \n",
       "120         True  \n",
       "121         True  \n",
       "\n",
       "[122 rows x 18 columns]"
      ]
     },
     "execution_count": 269,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ebola.isnull() #결측값 확인. True가 결측값"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 271,
   "id": "24727f39-55f8-4a1a-a755-6b1cae2cf924",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "29"
      ]
     },
     "execution_count": 271,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.count_nonzero(ebola['Cases_Guinea'].isnull()) #기니의 결측값이 29개."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 273,
   "id": "2ce8cd8c-8a54-4b33-ac83-3bdea6b71ea5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "84\n",
      "106\n"
     ]
    }
   ],
   "source": [
    "print(np.count_nonzero(ebola['Cases_Nigeria'].isnull())) \n",
    "print(np.count_nonzero(ebola['Cases_Spain'].isnull()))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 278,
   "id": "9c04294e-cb07-4bc8-85c9-9f43634f1b6c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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P+KII3Lrrbdm8eLF2XvvvXs649Of/nS+9KUv9bTHaDVupBMAAAAAAAAAAAAAgM3B/PnJrFnJihWd/pIlnX6SzJy5/vu21nLUUUflta99bb7yla8kSS677LL88Y9/zO67795j1r0755xzkiS33nprT/vcd999Oe644zZARqOTG7MBAAAAAAAAAAAAIMns2Q8UZa+yYkVnvBfnnXdexo8fv0bR8rRp0/KXf/mXOfTQQ7P//vtnn332ybe+9a0kyR133JHnP//52W+//bL33nvnq1/9apJk4cKFecYznpEDDjgghx9+eH7/+98nST760Y9mr732yr777ptXvepV65zflClTctNNNyXpFFe/9rWvzb777puXvexlWdF9IYOdPWPGjLzrXe/KM57xjPzzP/9zTj755Jx++ulJks9+9rM58MADs99+++WlL33p6r22VAqzAQAAAAAAAAAAACDJ0qXrNj5cixYtygEHHPBn4xMmTMhZZ52VSy+9NOedd16OP/74tNby3e9+N7vsskt+9rOfZdGiRXnuc5+be++9N29+85tz5plnZuHChXn961+f2d2K8fe973356U9/mssvvzyf/vSne8r1F7/4RWbNmpXLL788D3vYw/LJT35yyLOTzk3bP/zhD3P88cevsddLXvKSXHLJJfnZz36WPffcM2eccUZPuW3uxo10AgAAAAAAAAAAAACwOZg0KVmyZODxjaG1lne961254IILMmbMmFx//fX54x//mH322ScnnHBC3vGOd+TII4/M0572tCxatCiLFi3KYYcdliS5//77s/POOydJ9t1338ycOTMvfvGL8+IXv7innB772Mfm4IMPTpK8+tWvzkc/+tE897nPHfTsJHnlK1854F6LFi3Ku9/97tx6661Zvnx5Dj/88J5y29wpzAYAAAAAAAAAAACAJHPmJLNmJStWPDA2cWJnvBdTp07NmWee+Wfj8+fPz4033piFCxdm/PjxmTJlSu66667svvvuWbhwYc4555z8wz/8Q57znOfkqKOOytSpU/PjH//4z/b5zne+kwsuuCD//u//nlNPPTVXXnllxo1bvzLhqvqzfmtt0LOTZOuttx5w/JhjjsnZZ5+d/fbbL/Pmzcv555+/XjmNFmNGOgEAAAAAAAAAAAAA2BzMnJnMnZtMnpxUddq5czvjvXjWs56Vu+++O5/97GdXj11yySVZsmRJdtppp4wfPz7nnXdelnSv6/7d736XiRMn5tWvfnVOOOGEXHrppXniE5+YG2+8cXVx9L333psrr7wyK1euzG9/+9s885nPzPvf//7Vt1Ovr6VLl64+48tf/nIOOeSQQc9em2XLlmXnnXfOvffem/nz5693TqOFG7MBAAAAAAAAAAAAoGvmzN4Lsfurqpx11ll561vfmve9732ZMGFCpkyZkpNPPjlvectbMn369EybNi177LFHkuSKK67IiSeemDFjxmT8+PH51Kc+lYc85CE588wz85a3vCW33XZb7rvvvrz1rW/N7rvvnle/+tW57bbb0lrL2972tmy//faD5jJv3rycffbZq/s/+clP1pjfc88988UvfjF/8zd/kyc84Ql54xvfOOjZU6dOHfJ7n3rqqXnyk5+cyZMnZ5999smyZcvW+x2OBtVaG+kc2ASmT5/eFixYMNJpAAAAAACwIcyY0Wm38H/2EwAAAAA2hKuvvjp77rnnSKfBKDXQ709VLWytTe+/dswmywoAAAAAAAAAAAAAYAs1bqQTAAAAAAAAAAAAAAA2nC984Qv553/+5zXGDj744HziE58YoYweHBRmwxZq/vxk9uxk6dJk0qRkzpxk5syRzgoAAAAAAAAAAADY2F73utflda973Uin8aAzZqQTADa8+fOTWbOSJUuS1jrtrFmd8Q2x95QpyZgxnXZD7AkAAAAAAAAAAAAw2inMhi3Q7NnJihVrjq1Y0RnvxcYs+AYAAAAAAAAAAAAYzRRmwxZo6dJ1Gx+ujVXwnbiJGwAAAAAAAAAAABjdFGbDFmjSpHUbH66NVfDtJm4AAAAAAAAAAABgtNviC7Or6rCq+lpVLamqu6rqzqr6TVXNr6pnrCX2UVX1war6RTfu5qr6UVUdW1U1jLN3q6rPVNW13bNvqKr/qqqXDjP3/avqX6vquqq6u6p+X1VnVdWzhvv9eXCaMyeZOHHNsYkTO+O92FgF3xvzJm4AAAAAAAAAAABYJ/PnJ1OmJGPGdNoNcMvo2LFjM23atEydOjX77bdfPvShD2XlypXrtdett96aT37yk6v7559/fo488sie8jv55JNz+umn/9n4U5/61A12xnve8558//vf72mPzd0WW5hdHZ9Ocm6SlyeZlKR1P49L8v8lOb+qPjRI/AFJrkzy9iS7J7kvybZJDkny2STfraqHDnH+EUkuTzIryZQkdyd5ZJLnJDmzqj4/VHF3VR2b5H+TzEzymCR3JnlUkhcn+e+qOnkYr4EHqZkzk7lzk8mTk6pOO3duZ7wXG6vge2PdxA0AAAAAAAAAAADrZP78ZNasZMmSpLVOO2tWz8XZW221VS677LJceeWV+d73vpdzzjkn733ve9drr/6F2RvT//zP/2yQfe6///6ccsopefazn71B9ttcbbGF2UmOSfI33eczk+zeWtuqtTYxyR5JvtWde1tVHdU3sKq2S/LtdAqpf57kwNbatkm2TvKmJPemU2D94YEOrqrHJflakolJLkryxNbadkm2S3JKd9nrkpw4SPxTknw6ybgkZyd5bGtt+yQ7JvlMd9lJVfWKYbwHHqRmzkwWL05Wruy0vRZlr9pzYxR8b6ybuAEAAAAAAAAAAGCdzJ6drFix5tiKFZ3xDWSnnXbK3Llz8/GPfzyttdx///058cQTc+CBB2bffffNZz7TKRVdvnx5Dj300Oy///7ZZ5998q1vdUpf3/nOd+bXv/51pk2blhNPPHH12pe97GXZY489MnPmzLTWVq/da6+9su++++aEE05Y51y32Wab1c+33357jjrqqOy111457rjjVt/4fe655+YpT3lK9t9//7z85S/P8uXLkyRTpkzJKaeckkMOOSRf//rXc8wxx+TMM89Mkpxyyik58MADs/fee2fWrFmr8x3ttuTC7Nd0218lObq19stVE621X6Rzi/ZvukP9C5xPSPLodG6pPqK1tqAbd09r7RNJTuqum1VVuw9w9inpFHH/IcmRrbVruvHLW2snJZnbXTe7qh4+QPz7k4xNckWSV7TWruvG/6m1dlyS/1q1rqrGruU9wAa1MQq+N9ZN3AAAAAAAAAAAALBOli5dt/H19PjHPz4rV67MDTfckDPOOCPbbbddLrnkklxyySX57Gc/m2uvvTYTJkzIWWedlUsvvTTnnXdejj/++LTW8r73vS+77bZbLrvssnzgAx9Ikvz0pz/NRz7ykVx11VX5zW9+k4suuig333xzzjrrrFx55ZW5/PLL8+53v7unnC+++OJ88IMfzBVXXJFf//rX+eY3v5mbbropp512Wr7//e/n0ksvzfTp0/OhD31odcyECRNy4YUX5lWvetUae73pTW/KJZdckkWLFuXOO+/Mt7/97Z5y21xsyYXZ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i16UO+64I694xSty3XXX5f7778///b//N6985SuzcOHCvP3tb8/y5cuzww47ZN68edl5553z0Y9+NJ/+9Kczbty47LXXXvnKV76yDm8kmTJlShYsWJCkU1z92te+Nj/96U+z++6750tf+lImTpw46NkzZszIU5/61Fx00UV54QtfmGXLlmWbbbbJCSeckM9+9rOZO3du7rnnnvzFX/xF/uVf/iUTJ04cMIdjjjkmW221VX7+859nyZIl+cIXvpAvfvGL+fGPf5wnP/nJmTdvXpLk3HPPzUknnZS77747u+22W77whS9km222ySmnnJL/+I//yJ133pmnPvWp+cxnPpOqyowZM/LkJz855513Xm699dacccYZedrTnrZO72e4ttgbswHYuObMSfr/5+PEiZ3xXgxW2N1rwffGMhpv+AYAAAAAAAAAADatRYsW5YADDviz8QkTJuSss87KpZdemvPOOy/HH398Wmv57ne/m1122SU/+9nPsmjRojz3uc/Nvffemze/+c0588wzs3Dhwrz+9a/P7G6h0vve97789Kc/zeWXX55Pf/rTPeX6i1/8IrNmzcrll1+ehz3sYfnkJz855NlJcuutt+aHP/xhjj/++DX2eslLXpJLLrkkP/vZz7LnnnvmjDPOGPLsW265JT/4wQ/y4Q9/OC94wQvytre9LVdeeWWuuOKKXHbZZbnpppty2mmn5fvf/34uvfTSTJ8+PR/60IeSJG9605tyySWXZNGiRbnzzjvz7W9/e/W+9913Xy6++OJ85CMfyXvf+96e3s9QtugbswHYeFbdBj17duc260mTOkXZvd4SPWfOmjdQJxum4HtjGW03fAMAAAAAAAAAwIPdUDdcT5w49PwOOwzvhuzhaq3lXe96Vy644IKMGTMm119/ff74xz9mn332yQknnJB3vOMdOfLII/O0pz0tixYtyqJFi3LYYYclSe6///7svPPOSZJ99903M2fOzItf/OK8+MUv7imnxz72sTn44IOTJK9+9avz0Y9+NM997nMHPTtJXvnKVw6416JFi/Lud787t956a5YvX57DDz98yLNf8IIXpKqyzz775FGPelT22WefJMnUqVOzePHiXHfddbnqqqtW53fPPffkKU95SpLOreTvf//7s2LFitx8882ZOnVqXvCCFyTpFIgnyQEHHJDFixev55tZO4XZAKy3mTN7L8QeaM9kwxd8byyTJiVLlgw8DgAAAAAAAAAAkHQKi88888w/G58/f35uvPHGLFy4MOPHj8+UKVNy1113Zffdd8/ChQtzzjnn5B/+4R/ynOc8J0cddVSmTp2aH//4x3+2z3e+851ccMEF+fd///eceuqpufLKKzNu3PqVCVfVn/Vba4OenSRbb731gOPHHHNMzj777Oy3336ZN29ezl9LVftDH/rQJMmYMWNWP6/q33fffRk7dmwOO+ywfPnLX14j7q677srf/u3fZsGCBXnsYx+bk08+OXfdddef7Tt27Njcd999Q+bQizEbbWcAWE8zZyaLFycrV3bazbUoO+kUjU+cuObY5nzDd5LMn59MmZKMGdNp588f6YwAAAAAAAAAAGDL9qxnPSt33313PvvZz64eu+SSS7JkyZLstNNOGT9+fM4777ws6d4S+bvf/S4TJ07Mq1/96pxwwgm59NJL88QnPjE33njj6uLoe++9N1deeWVWrlyZ3/72t3nmM5+Z97///atvp15fS5cuXX3Gl7/85RxyyCGDnr02y5Yty84775x777038zdAodJBBx2Uiy66KL/61a+SJCtWrMg111yzugh7hx12yPLlywcsgt8U3JgNAD0YbTd8z5+fzJqVrFjR6S9Z0uknm2/OAAAAAAAAAAAw2lVVzjrrrLz1rW/N+973vkyYMCFTpkzJySefnLe85S2ZPn16pk2blj322CNJcsUVV+TEE0/MmDFjMn78+HzqU5/KQx7ykJx55pl5y1vekttuuy333Xdf3vrWt2b33XfPq1/96tx2221preVtb3tbtt9++0FzmTdvXs4+++zV/Z/85CdrzO+555754he/mL/5m7/JE57whLzxjW8c9OypU6cO+b1PPfXUPPnJT87kyZOzzz77ZNmyZev9DpNkxx13zLx583L00Ufn7rvvTpKcdtpp2X333fOGN7wh++yzT6ZMmZIDDzywp3PWV7XWRuRgNq3p06e3BQsWjHQaAIywKVM6xdj9TZ7cuZ0cAAAAGCVmzOi0a/lnPwEAAACA5Oqrr86ee+450mkwSg30+1NVC1tr0/uvHbPJsgIARtzSpes2DgAAAAAAAAAAwPCMG+kEAIBNZ9KkgW/MnjRp0+cCAAAAAAAAAABsHF/4whfyz//8z2uMHXzwwfnEJz4xQhk9YM6cOfn617++xtjLX/7yzJ49e4Qy2nCqtTbSObAJTJ8+vS1YsGCk0wBghM2fn8yalaxY8cDYxInJ3LnJzJkjl9dQ5s9PZs/u3Oo9aVIyZ87mmysAAABsMjNmdNrzzx/JLAAAAABgVLj66quz5557jnQajFID/f5U1cLW2vT+a8dssqwAgBE3c2anCHvy5KSq027uRdmzZnVu+W6t086a1RkHAAAAAAAAAADYnCjMBoAHmZkzk8WLk5UrO+3mWpSddG7K7nu7d9LpbwH/agkAAAAAAAAAALCFUZgNAGy2li5dt3EAAAAAAAAAAICRojAbANhsTZq0buMAAAAAAAAAAAAjRWE2ALDZmjMnmThxzbGJEzvjAAAAAAAAAAAwWowdOzbTpk3L1KlTs99+++VDH/pQVq5cuV573XrrrfnkJz+5un/++efnyCOP7Cm/k08+OaeffvqfjT/1qU/dYGe85z3vyfe///2e9tjcKcwGADZbM2cmc+cmkycnVZ127tzOOAAAAAAAAAAAjBZbbbVVLrvsslx55ZX53ve+l3POOSfvfe9712uv/oXZG9P//M//bJB97r///pxyyil59rOfvUH221wpzAYANmszZyaLFycrV3ZaRdkAAAAAAAAAAPRkxow//6wqdF6xYuD5efM68zfd9Odz62innXbK3Llz8/GPfzyttdx///058cQTc+CBB2bffffNZz7zmSTJ8uXLc+ihh2b//ffPPvvsk29961tJkne+85359a9/nWnTpuXEE09cvfZlL3tZ9thjj8ycOTOttdVr99prr+y777454YQT1jnXbbbZZvXz7bffnqOOOip77bVXjjvuuNU3fp977rl5ylOekv333z8vf/nLs3z58iTJlClTcsopp+SQQw7J17/+9RxzzDE588wzkySnnHJKDjzwwOy9996ZNWvW6nwHMmPGjLztbW/L05/+9Oy555655JJL8pKXvCRPeMIT8u53v3v1un/913/Nk570pEybNi1/8zd/k/vvvz9J8sY3vjHTp0/P1KlTc9JJJ61eP2XKlJx00kmr3+/Pf/7zdX4//SnMBgAAAAAAAAAAAIBN6PGPf3xWrlyZG264IWeccUa22267XHLJJbnkkkvy2c9+Ntdee20mTJiQs846K5deemnOO++8HH/88Wmt5X3ve1922223XHbZZfnABz6QJPnpT3+aj3zkI7nqqqvym9/8JhdddFFuvvnmnHXWWbnyyitz+eWXr1HEvD4uvvjifPCDH8wVV1yRX//61/nmN7+Zm266Kaeddlq+//3v59JLL8306dPzoQ99aHXMhAkTcuGFF+ZVr3rVGnu96U1vyiWXXJJFixblzjvvzLe//e0hz37IQx6SCy64IMcdd1xe9KIX5ROf+EQWLVqUefPm5U9/+lOuvvrqfPWrX81FF12Uyy67LGPHjs38+fOTJHPmzMmCBQty+eWX54c//GEuv/zy1fvusMMOufTSS/PGN74xp59+ek/vJ0nG9bwDAAAAAAAAAAAAAIwW558/+NzEiUPP77DD0PPrYNUt0eeee24uv/zy1bdJ33bbbfnlL3+ZXXfdNe9617tywQUXZMyYMbn++uvzxz/+ccC9nvSkJ2XXXXdNkkybNi2LFy/OQQcdlAkTJuTYY4/N85///Bx55JE95fukJz0pj3/845MkRx99dC688MJMmDAhV111VQ4++OAkyT333JOnPOUpq2Ne+cpXDrjXeeedl/e///1ZsWJFbr755kydOjUveMELBj37hS98YZJkn332ydSpU7Pzzjsn6RS4//a3v82FF16YhQsX5sADD0yS3Hnnndlpp52SJF/72tcyd+7c3Hffffn973+fq666Kvvuu2+S5CUveUmS5IADDsg3v/nN9X43qyjMBgAAAAAAAAAAAIBN6De/+U3Gjh2bnXbaKa21fOxjH8vhhx++xpp58+blxhtvzMKFCzN+/PhMmTIld91114D7PfShD139PHbs2Nx3330ZN25cLr744vz3f/93vvKVr+TjH/94fvCDH6x3zlX1Z/3WWg477LB8+ctfHjBm6623/rOxu+66K3/7t3+bBQsW5LGPfWxOPvnkQb/XKqu+35gxY9b4rmPGjMl9992X1lpe+9rX5p/+6Z/WiLv22mtz+umn55JLLsnDH/7wHHPMMWuctWqvVe+sV2N63gEAAAAAAAAAAAAAGJYbb7wxxx13XN70pjelqnL44YfnU5/6VO69994kyTXXXJM77rgjt912W3baaaeMHz8+5513XpYsWZIk2XbbbbNs2bK1nrN8+fLcdtttOeKII/KRj3wkl112WU95X3zxxbn22muzcuXKfPWrX80hhxySgw46KBdddFF+9atfJUlWrFiRa665Zsh9VhVG77DDDlm+fPnqm8J7ceihh+bMM8/M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Sv3UFmd6y7v16hURERERERERERERERER8Y3ZIiIiIiIiIiIiIiIiIiIiIiIiIiIiIkvEidkiIiIiIiIiIiIiIiIiIiIiIiIiIiIiS2TNpCsgIiuHEMLRSyi+Vq/eSXolUbJ9a4sJvXqlfmqLM73l3Xr1ioiIiIiIiIiIiIiIiIgshRBjnHQdRGSFEEKYBZYy6AQgxhhX69U7bq8kSrZvbTGhV+8SHDIl1BZnesu79epdgkNERERERERERERERERExDdmi8hEuBi4Ycgyq4Dd9eqdAq8kSrZvbTGhV6/UT21xpre8W69eEREREREREREREREREZGh8Y3ZIjI2QgjnkCY9/E2M8SNDlt0JuIT2N+Tp1VvcK4mS7VtbTOjVO0xZmU5qizO99dZZb51eEREREREREREREREREZFhWTXpCojIiuIH+b93W0TZfk+R6NU7Dq8kSrZvbTGhV6/UT21xpre8W69eEREREREREREREREREZFF48RsERknPwQCi5swoVfvpL2SKNm+tcWEXr1SP7XFmd7ybr16RUREREREREREREREREQWzZpJV0BEVhRLeZPdDPB7YFav3gl5JVGyfWuLCb16pX5qizO95d169YqIiIiIiIiIiIiIiIiILJoQo1/tFZHxEELYCjgg//O0OKIBSK/ecXglUbJ9a4sJvXqlfmqLM73l3Xr1ioiIiIiIiIiIiIiIiIgsBSdmi4iIiIiIiIiIiIiIiIiIiIiIiIiIiCyRVZOugIiIiIiIiIiIiIiIiIiIiIiIiIiIiEjtODFbREREREREREREREREREREREREREREZIk4MVtERERERERERERERERERERERERERERkiayZdAVEREREREREREREREoRQtgTOHuB1TYCNwBXAhfn9X8BfAf4eoxxQ8k6ioiIiIiIiIiIiMjyIMQYJ10HEREREREREREREZEiDDgxux83AJ8D3hZjPHUklRoRIYTmDf73xRifOKm6iIiIiIiIiIiIiAismnQFRERERERERERERESmmC2ARwNfCyF8KYRwu0lXSERERERERERERESmkzWTroCIiIiIiIiIiIiIyBg5H7hv17IAbAesA3YB7gncB7g3N3/ByaHAD0MIj4sxfrl8VUVERERERERERESkJpyYLSIiIiIiIiIiIiIriY0xxnMWWOejACGE2wP/BDwDWJ3ztgc+HUJ4SIzxtFKVFBEREREREREREZH6WLXwKiIiIiIiIiIiIiIiK48Y4+9ijM8mvSn7kkbWlsCHQgg7TqZmIiIiIiIiIiIiIjKNODFbRERERERERERERKQPMcZTgIcANzQW3xp41WRqJCIiIiIiIiIiIiLTyJpJV0BEREREREREREREZNqJMf44hPBi4C2NxU8JIbwqxnjpQuVDCDsD+wJ3ANYBq4ErgAuAbw/iGAchhC2A+wB7ALsAM8DFwE9jjD+dZN1EREREREREREREpp0QY5x0HUREREREREREREREihBC2BM4u7Ho3Bjjnot0bQGcB+zcWPy8GONbeqx/D+BvgIcCd15A/z3g32KMn1ygDu8FjhqwypuIMYYFvPsCrwAeBqztsdofgP8A3hljvGnYOoiIiIiIiIiIiIgsd1ZNugIiIiIiIiIiIiIiIjUQY7wBOLZr8V+2rRtCOAT4PvB8Fp6UDXAA8IkQwgdDCFstqaJDEEJYFUJ4E/AT4LH0npQNcBvgGOD0EMJu46ifiIiIiIiIiIiISE2smXQFREREREREREREREQq4mTgJY1/3yuEEOL8z1N2vxjlJuAM0hu3rwQ2B3YF/oybT4Y+Agj5v0UJIawGPgw8pivrWuAHwIXAamBv4K65XgD7Ad8KIRwQY7y4dD1FREREREREREREaiHMv1csIiIiIiIiIiIiIrI8CCHsCZzdWHRujHHPJfi2B65gbpIywO1ijGd3rffnwMeA/wecCHw9xnhTi28t8ATg9cCOjazDY4wfbVl/J2Cb/M/mNj8OvLBXvWOM57S4Xge8tLHoEtKk8/fHGG/sWndv4K3c/A3hX4gxPqzXNkVERERERERERERWGk7MFhEREREREREREZFly6gnZmfnhcCtGosOjjGe1rXODsCNMcarB3TeEfgWc5OzvxdjvNcCZZo3+N8XY3ziINvKZe+Vt9d5s/dvSH/HRX3KrALeAxzZWPywGOMXBt2uiIiIiIiIiIiIyHKm+1OKIiIiIiIiIiIiIiLSn/Vd/96pe4UY4x8HnZSd1/8N8KrGogPypPJSvIS53wg2Aof1m5QNEGOcBZ4OnN9Y/E9FaiciIiIiIiIiIiJSIU7MFhEREREREREREREZjvVd/95qRN5Pdf277xuzF0sIYTfgEY1FH4gxnjFI2Rjj9cD/NRY9MISwdpT1ExEREREREREREamVNZOugIiIiIiIiIiIiIhIZSz6pSchhACsBbYDtujKXt317zstdjsL8ABu/jd8fMjypzX+fzPgnsCpS6yTiIiIiIiIiIiISPU4MVtEREREREREREREZDi27/r3df1WDiEcBBwBHAjchcHfsH2L4as2EAd1/fuKEMKeQ5TvnkB+O5yYLSIiIiIiIiIiIuLEbBERERERERERERGRIVnX9e9L21YKIfwJ8L/A/Ra5ne0WWW4hbtP179Na1xqcHZZYXkRERERERERERGRZ4MRsEREREREREREREZEBCSHcAtila/F5LevdDfgKS3vr9aollO3HqCdSbzNin4iIiIiIiIiIiEiVODFbRERERERERERERGRwDgBC499XAec2VwghbA58kJtPyr4EOJ70durfARcC18UYr+8qGwvUuZvNRuwLC68iIiIiIiIiIiIisvxxYraIiIiIiIiIiIiIyOAc0vXv78QYuydTHw7csfHvrwGPjDFe1U8cQth26dUbiD82/n8jsFWMceOYti0iIiIiIiIiIiKybCn1GUQRERERERERERERkWVFCGEL4O+7Fn+uZdW/bPz/LHDUQpOyM7dabN2G5OLG/68B9hrTdkVERERERERERESWNU7MFhEREREREREREREZjGcCOzX+fQPwgZb1bt/4/zNijL8f0H/gYis2JN/p+veDxrRdERERERERERERkWWNE7NFRERERERERERERBYghLA/8G9di98VY7ysZfXtG/8/yJuyOzx+yGrd0Pj/zYco95Wufz9xyO2KiIiIiIiIiIiISAtOzBYRERERERERERER6UMI4QHAScAWjcUXAq/sUWR94/9vH0JY8F58COFg4MFDVu3Kxv/fatBCMcbfAV9tLLpXCGHYSeEiIiIiIiIiIiIi0oUTs0VEREREREREREREWggh7B1CeDvpDdO7NLKuB46IMV7eo+jPGv+/M/CEBbZze+AEIAxZxV83/v+eIYRthij7yq5/vyuEcOgwGw8h3DqE8LBhyoiIiIiIiIiIiIgsZ5yYLSIiIiIiIiIiIiIriTUhhD1b0p+GEO4XQnhsCOGNIYSvA78Bng2sbpS/EnhkjPG0Ptv4WNe//yeE8KQQQtNDCGGzEMKRwDeB2wCXDfm3NOuwDfC5EMKjQgh/0v33dReMMX4DeH1j0VbASSGE/woh3KHXBkMI60IIh4cQPgycAxw5ZJ1FREREREREREREli0hxjjpOoiIiIiIiIiIiIiIFCFPSj57RLovA8+MMZ45wHZPBe7ftfgi4PvABmAn4ABgXc6bBQ4DPt1Y/30xxif22caewBnAlgvVJ8Y4723cIYRVwPtof6P3ucAvgSuAzXI97wDs2bXeh2OMRyy0fREREREREREREZGVwJpJV0BEREREREREREREZIq5Hvg88PYY49eGKHc48DXgTo1ltwL+qmXdm4CnxRg/E8K8+dM9iTGeE0J4IvAe0huvhyLGOAv8XQjhJ8BrgS0a2XvktBBXDLtdERERERERERERkeWKb8wWERERERERERERkWXLgG/MngVuAK4kvdX6bNLbor8FfD3GuGGR294WeB3wFNonTt8IfA54VYzxJ7lM86Z93zdmN7azB/Ak4GBgH9LbrW+2vbY3Znc5dgX+GTiCNIG8H78GvgR8IMb4nYXqJyIiIiIiIiIiIrJScGK2iIiIiIiIiIiIiEhB8gTt+wG3B7YBLgPOB74VY5y6N06HEO4M7AfsRJrkfT2wHjgT+EWM8ZKJVU5ERERERERERERkinFitoiIiIiIiIiIiIiIiIiIiIiIiIiIiMgSWTXpCoiIiIiIiIiIiIiIiIiIiIiIiIiIiIjUjhOzRURERERERERERERERERERERERERERJaIE7NFRERERERERERERERERERERERERERElogTs0VERERERERERERERERERERERERERESWiBOzRURERERERERERERERERERERERERERJaIE7NFRERERERERERERERERERERERERERElogTs0VERERERERERERERERERERERERERESWiBOzRURERERERERERERERERERERERERERJaIE7NFRERERERERERERERERERERERERERElogTs0VERERERERERERERERERERERERERESWiBOzRURERERERERERERERERERERERERERJaIE7NFRERERERERERERERERERERERERERElogTs0VERERERERERERERERERERERERERESWyP8HC1zqT0MrpBcAAAAASUVORK5CYII=\n",
      "text/plain": [
       "<Figure size 3600x720 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize = (50,10))\n",
    "plt.title(\"Ebola Virus Dataset\", fontsize=25)\n",
    "plt.plot(ebola['Date'],ebola['Cases_Liberia'],'o',color='blue',label = 'Cases_Liberia')\n",
    "plt.plot(ebola['Date'],ebola['Deaths_Liberia'],'o',color='red',label = 'Deaths_Liberia')\n",
    "plt.axhline(y = ebola['Cases_Liberia'].mean(),\n",
    "            linestyle = '--',color = 'blue',\n",
    "            label = 'Cases_Liberia_mean')\n",
    "plt.axhline(y = ebola['Deaths_Liberia'].mean(),\n",
    "            linestyle = '--',color = 'red',\n",
    "            label = 'Deaths_Liberia_mean')\n",
    "plt.axvline(x = ebola['Date'][60], color = 'red', label = 'line')#60번째에 수직선을 그려라\n",
    "plt.xticks(rotation = 90, size = 25)\n",
    "plt.yticks(size = 25)\n",
    "plt.xlabel('Date', size = 40)\n",
    "plt.ylabel('Frequency in Liberia', size = 40)\n",
    "plt.legend()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f70ba78f-2d96-4a2c-966d-590e80bab507",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9399b9d9-1877-4e33-9d8f-7108df85ebd0",
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
