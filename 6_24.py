{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "8eb9f914-e482-4cbd-abba-d0b1f6d547c1",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "988269b2-e254-4088-8842-3eaff172f66d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2.5.0\n"
     ]
    }
   ],
   "source": [
    "import tensorflow as tf\n",
    "print(tf.__version__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "de8c1773-df7f-4e28-ad2d-1131eddefbc2",
   "metadata": {},
   "outputs": [],
   "source": [
    "fashion_mnist = tf.keras.datasets.fashion_mnist"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "d980be27-0ddd-403b-96ac-cf00083d31bb",
   "metadata": {},
   "outputs": [],
   "source": [
    "(train_X, train_Y), (test_X, test_Y) = fashion_mnist.load_data()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "6ab39f57-1458-4220-9a47-bc647733af36",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 2 Axes>"
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
    "plt.imshow(train_X[3],cmap='gray')\n",
    "plt.colorbar()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "dc18e2cf-0fce-4d81-b3bb-2877eb6a20ba",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "train_Y[3] :  3\n"
     ]
    }
   ],
   "source": [
    "print(\"train_Y[3] : \",train_Y[3])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "f39c56c4-a0c7-4924-b236-988918da2260",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[  0   0   0   0   0   0   0   0  33  96 175 156  64  14  54 137 204 194\n",
      "  102   0   0   0   0   0   0   0   0   0]\n",
      " [  0   0   0   0   0   0  73 186 177 183 175 188 232 255 223 219 194 179\n",
      "  186 213 146   0   0   0   0   0   0   0]\n",
      " [  0   0   0   0   0  35 163 140 150 152 150 146 175 175 173 171 156 152\n",
      "  148 129 156 140   0   0   0   0   0   0]\n",
      " [  0   0   0   0   0 150 142 140 152 160 156 146 142 127 135 133 140 140\n",
      "  137 133 125 169  75   0   0   0   0   0]\n",
      " [  0   0   0   0   0  54 167 146 129 142 137 137 131 148 148 133 131 131\n",
      "  131 125 140 140   0   0   0   0   0   0]\n",
      " [  0   0   0   0   0   0 110 188 133 146 152 133 125 127 119 129 133 119\n",
      "  140 131 150  14   0   0   0   0   0   0]\n",
      " [  0   0   0   0   0   0   0 221 158 137 135 123 110 110 114 108 112 117\n",
      "  127 142  77   0   0   0   0   0   0   0]\n",
      " [  0   0   0   0   0   4   0  25 158 137 125 119 119 110 117 117 110 119\n",
      "  127 144   0   0   0   0   0   0   0   0]\n",
      " [  0   0   0   0   0   0   0   0 123 156 129 112 110 102 112 100 121 117\n",
      "  129 114   0   0   0   0   0   0   0   0]\n",
      " [  0   0   0   0   0   0   0   0 125 169 127 119 106 108 104  94 121 114\n",
      "  129  91   0   0   0   0   0   0   0   0]\n",
      " [  0   0   0   0   0   0   2   0  98 171 129 112 104 114 106 102 112 104\n",
      "  133  64   0   4   0   0   0   0   0   0]\n",
      " [  0   0   0   0   0   0   2   0  66 173 135 129  98 100 119 102 108  98\n",
      "  135  60   0   4   0   0   0   0   0   0]\n",
      " [  0   0   0   0   0   0   2   0  56 171 135 127 100 108 117  85 106 110\n",
      "  135  66   0   4   0   0   0   0   0   0]\n",
      " [  0   0   0   0   0   0   0   0  52 150 129 110 100  91 102  94  83 104\n",
      "  123  66   0   4   0   0   0   0   0   0]\n",
      " [  0   0   0   0   0   0   2   0  66 167 140 148 148 127 137 152 146 146\n",
      "  148  96   0   0   0   0   0   0   0   0]\n",
      " [  0   0   0   0   0   0   0   0  45 123  94 104  96 119 121 106  98 112\n",
      "   87 114   0   0   0   0   0   0   0   0]\n",
      " [  0   0   0   0   0   0   0   0 106  89  58  50  37  50  66  56  50  75\n",
      "   75 137  22   0   2   0   0   0   0   0]\n",
      " [  0   0   0   0   0   2   0  29 148 114 106 125  89 100 133 117 131 131\n",
      "  131 125 112   0   0   0   0   0   0   0]\n",
      " [  0   0   0   0   0   0   0 100 106 114  91 137  62 102 131  89 135 112\n",
      "  131 108 135  37   0   0   0   0   0   0]\n",
      " [  0   0   0   0   0   0   0 146 100 108  98 144  62 106 131  87 133 104\n",
      "  160 117 121  68   0   0   0   0   0   0]\n",
      " [  0   0   0   0   0   0  33 121 108  96 100 140  71 106 127  85 140 104\n",
      "  150 140 114  89   0   0   0   0   0   0]\n",
      " [  0   0   0   0   0   0  62 119 112 102 110 137  75 106 144  81 144 108\n",
      "  117 154 117 104  18   0   0   0   0   0]\n",
      " [  0   0   0   0   0   0  66 121 102 112 117 131  73 104 156  77 137 135\n",
      "   83 179 129 121  35   0   0   0   0   0]\n",
      " [  0   0   0   0   0   0  85 127  81 125 133 119  79 100 169  83 129 175\n",
      "   60 163 135 146  39   0   0   0   0   0]\n",
      " [  0   0   0   0   0   0 106 129  62 140 144 108  85  83 158  85 129 175\n",
      "   48 146 133 135  64   0   0   0   0   0]\n",
      " [  0   0   0   0   0   0 117 119  79 140 152 102  89 110 137  96 150 196\n",
      "   83 144 135 133  77   0   0   0   0   0]\n",
      " [  0   0   0   0   0   0 154 121  87 140 154 112  94  52 142 100  83 152\n",
      "   85 160 133 100  12   0   0   0   0   0]\n",
      " [  0   0   0   0   0   0   4   0   2   0  35   4  33   0   0   0   0   0\n",
      "    0   0   0   0   0   0   0   0   0   0]]\n"
     ]
    }
   ],
   "source": [
    "print(train_X[3])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "2be491e4-d244-4c95-a38b-85de9b6cd216",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "train_X[3].shape :  (28, 28)\n",
      "train_X[3].ndim :  2\n"
     ]
    }
   ],
   "source": [
    "print(\"train_X[3].shape : \", train_X[5].shape)\n",
    "print(\"train_X[3].ndim : \",train_X[5].ndim) #데이터,색깔하면 3차원"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "ebc142f5-7f16-4d3f-b218-755d6a072f9a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[[0, 0, 0, ..., 0, 0, 0],\n",
       "        [0, 0, 0, ..., 0, 0, 0],\n",
       "        [0, 0, 0, ..., 0, 0, 0],\n",
       "        ...,\n",
       "        [0, 0, 0, ..., 0, 0, 0],\n",
       "        [0, 0, 0, ..., 0, 0, 0],\n",
       "        [0, 0, 0, ..., 0, 0, 0]],\n",
       "\n",
       "       [[0, 0, 0, ..., 0, 0, 0],\n",
       "        [0, 0, 0, ..., 0, 0, 0],\n",
       "        [0, 0, 0, ..., 0, 0, 0],\n",
       "        ...,\n",
       "        [0, 0, 0, ..., 0, 0, 0],\n",
       "        [0, 0, 0, ..., 0, 0, 0],\n",
       "        [0, 0, 0, ..., 0, 0, 0]],\n",
       "\n",
       "       [[0, 0, 0, ..., 0, 0, 0],\n",
       "        [0, 0, 0, ..., 0, 0, 0],\n",
       "        [0, 0, 0, ..., 0, 0, 0],\n",
       "        ...,\n",
       "        [0, 0, 0, ..., 0, 0, 0],\n",
       "        [0, 0, 0, ..., 0, 0, 0],\n",
       "        [0, 0, 0, ..., 0, 0, 0]],\n",
       "\n",
       "       ...,\n",
       "\n",
       "       [[0, 0, 0, ..., 0, 0, 0],\n",
       "        [0, 0, 0, ..., 0, 0, 0],\n",
       "        [0, 0, 0, ..., 0, 0, 0],\n",
       "        ...,\n",
       "        [0, 0, 0, ..., 0, 0, 0],\n",
       "        [0, 0, 0, ..., 0, 0, 0],\n",
       "        [0, 0, 0, ..., 0, 0, 0]],\n",
       "\n",
       "       [[0, 0, 0, ..., 0, 0, 0],\n",
       "        [0, 0, 0, ..., 0, 0, 0],\n",
       "        [0, 0, 0, ..., 0, 0, 0],\n",
       "        ...,\n",
       "        [0, 0, 0, ..., 0, 0, 0],\n",
       "        [0, 0, 0, ..., 0, 0, 0],\n",
       "        [0, 0, 0, ..., 0, 0, 0]],\n",
       "\n",
       "       [[0, 0, 0, ..., 0, 0, 0],\n",
       "        [0, 0, 0, ..., 0, 0, 0],\n",
       "        [0, 0, 0, ..., 0, 0, 0],\n",
       "        ...,\n",
       "        [0, 0, 0, ..., 0, 0, 0],\n",
       "        [0, 0, 0, ..., 0, 0, 0],\n",
       "        [0, 0, 0, ..., 0, 0, 0]]], dtype=uint8)"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train_X"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "f1a8ae34-4037-4ddc-8ca4-dd0108e9d320",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(28, 28)"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train_X_flat = train_X[0].flatten()\n",
    "train_X[0].shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "a008d211-f1ad-4761-8cdd-04803514ca74",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train_X[0].ndim"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "0af8973f-2a9b-4747-a210-6e61e99e0195",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(784,)"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train_X_flat.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "c9277edd-daa4-4e6b-b830-da80c0e3eaef",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train_X_flat.ndim"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "47f69e20-93e5-47f4-bd9e-4790f787efb3",
   "metadata": {},
   "outputs": [],
   "source": [
    "input_cnt = len(train_X_flat) #784\n",
    "output_cnt = len(set(train_Y)) #10"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "5f319219-d3c7-41ab-bdde-817d8e295997",
   "metadata": {},
   "outputs": [],
   "source": [
    "weight = np.random.normal(0,1,[input_cnt,output_cnt]) #가중치 만들기\n",
    "bias = np.random.normal(0,1,[output_cnt])\n",
    "\n",
    "parameter = {'w' : weight, 'b' : bias}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "fe3ba8e1-c7ca-4ca8-8276-1d4010f623e7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(784, 10)"
      ]
     },
     "execution_count": 55,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "parameter['w'].shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "c9b3b1fa-c84f-471a-9bd6-8279d3b52d11",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "parameter['w'].ndim"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "8e71da7a-db9c-498a-b0cc-1937a14a2d92",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_w = pd.DataFrame(parameter['w'],\n",
    "             columns=['w1','w2','w3','w4','w5','w6','w7','w8','w9','w10'])\n",
    "df_b = pd.DataFrame(parameter['b'],columns=['b'])\n",
    "df_x = pd.DataFrame(train_X_flat,columns=['input_data'])\n",
    "df_data = pd.concat([df_x, df_w, df_b], axis = 1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "5eda7400-ad9f-415c-a0aa-9c87a706b5dd",
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
       "      <th>input_data</th>\n",
       "      <th>w1</th>\n",
       "      <th>w2</th>\n",
       "      <th>w3</th>\n",
       "      <th>w4</th>\n",
       "      <th>w5</th>\n",
       "      <th>w6</th>\n",
       "      <th>w7</th>\n",
       "      <th>w8</th>\n",
       "      <th>w9</th>\n",
       "      <th>w10</th>\n",
       "      <th>b</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>0.279218</td>\n",
       "      <td>-0.462796</td>\n",
       "      <td>0.746220</td>\n",
       "      <td>1.513011</td>\n",
       "      <td>-0.539327</td>\n",
       "      <td>0.624606</td>\n",
       "      <td>0.335401</td>\n",
       "      <td>0.528185</td>\n",
       "      <td>-1.335286</td>\n",
       "      <td>-2.395922</td>\n",
       "      <td>0.186218</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0</td>\n",
       "      <td>-0.273332</td>\n",
       "      <td>-0.684938</td>\n",
       "      <td>0.826777</td>\n",
       "      <td>0.108520</td>\n",
       "      <td>0.093063</td>\n",
       "      <td>-0.738021</td>\n",
       "      <td>0.957770</td>\n",
       "      <td>0.800769</td>\n",
       "      <td>-0.643039</td>\n",
       "      <td>2.078472</td>\n",
       "      <td>-0.032658</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0</td>\n",
       "      <td>0.324454</td>\n",
       "      <td>-1.498118</td>\n",
       "      <td>1.596344</td>\n",
       "      <td>0.600882</td>\n",
       "      <td>-0.732141</td>\n",
       "      <td>1.536219</td>\n",
       "      <td>-0.554721</td>\n",
       "      <td>-0.165569</td>\n",
       "      <td>0.474437</td>\n",
       "      <td>0.238963</td>\n",
       "      <td>0.322764</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0</td>\n",
       "      <td>-1.796723</td>\n",
       "      <td>1.764806</td>\n",
       "      <td>-1.755840</td>\n",
       "      <td>0.435550</td>\n",
       "      <td>0.027957</td>\n",
       "      <td>1.753932</td>\n",
       "      <td>1.810881</td>\n",
       "      <td>-1.775361</td>\n",
       "      <td>0.837745</td>\n",
       "      <td>0.764670</td>\n",
       "      <td>0.489934</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0</td>\n",
       "      <td>0.290645</td>\n",
       "      <td>1.413451</td>\n",
       "      <td>0.672426</td>\n",
       "      <td>0.365573</td>\n",
       "      <td>-0.239137</td>\n",
       "      <td>0.393250</td>\n",
       "      <td>0.641731</td>\n",
       "      <td>-0.037458</td>\n",
       "      <td>-0.063692</td>\n",
       "      <td>-1.328710</td>\n",
       "      <td>-0.725602</td>\n",
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
       "    </tr>\n",
       "    <tr>\n",
       "      <th>779</th>\n",
       "      <td>0</td>\n",
       "      <td>-0.203591</td>\n",
       "      <td>-0.729639</td>\n",
       "      <td>-1.673973</td>\n",
       "      <td>-1.904095</td>\n",
       "      <td>-0.645502</td>\n",
       "      <td>0.249906</td>\n",
       "      <td>-1.559224</td>\n",
       "      <td>0.148749</td>\n",
       "      <td>0.360745</td>\n",
       "      <td>-0.363968</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>780</th>\n",
       "      <td>0</td>\n",
       "      <td>1.523346</td>\n",
       "      <td>0.879687</td>\n",
       "      <td>-0.106200</td>\n",
       "      <td>-0.556362</td>\n",
       "      <td>0.908889</td>\n",
       "      <td>1.652006</td>\n",
       "      <td>1.101188</td>\n",
       "      <td>-0.068671</td>\n",
       "      <td>1.339013</td>\n",
       "      <td>0.014558</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>781</th>\n",
       "      <td>0</td>\n",
       "      <td>-0.661850</td>\n",
       "      <td>-0.573280</td>\n",
       "      <td>0.635693</td>\n",
       "      <td>-1.274135</td>\n",
       "      <td>-0.670377</td>\n",
       "      <td>-0.739098</td>\n",
       "      <td>0.718397</td>\n",
       "      <td>-0.712185</td>\n",
       "      <td>0.171124</td>\n",
       "      <td>1.755617</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>782</th>\n",
       "      <td>0</td>\n",
       "      <td>0.149736</td>\n",
       "      <td>1.426823</td>\n",
       "      <td>-0.461722</td>\n",
       "      <td>0.253563</td>\n",
       "      <td>1.534483</td>\n",
       "      <td>-1.113741</td>\n",
       "      <td>-2.547088</td>\n",
       "      <td>0.375978</td>\n",
       "      <td>0.062207</td>\n",
       "      <td>-0.029240</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>783</th>\n",
       "      <td>0</td>\n",
       "      <td>0.188832</td>\n",
       "      <td>0.935303</td>\n",
       "      <td>-0.482876</td>\n",
       "      <td>0.661183</td>\n",
       "      <td>0.814963</td>\n",
       "      <td>-0.552813</td>\n",
       "      <td>-1.641342</td>\n",
       "      <td>-0.072565</td>\n",
       "      <td>0.200321</td>\n",
       "      <td>-0.445379</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>784 rows × 12 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "     input_data        w1        w2        w3        w4        w5        w6  \\\n",
       "0             0  0.279218 -0.462796  0.746220  1.513011 -0.539327  0.624606   \n",
       "1             0 -0.273332 -0.684938  0.826777  0.108520  0.093063 -0.738021   \n",
       "2             0  0.324454 -1.498118  1.596344  0.600882 -0.732141  1.536219   \n",
       "3             0 -1.796723  1.764806 -1.755840  0.435550  0.027957  1.753932   \n",
       "4             0  0.290645  1.413451  0.672426  0.365573 -0.239137  0.393250   \n",
       "..          ...       ...       ...       ...       ...       ...       ...   \n",
       "779           0 -0.203591 -0.729639 -1.673973 -1.904095 -0.645502  0.249906   \n",
       "780           0  1.523346  0.879687 -0.106200 -0.556362  0.908889  1.652006   \n",
       "781           0 -0.661850 -0.573280  0.635693 -1.274135 -0.670377 -0.739098   \n",
       "782           0  0.149736  1.426823 -0.461722  0.253563  1.534483 -1.113741   \n",
       "783           0  0.188832  0.935303 -0.482876  0.661183  0.814963 -0.552813   \n",
       "\n",
       "           w7        w8        w9       w10         b  \n",
       "0    0.335401  0.528185 -1.335286 -2.395922  0.186218  \n",
       "1    0.957770  0.800769 -0.643039  2.078472 -0.032658  \n",
       "2   -0.554721 -0.165569  0.474437  0.238963  0.322764  \n",
       "3    1.810881 -1.775361  0.837745  0.764670  0.489934  \n",
       "4    0.641731 -0.037458 -0.063692 -1.328710 -0.725602  \n",
       "..        ...       ...       ...       ...       ...  \n",
       "779 -1.559224  0.148749  0.360745 -0.363968       NaN  \n",
       "780  1.101188 -0.068671  1.339013  0.014558       NaN  \n",
       "781  0.718397 -0.712185  0.171124  1.755617       NaN  \n",
       "782 -2.547088  0.375978  0.062207 -0.029240       NaN  \n",
       "783 -1.641342 -0.072565  0.200321 -0.445379       NaN  \n",
       "\n",
       "[784 rows x 12 columns]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "display(df_data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "4372e252-2e8c-41aa-b896-4f9ec7e67719",
   "metadata": {},
   "outputs": [],
   "source": [
    "y_hat_1 = np.matmul(df_data['input_data'],df_data['w1'])+df_data['b'][0]\n",
    "y_hat_2 = np.matmul(df_data['input_data'],df_data['w2'])+df_data['b'][1]\n",
    "y_hat_3 = np.matmul(df_data['input_data'],df_data['w3'])+df_data['b'][2]\n",
    "y_hat_4 = np.matmul(df_data['input_data'],df_data['w4'])+df_data['b'][3]\n",
    "y_hat_5 = np.matmul(df_data['input_data'],df_data['w5'])+df_data['b'][4]\n",
    "y_hat_6 = np.matmul(df_data['input_data'],df_data['w6'])+df_data['b'][5]\n",
    "y_hat_7 = np.matmul(df_data['input_data'],df_data['w7'])+df_data['b'][6]\n",
    "y_hat_8 = np.matmul(df_data['input_data'],df_data['w8'])+df_data['b'][7]\n",
    "y_hat_9 = np.matmul(df_data['input_data'],df_data['w9'])+df_data['b'][8]\n",
    "y_hat_10 = np.matmul(df_data['input_data'],df_data['w10'])+df_data['b'][9]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "c3b06457-3e27-49f6-821d-11d5e55540f9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "-4500.013846965818\n",
      "9483.296321406502\n",
      "1391.159767033435\n",
      "4487.771188140036\n",
      "-8566.649011169719\n",
      "-853.6379485157718\n",
      "-3698.1496755847716\n",
      "1077.8422414722002\n",
      "2167.773747452377\n",
      "3343.647743018936\n"
     ]
    }
   ],
   "source": [
    "print(y_hat_1)\n",
    "print(y_hat_2)\n",
    "print(y_hat_3)\n",
    "print(y_hat_4)\n",
    "print(y_hat_5)\n",
    "print(y_hat_6)\n",
    "print(y_hat_7)\n",
    "print(y_hat_8)\n",
    "print(y_hat_9)\n",
    "print(y_hat_10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "8f32e7f8-408b-4afb-8afe-fe6804e7aa22",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[-4500.01384697  9483.29632141  1391.15976703  4487.77118814\n",
      " -8566.64901117  -853.63794852 -3698.14967558  1077.84224147\n",
      "  2167.77374745  3343.64774302]\n"
     ]
    }
   ],
   "source": [
    "y_hat_total = np.matmul(df_data['input_data'],parameter['w'])+parameter['b']\n",
    "print(y_hat_total) #한번에 가중치, 편향값까지 계산"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "1f3642f3-bc91-4630-8f13-1ec38c4a81fd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2.718\n"
     ]
    }
   ],
   "source": [
    "print(np.round(np.exp(1),3)) # 반올림"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "id": "6b0beadd-560f-4098-8df2-314cc5624b2e",
   "metadata": {},
   "outputs": [],
   "source": [
    "kor_hat = 2\n",
    "chn_hat = 1\n",
    "usa_hat = 1.2\n",
    "rus_hat = 0.7\n",
    "\n",
    "kor_e = np.exp(kor_hat)\n",
    "chn_e = np.exp(chn_hat)\n",
    "usa_e = np.exp(usa_hat)\n",
    "rus_e = np.exp(rus_hat)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "id": "c8f90ae5-84b5-47e4-8e71-500caf316114",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "47.85\n"
     ]
    }
   ],
   "source": [
    "kor_w = kor_e/(kor_e+chn_e+usa_e+rus_e)\n",
    "print(np.round(kor_w*100,2))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "id": "d13dc678-0c22-4892-9d87-f3eb24f61a53",
   "metadata": {},
   "outputs": [],
   "source": [
    "def win_p(nation_n,nation_e) :\n",
    "    nation_n = str(nation_n)\n",
    "    win_p = nation_e / (kor_e+chn_e+usa_e+rus_e)\n",
    "    win_p = np.round(win_p*100,2)\n",
    "    print(\"{0} : {1}%\".format(nation_n,win_p))\n",
    "    \n",
    "    return win_p"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "id": "f4db4d12-46be-4158-bcd3-69b151a585ca",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "KOREA : 47.85%\n",
      "CHINA : 17.6%\n",
      "USA : 21.5%\n",
      "RUSSIA : 13.04%\n"
     ]
    }
   ],
   "source": [
    "dataset = ['KOREA',\"CHINA\",\"USA\",\"RUSSIA\"]\n",
    "dataset_e = [kor_e,chn_e,usa_e,rus_e]\n",
    "\n",
    "dataset_row = []\n",
    "\n",
    "for i in range(len(dataset)) :\n",
    "    dataset_row.append(win_p(dataset[i],dataset_e[i]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "id": "2e53bf2f-b2ee-49a5-acb0-6d153862130d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Pred - KOREA\n"
     ]
    }
   ],
   "source": [
    "def pred_label(dataset_row):\n",
    "    for i in range(len(dataset)):\n",
    "        if np.argmax(dataset_row) == i :\n",
    "            print(\"Pred -\",dataset[i],)\n",
    "\n",
    "pred_label(dataset_row)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "id": "55f726f8-632b-4df3-a185-fb754e690cb4",
   "metadata": {},
   "outputs": [],
   "source": [
    "import sklearn"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "id": "2b24c74b-dcf2-4d31-832d-8d753bac16e6",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.tree import DecisionTreeClassifier"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d871881b-f495-4ec4-b448-f78dca9c5f3e",
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
