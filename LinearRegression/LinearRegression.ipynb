{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "05ec7ae7-ed39-46ed-995d-8db42a2d37df",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "from sklearn import linear_model\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "974782dd-dd7a-445a-ac45-2a4ebb83ed1c",
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
       "      <th>area</th>\n",
       "      <th>price</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2600</td>\n",
       "      <td>550000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>3000</td>\n",
       "      <td>565000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3200</td>\n",
       "      <td>610000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3600</td>\n",
       "      <td>680000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>4000</td>\n",
       "      <td>725000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   area   price\n",
       "0  2600  550000\n",
       "1  3000  565000\n",
       "2  3200  610000\n",
       "3  3600  680000\n",
       "4  4000  725000"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.read_csv(\"C:/Users/anush/Downloads/homeprices.csv\")\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "c468e368-7adf-4d4a-9af7-55cd8a24f158",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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h+uenp645557aiwpP378ODp27AgACAkJgYeHB3bu3Klez8/PR1ZWFgYNGgQACA0NhdVqRWpqqhpz4MABWK1WNUYL12u/3W6H3W6Hu7vjP7NmzZqpvWWNuf1XIyIoLy9H586dYTAYHNpWUVGBr776Ss27Kbcf+KUIys7ORnJyMtq0aeMQ25TbHxUVhUOHDuHgwYPqy2g04rnnnsOOHTsANM32A7+8B039M/BqLrXfFT4DR44ciczMTId/5/3790dkZCQOHjyIX/3qVw3/c/Cmplq7uKeeekr0er3s3r1b8vPz1deFCxfUmE2bNomHh4e89957kp2dLcuWLZNmzZrJ3r171ZiZM2dKcHCwJCcnS0ZGhowYMaLWZYO9evUSs9ksZrNZevbsqfnSybq0PywsTHr06CG7du2SEydOyOrVq6VFixayfPlyNaaxtl9EZMGCBbJnzx7JycmRQ4cOyQsvvCDu7u6SlJQkIsqyUb1eL5s2bZLMzEyZPHlyrctGm2L77Xa7jB8/XoKDg+XgwYMO/0bKy8vVezTV9tfmylVjIo27/SLXfw+a8megyPXb39Q/A2tz+aoxkYb/OchC6CYAqPW1evVqh7hVq1bJr3/9a2nRooX07t3b4fkRIiIXL16U2NhY8fPzEy8vL4mIiJDc3FyHmOLiYomMjBQfHx/x8fGRyMhIsVgst7iF11aX9ufn58v06dPFaDRKixYt5K677pI33nhDqqur1ZjG2n4Rkccee0w6duwonp6e0rZtWxk5cqTDl2B1dbW89NJLYjAYRKfTydChQyUzM9PhHk21/Tk5OVf9N7Jr1y71Hk21/bWprRBqzO0Xqdt70FQ/A0Wu3/6m/hlYmysLoYb+OegmInJzfUpEREREjRPnCBEREZHLYiFERERELouFEBEREbksFkJERETkslgIERERkctiIUREREQui4UQERERuSwWQkREROSyWAgRERGRy2IhRERERC6LhRARERG5LBZCRERE5LL+P7wmEbZOch3mAAAAAElFTkSuQmCC",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "%matplotlib inline\n",
    "\n",
    "df = pd.read_csv(\"C:/Users/anush/Downloads/homeprices.csv\")\n",
    "plt.scatter(df.area, df.price, color='red', marker='+')\n",
    "plt.plot(df.area, reg.predict(df[['area']]), color='blue')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "42e280e6-6d57-452a-bb02-72cda2de5e03",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([628715.75342466])"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "reg.predict(pd.DataFrame([[3300]], columns=['area']))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "552e90f2-dea1-4f09-93cf-52b00905e422",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([135.78767123])"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "reg.coef_"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "6f1ac27c-530a-477d-a753-a7527236c6af",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "180616.43835616432"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "reg.intercept_"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "825bf2a4-3e39-4583-92d3-361592737095",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "628715.7534151643"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#y=m*x+b\n",
    "135.78767123*3300+180616.43835616432"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "9a1efc38-1dab-4bf9-9710-b321cf2edcd9",
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
       "      <th>area</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1500</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2300</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3540</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>4120</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>4560</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   area\n",
       "0  1000\n",
       "1  1500\n",
       "2  2300\n",
       "3  3540\n",
       "4  4120\n",
       "5  4560"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d = pd.read_csv(r\"C:\\Users\\anush\\Downloads\\areas.csv\")\n",
    "d.head(6)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "98eed2e7-90b1-4738-81f6-0588859bb62e",
   "metadata": {},
   "outputs": [],
   "source": [
    "p = reg.predict(d)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "d8923c1d-3338-4253-9ec3-e2e87cafa087",
   "metadata": {},
   "outputs": [],
   "source": [
    "d['prices']=p"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "cd80374e-9338-4c21-af3e-3b0c3db9b57d",
   "metadata": {},
   "outputs": [],
   "source": [
    "d.to_csv('prediction.csv',index=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "421c3808-4c36-4788-80cb-196bb7080583",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
