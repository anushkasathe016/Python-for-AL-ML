{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "88ee601c-107b-4ab4-bee8-07c5461bc9b1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello world\n"
     ]
    }
   ],
   "source": [
    "print(\"Hello world\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "58497fa3-9f15-49f1-aa11-59bfe927a4a4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "123\n"
     ]
    }
   ],
   "source": [
    "print(\"123\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1dd69ea5-c552-411c-b12e-dcd4cded044f",
   "metadata": {},
   "source": [
    "# VARIABLES"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "beb013ab-1b03-4908-8c8f-71c72ae6543a",
   "metadata": {},
   "outputs": [],
   "source": [
    "x=3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "ab477c21-30a0-4ea6-8736-716e2df69aca",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Variable   Type    Data/Info\n",
      "----------------------------\n",
      "x          int     3\n"
     ]
    }
   ],
   "source": [
    "%whos"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "9c6c2f43-06ec-4044-897c-b3270250d077",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'int'>\n"
     ]
    }
   ],
   "source": [
    "print(type(x))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "be0c41a6-e73c-47c2-a5f0-37c8ac23933a",
   "metadata": {},
   "outputs": [],
   "source": [
    "x=5.7"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "33eb8a18-0e90-47b7-bd92-89db4464ed6f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Variable   Type     Data/Info\n",
      "-----------------------------\n",
      "x          float    5.7\n"
     ]
    }
   ],
   "source": [
    "%whos"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "29b022c3-9d4e-49e1-96fd-741ab76ec42e",
   "metadata": {},
   "outputs": [],
   "source": [
    "abcd=55.3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "37086b27-0d23-44f0-829b-1760a899d4c0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Variable   Type     Data/Info\n",
      "-----------------------------\n",
      "abcd       float    55.3\n",
      "x          float    5.7\n"
     ]
    }
   ],
   "source": [
    "%whos"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "7a420598-b415-4057-9578-1556a7cc45fb",
   "metadata": {},
   "outputs": [],
   "source": [
    "a,b,c,d,f=3,5,6.0,-3,5.2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "f4ee30a7-5a63-4275-8e3f-6f5252c0f3ed",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Variable   Type     Data/Info\n",
      "-----------------------------\n",
      "a          int      3\n",
      "abcd       float    55.3\n",
      "b          int      5\n",
      "c          float    6.0\n",
      "d          int      -3\n",
      "f          float    5.2\n",
      "x          float    5.7\n"
     ]
    }
   ],
   "source": [
    "%whos"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "7e46397f-cefb-4b6c-a670-d7613271daec",
   "metadata": {},
   "outputs": [],
   "source": [
    "del abcd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "f309a2a7-9a0d-4eac-869a-d25820b4d20f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Variable   Type     Data/Info\n",
      "-----------------------------\n",
      "a          int      3\n",
      "b          int      5\n",
      "c          float    6.0\n",
      "d          int      -3\n",
      "f          float    5.2\n",
      "x          float    5.7\n"
     ]
    }
   ],
   "source": [
    "%whos"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "4181dc6c-fd39-4f3c-bc9d-ea6cf8d143be",
   "metadata": {},
   "outputs": [],
   "source": [
    "c=2+4j"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "7c22e45c-85a7-4b8e-93c7-f6ecb2054828",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'complex'>\n"
     ]
    }
   ],
   "source": [
    "print(type(c))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "41c7578c-d3a4-4bf3-8a4a-c6ac89caea57",
   "metadata": {},
   "outputs": [],
   "source": [
    "s=\"hello how are you\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "dca7869f-7847-4553-911b-e3a5ccd862a7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'str'>\n"
     ]
    }
   ],
   "source": [
    "print(type(s))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a205315e-77d8-4253-b99a-3a6774a8a7d9",
   "metadata": {},
   "source": [
    "# OPERATORS"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "4a326f62-60dc-4b3f-bb74-793166e6e2bd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Variable   Type       Data/Info\n",
      "-------------------------------\n",
      "a          int        3\n",
      "b          int        5\n",
      "c          complex    (2+4j)\n",
      "d          int        -3\n",
      "f          float      5.2\n",
      "s          str        hello how are you\n",
      "x          float      5.7\n"
     ]
    }
   ],
   "source": [
    "%whos"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "8ace3865-55f0-441a-9cc3-8156ba6de7cd",
   "metadata": {},
   "outputs": [],
   "source": [
    "sumOfaAndb=a+b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "3d21bcd2-2c21-479d-8799-29b7ad33ad7e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "8\n"
     ]
    }
   ],
   "source": [
    "print(sumOfaAndb)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "e54d3b41-1df4-49de-a95b-c5d6dbc2d69c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'int'>\n"
     ]
    }
   ],
   "source": [
    "print(type(sumOfaAndb))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "5d445563-78ae-407c-a7ae-645ba4c615da",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "int"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(a+b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "6933f391-aea2-4718-aec6-ff0ac63b0bdb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "float"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(a+f)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "698a5095-439f-4be2-93ab-b9842a6100ab",
   "metadata": {},
   "outputs": [],
   "source": [
    "v=((a+f)**3)/4"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "07022262-121a-42eb-9e62-32e61e4573a4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "137.84199999999996\n"
     ]
    }
   ],
   "source": [
    "print(v)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "e4af2761-fca6-4f7f-921f-76fd606b5ddd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello how are you\n"
     ]
    }
   ],
   "source": [
    "a1=\"hellow\"\n",
    "a2=\"world\"\n",
    "ss=a1+a2\n",
    "print(s)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "37acbf27-bf66-439c-a864-6e37f772600e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "10//3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "aec1eafb-0648-4154-b381-e45d980309f7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3.3333333333333335"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "10/3"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a5f9491b-89ce-4f24-9a4e-d45d6d11e58b",
   "metadata": {},
   "source": [
    "# BOOLEAN"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "787cc2f7-a125-4318-a2e1-1d20fc1589dd",
   "metadata": {},
   "outputs": [],
   "source": [
    "a=True\n",
    "b=True\n",
    "c=False"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "c2decbba-6391-4e25-b63d-c4ffd2e37f7d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Variable     Type     Data/Info\n",
      "-------------------------------\n",
      "a            bool     True\n",
      "a1           str      hellow\n",
      "a2           str      world\n",
      "b            bool     True\n",
      "c            bool     False\n",
      "d            int      -3\n",
      "f            float    5.2\n",
      "s            str      hello how are you\n",
      "ss           str      hellowworld\n",
      "sumOfaAndb   int      8\n",
      "v            float    137.84199999999996\n",
      "x            float    5.7\n"
     ]
    }
   ],
   "source": [
    " %whos"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "f4bf2de8-2cc9-4fd9-b5c5-702946cb97a9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "False\n",
      "False\n"
     ]
    }
   ],
   "source": [
    "print (a and b)\n",
    "print (a and c)\n",
    "print (c and a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "841597fb-e381-4004-9981-c32db0b95839",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "d=a or c\n",
    "print(d)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "6a565660-af07-4930-a248-d6d158d5a385",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "not(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "f6295684-959f-4e41-808a-b5aace469e1d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "not(b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "d92f2d2d-701f-40b6-92e4-aee100b05d15",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "not(c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "fb579e53-b0a2-49e4-abf6-42a68d8bc888",
   "metadata": {},
   "outputs": [],
   "source": [
    "t=not(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "0858c7d7-8bea-428b-ae17-05cecccacdff",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "bool"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(t)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "817f8742-aa0a-4d26-9f8a-b4cf1fa4c6db",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n"
     ]
    }
   ],
   "source": [
    "print(t)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "37698c90-668f-4f86-8697-b6afe2eeb815",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "not((a and b) or (c or d))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9b111c30-c571-4048-bc3a-9f1114489167",
   "metadata": {},
   "source": [
    "# COMPARISONS"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "6a63bda7-5434-475d-a03c-20aa75552adb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "print(2<3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "b95ca238-8b26-4d04-befb-aa0d06edd193",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'bool'>\n"
     ]
    }
   ],
   "source": [
    "c=2<3\n",
    "print(type(c))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "d7a3443d-d69b-4ae9-9109-3fb1f8f77654",
   "metadata": {},
   "outputs": [],
   "source": [
    "d=3==4"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "bb3b2dfb-cee5-4c90-8287-0362bf7fc086",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n"
     ]
    }
   ],
   "source": [
    "print(d)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "59c9e403-1068-4f17-af3b-1ecf1fcb662c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "3==3.0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "09599397-ecf3-4694-b735-8b197cb0bab3",
   "metadata": {},
   "outputs": [],
   "source": [
    "x=4\n",
    "y=9\n",
    "z=8.3\n",
    "r=-3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "57dff4f2-cd0e-490c-b9e0-da83d8e75846",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 51,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "(x<y) and (z<y) or (r==)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "18141c84-ae15-4b3f-ba36-4eec2896bd59",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 52,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "(x<y) and (r==x) or (z>y) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "ba67ad56-45b6-4e2b-bcb5-3ffd8fbed7bd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "(r==x)and(x<y)or(z>y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "96f7e568-8275-41ad-bc42-1273738b4cef",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "False or False and True"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "6f721ac8-0597-4b8b-89bb-ead022f4ab52",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 55,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "(True or False)and False"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "c693f777-81c3-46e5-89b3-550911866013",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n"
     ]
    }
   ],
   "source": [
    "print((not(2!=3) and True)or(False and True))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "d642bdd4-99d2-47d7-9ba6-de1eb47ed1d0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n"
     ]
    }
   ],
   "source": [
    "print(round(4.556))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "07a2555f-0469-4022-953d-285dd84147bf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4\n"
     ]
    }
   ],
   "source": [
    "print(round(4.345))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "de44f7a7-e44a-401d-87dc-670bed7e9c33",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4.446\n"
     ]
    }
   ],
   "source": [
    "print(round(4.446389,3))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "3e4c5822-aa5e-4b21-a360-abf04af45d8a",
   "metadata": {},
   "outputs": [],
   "source": [
    "g=divmod(34,9)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "7485c1e8-3ba3-4cfc-985c-01526b4c4a3a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "tuple"
      ]
     },
     "execution_count": 64,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(g)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "cf4e2446-447d-40c7-bfb6-22055c624142",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(3, 7)\n"
     ]
    }
   ],
   "source": [
    "print(g)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "0a92efca-7b22-4dff-b6b9-be7587257e4c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 66,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "g[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "704a331d-324b-4d1e-94cc-92be048e58c2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "7"
      ]
     },
     "execution_count": 67,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "g[1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "id": "8c56b05d-81cf-4744-84ed-99f3be78260e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 68,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "34//9"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "id": "adebc23a-b561-4a3f-8d60-36adf5466243",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "7"
      ]
     },
     "execution_count": 69,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "34%9"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "id": "597923a8-c8d8-4256-a26c-292ae201835e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 70,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "isinstance(3,int)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "19420642-59a5-4165-9b84-ded49bb7d451",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 71,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "isinstance(3.4,float)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "id": "40345c07-0624-4bd2-b5ac-2ae084c7aa19",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 72,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "isinstance(3+3j,(int,float,str))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "id": "daf56254-b773-4a7c-8c69-cba552d325d5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 73,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "isinstance(3+3j,(complex))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "id": "e9f852a1-ad78-41f1-a1e7-e060989b34ee",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "16"
      ]
     },
     "execution_count": 74,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pow(2,4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "id": "247fcadd-2d91-4dfd-a7ee-e8e8015070f9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "16"
      ]
     },
     "execution_count": 75,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "2**4"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "id": "4489b1bc-f0a5-4604-9d0f-647686e383f9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 76,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pow(2,4,7)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "id": "45cdcf8a-d337-4a3c-9d26-f3e2488988be",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a number 56\n"
     ]
    }
   ],
   "source": [
    "x=input(\"Enter a number\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "id": "613ff292-211a-4738-bde2-2a66f5c6fdf8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "str"
      ]
     },
     "execution_count": 78,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "id": "193f7068-1d6b-4be8-823d-6f2ee82b719d",
   "metadata": {},
   "outputs": [],
   "source": [
    "x=int(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "id": "2617123f-b5b3-490c-8c97-d47e13d25407",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "int"
      ]
     },
     "execution_count": 80,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "id": "38a29897-ce28-4606-9fed-8bbcf5f9c0d6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "22\n"
     ]
    }
   ],
   "source": [
    "print(x-34)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "id": "266ad3f8-b051-4ed5-ad2a-32c6c63f2d78",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a real number 7\n"
     ]
    }
   ],
   "source": [
    "a=int(input(\"Enter a real number\"))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "id": "5d3205ef-9aea-4167-a409-eeb0d00e02d2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter a real number :  4.3\n"
     ]
    }
   ],
   "source": [
    "b=float(input(\"enter a real number : \"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "id": "7cf9e79b-1e35-4cd0-9eca-d78608c97595",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\u001b[1;31mSignature:\u001b[0m \u001b[0mpow\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mbase\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mexp\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mmod\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mNone\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
       "\u001b[1;31mDocstring:\u001b[0m\n",
       "Equivalent to base**exp with 2 arguments or base**exp % mod with 3 arguments\n",
       "\n",
       "Some types, such as ints, are able to use a more efficient algorithm when\n",
       "invoked using the three argument form.\n",
       "\u001b[1;31mType:\u001b[0m      builtin_function_or_method"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "pow?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "id": "daec7324-f7d0-4ec8-9e1e-4adf88c1ad8e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\u001b[1;31mSignature:\u001b[0m \u001b[0mpow\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mbase\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mexp\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mmod\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mNone\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
       "\u001b[1;31mDocstring:\u001b[0m\n",
       "Equivalent to base**exp with 2 arguments or base**exp % mod with 3 arguments\n",
       "\n",
       "Some types, such as ints, are able to use a more efficient algorithm when\n",
       "invoked using the three argument form.\n",
       "\u001b[1;31mType:\u001b[0m      builtin_function_or_method"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "pow??"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "id": "2f8f176e-2dce-4144-a64c-f0d05f444cd1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Help on built-in function pow in module builtins:\n",
      "\n",
      "pow(base, exp, mod=None)\n",
      "    Equivalent to base**exp with 2 arguments or base**exp % mod with 3 arguments\n",
      "\n",
      "    Some types, such as ints, are able to use a more efficient algorithm when\n",
      "    invoked using the three argument form.\n",
      "\n"
     ]
    }
   ],
   "source": [
    "help(pow)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "id": "59252434-ef50-4eea-95da-e5bc75f5a269",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Help on method raw_input in module ipykernel.kernelbase:\n",
      "\n",
      "raw_input(prompt='') method of ipykernel.ipkernel.IPythonKernel instance\n",
      "    Forward raw_input to frontends\n",
      "\n",
      "    Raises\n",
      "    ------\n",
      "    StdinNotImplementedError if active frontend doesn't support stdin.\n",
      "\n"
     ]
    }
   ],
   "source": [
    "help(input)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a3410a21-a21d-41e1-adea-e0256609ffba",
   "metadata": {},
   "source": [
    "# CONTROL FLOW"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "id": "76fa54ed-ed2b-4beb-968e-f16fafd4b6dd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 5\n",
      " 1\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n",
      "I m still inside if condition\n",
      "I m outside if conditions\n"
     ]
    }
   ],
   "source": [
    "a=int(input())\n",
    "b=int(input())\n",
    "if a>b:\n",
    "    print(a)\n",
    "    print(\"I m still inside if condition\")\n",
    "    x=5\n",
    "print(\"I m outside if conditions\")    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "id": "f7c0b0ce-f8b3-4a38-9f94-3f4a48ab9827",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 6\n",
      " 8\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "I m outside if conditions\n"
     ]
    }
   ],
   "source": [
    "a=int(input())\n",
    "b=int(input())\n",
    "if a>b:\n",
    "    print(a)\n",
    "    print(\"I m still inside if condition\")\n",
    "    x=5\n",
    "print(\"I m outside if conditions\") "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "id": "6a6d0356-4641-4e1d-b396-cee54d966ce2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 6\n",
      " 2\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "6\n"
     ]
    }
   ],
   "source": [
    "a=int(input())\n",
    "b=int(input())\n",
    "if a>b:\n",
    "    print(a)\n",
    "if b>a:    \n",
    "    print(b)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "id": "251412af-4a9c-45b1-9730-8f2fcc248b97",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 10\n",
      " 22\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "22\n",
      "else part\n"
     ]
    }
   ],
   "source": [
    "a=int(input())\n",
    "b=int(input())\n",
    "if a>b:\n",
    "    print(a)\n",
    "    print(\"if part\")\n",
    "else:\n",
    "    print(b)\n",
    "    print(\"else part\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "id": "de2fc0a0-5df2-4196-942c-a30474f3ed03",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "B\n",
      "Not in if\n"
     ]
    }
   ],
   "source": [
    "a=1\n",
    "b=5\n",
    "if a==b:\n",
    "    print(\"Equal\")\n",
    "elif a>b:\n",
    "    print(\"A\")\n",
    "else:\n",
    "    print(\"B\")\n",
    "print(\"Not in if\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "id": "4bcea717-cb05-4fe5-944e-702be33fbc9d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter marks :  82\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "A- Grade\n"
     ]
    }
   ],
   "source": [
    "a=int(input(\"Enter marks : \"))\n",
    "if a>=85:\n",
    "    print(\"A Grade\")\n",
    "elif(a<85)and(a>=80):\n",
    "    print(\"A- Grade\")\n",
    "elif(a<80) and (a>=75):\n",
    "    print(\"B Grade\")\n",
    "elif(a<75)and(a>=70):\n",
    "    print(\"B- Grade\")\n",
    "else:\n",
    "    print(\"below avg\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "id": "fa6b2d93-4e3b-4aeb-bb82-f8167ceec684",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter marks :  35\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "below avg\n"
     ]
    }
   ],
   "source": [
    "a=int(input(\"Enter marks : \"))\n",
    "if a>=85:\n",
    "    print(\"A Grade\")\n",
    "elif(a<85)and(a>=80):\n",
    "    print(\"A- Grade\")\n",
    "elif(a<80) and (a>=75):\n",
    "    print(\"B Grade\")\n",
    "elif(a<75)and(a>=70):\n",
    "    print(\"B- Grade\")\n",
    "else:\n",
    "    print(\"below avg\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "id": "d3e3a46b-1432-43dd-b47d-8d083758a1eb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Else part\n"
     ]
    }
   ],
   "source": [
    "a=3\n",
    "if a>10:\n",
    "    print(\">10\")\n",
    "elif not(a>b):\n",
    "    print(\"Else part\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "id": "baf8c3ff-2006-462b-8079-e2096bb16895",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 12\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      ">10\n",
      "Inside the top if \n",
      "<=20\n",
      "Inside the else part of nested if\n",
      "outside all ifs\n"
     ]
    }
   ],
   "source": [
    "a= int(input())\n",
    "if a>10:\n",
    "    print(\">10\")\n",
    "    print(\"Inside the top if \")\n",
    "    if a>20:\n",
    "        print(\">20\")\n",
    "        print(\"Inside the nested if\")\n",
    "    else:\n",
    "        print(\"<=20\")\n",
    "        print(\"Inside the else part of nested if\")\n",
    "print(\"outside all ifs\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "id": "5b828b11-1a0f-481c-8dac-003a11a4c354",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 50\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      ">10\n",
      "Inside the top if \n",
      ">20\n",
      "Inside the nested if\n",
      "outside all ifs\n"
     ]
    }
   ],
   "source": [
    "a= int(input())\n",
    "if a>10:\n",
    "    print(\">10\")\n",
    "    print(\"Inside the top if \")\n",
    "    if a>20:\n",
    "        print(\">20\")\n",
    "        print(\"Inside the nested if\")\n",
    "    else:\n",
    "        print(\"<=20\")\n",
    "        print(\"Inside the else part of nested if\")\n",
    "print(\"outside all ifs\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 104,
   "id": "ad1c0a23-8f2f-4b71-9217-f053405d0aad",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 25\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      ">10\n",
      "Inside the top if \n",
      ">20\n",
      "Inside the nested if\n",
      "<=30\n",
      "inside the else part of neted if of nested if\n",
      "outside all ifs\n"
     ]
    }
   ],
   "source": [
    "a= int(input())\n",
    "if a>10:\n",
    "    print(\">10\")\n",
    "    print(\"Inside the top if \")\n",
    "    if a>20:\n",
    "        print(\">20\")\n",
    "        print(\"Inside the nested if\")\n",
    "        if a>30:\n",
    "            print(\">30\")\n",
    "            print(\"inside the nested if of nested if \")\n",
    "        else:\n",
    "            print(\"<=30\")\n",
    "            print(\"inside the else part of neted if of nested if\")\n",
    "    else:\n",
    "        print(\"<=20\")\n",
    "        print(\"Inside the else part of nested if\")\n",
    "print(\"outside all ifs\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "id": "04080534-cde0-4f25-a7a5-f31c21339790",
   "metadata": {},
   "outputs": [],
   "source": [
    "#comment"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "id": "55188910-6dff-41d7-9bc7-3f09b3b51b4c",
   "metadata": {},
   "outputs": [],
   "source": [
    "#single line comment"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 109,
   "id": "920b9baf-341a-418d-8b09-7d2cbe29bbb8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'multi .......\\n.........lines\\n................comments'"
      ]
     },
     "execution_count": 109,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\"\"\"multi .......\n",
    ".........lines\n",
    "................comments\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "id": "2e90b67f-d34b-4564-9fcf-f43d1c546cb2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'user will enter a floating points number let say 238.915. your task is \\nto find out the integer portion before the point (in this case 238) and\\nthen check if that integer portion is an even number or not'"
      ]
     },
     "execution_count": 110,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\"\"\"user will enter a floating points number let say 238.915. your task is \n",
    "to find out the integer portion before the point (in this case 238) and\n",
    "then check if that integer portion is an even number or not\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 112,
   "id": "53efe6fa-2426-4cd7-a338-43bed0e2ac10",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a real number:  25.3647\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "25\n"
     ]
    }
   ],
   "source": [
    "\"\"\"user will enter a floating points number let say 238.915. your task is \n",
    "to find out the integer portion before the point (in this case 238) and\n",
    "then check if that integer portion is an even number or not\"\"\"\n",
    "\n",
    "x=float(input(\"Enter a real number: \")) \n",
    "y=round(x)\n",
    "if y>x:\n",
    "    intPortion=y-1 #29.6\n",
    "else:\n",
    "    intPortion=y\n",
    "print(intPortion)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 113,
   "id": "4a47dfe6-56cd-437b-b383-ca7bf34d3551",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "-9"
      ]
     },
     "execution_count": 113,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "round(-9,3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 118,
   "id": "46276c2f-6253-486e-a85b-f0112cb436dc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a real number:  22.6\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "even\n"
     ]
    }
   ],
   "source": [
    "\"\"\"user will enter a floating points number let say 238.915. your task is \n",
    "to find out the integer portion before the point (in this case 238) and\n",
    "then check if that integer portion is an even number or not\"\"\"\n",
    "\n",
    "x=float(input(\"Enter a real number: \")) \n",
    "y=round(x)\n",
    "if x>0:\n",
    "    if y>x:\n",
    "        intPortion=y-1 #29.6\n",
    "    else:\n",
    "        intPortion=y\n",
    "else:  \n",
    "    if y<x:\n",
    "        intPortion=y+1\n",
    "    else:\n",
    "        intPortion=y\n",
    "if intPortion%2==0:\n",
    "    print(\"even\")\n",
    "else:\n",
    "    print(\"odd\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "15b9d03f-780d-4c0a-8a23-d2ee4d993272",
   "metadata": {},
   "source": [
    "# CONTROL FLOW"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 119,
   "id": "bc084fed-4851-43e3-a5be-2d5596d391d8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 5\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "This is iteration number : 1\n",
      "4\n",
      "This is iteration number : 1\n",
      "9\n",
      "This is iteration number : 1\n",
      "16\n",
      "This is iteration number : 1\n",
      "Done loop\n"
     ]
    }
   ],
   "source": [
    "n=int(input())\n",
    "i=1\n",
    "while i<n:\n",
    "    print(i**2)\n",
    "    print(\"This is iteration number :\",1)\n",
    "    i+=1  #i=i+1\n",
    "print(\"Done loop\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 120,
   "id": "0bca52ea-4236-4be9-b6af-f3ee1e6e8e81",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Inside ELSE\n",
      "Inside ELSE\n",
      "Inside ELSE\n",
      "Inside ELSE\n",
      "Inside ELSE\n",
      "Inside ELSE\n",
      "Inside ELSE\n",
      "Inside ELSE\n",
      "Inside IF\n",
      "Loop is done\n"
     ]
    }
   ],
   "source": [
    "n=10\n",
    "i=1\n",
    "while True:\n",
    "    if i%9==0:\n",
    "        print(\"Inside IF\")\n",
    "        break\n",
    "    else:\n",
    "        print(\"Inside ELSE\")\n",
    "        i=i+1  #i+=1\n",
    "print(\"Loop is done\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 122,
   "id": "421eafdd-8d2e-4e8d-9921-cfa923ba5bd2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Inside IF\n",
      "Inside IF\n",
      "Inside IF\n",
      "Inside IF\n",
      "Inside IF\n",
      "Inside IF\n",
      "Inside IF\n",
      "Inside IF\n",
      "something\n",
      "somethingelse\n",
      "done\n"
     ]
    }
   ],
   "source": [
    "n=10\n",
    "i=1\n",
    "while True:\n",
    "    if i%9 !=0:\n",
    "        print(\"Inside IF\")\n",
    "        i +=1\n",
    "        continue\n",
    "    print(\"something\")\n",
    "    print(\"somethingelse\")\n",
    "    break\n",
    "    \n",
    "print(\"done\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 123,
   "id": "5afa0dab-e6a7-4abe-bdf2-8dd28af2256a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "2\n",
      "3\n",
      "4\n",
      "5\n",
      "6\n",
      "7\n",
      "8\n",
      "9\n",
      "10\n",
      "[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]\n"
     ]
    }
   ],
   "source": [
    "l=[]\n",
    "for i in range (10):\n",
    "    print(i+1)\n",
    "    l.append(i**2)\n",
    "print(l)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 124,
   "id": "70e90dbf-0c3d-48dc-a245-4f51f1f69b66",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "3\n",
      "5\n",
      "7\n",
      "9\n",
      "[0, 4, 16, 36, 64]\n"
     ]
    }
   ],
   "source": [
    "l=[]\n",
    "for i in range (0,10,2):\n",
    "    print(i+1)\n",
    "    l.append(i**2)\n",
    "print(l)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 125,
   "id": "25cef6be-3b53-4426-815a-cd261aee47b0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "4\n",
      "7\n",
      "10\n",
      "13\n",
      "16\n",
      "19\n",
      "22\n",
      "25\n",
      "[0, 9, 36, 81, 144, 225, 324, 441, 576]\n"
     ]
    }
   ],
   "source": [
    "l=[]\n",
    "for i in range (0,25,3):\n",
    "    print(i+1)\n",
    "    l.append(i**2)\n",
    "print(l)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 126,
   "id": "bd4b94a1-92a4-44d7-bde9-332f8d72b87a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "cherry\n",
      "4.9\n",
      "apple\n",
      "loop terminates with success\n",
      "out side of the loop\n"
     ]
    }
   ],
   "source": [
    "s={\"apple\",4.9,\"cherry\"}\n",
    "for x in s:\n",
    "    print(x)\n",
    "else:\n",
    "    print(\"loop terminates with success\")\n",
    "print(\"out side of the loop\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 128,
   "id": "e51cccc1-a6a0-4f13-9aba-794f9cfdcbed",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "cherry\n",
      "4.9\n",
      "out side of the loop\n"
     ]
    }
   ],
   "source": [
    "s={\"apple\",4.9,\"cherry\"}\n",
    "i=1\n",
    "for x in s:\n",
    "    print(x)\n",
    "    i+=1\n",
    "    if i==3:\n",
    "        break\n",
    "    else:\n",
    "        pass\n",
    "else:\n",
    "    print(\"loop terminates with success\")\n",
    "print(\"out side of the loop\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 129,
   "id": "faec4d28-7399-471d-a906-0765ba9b5426",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "a 10\n",
      "b -19\n",
      "c abc\n"
     ]
    }
   ],
   "source": [
    "d={\"a\":10,\"b\":-19,\"c\":\"abc\"}\n",
    "for x in d:\n",
    "    print(x,d[x])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 134,
   "id": "c8554a0e-2c4e-4246-9ffe-f12106fe8aee",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[-5, 1, 2, 2, 3, 4, 7, 9]\n"
     ]
    }
   ],
   "source": [
    "\"\"\"given a list of numbers ie [1,2,4,-5,7,9,3,2],make another list\n",
    "that contains all the items in sorted order from min to max ie your result\n",
    "will be another list like[-5,1,2,2,3,3,7,9]\"\"\"\n",
    "\n",
    "l=[1,2,4,-5,7,9,3,2]\n",
    "for j in range(len(l)):\n",
    "    m=l[j]\n",
    "    idx=j\n",
    "    c=j\n",
    "    for i in range(j,len(l)):\n",
    "        if l[i]<m:\n",
    "            m=l[i]\n",
    "            idx=c\n",
    "        c+=1\n",
    "    temp=l[j]\n",
    "    l[j]=m\n",
    "    l[idx]=temp\n",
    "print(l)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 135,
   "id": "af4fd30c-9dd2-4de0-bc98-9b391e42e4c7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[-5, 1, 2, 2, 3, 4, 7, 9]"
      ]
     },
     "execution_count": 135,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 136,
   "id": "980e8d0d-6903-43a9-b679-56dabe1a0402",
   "metadata": {},
   "outputs": [],
   "source": [
    "def printSuccess():\n",
    "    print(\"I m done\")\n",
    "    print(\"Send me another task\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 138,
   "id": "1c44d30b-e25e-4f43-86ba-d10cb241e155",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "I m done\n",
      "Send me another task\n"
     ]
    }
   ],
   "source": [
    "printSuccess()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 139,
   "id": "bc410b98-6d86-4eac-9644-bfecdce50183",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "11"
      ]
     },
     "execution_count": 139,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "3+8"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 140,
   "id": "39436259-3859-400e-83b4-35571b8f0200",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "I m done\n",
      "Send me another task\n"
     ]
    }
   ],
   "source": [
    "printSuccess()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 141,
   "id": "59bfb780-1d29-4c94-8707-6c908613a050",
   "metadata": {},
   "outputs": [],
   "source": [
    "def printS2():\n",
    "    \"\"\"this function is doing nothing except\n",
    "    printing a message. that message is \"hello\"\n",
    "    \"\"\"\n",
    "    print(\"hello\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 142,
   "id": "dc62fe04-f834-4667-8240-0d2d8b503d6d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\u001b[1;31mSignature:\u001b[0m \u001b[0mprintS2\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
       "\u001b[1;31mDocstring:\u001b[0m\n",
       "this function is doing nothing except\n",
       "printing a message. that message is \"hello\"\n",
       "\u001b[1;31mFile:\u001b[0m      c:\\users\\anush\\appdata\\local\\temp\\ipykernel_11792\\978269780.py\n",
       "\u001b[1;31mType:\u001b[0m      function"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "printS2?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 143,
   "id": "3712f85e-2fb5-46ba-b474-77829ffe10b0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\u001b[1;31mSignature:\u001b[0m \u001b[0mprintS2\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
       "\u001b[1;31mSource:\u001b[0m   \n",
       "\u001b[1;32mdef\u001b[0m \u001b[0mprintS2\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\n",
       "\u001b[0m    \u001b[1;34m\"\"\"this function is doing nothing except\n",
       "    printing a message. that message is \"hello\"\n",
       "    \"\"\"\u001b[0m\u001b[1;33m\n",
       "\u001b[0m    \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"hello\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
       "\u001b[1;31mFile:\u001b[0m      c:\\users\\anush\\appdata\\local\\temp\\ipykernel_11792\\978269780.py\n",
       "\u001b[1;31mType:\u001b[0m      function"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "printS2??"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 144,
   "id": "1aaa0d82-5c4f-4907-be52-ff417ef68118",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\u001b[1;31mSignature:\u001b[0m \u001b[0mlen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mobj\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m/\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
       "\u001b[1;31mDocstring:\u001b[0m Return the number of items in a container.\n",
       "\u001b[1;31mType:\u001b[0m      builtin_function_or_method"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "len?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 145,
   "id": "ce8a69d1-6ea8-420e-acd1-cee065ae084f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\u001b[1;31mSignature:\u001b[0m \u001b[0mlen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mobj\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m/\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
       "\u001b[1;31mDocstring:\u001b[0m Return the number of items in a container.\n",
       "\u001b[1;31mType:\u001b[0m      builtin_function_or_method"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "len??"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 146,
   "id": "782d7772-2e28-4372-a6f7-e4c804ab170a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Help on function printS2 in module __main__:\n",
      "\n",
      "printS2()\n",
      "    this function is doing nothing except\n",
      "    printing a message. that message is \"hello\"\n",
      "\n"
     ]
    }
   ],
   "source": [
    "help(printS2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 147,
   "id": "208cabc5-8e97-4e00-84e4-f936ef80e9e8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello\n"
     ]
    }
   ],
   "source": [
    "printS2()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 151,
   "id": "7e84bfd6-8191-4072-8b43-d73a57d9d410",
   "metadata": {},
   "outputs": [],
   "source": [
    "def printMsg(msg):\n",
    "    \"\"\"the function prints the message supplied by the user or \n",
    "    prints that msg is not in the form of string\"\"\"\n",
    "    if isinstance(msg,str):\n",
    "        print(msg)\n",
    "    else:\n",
    "        print(\"Your input agrument is not a string\")\n",
    "        print(\"here is the type of what you have supplied \",type(msg))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 152,
   "id": "a8c7ce0b-03a1-4482-8944-b291e14c8959",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Help on function printMsg in module __main__:\n",
      "\n",
      "printMsg(msg)\n",
      "    the function prints the message supplied by the user or\n",
      "    prints that msg is not in the form of string\n",
      "\n"
     ]
    }
   ],
   "source": [
    "help(printMsg)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 153,
   "id": "4c373c4e-a957-4783-b685-ff1770d11a24",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\u001b[1;31mSignature:\u001b[0m \u001b[0mprintMsg\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmsg\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
       "\u001b[1;31mSource:\u001b[0m   \n",
       "\u001b[1;32mdef\u001b[0m \u001b[0mprintMsg\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmsg\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\n",
       "\u001b[0m    \u001b[1;34m\"\"\"the function prints the message supplied by the user or \n",
       "    prints that msg is not in the form of string\"\"\"\u001b[0m\u001b[1;33m\n",
       "\u001b[0m    \u001b[1;32mif\u001b[0m \u001b[0misinstance\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmsg\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mstr\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\n",
       "\u001b[0m        \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmsg\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\n",
       "\u001b[0m    \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\n",
       "\u001b[0m        \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Your input agrument is not a string\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\n",
       "\u001b[0m        \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"here is the type of what you have supplied \"\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mtype\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmsg\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
       "\u001b[1;31mFile:\u001b[0m      c:\\users\\anush\\appdata\\local\\temp\\ipykernel_11792\\1949362964.py\n",
       "\u001b[1;31mType:\u001b[0m      function"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "printMsg??"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 154,
   "id": "d6916560-502f-4ad6-938a-f269e0212eba",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "this is the message\n"
     ]
    }
   ],
   "source": [
    "printMsg(\"this is the message\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 155,
   "id": "408c5127-f6cd-4a9e-b371-c06f2df1386e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Your input agrument is not a string\n",
      "here is the type of what you have supplied  <class 'int'>\n"
     ]
    }
   ],
   "source": [
    "printMsg(34)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 156,
   "id": "45c1d5b2-bb71-4624-8b37-c40f32a88858",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello there\n"
     ]
    }
   ],
   "source": [
    "y=\"hello there\"\n",
    "printMsg(y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 157,
   "id": "7f2be684-76b2-419e-9e36-c95a31adba7e",
   "metadata": {},
   "outputs": [],
   "source": [
    "def mypow(a,b):\n",
    "    \"\"\"this function computes power just like builtin\n",
    "    pow function\"\"\"\n",
    "    c=a**b\n",
    "    print(c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 158,
   "id": "094aded9-7bba-4a71-975c-50a21fb929ea",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\u001b[1;31mSignature:\u001b[0m \u001b[0mmypow\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0ma\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mb\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
       "\u001b[1;31mDocstring:\u001b[0m\n",
       "this function computes power just like builtin\n",
       "pow function\n",
       "\u001b[1;31mFile:\u001b[0m      c:\\users\\anush\\appdata\\local\\temp\\ipykernel_11792\\1501445254.py\n",
       "\u001b[1;31mType:\u001b[0m      function"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "mypow?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 159,
   "id": "00ca3e95-7f4f-47f0-9d56-f438aedf67bd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "81\n"
     ]
    }
   ],
   "source": [
    "mypow(3,4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 168,
   "id": "55868970-beef-4f16-a326-1c6a34cde102",
   "metadata": {},
   "outputs": [],
   "source": [
    "def checkArgs(a,b,c):\n",
    "    if isinstance(a,(int,float)) and isinstance(b,(int,float)) and isinstance(c,(int,float)):\n",
    "        print((a+b+c)**2)\n",
    "    else:\n",
    "        print(\"Error: the input arg are not of the expected types\")\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 169,
   "id": "4bd4d666-b9db-4db4-a225-ce00ca5be266",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "144\n"
     ]
    }
   ],
   "source": [
    "checkArgs(3,4,5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 170,
   "id": "655506c2-714a-4213-9f11-8a0900dfbf5f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Error: the input arg are not of the expected types\n"
     ]
    }
   ],
   "source": [
    "checkArgs(3,4,\"g\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 174,
   "id": "9c2b510b-626c-4e28-830b-62b94716f67f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "196\n"
     ]
    }
   ],
   "source": [
    "checkArgs(3,8,3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 175,
   "id": "c55e821b-2196-4078-93d3-7cd9415f5ec9",
   "metadata": {},
   "outputs": [],
   "source": [
    "def f(a,b,c):\n",
    "    print(\"A is :\",a)\n",
    "    print(\"B is :\",b)\n",
    "    print(\"C is :\",c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 176,
   "id": "0b83cea2-679d-4c61-84da-310e7a19432f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "A is : 2\n",
      "B is : 10.3\n",
      "C is : game\n"
     ]
    }
   ],
   "source": [
    "f(2,10.3,\"game\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 177,
   "id": "32fe206c-5a62-4a28-a3d2-15929c22cdfc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "A is : 2\n",
      "B is : 3\n",
      "C is : game\n"
     ]
    }
   ],
   "source": [
    "f(a=2,b=3,c=\"game\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 180,
   "id": "54912cb9-5ee6-4d24-8102-5a4bcf09cb16",
   "metadata": {},
   "outputs": [],
   "source": [
    "def myadd(a,b):\n",
    "    Value=a+b\n",
    "    return Value"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 182,
   "id": "35a682c2-0525-4078-91ca-daddd613e8d5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n"
     ]
    }
   ],
   "source": [
    "d=myadd(2,3)\n",
    "print(d)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 183,
   "id": "d25c8af5-19c7-480b-9d78-0bc083eb1ebc",
   "metadata": {},
   "outputs": [],
   "source": [
    "VarOutSideTheFunction=3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 187,
   "id": "f22c80b2-e665-47f2-9698-7f59eadd8d18",
   "metadata": {},
   "outputs": [],
   "source": [
    "def j():\n",
    "    VarOutSideTheFunction=7\n",
    "    print(VarOutSideTheFunction)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 188,
   "id": "843a0492-c785-4caf-a818-04b374622fa7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "7\n"
     ]
    }
   ],
   "source": [
    "j()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 189,
   "id": "e4fa988d-90dc-4e55-8687-e1c9a63c1ebc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n"
     ]
    }
   ],
   "source": [
    "print(VarOutSideTheFunction)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 190,
   "id": "f85052d3-5214-468e-8a1d-86b1a24dcfc0",
   "metadata": {},
   "outputs": [],
   "source": [
    "def j():\n",
    "    VarOutSideTheFunction=7\n",
    "    #print(VarOutSideTheFunction)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 191,
   "id": "be495ff3-3526-4b3e-9499-15f1bd194532",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "None\n"
     ]
    }
   ],
   "source": [
    "print(j())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 195,
   "id": "7d6f47bf-4b1f-4e75-9050-73f9d7b77f64",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'NoneType'>\n"
     ]
    }
   ],
   "source": [
    "print(type(j()))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 196,
   "id": "a7ddd493-3d33-4ec4-88fa-bd8ede1fecf9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n"
     ]
    }
   ],
   "source": [
    "print(VarOutSideTheFunction)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 197,
   "id": "ca06b34a-7b96-4364-b9c5-f576d7be7f0e",
   "metadata": {},
   "outputs": [],
   "source": [
    "def h():\n",
    "    print(\"A\")\n",
    "    a=3\n",
    "    b=5\n",
    "    c=a+b\n",
    "    print(\"something\")\n",
    "    return\n",
    "    print(\"b\")\n",
    "    print(\"c\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 198,
   "id": "da720f4a-cbd1-4054-9f12-fa43e80850d3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "A\n",
      "something\n"
     ]
    }
   ],
   "source": [
    "h()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 199,
   "id": "912418e0-1467-40ea-8120-2b88678b1049",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "A\n",
      "something\n",
      "None\n"
     ]
    }
   ],
   "source": [
    "print(h())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 200,
   "id": "043dcd73-0892-4a44-be3b-b80d1e94f045",
   "metadata": {},
   "outputs": [],
   "source": [
    "def h():\n",
    "    print(\"A\")\n",
    "    a=3\n",
    "    b=5\n",
    "    c=a+b\n",
    "    print(\"something\")\n",
    "    return c\n",
    "    print(\"b\")\n",
    "    print(\"c\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 201,
   "id": "d8f496ca-fe12-4b41-82ec-86447b38d969",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "A\n",
      "something\n",
      "<class 'int'>\n"
     ]
    }
   ],
   "source": [
    "print(type(h()))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 202,
   "id": "a09485f7-aefd-4b62-a367-0c40fd0ca9fe",
   "metadata": {},
   "outputs": [],
   "source": [
    "def k():\n",
    "    a=5\n",
    "    b=7\n",
    "    d=\"something\"\n",
    "    return a,b,d"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 205,
   "id": "6a41bf3e-5809-408e-b526-1d88b5d0efd5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5 7 something\n"
     ]
    }
   ],
   "source": [
    "x,y,z=k()\n",
    "print(x,y,z)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 206,
   "id": "062a18e6-0417-47a2-a79d-d22c6194e9e6",
   "metadata": {},
   "outputs": [],
   "source": [
    "def MyAddUniversity(*args):\n",
    "    s=0\n",
    "    for i in range(len(args)):\n",
    "        s+=args[i]\n",
    "        return s\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 207,
   "id": "8d0c1473-7bbd-43db-b3e0-1e383dec3991",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n"
     ]
    }
   ],
   "source": [
    "print(MyAddUniversity(2,4,5,4.6,78))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 208,
   "id": "83ac7596-80b7-4d53-9d71-741227d16a2b",
   "metadata": {},
   "outputs": [],
   "source": [
    "def printAllVarNamesAndValues(**args):\n",
    "    for x in args:\n",
    "        print(\"variable name is: \",x , \"and value is : \",args[x])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 209,
   "id": "a7a57398-2b34-4cbf-b76b-951ddc2e446c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "variable name is:  a and value is :  3\n",
      "variable name is:  b and value is :  b\n",
      "variable name is:  c and value is :  aaa\n",
      "variable name is:  y and value is :  8.7\n"
     ]
    }
   ],
   "source": [
    "printAllVarNamesAndValues(a=3,b=\"b\",c=\"aaa\",y=8.7)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 210,
   "id": "5b96f6e2-f3a6-4b62-a5ff-f2c4d0b3ab62",
   "metadata": {},
   "outputs": [],
   "source": [
    "def aa(s=4):\n",
    "    print(s)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 211,
   "id": "f42cd539-91ca-4e98-98b2-20f591a96bf5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4\n"
     ]
    }
   ],
   "source": [
    "aa()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 212,
   "id": "4150267d-b728-4f97-b0be-4945665e69dd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "32\n"
     ]
    }
   ],
   "source": [
    "aa(32)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 214,
   "id": "444f274a-f522-41ed-b38c-0f21e3527a9e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[-9, 2, 3]\n"
     ]
    }
   ],
   "source": [
    "List=[1,2,3]\n",
    "l1=List\n",
    "l1[0]=-9\n",
    "print(List)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 219,
   "id": "10e4c13b-e3a1-4fa7-adda-2dfead4628bb",
   "metadata": {},
   "outputs": [],
   "source": [
    "def qq(List=[1,2]):\n",
    "    for i in List:\n",
    "        print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 221,
   "id": "e20016bc-95d3-4e23-b1e9-1cd5f9daeb03",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "2\n"
     ]
    }
   ],
   "source": [
    "l1=[12,32,1]\n",
    "qq()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 222,
   "id": "805e963e-5af1-4e6d-bbd2-43dd14502dc3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "12\n",
      "32\n",
      "1\n"
     ]
    }
   ],
   "source": [
    "qq(l1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 223,
   "id": "fd89dd40-1dc9-4dfd-bacf-7fe655cca49f",
   "metadata": {},
   "outputs": [],
   "source": [
    "def checkIfNotNum(**args):\n",
    "    retVal= True\n",
    "    for x in args:\n",
    "        if not (isinstance(x,(int,float))):\n",
    "            return False\n",
    "    return True\n",
    "\n",
    "def addAllNum(*args):\n",
    "    s=0\n",
    "    for x in args:\n",
    "        s+=x\n",
    "    return s\n",
    "\n",
    "myName=\"Python Course\"\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 230,
   "id": "9c4d3b32-26d8-4933-96e6-9de89574347a",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "<>:2: SyntaxWarning: invalid escape sequence '\\P'\n",
      "<>:2: SyntaxWarning: invalid escape sequence '\\P'\n",
      "C:\\Users\\anush\\AppData\\Local\\Temp\\ipykernel_11792\\605519076.py:2: SyntaxWarning: invalid escape sequence '\\P'\n",
      "  sys.path.append('D:\\PythonTutorial')\n"
     ]
    }
   ],
   "source": [
    "import sys\n",
    "sys.path.append('D:\\PythonTutorial')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 231,
   "id": "f39d286c-881f-468e-93fd-8613076d9578",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'null' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[231], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mpython11\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mpy\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m \u001b[38;5;21;01mpp\u001b[39;00m\n",
      "File \u001b[1;32mD:\\PythonTutorial\\python11.py:3410\u001b[0m\n\u001b[0;32m      1\u001b[0m {\n\u001b[0;32m      2\u001b[0m  \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcells\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m      3\u001b[0m   {\n\u001b[0;32m      4\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m      5\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m1\u001b[39m,\n\u001b[0;32m      6\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m88ee601c-107b-4ab4-bee8-07c5461bc9b1\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m      7\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m      8\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m      9\u001b[0m     {\n\u001b[0;32m     10\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     11\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     12\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m     13\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mHello world\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m     14\u001b[0m      ]\n\u001b[0;32m     15\u001b[0m     }\n\u001b[0;32m     16\u001b[0m    ],\n\u001b[0;32m     17\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m     18\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mprint(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mHello world\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m     19\u001b[0m    ]\n\u001b[0;32m     20\u001b[0m   },\n\u001b[0;32m     21\u001b[0m   {\n\u001b[0;32m     22\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     23\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m3\u001b[39m,\n\u001b[0;32m     24\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m58497fa3-9f15-49f1-aa11-59bfe927a4a4\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     25\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m     26\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m     27\u001b[0m     {\n\u001b[0;32m     28\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     29\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     30\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m     31\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m123\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m     32\u001b[0m      ]\n\u001b[0;32m     33\u001b[0m     }\n\u001b[0;32m     34\u001b[0m    ],\n\u001b[0;32m     35\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m     36\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mprint(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m123\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m     37\u001b[0m    ]\n\u001b[0;32m     38\u001b[0m   },\n\u001b[0;32m     39\u001b[0m   {\n\u001b[0;32m     40\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmarkdown\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     41\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m1dd69ea5-c552-411c-b12e-dcd4cded044f\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     42\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m     43\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m     44\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m# VARIABLES\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m     45\u001b[0m    ]\n\u001b[0;32m     46\u001b[0m   },\n\u001b[0;32m     47\u001b[0m   {\n\u001b[0;32m     48\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     49\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m5\u001b[39m,\n\u001b[0;32m     50\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mbeb013ab-1b03-4908-8c8f-71c72ae6543a\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     51\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m     52\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [],\n\u001b[0;32m     53\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m     54\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mx=3\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m     55\u001b[0m    ]\n\u001b[0;32m     56\u001b[0m   },\n\u001b[0;32m     57\u001b[0m   {\n\u001b[0;32m     58\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     59\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m6\u001b[39m,\n\u001b[0;32m     60\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mab477c21-30a0-4ea6-8736-716e2df69aca\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     61\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m     62\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m     63\u001b[0m     {\n\u001b[0;32m     64\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     65\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     66\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m     67\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mVariable   Type    Data/Info\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     68\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m----------------------------\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     69\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mx          int     3\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m     70\u001b[0m      ]\n\u001b[0;32m     71\u001b[0m     }\n\u001b[0;32m     72\u001b[0m    ],\n\u001b[0;32m     73\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m     74\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m%\u001b[39m\u001b[38;5;124mwhos\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m     75\u001b[0m    ]\n\u001b[0;32m     76\u001b[0m   },\n\u001b[0;32m     77\u001b[0m   {\n\u001b[0;32m     78\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     79\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m7\u001b[39m,\n\u001b[0;32m     80\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m9c6c2f43-06ec-4044-897c-b3270250d077\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     81\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m     82\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m     83\u001b[0m     {\n\u001b[0;32m     84\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     85\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     86\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m     87\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m<class \u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mint\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124m>\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m     88\u001b[0m      ]\n\u001b[0;32m     89\u001b[0m     }\n\u001b[0;32m     90\u001b[0m    ],\n\u001b[0;32m     91\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m     92\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mprint(type(x))\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m     93\u001b[0m    ]\n\u001b[0;32m     94\u001b[0m   },\n\u001b[0;32m     95\u001b[0m   {\n\u001b[0;32m     96\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     97\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m8\u001b[39m,\n\u001b[0;32m     98\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mbe0c41a6-e73c-47c2-a5f0-37c8ac23933a\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     99\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m    100\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [],\n\u001b[0;32m    101\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    102\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mx=5.7\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    103\u001b[0m    ]\n\u001b[0;32m    104\u001b[0m   },\n\u001b[0;32m    105\u001b[0m   {\n\u001b[0;32m    106\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    107\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m9\u001b[39m,\n\u001b[0;32m    108\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m33eb8a18-0e90-47b7-bd92-89db4464ed6f\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    109\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m    110\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    111\u001b[0m     {\n\u001b[0;32m    112\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    113\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    114\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    115\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mVariable   Type     Data/Info\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    116\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m-----------------------------\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    117\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mx          float    5.7\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    118\u001b[0m      ]\n\u001b[0;32m    119\u001b[0m     }\n\u001b[0;32m    120\u001b[0m    ],\n\u001b[0;32m    121\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    122\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m%\u001b[39m\u001b[38;5;124mwhos\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    123\u001b[0m    ]\n\u001b[0;32m    124\u001b[0m   },\n\u001b[0;32m    125\u001b[0m   {\n\u001b[0;32m    126\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    127\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m10\u001b[39m,\n\u001b[0;32m    128\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m29b022c3-9d4e-49e1-96fd-741ab76ec42e\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    129\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m    130\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [],\n\u001b[0;32m    131\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    132\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mabcd=55.3\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    133\u001b[0m    ]\n\u001b[0;32m    134\u001b[0m   },\n\u001b[0;32m    135\u001b[0m   {\n\u001b[0;32m    136\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    137\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m11\u001b[39m,\n\u001b[0;32m    138\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m37086b27-0d23-44f0-829b-1760a899d4c0\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    139\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m    140\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    141\u001b[0m     {\n\u001b[0;32m    142\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    143\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    144\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    145\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mVariable   Type     Data/Info\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    146\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m-----------------------------\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    147\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mabcd       float    55.3\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    148\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mx          float    5.7\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    149\u001b[0m      ]\n\u001b[0;32m    150\u001b[0m     }\n\u001b[0;32m    151\u001b[0m    ],\n\u001b[0;32m    152\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    153\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m%\u001b[39m\u001b[38;5;124mwhos\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    154\u001b[0m    ]\n\u001b[0;32m    155\u001b[0m   },\n\u001b[0;32m    156\u001b[0m   {\n\u001b[0;32m    157\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    158\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m12\u001b[39m,\n\u001b[0;32m    159\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m7a420598-b415-4057-9578-1556a7cc45fb\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    160\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m    161\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [],\n\u001b[0;32m    162\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    163\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124ma,b,c,d,f=3,5,6.0,-3,5.2\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    164\u001b[0m    ]\n\u001b[0;32m    165\u001b[0m   },\n\u001b[0;32m    166\u001b[0m   {\n\u001b[0;32m    167\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    168\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m13\u001b[39m,\n\u001b[0;32m    169\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mf4ee30a7-5a63-4275-8e3f-6f5252c0f3ed\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    170\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m    171\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    172\u001b[0m     {\n\u001b[0;32m    173\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    174\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    175\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    176\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mVariable   Type     Data/Info\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    177\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m-----------------------------\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    178\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124ma          int      3\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    179\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mabcd       float    55.3\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    180\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mb          int      5\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    181\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mc          float    6.0\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    182\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124md          int      -3\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    183\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mf          float    5.2\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    184\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mx          float    5.7\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    185\u001b[0m      ]\n\u001b[0;32m    186\u001b[0m     }\n\u001b[0;32m    187\u001b[0m    ],\n\u001b[0;32m    188\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    189\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m%\u001b[39m\u001b[38;5;124mwhos\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    190\u001b[0m    ]\n\u001b[0;32m    191\u001b[0m   },\n\u001b[0;32m    192\u001b[0m   {\n\u001b[0;32m    193\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    194\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m14\u001b[39m,\n\u001b[0;32m    195\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m7e46397f-cefb-4b6c-a670-d7613271daec\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    196\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m    197\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [],\n\u001b[0;32m    198\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    199\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdel abcd\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    200\u001b[0m    ]\n\u001b[0;32m    201\u001b[0m   },\n\u001b[0;32m    202\u001b[0m   {\n\u001b[0;32m    203\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    204\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m15\u001b[39m,\n\u001b[0;32m    205\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mf309a2a7-9a0d-4eac-869a-d25820b4d20f\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    206\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m    207\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    208\u001b[0m     {\n\u001b[0;32m    209\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    210\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    211\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    212\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mVariable   Type     Data/Info\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    213\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m-----------------------------\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    214\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124ma          int      3\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    215\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mb          int      5\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    216\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mc          float    6.0\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    217\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124md          int      -3\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    218\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mf          float    5.2\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    219\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mx          float    5.7\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    220\u001b[0m      ]\n\u001b[0;32m    221\u001b[0m     }\n\u001b[0;32m    222\u001b[0m    ],\n\u001b[0;32m    223\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    224\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m%\u001b[39m\u001b[38;5;124mwhos\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    225\u001b[0m    ]\n\u001b[0;32m    226\u001b[0m   },\n\u001b[0;32m    227\u001b[0m   {\n\u001b[0;32m    228\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    229\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m16\u001b[39m,\n\u001b[0;32m    230\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m4181dc6c-fd39-4f3c-bc9d-ea6cf8d143be\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    231\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m    232\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [],\n\u001b[0;32m    233\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    234\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mc=2+4j\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    235\u001b[0m    ]\n\u001b[0;32m    236\u001b[0m   },\n\u001b[0;32m    237\u001b[0m   {\n\u001b[0;32m    238\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    239\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m17\u001b[39m,\n\u001b[0;32m    240\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m7c22e45c-85a7-4b8e-93c7-f6ecb2054828\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    241\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m    242\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    243\u001b[0m     {\n\u001b[0;32m    244\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    245\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    246\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    247\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m<class \u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mcomplex\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124m>\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    248\u001b[0m      ]\n\u001b[0;32m    249\u001b[0m     }\n\u001b[0;32m    250\u001b[0m    ],\n\u001b[0;32m    251\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    252\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mprint(type(c))\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    253\u001b[0m    ]\n\u001b[0;32m    254\u001b[0m   },\n\u001b[0;32m    255\u001b[0m   {\n\u001b[0;32m    256\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    257\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m18\u001b[39m,\n\u001b[0;32m    258\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m41c7578c-d3a4-4bf3-8a4a-c6ac89caea57\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    259\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m    260\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [],\n\u001b[0;32m    261\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    262\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124ms=\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mhello how are you\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    263\u001b[0m    ]\n\u001b[0;32m    264\u001b[0m   },\n\u001b[0;32m    265\u001b[0m   {\n\u001b[0;32m    266\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    267\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m19\u001b[39m,\n\u001b[0;32m    268\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdca7869f-7847-4553-911b-e3a5ccd862a7\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    269\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m    270\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    271\u001b[0m     {\n\u001b[0;32m    272\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    273\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    274\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    275\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m<class \u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mstr\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124m>\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    276\u001b[0m      ]\n\u001b[0;32m    277\u001b[0m     }\n\u001b[0;32m    278\u001b[0m    ],\n\u001b[0;32m    279\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    280\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mprint(type(s))\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    281\u001b[0m    ]\n\u001b[0;32m    282\u001b[0m   },\n\u001b[0;32m    283\u001b[0m   {\n\u001b[0;32m    284\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmarkdown\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    285\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124ma205315e-77d8-4253-b99a-3a6774a8a7d9\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    286\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m    287\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    288\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m# OPERATORS\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    289\u001b[0m    ]\n\u001b[0;32m    290\u001b[0m   },\n\u001b[0;32m    291\u001b[0m   {\n\u001b[0;32m    292\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    293\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m20\u001b[39m,\n\u001b[0;32m    294\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m4a326f62-60dc-4b3f-bb74-793166e6e2bd\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    295\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m    296\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    297\u001b[0m     {\n\u001b[0;32m    298\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    299\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    300\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    301\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mVariable   Type       Data/Info\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    302\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m-------------------------------\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    303\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124ma          int        3\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    304\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mb          int        5\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    305\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mc          complex    (2+4j)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    306\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124md          int        -3\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    307\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mf          float      5.2\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    308\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124ms          str        hello how are you\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    309\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mx          float      5.7\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    310\u001b[0m      ]\n\u001b[0;32m    311\u001b[0m     }\n\u001b[0;32m    312\u001b[0m    ],\n\u001b[0;32m    313\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    314\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m%\u001b[39m\u001b[38;5;124mwhos\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    315\u001b[0m    ]\n\u001b[0;32m    316\u001b[0m   },\n\u001b[0;32m    317\u001b[0m   {\n\u001b[0;32m    318\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    319\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m21\u001b[39m,\n\u001b[0;32m    320\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m8ace3865-55f0-441a-9cc3-8156ba6de7cd\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    321\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m    322\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [],\n\u001b[0;32m    323\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    324\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msumOfaAndb=a+b\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    325\u001b[0m    ]\n\u001b[0;32m    326\u001b[0m   },\n\u001b[0;32m    327\u001b[0m   {\n\u001b[0;32m    328\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    329\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m23\u001b[39m,\n\u001b[0;32m    330\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m3d21bcd2-2c21-479d-8799-29b7ad33ad7e\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    331\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m    332\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    333\u001b[0m     {\n\u001b[0;32m    334\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    335\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    336\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    337\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m8\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    338\u001b[0m      ]\n\u001b[0;32m    339\u001b[0m     }\n\u001b[0;32m    340\u001b[0m    ],\n\u001b[0;32m    341\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    342\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mprint(sumOfaAndb)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    343\u001b[0m    ]\n\u001b[0;32m    344\u001b[0m   },\n\u001b[0;32m    345\u001b[0m   {\n\u001b[0;32m    346\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    347\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m25\u001b[39m,\n\u001b[0;32m    348\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124me54d3b41-1df4-49de-a95b-c5d6dbc2d69c\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    349\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m    350\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    351\u001b[0m     {\n\u001b[0;32m    352\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    353\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    354\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    355\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m<class \u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mint\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124m>\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    356\u001b[0m      ]\n\u001b[0;32m    357\u001b[0m     }\n\u001b[0;32m    358\u001b[0m    ],\n\u001b[0;32m    359\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    360\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mprint(type(sumOfaAndb))\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    361\u001b[0m    ]\n\u001b[0;32m    362\u001b[0m   },\n\u001b[0;32m    363\u001b[0m   {\n\u001b[0;32m    364\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    365\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m26\u001b[39m,\n\u001b[0;32m    366\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m5d445563-78ae-407c-a7ae-645ba4c615da\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    367\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m    368\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    369\u001b[0m     {\n\u001b[0;32m    370\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {\n\u001b[0;32m    371\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext/plain\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    372\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mint\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    373\u001b[0m       ]\n\u001b[0;32m    374\u001b[0m      },\n\u001b[0;32m    375\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m26\u001b[39m,\n\u001b[0;32m    376\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m    377\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecute_result\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    378\u001b[0m     }\n\u001b[0;32m    379\u001b[0m    ],\n\u001b[0;32m    380\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    381\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtype(a+b)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    382\u001b[0m    ]\n\u001b[0;32m    383\u001b[0m   },\n\u001b[0;32m    384\u001b[0m   {\n\u001b[0;32m    385\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    386\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m27\u001b[39m,\n\u001b[0;32m    387\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m6933f391-aea2-4718-aec6-ff0ac63b0bdb\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    388\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m    389\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    390\u001b[0m     {\n\u001b[0;32m    391\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {\n\u001b[0;32m    392\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext/plain\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    393\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mfloat\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    394\u001b[0m       ]\n\u001b[0;32m    395\u001b[0m      },\n\u001b[0;32m    396\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m27\u001b[39m,\n\u001b[0;32m    397\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m    398\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecute_result\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    399\u001b[0m     }\n\u001b[0;32m    400\u001b[0m    ],\n\u001b[0;32m    401\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    402\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtype(a+f)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    403\u001b[0m    ]\n\u001b[0;32m    404\u001b[0m   },\n\u001b[0;32m    405\u001b[0m   {\n\u001b[0;32m    406\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    407\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m28\u001b[39m,\n\u001b[0;32m    408\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m698a5095-439f-4be2-93ab-b9842a6100ab\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    409\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m    410\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [],\n\u001b[0;32m    411\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    412\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mv=((a+f)**3)/4\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    413\u001b[0m    ]\n\u001b[0;32m    414\u001b[0m   },\n\u001b[0;32m    415\u001b[0m   {\n\u001b[0;32m    416\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    417\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m29\u001b[39m,\n\u001b[0;32m    418\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m07022262-121a-42eb-9e62-32e61e4573a4\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    419\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m    420\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    421\u001b[0m     {\n\u001b[0;32m    422\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    423\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    424\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    425\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m137.84199999999996\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    426\u001b[0m      ]\n\u001b[0;32m    427\u001b[0m     }\n\u001b[0;32m    428\u001b[0m    ],\n\u001b[0;32m    429\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    430\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mprint(v)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    431\u001b[0m    ]\n\u001b[0;32m    432\u001b[0m   },\n\u001b[0;32m    433\u001b[0m   {\n\u001b[0;32m    434\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    435\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m30\u001b[39m,\n\u001b[0;32m    436\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124me4af2761-fca6-4f7f-921f-76fd606b5ddd\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    437\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m    438\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    439\u001b[0m     {\n\u001b[0;32m    440\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    441\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    442\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    443\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mhello how are you\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    444\u001b[0m      ]\n\u001b[0;32m    445\u001b[0m     }\n\u001b[0;32m    446\u001b[0m    ],\n\u001b[0;32m    447\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    448\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124ma1=\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mhellow\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    449\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124ma2=\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mworld\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    450\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mss=a1+a2\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    451\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mprint(s)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    452\u001b[0m    ]\n\u001b[0;32m    453\u001b[0m   },\n\u001b[0;32m    454\u001b[0m   {\n\u001b[0;32m    455\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    456\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m31\u001b[39m,\n\u001b[0;32m    457\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m37acbf27-bf66-439c-a864-6e37f772600e\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    458\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m    459\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    460\u001b[0m     {\n\u001b[0;32m    461\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {\n\u001b[0;32m    462\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext/plain\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    463\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m3\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    464\u001b[0m       ]\n\u001b[0;32m    465\u001b[0m      },\n\u001b[0;32m    466\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m31\u001b[39m,\n\u001b[0;32m    467\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m    468\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecute_result\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    469\u001b[0m     }\n\u001b[0;32m    470\u001b[0m    ],\n\u001b[0;32m    471\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    472\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m10//3\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    473\u001b[0m    ]\n\u001b[0;32m    474\u001b[0m   },\n\u001b[0;32m    475\u001b[0m   {\n\u001b[0;32m    476\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    477\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m32\u001b[39m,\n\u001b[0;32m    478\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124maec1eafb-0648-4154-b381-e45d980309f7\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    479\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m    480\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    481\u001b[0m     {\n\u001b[0;32m    482\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {\n\u001b[0;32m    483\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext/plain\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    484\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m3.3333333333333335\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    485\u001b[0m       ]\n\u001b[0;32m    486\u001b[0m      },\n\u001b[0;32m    487\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m32\u001b[39m,\n\u001b[0;32m    488\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m    489\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecute_result\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    490\u001b[0m     }\n\u001b[0;32m    491\u001b[0m    ],\n\u001b[0;32m    492\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    493\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m10/3\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    494\u001b[0m    ]\n\u001b[0;32m    495\u001b[0m   },\n\u001b[0;32m    496\u001b[0m   {\n\u001b[0;32m    497\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmarkdown\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    498\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124ma5f9491b-89ce-4f24-9a4e-d45d6d11e58b\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    499\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m    500\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    501\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m# BOOLEAN\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    502\u001b[0m    ]\n\u001b[0;32m    503\u001b[0m   },\n\u001b[0;32m    504\u001b[0m   {\n\u001b[0;32m    505\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    506\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m33\u001b[39m,\n\u001b[0;32m    507\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m787cc2f7-a125-4318-a2e1-1d20fc1589dd\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    508\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m    509\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [],\n\u001b[0;32m    510\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    511\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124ma=True\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    512\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mb=True\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    513\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mc=False\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    514\u001b[0m    ]\n\u001b[0;32m    515\u001b[0m   },\n\u001b[0;32m    516\u001b[0m   {\n\u001b[0;32m    517\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    518\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m34\u001b[39m,\n\u001b[0;32m    519\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mc2decbba-6391-4e25-b63d-c4ffd2e37f7d\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    520\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m    521\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    522\u001b[0m     {\n\u001b[0;32m    523\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    524\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    525\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    526\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mVariable     Type     Data/Info\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    527\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m-------------------------------\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    528\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124ma            bool     True\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    529\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124ma1           str      hellow\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    530\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124ma2           str      world\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    531\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mb            bool     True\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    532\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mc            bool     False\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    533\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124md            int      -3\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    534\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mf            float    5.2\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    535\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124ms            str      hello how are you\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    536\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mss           str      hellowworld\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    537\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msumOfaAndb   int      8\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    538\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mv            float    137.84199999999996\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    539\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mx            float    5.7\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    540\u001b[0m      ]\n\u001b[0;32m    541\u001b[0m     }\n\u001b[0;32m    542\u001b[0m    ],\n\u001b[0;32m    543\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    544\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m \u001b[39m\u001b[38;5;124m%\u001b[39m\u001b[38;5;124mwhos\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    545\u001b[0m    ]\n\u001b[0;32m    546\u001b[0m   },\n\u001b[0;32m    547\u001b[0m   {\n\u001b[0;32m    548\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    549\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m36\u001b[39m,\n\u001b[0;32m    550\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mf4bf2de8-2cc9-4fd9-b5c5-702946cb97a9\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    551\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m    552\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    553\u001b[0m     {\n\u001b[0;32m    554\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    555\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    556\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    557\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mTrue\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    558\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mFalse\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    559\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mFalse\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    560\u001b[0m      ]\n\u001b[0;32m    561\u001b[0m     }\n\u001b[0;32m    562\u001b[0m    ],\n\u001b[0;32m    563\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    564\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mprint (a and b)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    565\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mprint (a and c)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    566\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mprint (c and a)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    567\u001b[0m    ]\n\u001b[0;32m    568\u001b[0m   },\n\u001b[0;32m    569\u001b[0m   {\n\u001b[0;32m    570\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    571\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m37\u001b[39m,\n\u001b[0;32m    572\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m841597fb-e381-4004-9981-c32db0b95839\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    573\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m    574\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    575\u001b[0m     {\n\u001b[0;32m    576\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    577\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    578\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    579\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mTrue\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    580\u001b[0m      ]\n\u001b[0;32m    581\u001b[0m     }\n\u001b[0;32m    582\u001b[0m    ],\n\u001b[0;32m    583\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    584\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124md=a or c\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    585\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mprint(d)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    586\u001b[0m    ]\n\u001b[0;32m    587\u001b[0m   },\n\u001b[0;32m    588\u001b[0m   {\n\u001b[0;32m    589\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    590\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m38\u001b[39m,\n\u001b[0;32m    591\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m6a565660-af07-4930-a248-d6d158d5a385\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    592\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m    593\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    594\u001b[0m     {\n\u001b[0;32m    595\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {\n\u001b[0;32m    596\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext/plain\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    597\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mFalse\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    598\u001b[0m       ]\n\u001b[0;32m    599\u001b[0m      },\n\u001b[0;32m    600\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m38\u001b[39m,\n\u001b[0;32m    601\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m    602\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecute_result\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    603\u001b[0m     }\n\u001b[0;32m    604\u001b[0m    ],\n\u001b[0;32m    605\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    606\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mnot(a)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    607\u001b[0m    ]\n\u001b[0;32m    608\u001b[0m   },\n\u001b[0;32m    609\u001b[0m   {\n\u001b[0;32m    610\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    611\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m39\u001b[39m,\n\u001b[0;32m    612\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mf6295684-959f-4e41-808a-b5aace469e1d\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    613\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m    614\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    615\u001b[0m     {\n\u001b[0;32m    616\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {\n\u001b[0;32m    617\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext/plain\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    618\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mFalse\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    619\u001b[0m       ]\n\u001b[0;32m    620\u001b[0m      },\n\u001b[0;32m    621\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m39\u001b[39m,\n\u001b[0;32m    622\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m    623\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecute_result\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    624\u001b[0m     }\n\u001b[0;32m    625\u001b[0m    ],\n\u001b[0;32m    626\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    627\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mnot(b)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    628\u001b[0m    ]\n\u001b[0;32m    629\u001b[0m   },\n\u001b[0;32m    630\u001b[0m   {\n\u001b[0;32m    631\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    632\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m40\u001b[39m,\n\u001b[0;32m    633\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124md92f2d2d-701f-40b6-92e4-aee100b05d15\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    634\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m    635\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    636\u001b[0m     {\n\u001b[0;32m    637\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {\n\u001b[0;32m    638\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext/plain\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    639\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mTrue\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    640\u001b[0m       ]\n\u001b[0;32m    641\u001b[0m      },\n\u001b[0;32m    642\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m40\u001b[39m,\n\u001b[0;32m    643\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m    644\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecute_result\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    645\u001b[0m     }\n\u001b[0;32m    646\u001b[0m    ],\n\u001b[0;32m    647\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    648\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mnot(c)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    649\u001b[0m    ]\n\u001b[0;32m    650\u001b[0m   },\n\u001b[0;32m    651\u001b[0m   {\n\u001b[0;32m    652\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    653\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m41\u001b[39m,\n\u001b[0;32m    654\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mfb579e53-b0a2-49e4-abf6-42a68d8bc888\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    655\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m    656\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [],\n\u001b[0;32m    657\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    658\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mt=not(a)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    659\u001b[0m    ]\n\u001b[0;32m    660\u001b[0m   },\n\u001b[0;32m    661\u001b[0m   {\n\u001b[0;32m    662\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    663\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m42\u001b[39m,\n\u001b[0;32m    664\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m0858c7d7-8bea-428b-ae17-05cecccacdff\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    665\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m    666\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    667\u001b[0m     {\n\u001b[0;32m    668\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {\n\u001b[0;32m    669\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext/plain\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    670\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mbool\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    671\u001b[0m       ]\n\u001b[0;32m    672\u001b[0m      },\n\u001b[0;32m    673\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m42\u001b[39m,\n\u001b[0;32m    674\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m    675\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecute_result\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    676\u001b[0m     }\n\u001b[0;32m    677\u001b[0m    ],\n\u001b[0;32m    678\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    679\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtype(t)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    680\u001b[0m    ]\n\u001b[0;32m    681\u001b[0m   },\n\u001b[0;32m    682\u001b[0m   {\n\u001b[0;32m    683\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    684\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m43\u001b[39m,\n\u001b[0;32m    685\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m817f8742-aa0a-4d26-9f8a-b4cf1fa4c6db\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    686\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m    687\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    688\u001b[0m     {\n\u001b[0;32m    689\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    690\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    691\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    692\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mFalse\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    693\u001b[0m      ]\n\u001b[0;32m    694\u001b[0m     }\n\u001b[0;32m    695\u001b[0m    ],\n\u001b[0;32m    696\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    697\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mprint(t)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    698\u001b[0m    ]\n\u001b[0;32m    699\u001b[0m   },\n\u001b[0;32m    700\u001b[0m   {\n\u001b[0;32m    701\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    702\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m44\u001b[39m,\n\u001b[0;32m    703\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m37698c90-668f-4f86-8697-b6afe2eeb815\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    704\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m    705\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    706\u001b[0m     {\n\u001b[0;32m    707\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {\n\u001b[0;32m    708\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext/plain\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    709\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mFalse\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    710\u001b[0m       ]\n\u001b[0;32m    711\u001b[0m      },\n\u001b[0;32m    712\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m44\u001b[39m,\n\u001b[0;32m    713\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m    714\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecute_result\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    715\u001b[0m     }\n\u001b[0;32m    716\u001b[0m    ],\n\u001b[0;32m    717\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    718\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mnot((a and b) or (c or d))\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    719\u001b[0m    ]\n\u001b[0;32m    720\u001b[0m   },\n\u001b[0;32m    721\u001b[0m   {\n\u001b[0;32m    722\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmarkdown\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    723\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m9b111c30-c571-4048-bc3a-9f1114489167\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    724\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m    725\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    726\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m# COMPARISONS\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    727\u001b[0m    ]\n\u001b[0;32m    728\u001b[0m   },\n\u001b[0;32m    729\u001b[0m   {\n\u001b[0;32m    730\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    731\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m45\u001b[39m,\n\u001b[0;32m    732\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m6a63bda7-5434-475d-a03c-20aa75552adb\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    733\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m    734\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    735\u001b[0m     {\n\u001b[0;32m    736\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    737\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    738\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    739\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mTrue\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    740\u001b[0m      ]\n\u001b[0;32m    741\u001b[0m     }\n\u001b[0;32m    742\u001b[0m    ],\n\u001b[0;32m    743\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    744\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mprint(2<3)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    745\u001b[0m    ]\n\u001b[0;32m    746\u001b[0m   },\n\u001b[0;32m    747\u001b[0m   {\n\u001b[0;32m    748\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    749\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m46\u001b[39m,\n\u001b[0;32m    750\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mb95ca238-8b26-4d04-befb-aa0d06edd193\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    751\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m    752\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    753\u001b[0m     {\n\u001b[0;32m    754\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    755\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    756\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    757\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m<class \u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mbool\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124m>\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    758\u001b[0m      ]\n\u001b[0;32m    759\u001b[0m     }\n\u001b[0;32m    760\u001b[0m    ],\n\u001b[0;32m    761\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    762\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mc=2<3\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    763\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mprint(type(c))\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    764\u001b[0m    ]\n\u001b[0;32m    765\u001b[0m   },\n\u001b[0;32m    766\u001b[0m   {\n\u001b[0;32m    767\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    768\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m47\u001b[39m,\n\u001b[0;32m    769\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124md7a3443d-d69b-4ae9-9109-3fb1f8f77654\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    770\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m    771\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [],\n\u001b[0;32m    772\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    773\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124md=3==4\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    774\u001b[0m    ]\n\u001b[0;32m    775\u001b[0m   },\n\u001b[0;32m    776\u001b[0m   {\n\u001b[0;32m    777\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    778\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m48\u001b[39m,\n\u001b[0;32m    779\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mbb3b2dfb-cee5-4c90-8287-0362bf7fc086\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    780\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m    781\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    782\u001b[0m     {\n\u001b[0;32m    783\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    784\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    785\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    786\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mFalse\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    787\u001b[0m      ]\n\u001b[0;32m    788\u001b[0m     }\n\u001b[0;32m    789\u001b[0m    ],\n\u001b[0;32m    790\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    791\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mprint(d)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    792\u001b[0m    ]\n\u001b[0;32m    793\u001b[0m   },\n\u001b[0;32m    794\u001b[0m   {\n\u001b[0;32m    795\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    796\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m49\u001b[39m,\n\u001b[0;32m    797\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m59c9e403-1068-4f17-af3b-1ecf1fcb662c\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    798\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m    799\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    800\u001b[0m     {\n\u001b[0;32m    801\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {\n\u001b[0;32m    802\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext/plain\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    803\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mTrue\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    804\u001b[0m       ]\n\u001b[0;32m    805\u001b[0m      },\n\u001b[0;32m    806\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m49\u001b[39m,\n\u001b[0;32m    807\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m    808\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecute_result\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    809\u001b[0m     }\n\u001b[0;32m    810\u001b[0m    ],\n\u001b[0;32m    811\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    812\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m3==3.0\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    813\u001b[0m    ]\n\u001b[0;32m    814\u001b[0m   },\n\u001b[0;32m    815\u001b[0m   {\n\u001b[0;32m    816\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    817\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m50\u001b[39m,\n\u001b[0;32m    818\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m09599397-ecf3-4694-b735-8b197cb0bab3\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    819\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m    820\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [],\n\u001b[0;32m    821\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    822\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mx=4\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    823\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124my=9\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    824\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mz=8.3\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    825\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mr=-3\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    826\u001b[0m    ]\n\u001b[0;32m    827\u001b[0m   },\n\u001b[0;32m    828\u001b[0m   {\n\u001b[0;32m    829\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    830\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m51\u001b[39m,\n\u001b[0;32m    831\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m57dff4f2-cd0e-490c-b9e0-da83d8e75846\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    832\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m    833\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    834\u001b[0m     {\n\u001b[0;32m    835\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {\n\u001b[0;32m    836\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext/plain\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    837\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mTrue\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    838\u001b[0m       ]\n\u001b[0;32m    839\u001b[0m      },\n\u001b[0;32m    840\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m51\u001b[39m,\n\u001b[0;32m    841\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m    842\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecute_result\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    843\u001b[0m     }\n\u001b[0;32m    844\u001b[0m    ],\n\u001b[0;32m    845\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    846\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m(x<y) and (z<y) or (r==)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    847\u001b[0m    ]\n\u001b[0;32m    848\u001b[0m   },\n\u001b[0;32m    849\u001b[0m   {\n\u001b[0;32m    850\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    851\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m52\u001b[39m,\n\u001b[0;32m    852\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m18141c84-ae15-4b3f-ba36-4eec2896bd59\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    853\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m    854\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    855\u001b[0m     {\n\u001b[0;32m    856\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {\n\u001b[0;32m    857\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext/plain\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    858\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mFalse\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    859\u001b[0m       ]\n\u001b[0;32m    860\u001b[0m      },\n\u001b[0;32m    861\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m52\u001b[39m,\n\u001b[0;32m    862\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m    863\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecute_result\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    864\u001b[0m     }\n\u001b[0;32m    865\u001b[0m    ],\n\u001b[0;32m    866\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    867\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m(x<y) and (r==x) or (z>y) \u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    868\u001b[0m    ]\n\u001b[0;32m    869\u001b[0m   },\n\u001b[0;32m    870\u001b[0m   {\n\u001b[0;32m    871\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    872\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m53\u001b[39m,\n\u001b[0;32m    873\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mba67ad56-45b6-4e2b-bcb5-3ffd8fbed7bd\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    874\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m    875\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    876\u001b[0m     {\n\u001b[0;32m    877\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {\n\u001b[0;32m    878\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext/plain\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    879\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mFalse\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    880\u001b[0m       ]\n\u001b[0;32m    881\u001b[0m      },\n\u001b[0;32m    882\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m53\u001b[39m,\n\u001b[0;32m    883\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m    884\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecute_result\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    885\u001b[0m     }\n\u001b[0;32m    886\u001b[0m    ],\n\u001b[0;32m    887\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    888\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m(r==x)and(x<y)or(z>y)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    889\u001b[0m    ]\n\u001b[0;32m    890\u001b[0m   },\n\u001b[0;32m    891\u001b[0m   {\n\u001b[0;32m    892\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    893\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m54\u001b[39m,\n\u001b[0;32m    894\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m96f7e568-8275-41ad-bc42-1273738b4cef\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    895\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m    896\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    897\u001b[0m     {\n\u001b[0;32m    898\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {\n\u001b[0;32m    899\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext/plain\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    900\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mFalse\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    901\u001b[0m       ]\n\u001b[0;32m    902\u001b[0m      },\n\u001b[0;32m    903\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m54\u001b[39m,\n\u001b[0;32m    904\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m    905\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecute_result\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    906\u001b[0m     }\n\u001b[0;32m    907\u001b[0m    ],\n\u001b[0;32m    908\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    909\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mFalse or False and True\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    910\u001b[0m    ]\n\u001b[0;32m    911\u001b[0m   },\n\u001b[0;32m    912\u001b[0m   {\n\u001b[0;32m    913\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    914\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m55\u001b[39m,\n\u001b[0;32m    915\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m6f721ac8-0597-4b8b-89bb-ead022f4ab52\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    916\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m    917\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    918\u001b[0m     {\n\u001b[0;32m    919\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {\n\u001b[0;32m    920\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext/plain\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    921\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mFalse\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    922\u001b[0m       ]\n\u001b[0;32m    923\u001b[0m      },\n\u001b[0;32m    924\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m55\u001b[39m,\n\u001b[0;32m    925\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m    926\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecute_result\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    927\u001b[0m     }\n\u001b[0;32m    928\u001b[0m    ],\n\u001b[0;32m    929\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    930\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m(True or False)and False\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    931\u001b[0m    ]\n\u001b[0;32m    932\u001b[0m   },\n\u001b[0;32m    933\u001b[0m   {\n\u001b[0;32m    934\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    935\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m57\u001b[39m,\n\u001b[0;32m    936\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mc693f777-81c3-46e5-89b3-550911866013\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    937\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m    938\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    939\u001b[0m     {\n\u001b[0;32m    940\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    941\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    942\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    943\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mFalse\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    944\u001b[0m      ]\n\u001b[0;32m    945\u001b[0m     }\n\u001b[0;32m    946\u001b[0m    ],\n\u001b[0;32m    947\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    948\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mprint((not(2!=3) and True)or(False and True))\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    949\u001b[0m    ]\n\u001b[0;32m    950\u001b[0m   },\n\u001b[0;32m    951\u001b[0m   {\n\u001b[0;32m    952\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    953\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m58\u001b[39m,\n\u001b[0;32m    954\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124md642bdd4-99d2-47d7-9ba6-de1eb47ed1d0\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    955\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m    956\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    957\u001b[0m     {\n\u001b[0;32m    958\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    959\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    960\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    961\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m5\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    962\u001b[0m      ]\n\u001b[0;32m    963\u001b[0m     }\n\u001b[0;32m    964\u001b[0m    ],\n\u001b[0;32m    965\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    966\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mprint(round(4.556))\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    967\u001b[0m    ]\n\u001b[0;32m    968\u001b[0m   },\n\u001b[0;32m    969\u001b[0m   {\n\u001b[0;32m    970\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    971\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m59\u001b[39m,\n\u001b[0;32m    972\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m07a2555f-0469-4022-953d-285dd84147bf\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    973\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m    974\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    975\u001b[0m     {\n\u001b[0;32m    976\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    977\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    978\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    979\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m4\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    980\u001b[0m      ]\n\u001b[0;32m    981\u001b[0m     }\n\u001b[0;32m    982\u001b[0m    ],\n\u001b[0;32m    983\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    984\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mprint(round(4.345))\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    985\u001b[0m    ]\n\u001b[0;32m    986\u001b[0m   },\n\u001b[0;32m    987\u001b[0m   {\n\u001b[0;32m    988\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    989\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m62\u001b[39m,\n\u001b[0;32m    990\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mde44f7a7-e44a-401d-87dc-670bed7e9c33\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    991\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m    992\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    993\u001b[0m     {\n\u001b[0;32m    994\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    995\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    996\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m    997\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m4.446\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    998\u001b[0m      ]\n\u001b[0;32m    999\u001b[0m     }\n\u001b[0;32m   1000\u001b[0m    ],\n\u001b[0;32m   1001\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1002\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mprint(round(4.446389,3))\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1003\u001b[0m    ]\n\u001b[0;32m   1004\u001b[0m   },\n\u001b[0;32m   1005\u001b[0m   {\n\u001b[0;32m   1006\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1007\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m63\u001b[39m,\n\u001b[0;32m   1008\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m3e4c5822-aa5e-4b21-a360-abf04af45d8a\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1009\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   1010\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [],\n\u001b[0;32m   1011\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1012\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mg=divmod(34,9)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1013\u001b[0m    ]\n\u001b[0;32m   1014\u001b[0m   },\n\u001b[0;32m   1015\u001b[0m   {\n\u001b[0;32m   1016\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1017\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m64\u001b[39m,\n\u001b[0;32m   1018\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m7485c1e8-3ba3-4cfc-985c-01526b4c4a3a\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1019\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   1020\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1021\u001b[0m     {\n\u001b[0;32m   1022\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {\n\u001b[0;32m   1023\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext/plain\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1024\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtuple\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1025\u001b[0m       ]\n\u001b[0;32m   1026\u001b[0m      },\n\u001b[0;32m   1027\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m64\u001b[39m,\n\u001b[0;32m   1028\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   1029\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecute_result\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1030\u001b[0m     }\n\u001b[0;32m   1031\u001b[0m    ],\n\u001b[0;32m   1032\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1033\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtype(g)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1034\u001b[0m    ]\n\u001b[0;32m   1035\u001b[0m   },\n\u001b[0;32m   1036\u001b[0m   {\n\u001b[0;32m   1037\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1038\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m65\u001b[39m,\n\u001b[0;32m   1039\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcf4e2446-447d-40c7-bfb6-22055c624142\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1040\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   1041\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1042\u001b[0m     {\n\u001b[0;32m   1043\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1044\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1045\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1046\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m(3, 7)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1047\u001b[0m      ]\n\u001b[0;32m   1048\u001b[0m     }\n\u001b[0;32m   1049\u001b[0m    ],\n\u001b[0;32m   1050\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1051\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mprint(g)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1052\u001b[0m    ]\n\u001b[0;32m   1053\u001b[0m   },\n\u001b[0;32m   1054\u001b[0m   {\n\u001b[0;32m   1055\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1056\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m66\u001b[39m,\n\u001b[0;32m   1057\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m0a92efca-7b22-4dff-b6b9-be7587257e4c\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1058\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   1059\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1060\u001b[0m     {\n\u001b[0;32m   1061\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {\n\u001b[0;32m   1062\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext/plain\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1063\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m3\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1064\u001b[0m       ]\n\u001b[0;32m   1065\u001b[0m      },\n\u001b[0;32m   1066\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m66\u001b[39m,\n\u001b[0;32m   1067\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   1068\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecute_result\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1069\u001b[0m     }\n\u001b[0;32m   1070\u001b[0m    ],\n\u001b[0;32m   1071\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1072\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mg[0]\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1073\u001b[0m    ]\n\u001b[0;32m   1074\u001b[0m   },\n\u001b[0;32m   1075\u001b[0m   {\n\u001b[0;32m   1076\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1077\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m67\u001b[39m,\n\u001b[0;32m   1078\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m704a331d-324b-4d1e-94cc-92be048e58c2\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1079\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   1080\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1081\u001b[0m     {\n\u001b[0;32m   1082\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {\n\u001b[0;32m   1083\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext/plain\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1084\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m7\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1085\u001b[0m       ]\n\u001b[0;32m   1086\u001b[0m      },\n\u001b[0;32m   1087\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m67\u001b[39m,\n\u001b[0;32m   1088\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   1089\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecute_result\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1090\u001b[0m     }\n\u001b[0;32m   1091\u001b[0m    ],\n\u001b[0;32m   1092\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1093\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mg[1]\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1094\u001b[0m    ]\n\u001b[0;32m   1095\u001b[0m   },\n\u001b[0;32m   1096\u001b[0m   {\n\u001b[0;32m   1097\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1098\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m68\u001b[39m,\n\u001b[0;32m   1099\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m8c56b05d-81cf-4744-84ed-99f3be78260e\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1100\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   1101\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1102\u001b[0m     {\n\u001b[0;32m   1103\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {\n\u001b[0;32m   1104\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext/plain\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1105\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m3\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1106\u001b[0m       ]\n\u001b[0;32m   1107\u001b[0m      },\n\u001b[0;32m   1108\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m68\u001b[39m,\n\u001b[0;32m   1109\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   1110\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecute_result\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1111\u001b[0m     }\n\u001b[0;32m   1112\u001b[0m    ],\n\u001b[0;32m   1113\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1114\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m34//9\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1115\u001b[0m    ]\n\u001b[0;32m   1116\u001b[0m   },\n\u001b[0;32m   1117\u001b[0m   {\n\u001b[0;32m   1118\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1119\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m69\u001b[39m,\n\u001b[0;32m   1120\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124madebc23a-b561-4a3f-8d60-36adf5466243\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1121\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   1122\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1123\u001b[0m     {\n\u001b[0;32m   1124\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {\n\u001b[0;32m   1125\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext/plain\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1126\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m7\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1127\u001b[0m       ]\n\u001b[0;32m   1128\u001b[0m      },\n\u001b[0;32m   1129\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m69\u001b[39m,\n\u001b[0;32m   1130\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   1131\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecute_result\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1132\u001b[0m     }\n\u001b[0;32m   1133\u001b[0m    ],\n\u001b[0;32m   1134\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1135\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m34\u001b[39m\u001b[38;5;124m%\u001b[39m\u001b[38;5;124m9\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1136\u001b[0m    ]\n\u001b[0;32m   1137\u001b[0m   },\n\u001b[0;32m   1138\u001b[0m   {\n\u001b[0;32m   1139\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1140\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m70\u001b[39m,\n\u001b[0;32m   1141\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m597923a8-c8d8-4256-a26c-292ae201835e\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1142\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   1143\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1144\u001b[0m     {\n\u001b[0;32m   1145\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {\n\u001b[0;32m   1146\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext/plain\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1147\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mTrue\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1148\u001b[0m       ]\n\u001b[0;32m   1149\u001b[0m      },\n\u001b[0;32m   1150\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m70\u001b[39m,\n\u001b[0;32m   1151\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   1152\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecute_result\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1153\u001b[0m     }\n\u001b[0;32m   1154\u001b[0m    ],\n\u001b[0;32m   1155\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1156\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124misinstance(3,int)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1157\u001b[0m    ]\n\u001b[0;32m   1158\u001b[0m   },\n\u001b[0;32m   1159\u001b[0m   {\n\u001b[0;32m   1160\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1161\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m71\u001b[39m,\n\u001b[0;32m   1162\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m19420642-59a5-4165-9b84-ded49bb7d451\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1163\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   1164\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1165\u001b[0m     {\n\u001b[0;32m   1166\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {\n\u001b[0;32m   1167\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext/plain\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1168\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mTrue\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1169\u001b[0m       ]\n\u001b[0;32m   1170\u001b[0m      },\n\u001b[0;32m   1171\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m71\u001b[39m,\n\u001b[0;32m   1172\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   1173\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecute_result\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1174\u001b[0m     }\n\u001b[0;32m   1175\u001b[0m    ],\n\u001b[0;32m   1176\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1177\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124misinstance(3.4,float)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1178\u001b[0m    ]\n\u001b[0;32m   1179\u001b[0m   },\n\u001b[0;32m   1180\u001b[0m   {\n\u001b[0;32m   1181\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1182\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m72\u001b[39m,\n\u001b[0;32m   1183\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m40345c07-0624-4bd2-b5ac-2ae084c7aa19\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1184\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   1185\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1186\u001b[0m     {\n\u001b[0;32m   1187\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {\n\u001b[0;32m   1188\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext/plain\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1189\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mFalse\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1190\u001b[0m       ]\n\u001b[0;32m   1191\u001b[0m      },\n\u001b[0;32m   1192\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m72\u001b[39m,\n\u001b[0;32m   1193\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   1194\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecute_result\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1195\u001b[0m     }\n\u001b[0;32m   1196\u001b[0m    ],\n\u001b[0;32m   1197\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1198\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124misinstance(3+3j,(int,float,str))\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1199\u001b[0m    ]\n\u001b[0;32m   1200\u001b[0m   },\n\u001b[0;32m   1201\u001b[0m   {\n\u001b[0;32m   1202\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1203\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m73\u001b[39m,\n\u001b[0;32m   1204\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdaf56254-b773-4a7c-8c69-cba552d325d5\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1205\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   1206\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1207\u001b[0m     {\n\u001b[0;32m   1208\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {\n\u001b[0;32m   1209\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext/plain\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1210\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mTrue\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1211\u001b[0m       ]\n\u001b[0;32m   1212\u001b[0m      },\n\u001b[0;32m   1213\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m73\u001b[39m,\n\u001b[0;32m   1214\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   1215\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecute_result\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1216\u001b[0m     }\n\u001b[0;32m   1217\u001b[0m    ],\n\u001b[0;32m   1218\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1219\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124misinstance(3+3j,(complex))\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1220\u001b[0m    ]\n\u001b[0;32m   1221\u001b[0m   },\n\u001b[0;32m   1222\u001b[0m   {\n\u001b[0;32m   1223\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1224\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m74\u001b[39m,\n\u001b[0;32m   1225\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124me9f852a1-ad78-41f1-a1e7-e060989b34ee\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1226\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   1227\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1228\u001b[0m     {\n\u001b[0;32m   1229\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {\n\u001b[0;32m   1230\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext/plain\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1231\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m16\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1232\u001b[0m       ]\n\u001b[0;32m   1233\u001b[0m      },\n\u001b[0;32m   1234\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m74\u001b[39m,\n\u001b[0;32m   1235\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   1236\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecute_result\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1237\u001b[0m     }\n\u001b[0;32m   1238\u001b[0m    ],\n\u001b[0;32m   1239\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1240\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mpow(2,4)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1241\u001b[0m    ]\n\u001b[0;32m   1242\u001b[0m   },\n\u001b[0;32m   1243\u001b[0m   {\n\u001b[0;32m   1244\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1245\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m75\u001b[39m,\n\u001b[0;32m   1246\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m247fcadd-2d91-4dfd-a7ee-e8e8015070f9\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1247\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   1248\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1249\u001b[0m     {\n\u001b[0;32m   1250\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {\n\u001b[0;32m   1251\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext/plain\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1252\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m16\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1253\u001b[0m       ]\n\u001b[0;32m   1254\u001b[0m      },\n\u001b[0;32m   1255\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m75\u001b[39m,\n\u001b[0;32m   1256\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   1257\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecute_result\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1258\u001b[0m     }\n\u001b[0;32m   1259\u001b[0m    ],\n\u001b[0;32m   1260\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1261\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m2**4\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1262\u001b[0m    ]\n\u001b[0;32m   1263\u001b[0m   },\n\u001b[0;32m   1264\u001b[0m   {\n\u001b[0;32m   1265\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1266\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m76\u001b[39m,\n\u001b[0;32m   1267\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m4489b1bc-f0a5-4604-9d0f-647686e383f9\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1268\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   1269\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1270\u001b[0m     {\n\u001b[0;32m   1271\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {\n\u001b[0;32m   1272\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext/plain\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1273\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m2\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1274\u001b[0m       ]\n\u001b[0;32m   1275\u001b[0m      },\n\u001b[0;32m   1276\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m76\u001b[39m,\n\u001b[0;32m   1277\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   1278\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecute_result\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1279\u001b[0m     }\n\u001b[0;32m   1280\u001b[0m    ],\n\u001b[0;32m   1281\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1282\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mpow(2,4,7)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1283\u001b[0m    ]\n\u001b[0;32m   1284\u001b[0m   },\n\u001b[0;32m   1285\u001b[0m   {\n\u001b[0;32m   1286\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1287\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m77\u001b[39m,\n\u001b[0;32m   1288\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m45cdcf8a-d337-4a3c-9d26-f3e2488988be\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1289\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   1290\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1291\u001b[0m     {\n\u001b[0;32m   1292\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdin\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1293\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1294\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1295\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mEnter a number 56\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1296\u001b[0m      ]\n\u001b[0;32m   1297\u001b[0m     }\n\u001b[0;32m   1298\u001b[0m    ],\n\u001b[0;32m   1299\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1300\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mx=input(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mEnter a number\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1301\u001b[0m    ]\n\u001b[0;32m   1302\u001b[0m   },\n\u001b[0;32m   1303\u001b[0m   {\n\u001b[0;32m   1304\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1305\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m78\u001b[39m,\n\u001b[0;32m   1306\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m613ff292-211a-4738-bde2-2a66f5c6fdf8\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1307\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   1308\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1309\u001b[0m     {\n\u001b[0;32m   1310\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {\n\u001b[0;32m   1311\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext/plain\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1312\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstr\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1313\u001b[0m       ]\n\u001b[0;32m   1314\u001b[0m      },\n\u001b[0;32m   1315\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m78\u001b[39m,\n\u001b[0;32m   1316\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   1317\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecute_result\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1318\u001b[0m     }\n\u001b[0;32m   1319\u001b[0m    ],\n\u001b[0;32m   1320\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1321\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtype(x)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1322\u001b[0m    ]\n\u001b[0;32m   1323\u001b[0m   },\n\u001b[0;32m   1324\u001b[0m   {\n\u001b[0;32m   1325\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1326\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m79\u001b[39m,\n\u001b[0;32m   1327\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m193f7068-1d6b-4be8-823d-6f2ee82b719d\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1328\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   1329\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [],\n\u001b[0;32m   1330\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1331\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mx=int(x)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1332\u001b[0m    ]\n\u001b[0;32m   1333\u001b[0m   },\n\u001b[0;32m   1334\u001b[0m   {\n\u001b[0;32m   1335\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1336\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m80\u001b[39m,\n\u001b[0;32m   1337\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m2617123f-b5b3-490c-8c97-d47e13d25407\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1338\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   1339\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1340\u001b[0m     {\n\u001b[0;32m   1341\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {\n\u001b[0;32m   1342\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext/plain\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1343\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mint\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1344\u001b[0m       ]\n\u001b[0;32m   1345\u001b[0m      },\n\u001b[0;32m   1346\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m80\u001b[39m,\n\u001b[0;32m   1347\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   1348\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecute_result\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1349\u001b[0m     }\n\u001b[0;32m   1350\u001b[0m    ],\n\u001b[0;32m   1351\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1352\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtype(x)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1353\u001b[0m    ]\n\u001b[0;32m   1354\u001b[0m   },\n\u001b[0;32m   1355\u001b[0m   {\n\u001b[0;32m   1356\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1357\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m81\u001b[39m,\n\u001b[0;32m   1358\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m38a29897-ce28-4606-9fed-8bbcf5f9c0d6\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1359\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   1360\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1361\u001b[0m     {\n\u001b[0;32m   1362\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1363\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1364\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1365\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m22\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1366\u001b[0m      ]\n\u001b[0;32m   1367\u001b[0m     }\n\u001b[0;32m   1368\u001b[0m    ],\n\u001b[0;32m   1369\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1370\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mprint(x-34)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1371\u001b[0m    ]\n\u001b[0;32m   1372\u001b[0m   },\n\u001b[0;32m   1373\u001b[0m   {\n\u001b[0;32m   1374\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1375\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m84\u001b[39m,\n\u001b[0;32m   1376\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m266ad3f8-b051-4ed5-ad2a-32c6c63f2d78\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1377\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   1378\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1379\u001b[0m     {\n\u001b[0;32m   1380\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdin\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1381\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1382\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1383\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mEnter a real number 7\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1384\u001b[0m      ]\n\u001b[0;32m   1385\u001b[0m     }\n\u001b[0;32m   1386\u001b[0m    ],\n\u001b[0;32m   1387\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1388\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124ma=int(input(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mEnter a real number\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m))\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1389\u001b[0m    ]\n\u001b[0;32m   1390\u001b[0m   },\n\u001b[0;32m   1391\u001b[0m   {\n\u001b[0;32m   1392\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1393\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m85\u001b[39m,\n\u001b[0;32m   1394\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m5d3205ef-9aea-4167-a409-eeb0d00e02d2\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1395\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   1396\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1397\u001b[0m     {\n\u001b[0;32m   1398\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdin\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1399\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1400\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1401\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124menter a real number :  4.3\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1402\u001b[0m      ]\n\u001b[0;32m   1403\u001b[0m     }\n\u001b[0;32m   1404\u001b[0m    ],\n\u001b[0;32m   1405\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1406\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mb=float(input(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124menter a real number : \u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m))\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1407\u001b[0m    ]\n\u001b[0;32m   1408\u001b[0m   },\n\u001b[0;32m   1409\u001b[0m   {\n\u001b[0;32m   1410\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1411\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m86\u001b[39m,\n\u001b[0;32m   1412\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m7cf9e79b-1e35-4cd0-9eca-d78608c97595\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1413\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   1414\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1415\u001b[0m     {\n\u001b[0;32m   1416\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {\n\u001b[0;32m   1417\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext/plain\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1418\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;31mSignature:\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m \u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0mpow\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;33m(\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0mbase\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;33m,\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m \u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0mexp\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;33m,\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m \u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0mmod\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;33m=\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;32mNone\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;33m)\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;33m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;33m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1419\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;31mDocstring:\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1420\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mEquivalent to base**exp with 2 arguments or base**exp \u001b[39m\u001b[38;5;124m%\u001b[39m\u001b[38;5;124m mod with 3 arguments\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1421\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1422\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mSome types, such as ints, are able to use a more efficient algorithm when\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1423\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124minvoked using the three argument form.\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1424\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;31mType:\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m      builtin_function_or_method\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1425\u001b[0m       ]\n\u001b[0;32m   1426\u001b[0m      },\n\u001b[0;32m   1427\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   1428\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdisplay_data\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1429\u001b[0m     }\n\u001b[0;32m   1430\u001b[0m    ],\n\u001b[0;32m   1431\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1432\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mpow?\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1433\u001b[0m    ]\n\u001b[0;32m   1434\u001b[0m   },\n\u001b[0;32m   1435\u001b[0m   {\n\u001b[0;32m   1436\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1437\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m87\u001b[39m,\n\u001b[0;32m   1438\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdaec7324-f7d0-4ec8-9e1e-4adf88c1ad8e\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1439\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   1440\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1441\u001b[0m     {\n\u001b[0;32m   1442\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {\n\u001b[0;32m   1443\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext/plain\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1444\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;31mSignature:\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m \u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0mpow\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;33m(\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0mbase\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;33m,\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m \u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0mexp\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;33m,\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m \u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0mmod\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;33m=\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;32mNone\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;33m)\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;33m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;33m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1445\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;31mDocstring:\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1446\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mEquivalent to base**exp with 2 arguments or base**exp \u001b[39m\u001b[38;5;124m%\u001b[39m\u001b[38;5;124m mod with 3 arguments\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1447\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1448\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mSome types, such as ints, are able to use a more efficient algorithm when\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1449\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124minvoked using the three argument form.\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1450\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;31mType:\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m      builtin_function_or_method\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1451\u001b[0m       ]\n\u001b[0;32m   1452\u001b[0m      },\n\u001b[0;32m   1453\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   1454\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdisplay_data\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1455\u001b[0m     }\n\u001b[0;32m   1456\u001b[0m    ],\n\u001b[0;32m   1457\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1458\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mpow??\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1459\u001b[0m    ]\n\u001b[0;32m   1460\u001b[0m   },\n\u001b[0;32m   1461\u001b[0m   {\n\u001b[0;32m   1462\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1463\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m88\u001b[39m,\n\u001b[0;32m   1464\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m2f8f176e-2dce-4144-a64c-f0d05f444cd1\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1465\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   1466\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1467\u001b[0m     {\n\u001b[0;32m   1468\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1469\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1470\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1471\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mHelp on built-in function pow in module builtins:\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1472\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1473\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mpow(base, exp, mod=None)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1474\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    Equivalent to base**exp with 2 arguments or base**exp \u001b[39m\u001b[38;5;124m%\u001b[39m\u001b[38;5;124m mod with 3 arguments\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1475\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1476\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    Some types, such as ints, are able to use a more efficient algorithm when\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1477\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    invoked using the three argument form.\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1478\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1479\u001b[0m      ]\n\u001b[0;32m   1480\u001b[0m     }\n\u001b[0;32m   1481\u001b[0m    ],\n\u001b[0;32m   1482\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1483\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mhelp(pow)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1484\u001b[0m    ]\n\u001b[0;32m   1485\u001b[0m   },\n\u001b[0;32m   1486\u001b[0m   {\n\u001b[0;32m   1487\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1488\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m89\u001b[39m,\n\u001b[0;32m   1489\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m59252434-ef50-4eea-95da-e5bc75f5a269\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1490\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   1491\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1492\u001b[0m     {\n\u001b[0;32m   1493\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1494\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1495\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1496\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mHelp on method raw_input in module ipykernel.kernelbase:\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1497\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1498\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mraw_input(prompt=\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124m) method of ipykernel.ipkernel.IPythonKernel instance\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1499\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    Forward raw_input to frontends\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1500\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1501\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    Raises\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1502\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    ------\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1503\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    StdinNotImplementedError if active frontend doesn\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mt support stdin.\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1504\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1505\u001b[0m      ]\n\u001b[0;32m   1506\u001b[0m     }\n\u001b[0;32m   1507\u001b[0m    ],\n\u001b[0;32m   1508\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1509\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mhelp(input)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1510\u001b[0m    ]\n\u001b[0;32m   1511\u001b[0m   },\n\u001b[0;32m   1512\u001b[0m   {\n\u001b[0;32m   1513\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmarkdown\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1514\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124ma3410a21-a21d-41e1-adea-e0256609ffba\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1515\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   1516\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1517\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m# CONTROL FLOW\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1518\u001b[0m    ]\n\u001b[0;32m   1519\u001b[0m   },\n\u001b[0;32m   1520\u001b[0m   {\n\u001b[0;32m   1521\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1522\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m91\u001b[39m,\n\u001b[0;32m   1523\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m76fa54ed-ed2b-4beb-968e-f16fafd4b6dd\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1524\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   1525\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1526\u001b[0m     {\n\u001b[0;32m   1527\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdin\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1528\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1529\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1530\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m 5\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1531\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m 1\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1532\u001b[0m      ]\n\u001b[0;32m   1533\u001b[0m     },\n\u001b[0;32m   1534\u001b[0m     {\n\u001b[0;32m   1535\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1536\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1537\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1538\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m5\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1539\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mI m still inside if condition\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1540\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mI m outside if conditions\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1541\u001b[0m      ]\n\u001b[0;32m   1542\u001b[0m     }\n\u001b[0;32m   1543\u001b[0m    ],\n\u001b[0;32m   1544\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1545\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124ma=int(input())\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1546\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mb=int(input())\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1547\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mif a>b:\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1548\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    print(a)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1549\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    print(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mI m still inside if condition\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1550\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    x=5\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1551\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mprint(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mI m outside if conditions\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)    \u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1552\u001b[0m    ]\n\u001b[0;32m   1553\u001b[0m   },\n\u001b[0;32m   1554\u001b[0m   {\n\u001b[0;32m   1555\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1556\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m92\u001b[39m,\n\u001b[0;32m   1557\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mf7c0b0ce-f8b3-4a38-9f94-3f4a48ab9827\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1558\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   1559\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1560\u001b[0m     {\n\u001b[0;32m   1561\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdin\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1562\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1563\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1564\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m 6\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1565\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m 8\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1566\u001b[0m      ]\n\u001b[0;32m   1567\u001b[0m     },\n\u001b[0;32m   1568\u001b[0m     {\n\u001b[0;32m   1569\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1570\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1571\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1572\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mI m outside if conditions\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1573\u001b[0m      ]\n\u001b[0;32m   1574\u001b[0m     }\n\u001b[0;32m   1575\u001b[0m    ],\n\u001b[0;32m   1576\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1577\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124ma=int(input())\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1578\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mb=int(input())\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1579\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mif a>b:\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1580\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    print(a)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1581\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    print(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mI m still inside if condition\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1582\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    x=5\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1583\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mprint(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mI m outside if conditions\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m) \u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1584\u001b[0m    ]\n\u001b[0;32m   1585\u001b[0m   },\n\u001b[0;32m   1586\u001b[0m   {\n\u001b[0;32m   1587\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1588\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m93\u001b[39m,\n\u001b[0;32m   1589\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m6a6d0356-4641-4e1d-b396-cee54d966ce2\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1590\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   1591\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1592\u001b[0m     {\n\u001b[0;32m   1593\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdin\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1594\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1595\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1596\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m 6\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1597\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m 2\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1598\u001b[0m      ]\n\u001b[0;32m   1599\u001b[0m     },\n\u001b[0;32m   1600\u001b[0m     {\n\u001b[0;32m   1601\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1602\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1603\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1604\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m6\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1605\u001b[0m      ]\n\u001b[0;32m   1606\u001b[0m     }\n\u001b[0;32m   1607\u001b[0m    ],\n\u001b[0;32m   1608\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1609\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124ma=int(input())\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1610\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mb=int(input())\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1611\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mif a>b:\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1612\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    print(a)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1613\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mif b>a:    \u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1614\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    print(b)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1615\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    \u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1616\u001b[0m    ]\n\u001b[0;32m   1617\u001b[0m   },\n\u001b[0;32m   1618\u001b[0m   {\n\u001b[0;32m   1619\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1620\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m95\u001b[39m,\n\u001b[0;32m   1621\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m251412af-4a9c-45b1-9730-8f2fcc248b97\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1622\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   1623\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1624\u001b[0m     {\n\u001b[0;32m   1625\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdin\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1626\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1627\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1628\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m 10\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1629\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m 22\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1630\u001b[0m      ]\n\u001b[0;32m   1631\u001b[0m     },\n\u001b[0;32m   1632\u001b[0m     {\n\u001b[0;32m   1633\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1634\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1635\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1636\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m22\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1637\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124melse part\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1638\u001b[0m      ]\n\u001b[0;32m   1639\u001b[0m     }\n\u001b[0;32m   1640\u001b[0m    ],\n\u001b[0;32m   1641\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1642\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124ma=int(input())\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1643\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mb=int(input())\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1644\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mif a>b:\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1645\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    print(a)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1646\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    print(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mif part\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1647\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124melse:\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1648\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    print(b)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1649\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    print(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124melse part\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1650\u001b[0m    ]\n\u001b[0;32m   1651\u001b[0m   },\n\u001b[0;32m   1652\u001b[0m   {\n\u001b[0;32m   1653\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1654\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m97\u001b[39m,\n\u001b[0;32m   1655\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mde2fc0a0-5df2-4196-942c-a30474f3ed03\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1656\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   1657\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1658\u001b[0m     {\n\u001b[0;32m   1659\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1660\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1661\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1662\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mB\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1663\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mNot in if\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1664\u001b[0m      ]\n\u001b[0;32m   1665\u001b[0m     }\n\u001b[0;32m   1666\u001b[0m    ],\n\u001b[0;32m   1667\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1668\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124ma=1\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1669\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mb=5\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1670\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mif a==b:\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1671\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    print(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mEqual\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1672\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124melif a>b:\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1673\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    print(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mA\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1674\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124melse:\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1675\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    print(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mB\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1676\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mprint(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mNot in if\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1677\u001b[0m    ]\n\u001b[0;32m   1678\u001b[0m   },\n\u001b[0;32m   1679\u001b[0m   {\n\u001b[0;32m   1680\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1681\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m98\u001b[39m,\n\u001b[0;32m   1682\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m4bcea717-cb05-4fe5-944e-702be33fbc9d\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1683\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   1684\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1685\u001b[0m     {\n\u001b[0;32m   1686\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdin\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1687\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1688\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1689\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mEnter marks :  82\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1690\u001b[0m      ]\n\u001b[0;32m   1691\u001b[0m     },\n\u001b[0;32m   1692\u001b[0m     {\n\u001b[0;32m   1693\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1694\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1695\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1696\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mA- Grade\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1697\u001b[0m      ]\n\u001b[0;32m   1698\u001b[0m     }\n\u001b[0;32m   1699\u001b[0m    ],\n\u001b[0;32m   1700\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1701\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124ma=int(input(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mEnter marks : \u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m))\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1702\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mif a>=85:\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1703\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    print(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mA Grade\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1704\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124melif(a<85)and(a>=80):\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1705\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    print(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mA- Grade\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1706\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124melif(a<80) and (a>=75):\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1707\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    print(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mB Grade\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1708\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124melif(a<75)and(a>=70):\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1709\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    print(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mB- Grade\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1710\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124melse:\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1711\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    print(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mbelow avg\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1712\u001b[0m    ]\n\u001b[0;32m   1713\u001b[0m   },\n\u001b[0;32m   1714\u001b[0m   {\n\u001b[0;32m   1715\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1716\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m99\u001b[39m,\n\u001b[0;32m   1717\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mfa6b2d93-4e3b-4aeb-bb82-f8167ceec684\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1718\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   1719\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1720\u001b[0m     {\n\u001b[0;32m   1721\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdin\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1722\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1723\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1724\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mEnter marks :  35\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1725\u001b[0m      ]\n\u001b[0;32m   1726\u001b[0m     },\n\u001b[0;32m   1727\u001b[0m     {\n\u001b[0;32m   1728\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1729\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1730\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1731\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mbelow avg\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1732\u001b[0m      ]\n\u001b[0;32m   1733\u001b[0m     }\n\u001b[0;32m   1734\u001b[0m    ],\n\u001b[0;32m   1735\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1736\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124ma=int(input(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mEnter marks : \u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m))\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1737\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mif a>=85:\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1738\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    print(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mA Grade\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1739\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124melif(a<85)and(a>=80):\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1740\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    print(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mA- Grade\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1741\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124melif(a<80) and (a>=75):\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1742\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    print(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mB Grade\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1743\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124melif(a<75)and(a>=70):\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1744\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    print(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mB- Grade\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1745\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124melse:\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1746\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    print(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mbelow avg\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1747\u001b[0m    ]\n\u001b[0;32m   1748\u001b[0m   },\n\u001b[0;32m   1749\u001b[0m   {\n\u001b[0;32m   1750\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1751\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m100\u001b[39m,\n\u001b[0;32m   1752\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124md3e3a46b-1432-43dd-b47d-8d083758a1eb\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1753\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   1754\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1755\u001b[0m     {\n\u001b[0;32m   1756\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1757\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1758\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1759\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mElse part\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1760\u001b[0m      ]\n\u001b[0;32m   1761\u001b[0m     }\n\u001b[0;32m   1762\u001b[0m    ],\n\u001b[0;32m   1763\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1764\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124ma=3\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1765\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mif a>10:\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1766\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    print(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m>10\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1767\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124melif not(a>b):\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1768\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    print(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mElse part\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1769\u001b[0m    ]\n\u001b[0;32m   1770\u001b[0m   },\n\u001b[0;32m   1771\u001b[0m   {\n\u001b[0;32m   1772\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1773\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m101\u001b[39m,\n\u001b[0;32m   1774\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mbaf8c3ff-2006-462b-8079-e2096bb16895\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1775\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   1776\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1777\u001b[0m     {\n\u001b[0;32m   1778\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdin\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1779\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1780\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1781\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m 12\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1782\u001b[0m      ]\n\u001b[0;32m   1783\u001b[0m     },\n\u001b[0;32m   1784\u001b[0m     {\n\u001b[0;32m   1785\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1786\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1787\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1788\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m>10\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1789\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mInside the top if \u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1790\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m<=20\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1791\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mInside the else part of nested if\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1792\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutside all ifs\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1793\u001b[0m      ]\n\u001b[0;32m   1794\u001b[0m     }\n\u001b[0;32m   1795\u001b[0m    ],\n\u001b[0;32m   1796\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1797\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124ma= int(input())\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1798\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mif a>10:\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1799\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    print(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m>10\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1800\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    print(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mInside the top if \u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1801\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    if a>20:\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1802\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m        print(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m>20\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1803\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m        print(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mInside the nested if\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1804\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    else:\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1805\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m        print(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m<=20\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1806\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m        print(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mInside the else part of nested if\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1807\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mprint(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124moutside all ifs\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1808\u001b[0m    ]\n\u001b[0;32m   1809\u001b[0m   },\n\u001b[0;32m   1810\u001b[0m   {\n\u001b[0;32m   1811\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1812\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m102\u001b[39m,\n\u001b[0;32m   1813\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m5b828b11-1a0f-481c-8dac-003a11a4c354\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1814\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   1815\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1816\u001b[0m     {\n\u001b[0;32m   1817\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdin\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1818\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1819\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1820\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m 50\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1821\u001b[0m      ]\n\u001b[0;32m   1822\u001b[0m     },\n\u001b[0;32m   1823\u001b[0m     {\n\u001b[0;32m   1824\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1825\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1826\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1827\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m>10\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1828\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mInside the top if \u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1829\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m>20\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1830\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mInside the nested if\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1831\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutside all ifs\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1832\u001b[0m      ]\n\u001b[0;32m   1833\u001b[0m     }\n\u001b[0;32m   1834\u001b[0m    ],\n\u001b[0;32m   1835\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1836\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124ma= int(input())\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1837\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mif a>10:\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1838\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    print(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m>10\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1839\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    print(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mInside the top if \u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1840\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    if a>20:\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1841\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m        print(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m>20\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1842\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m        print(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mInside the nested if\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1843\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    else:\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1844\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m        print(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m<=20\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1845\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m        print(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mInside the else part of nested if\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1846\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mprint(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124moutside all ifs\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1847\u001b[0m    ]\n\u001b[0;32m   1848\u001b[0m   },\n\u001b[0;32m   1849\u001b[0m   {\n\u001b[0;32m   1850\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1851\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m104\u001b[39m,\n\u001b[0;32m   1852\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mad1c0a23-8f2f-4b71-9217-f053405d0aad\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1853\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   1854\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1855\u001b[0m     {\n\u001b[0;32m   1856\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdin\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1857\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1858\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1859\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m 25\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1860\u001b[0m      ]\n\u001b[0;32m   1861\u001b[0m     },\n\u001b[0;32m   1862\u001b[0m     {\n\u001b[0;32m   1863\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1864\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1865\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1866\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m>10\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1867\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mInside the top if \u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1868\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m>20\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1869\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mInside the nested if\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1870\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m<=30\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1871\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124minside the else part of neted if of nested if\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1872\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutside all ifs\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1873\u001b[0m      ]\n\u001b[0;32m   1874\u001b[0m     }\n\u001b[0;32m   1875\u001b[0m    ],\n\u001b[0;32m   1876\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1877\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124ma= int(input())\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1878\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mif a>10:\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1879\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    print(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m>10\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1880\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    print(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mInside the top if \u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1881\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    if a>20:\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1882\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m        print(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m>20\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1883\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m        print(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mInside the nested if\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1884\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m        if a>30:\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1885\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m            print(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m>30\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1886\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m            print(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124minside the nested if of nested if \u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1887\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m        else:\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1888\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m            print(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m<=30\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1889\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m            print(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124minside the else part of neted if of nested if\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1890\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    else:\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1891\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m        print(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m<=20\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1892\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m        print(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mInside the else part of nested if\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1893\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mprint(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124moutside all ifs\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1894\u001b[0m    ]\n\u001b[0;32m   1895\u001b[0m   },\n\u001b[0;32m   1896\u001b[0m   {\n\u001b[0;32m   1897\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1898\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m105\u001b[39m,\n\u001b[0;32m   1899\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m04080534-cde0-4f25-a7a5-f31c21339790\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1900\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   1901\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [],\n\u001b[0;32m   1902\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1903\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m#comment\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1904\u001b[0m    ]\n\u001b[0;32m   1905\u001b[0m   },\n\u001b[0;32m   1906\u001b[0m   {\n\u001b[0;32m   1907\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1908\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m106\u001b[39m,\n\u001b[0;32m   1909\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m55188910-6dff-41d7-9bc7-3f09b3b51b4c\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1910\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   1911\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [],\n\u001b[0;32m   1912\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1913\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m#single line comment\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1914\u001b[0m    ]\n\u001b[0;32m   1915\u001b[0m   },\n\u001b[0;32m   1916\u001b[0m   {\n\u001b[0;32m   1917\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1918\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m109\u001b[39m,\n\u001b[0;32m   1919\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m920b9baf-341a-418d-8b09-7d2cbe29bbb8\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1920\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   1921\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1922\u001b[0m     {\n\u001b[0;32m   1923\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {\n\u001b[0;32m   1924\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext/plain\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1925\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mmulti .......\u001b[39m\u001b[38;5;130;01m\\\\\u001b[39;00m\u001b[38;5;124mn.........lines\u001b[39m\u001b[38;5;130;01m\\\\\u001b[39;00m\u001b[38;5;124mn................comments\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1926\u001b[0m       ]\n\u001b[0;32m   1927\u001b[0m      },\n\u001b[0;32m   1928\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m109\u001b[39m,\n\u001b[0;32m   1929\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   1930\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecute_result\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1931\u001b[0m     }\n\u001b[0;32m   1932\u001b[0m    ],\n\u001b[0;32m   1933\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1934\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mmulti .......\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1935\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m.........lines\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1936\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m................comments\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1937\u001b[0m    ]\n\u001b[0;32m   1938\u001b[0m   },\n\u001b[0;32m   1939\u001b[0m   {\n\u001b[0;32m   1940\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1941\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m110\u001b[39m,\n\u001b[0;32m   1942\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m2e90b67f-d34b-4564-9fcf-f43d1c546cb2\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1943\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   1944\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1945\u001b[0m     {\n\u001b[0;32m   1946\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {\n\u001b[0;32m   1947\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext/plain\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1948\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124muser will enter a floating points number let say 238.915. your task is \u001b[39m\u001b[38;5;130;01m\\\\\u001b[39;00m\u001b[38;5;124mnto find out the integer portion before the point (in this case 238) and\u001b[39m\u001b[38;5;130;01m\\\\\u001b[39;00m\u001b[38;5;124mnthen check if that integer portion is an even number or not\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1949\u001b[0m       ]\n\u001b[0;32m   1950\u001b[0m      },\n\u001b[0;32m   1951\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m110\u001b[39m,\n\u001b[0;32m   1952\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   1953\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecute_result\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1954\u001b[0m     }\n\u001b[0;32m   1955\u001b[0m    ],\n\u001b[0;32m   1956\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1957\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124muser will enter a floating points number let say 238.915. your task is \u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1958\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mto find out the integer portion before the point (in this case 238) and\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1959\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mthen check if that integer portion is an even number or not\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1960\u001b[0m    ]\n\u001b[0;32m   1961\u001b[0m   },\n\u001b[0;32m   1962\u001b[0m   {\n\u001b[0;32m   1963\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1964\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m112\u001b[39m,\n\u001b[0;32m   1965\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m53efe6fa-2426-4cd7-a338-43bed0e2ac10\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1966\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   1967\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1968\u001b[0m     {\n\u001b[0;32m   1969\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdin\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1970\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1971\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1972\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mEnter a real number:  25.3647\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1973\u001b[0m      ]\n\u001b[0;32m   1974\u001b[0m     },\n\u001b[0;32m   1975\u001b[0m     {\n\u001b[0;32m   1976\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1977\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1978\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1979\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m25\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1980\u001b[0m      ]\n\u001b[0;32m   1981\u001b[0m     }\n\u001b[0;32m   1982\u001b[0m    ],\n\u001b[0;32m   1983\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   1984\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124muser will enter a floating points number let say 238.915. your task is \u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1985\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mto find out the integer portion before the point (in this case 238) and\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1986\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mthen check if that integer portion is an even number or not\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1987\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1988\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mx=float(input(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mEnter a real number: \u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)) \u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1989\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124my=round(x)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1990\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mif y>x:\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1991\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    intPortion=y-1 #29.6\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1992\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124melse:\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1993\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    intPortion=y\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1994\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mprint(intPortion)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1995\u001b[0m    ]\n\u001b[0;32m   1996\u001b[0m   },\n\u001b[0;32m   1997\u001b[0m   {\n\u001b[0;32m   1998\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1999\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m113\u001b[39m,\n\u001b[0;32m   2000\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m4a47dfe6-56cd-437b-b383-ca7bf34d3551\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2001\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   2002\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2003\u001b[0m     {\n\u001b[0;32m   2004\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {\n\u001b[0;32m   2005\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext/plain\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2006\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m-9\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2007\u001b[0m       ]\n\u001b[0;32m   2008\u001b[0m      },\n\u001b[0;32m   2009\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m113\u001b[39m,\n\u001b[0;32m   2010\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   2011\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecute_result\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2012\u001b[0m     }\n\u001b[0;32m   2013\u001b[0m    ],\n\u001b[0;32m   2014\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2015\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mround(-9,3)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2016\u001b[0m    ]\n\u001b[0;32m   2017\u001b[0m   },\n\u001b[0;32m   2018\u001b[0m   {\n\u001b[0;32m   2019\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2020\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m118\u001b[39m,\n\u001b[0;32m   2021\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m46276c2f-6253-486e-a85b-f0112cb436dc\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2022\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   2023\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2024\u001b[0m     {\n\u001b[0;32m   2025\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdin\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2026\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2027\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2028\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mEnter a real number:  22.6\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2029\u001b[0m      ]\n\u001b[0;32m   2030\u001b[0m     },\n\u001b[0;32m   2031\u001b[0m     {\n\u001b[0;32m   2032\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2033\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2034\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2035\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124meven\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2036\u001b[0m      ]\n\u001b[0;32m   2037\u001b[0m     }\n\u001b[0;32m   2038\u001b[0m    ],\n\u001b[0;32m   2039\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2040\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124muser will enter a floating points number let say 238.915. your task is \u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2041\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mto find out the integer portion before the point (in this case 238) and\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2042\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mthen check if that integer portion is an even number or not\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2043\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2044\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mx=float(input(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mEnter a real number: \u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)) \u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2045\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124my=round(x)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2046\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mif x>0:\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2047\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    if y>x:\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2048\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m        intPortion=y-1 #29.6\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2049\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    else:\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2050\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m        intPortion=y\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2051\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124melse:  \u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2052\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    if y<x:\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2053\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m        intPortion=y+1\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2054\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    else:\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2055\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m        intPortion=y\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2056\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mif intPortion\u001b[39m\u001b[38;5;124m%\u001b[39m\u001b[38;5;124m2==0:\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2057\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    print(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124meven\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2058\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124melse:\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2059\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    print(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124modd\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2060\u001b[0m    ]\n\u001b[0;32m   2061\u001b[0m   },\n\u001b[0;32m   2062\u001b[0m   {\n\u001b[0;32m   2063\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmarkdown\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2064\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m15b9d03f-780d-4c0a-8a23-d2ee4d993272\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2065\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   2066\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2067\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m# CONTROL FLOW\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2068\u001b[0m    ]\n\u001b[0;32m   2069\u001b[0m   },\n\u001b[0;32m   2070\u001b[0m   {\n\u001b[0;32m   2071\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2072\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m119\u001b[39m,\n\u001b[0;32m   2073\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mbc084fed-4851-43e3-a5be-2d5596d391d8\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2074\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   2075\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2076\u001b[0m     {\n\u001b[0;32m   2077\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdin\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2078\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2079\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2080\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m 5\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2081\u001b[0m      ]\n\u001b[0;32m   2082\u001b[0m     },\n\u001b[0;32m   2083\u001b[0m     {\n\u001b[0;32m   2084\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2085\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2086\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2087\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m1\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2088\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mThis is iteration number : 1\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2089\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m4\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2090\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mThis is iteration number : 1\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2091\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m9\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2092\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mThis is iteration number : 1\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2093\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m16\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2094\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mThis is iteration number : 1\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2095\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mDone loop\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2096\u001b[0m      ]\n\u001b[0;32m   2097\u001b[0m     }\n\u001b[0;32m   2098\u001b[0m    ],\n\u001b[0;32m   2099\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2100\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mn=int(input())\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2101\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mi=1\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2102\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mwhile i<n:\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2103\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    print(i**2)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2104\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    print(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mThis is iteration number :\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m,1)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2105\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    i+=1  #i=i+1\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2106\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mprint(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mDone loop\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2107\u001b[0m    ]\n\u001b[0;32m   2108\u001b[0m   },\n\u001b[0;32m   2109\u001b[0m   {\n\u001b[0;32m   2110\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2111\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m120\u001b[39m,\n\u001b[0;32m   2112\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m0bca52ea-4236-4be9-b6af-f3ee1e6e8e81\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2113\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   2114\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2115\u001b[0m     {\n\u001b[0;32m   2116\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2117\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2118\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2119\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mInside ELSE\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2120\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mInside ELSE\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2121\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mInside ELSE\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2122\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mInside ELSE\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2123\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mInside ELSE\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2124\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mInside ELSE\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2125\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mInside ELSE\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2126\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mInside ELSE\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2127\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mInside IF\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2128\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mLoop is done\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2129\u001b[0m      ]\n\u001b[0;32m   2130\u001b[0m     }\n\u001b[0;32m   2131\u001b[0m    ],\n\u001b[0;32m   2132\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2133\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mn=10\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2134\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mi=1\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2135\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mwhile True:\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2136\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    if i\u001b[39m\u001b[38;5;124m%\u001b[39m\u001b[38;5;124m9==0:\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2137\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m        print(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mInside IF\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2138\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m        break\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2139\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    else:\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2140\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m        print(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mInside ELSE\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2141\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m        i=i+1  #i+=1\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2142\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mprint(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mLoop is done\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2143\u001b[0m    ]\n\u001b[0;32m   2144\u001b[0m   },\n\u001b[0;32m   2145\u001b[0m   {\n\u001b[0;32m   2146\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2147\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m122\u001b[39m,\n\u001b[0;32m   2148\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m421eafdd-8d2e-4e8d-9921-cfa923ba5bd2\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2149\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   2150\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2151\u001b[0m     {\n\u001b[0;32m   2152\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2153\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2154\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2155\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mInside IF\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2156\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mInside IF\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2157\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mInside IF\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2158\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mInside IF\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2159\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mInside IF\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2160\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mInside IF\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2161\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mInside IF\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2162\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mInside IF\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2163\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msomething\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2164\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msomethingelse\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2165\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdone\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2166\u001b[0m      ]\n\u001b[0;32m   2167\u001b[0m     }\n\u001b[0;32m   2168\u001b[0m    ],\n\u001b[0;32m   2169\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2170\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mn=10\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2171\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mi=1\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2172\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mwhile True:\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2173\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    if i\u001b[39m\u001b[38;5;124m%\u001b[39m\u001b[38;5;124m9 !=0:\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2174\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m        print(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mInside IF\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2175\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m        i +=1\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2176\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m        continue\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2177\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    print(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124msomething\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2178\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    print(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124msomethingelse\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2179\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    break\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2180\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    \u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2181\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mprint(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mdone\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2182\u001b[0m    ]\n\u001b[0;32m   2183\u001b[0m   },\n\u001b[0;32m   2184\u001b[0m   {\n\u001b[0;32m   2185\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2186\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m123\u001b[39m,\n\u001b[0;32m   2187\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m5afa0dab-e6a7-4abe-bdf2-8dd28af2256a\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2188\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   2189\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2190\u001b[0m     {\n\u001b[0;32m   2191\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2192\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2193\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2194\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m1\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2195\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m2\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2196\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m3\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2197\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m4\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2198\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m5\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2199\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m6\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2200\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m7\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2201\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m8\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2202\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m9\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2203\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m10\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2204\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2205\u001b[0m      ]\n\u001b[0;32m   2206\u001b[0m     }\n\u001b[0;32m   2207\u001b[0m    ],\n\u001b[0;32m   2208\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2209\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124ml=[]\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2210\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mfor i in range (10):\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2211\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    print(i+1)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2212\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    l.append(i**2)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2213\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mprint(l)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2214\u001b[0m    ]\n\u001b[0;32m   2215\u001b[0m   },\n\u001b[0;32m   2216\u001b[0m   {\n\u001b[0;32m   2217\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2218\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m124\u001b[39m,\n\u001b[0;32m   2219\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m70e90dbf-0c3d-48dc-a245-4f51f1f69b66\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2220\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   2221\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2222\u001b[0m     {\n\u001b[0;32m   2223\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2224\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2225\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2226\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m1\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2227\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m3\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2228\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m5\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2229\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m7\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2230\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m9\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2231\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m[0, 4, 16, 36, 64]\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2232\u001b[0m      ]\n\u001b[0;32m   2233\u001b[0m     }\n\u001b[0;32m   2234\u001b[0m    ],\n\u001b[0;32m   2235\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2236\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124ml=[]\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2237\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mfor i in range (0,10,2):\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2238\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    print(i+1)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2239\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    l.append(i**2)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2240\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mprint(l)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2241\u001b[0m    ]\n\u001b[0;32m   2242\u001b[0m   },\n\u001b[0;32m   2243\u001b[0m   {\n\u001b[0;32m   2244\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2245\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m125\u001b[39m,\n\u001b[0;32m   2246\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m25cef6be-3b53-4426-815a-cd261aee47b0\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2247\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   2248\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2249\u001b[0m     {\n\u001b[0;32m   2250\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2251\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2252\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2253\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m1\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2254\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m4\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2255\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m7\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2256\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m10\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2257\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m13\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2258\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m16\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2259\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m19\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2260\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m22\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2261\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m25\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2262\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m[0, 9, 36, 81, 144, 225, 324, 441, 576]\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2263\u001b[0m      ]\n\u001b[0;32m   2264\u001b[0m     }\n\u001b[0;32m   2265\u001b[0m    ],\n\u001b[0;32m   2266\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2267\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124ml=[]\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2268\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mfor i in range (0,25,3):\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2269\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    print(i+1)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2270\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    l.append(i**2)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2271\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mprint(l)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2272\u001b[0m    ]\n\u001b[0;32m   2273\u001b[0m   },\n\u001b[0;32m   2274\u001b[0m   {\n\u001b[0;32m   2275\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2276\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m126\u001b[39m,\n\u001b[0;32m   2277\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mbd4b94a1-92a4-44d7-bde9-332f8d72b87a\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2278\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   2279\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2280\u001b[0m     {\n\u001b[0;32m   2281\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2282\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2283\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2284\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcherry\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2285\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m4.9\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2286\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mapple\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2287\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mloop terminates with success\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2288\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mout side of the loop\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2289\u001b[0m      ]\n\u001b[0;32m   2290\u001b[0m     }\n\u001b[0;32m   2291\u001b[0m    ],\n\u001b[0;32m   2292\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2293\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124ms=\u001b[39m\u001b[38;5;124m{\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mapple\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m,4.9,\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mcherry\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m}\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2294\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mfor x in s:\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2295\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    print(x)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2296\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124melse:\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2297\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    print(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mloop terminates with success\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2298\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mprint(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mout side of the loop\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2299\u001b[0m    ]\n\u001b[0;32m   2300\u001b[0m   },\n\u001b[0;32m   2301\u001b[0m   {\n\u001b[0;32m   2302\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2303\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m128\u001b[39m,\n\u001b[0;32m   2304\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124me51cccc1-a6a0-4f13-9aba-794f9cfdcbed\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2305\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   2306\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2307\u001b[0m     {\n\u001b[0;32m   2308\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2309\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2310\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2311\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcherry\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2312\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m4.9\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2313\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mout side of the loop\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2314\u001b[0m      ]\n\u001b[0;32m   2315\u001b[0m     }\n\u001b[0;32m   2316\u001b[0m    ],\n\u001b[0;32m   2317\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2318\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124ms=\u001b[39m\u001b[38;5;124m{\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mapple\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m,4.9,\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mcherry\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m}\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2319\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mi=1\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2320\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mfor x in s:\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2321\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    print(x)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2322\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    i+=1\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2323\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    if i==3:\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2324\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m        break\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2325\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    else:\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2326\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m        pass\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2327\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124melse:\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2328\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    print(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mloop terminates with success\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2329\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mprint(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mout side of the loop\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2330\u001b[0m    ]\n\u001b[0;32m   2331\u001b[0m   },\n\u001b[0;32m   2332\u001b[0m   {\n\u001b[0;32m   2333\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2334\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m129\u001b[39m,\n\u001b[0;32m   2335\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mfaec4d28-7399-471d-a906-0765ba9b5426\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2336\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   2337\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2338\u001b[0m     {\n\u001b[0;32m   2339\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2340\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2341\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2342\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124ma 10\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2343\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mb -19\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2344\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mc abc\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2345\u001b[0m      ]\n\u001b[0;32m   2346\u001b[0m     }\n\u001b[0;32m   2347\u001b[0m    ],\n\u001b[0;32m   2348\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2349\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124md=\u001b[39m\u001b[38;5;124m{\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124ma\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m:10,\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mb\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m:-19,\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mc\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m:\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mabc\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m}\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2350\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mfor x in d:\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2351\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    print(x,d[x])\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2352\u001b[0m    ]\n\u001b[0;32m   2353\u001b[0m   },\n\u001b[0;32m   2354\u001b[0m   {\n\u001b[0;32m   2355\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2356\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m134\u001b[39m,\n\u001b[0;32m   2357\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mc8554a0e-2c4e-4246-9ffe-f12106fe8aee\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2358\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   2359\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2360\u001b[0m     {\n\u001b[0;32m   2361\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2362\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2363\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2364\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m[-5, 1, 2, 2, 3, 4, 7, 9]\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2365\u001b[0m      ]\n\u001b[0;32m   2366\u001b[0m     }\n\u001b[0;32m   2367\u001b[0m    ],\n\u001b[0;32m   2368\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2369\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mgiven a list of numbers ie [1,2,4,-5,7,9,3,2],make another list\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2370\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mthat contains all the items in sorted order from min to max ie your result\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2371\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mwill be another list like[-5,1,2,2,3,3,7,9]\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2372\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2373\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124ml=[1,2,4,-5,7,9,3,2]\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2374\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mfor j in range(len(l)):\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2375\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    m=l[j]\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2376\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    idx=j\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2377\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    c=j\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2378\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    for i in range(j,len(l)):\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2379\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m        if l[i]<m:\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2380\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m            m=l[i]\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2381\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m            idx=c\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2382\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m        c+=1\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2383\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    temp=l[j]\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2384\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    l[j]=m\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2385\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    l[idx]=temp\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2386\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mprint(l)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2387\u001b[0m    ]\n\u001b[0;32m   2388\u001b[0m   },\n\u001b[0;32m   2389\u001b[0m   {\n\u001b[0;32m   2390\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2391\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m135\u001b[39m,\n\u001b[0;32m   2392\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124maf4fd30c-9dd2-4de0-bc98-9b391e42e4c7\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2393\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   2394\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2395\u001b[0m     {\n\u001b[0;32m   2396\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {\n\u001b[0;32m   2397\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext/plain\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2398\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m[-5, 1, 2, 2, 3, 4, 7, 9]\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2399\u001b[0m       ]\n\u001b[0;32m   2400\u001b[0m      },\n\u001b[0;32m   2401\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m135\u001b[39m,\n\u001b[0;32m   2402\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   2403\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecute_result\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2404\u001b[0m     }\n\u001b[0;32m   2405\u001b[0m    ],\n\u001b[0;32m   2406\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2407\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124ml\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2408\u001b[0m    ]\n\u001b[0;32m   2409\u001b[0m   },\n\u001b[0;32m   2410\u001b[0m   {\n\u001b[0;32m   2411\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2412\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m136\u001b[39m,\n\u001b[0;32m   2413\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m980e8d0d-6903-43a9-b679-56dabe1a0402\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2414\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   2415\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [],\n\u001b[0;32m   2416\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2417\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdef printSuccess():\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2418\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    print(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mI m done\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2419\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    print(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mSend me another task\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2420\u001b[0m    ]\n\u001b[0;32m   2421\u001b[0m   },\n\u001b[0;32m   2422\u001b[0m   {\n\u001b[0;32m   2423\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2424\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m138\u001b[39m,\n\u001b[0;32m   2425\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m1c44d30b-e25e-4f43-86ba-d10cb241e155\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2426\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   2427\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2428\u001b[0m     {\n\u001b[0;32m   2429\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2430\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2431\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2432\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mI m done\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2433\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mSend me another task\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2434\u001b[0m      ]\n\u001b[0;32m   2435\u001b[0m     }\n\u001b[0;32m   2436\u001b[0m    ],\n\u001b[0;32m   2437\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2438\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mprintSuccess()\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2439\u001b[0m    ]\n\u001b[0;32m   2440\u001b[0m   },\n\u001b[0;32m   2441\u001b[0m   {\n\u001b[0;32m   2442\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2443\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m139\u001b[39m,\n\u001b[0;32m   2444\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mbc410b98-6d86-4eac-9644-bfecdce50183\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2445\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   2446\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2447\u001b[0m     {\n\u001b[0;32m   2448\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {\n\u001b[0;32m   2449\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext/plain\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2450\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m11\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2451\u001b[0m       ]\n\u001b[0;32m   2452\u001b[0m      },\n\u001b[0;32m   2453\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m139\u001b[39m,\n\u001b[0;32m   2454\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   2455\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecute_result\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2456\u001b[0m     }\n\u001b[0;32m   2457\u001b[0m    ],\n\u001b[0;32m   2458\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2459\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m3+8\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2460\u001b[0m    ]\n\u001b[0;32m   2461\u001b[0m   },\n\u001b[0;32m   2462\u001b[0m   {\n\u001b[0;32m   2463\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2464\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m140\u001b[39m,\n\u001b[0;32m   2465\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m39436259-3859-400e-83b4-35571b8f0200\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2466\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   2467\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2468\u001b[0m     {\n\u001b[0;32m   2469\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2470\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2471\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2472\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mI m done\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2473\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mSend me another task\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2474\u001b[0m      ]\n\u001b[0;32m   2475\u001b[0m     }\n\u001b[0;32m   2476\u001b[0m    ],\n\u001b[0;32m   2477\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2478\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mprintSuccess()\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2479\u001b[0m    ]\n\u001b[0;32m   2480\u001b[0m   },\n\u001b[0;32m   2481\u001b[0m   {\n\u001b[0;32m   2482\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2483\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m141\u001b[39m,\n\u001b[0;32m   2484\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m59bfb780-1d29-4c94-8707-6c908613a050\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2485\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   2486\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [],\n\u001b[0;32m   2487\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2488\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdef printS2():\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2489\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    \u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mthis function is doing nothing except\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2490\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    printing a message. that message is \u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mhello\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2491\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    \u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2492\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    print(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mhello\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2493\u001b[0m    ]\n\u001b[0;32m   2494\u001b[0m   },\n\u001b[0;32m   2495\u001b[0m   {\n\u001b[0;32m   2496\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2497\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m142\u001b[39m,\n\u001b[0;32m   2498\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdc62fe04-f834-4667-8240-0d2d8b503d6d\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2499\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   2500\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2501\u001b[0m     {\n\u001b[0;32m   2502\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {\n\u001b[0;32m   2503\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext/plain\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2504\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;31mSignature:\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m \u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0mprintS2\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;33m(\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;33m)\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;33m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;33m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2505\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;31mDocstring:\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2506\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mthis function is doing nothing except\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2507\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mprinting a message. that message is \u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mhello\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2508\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;31mFile:\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m      c:\u001b[39m\u001b[38;5;130;01m\\\\\u001b[39;00m\u001b[38;5;124musers\u001b[39m\u001b[38;5;130;01m\\\\\u001b[39;00m\u001b[38;5;124manush\u001b[39m\u001b[38;5;130;01m\\\\\u001b[39;00m\u001b[38;5;124mappdata\u001b[39m\u001b[38;5;130;01m\\\\\u001b[39;00m\u001b[38;5;124mlocal\u001b[39m\u001b[38;5;130;01m\\\\\u001b[39;00m\u001b[38;5;124mtemp\u001b[39m\u001b[38;5;130;01m\\\\\u001b[39;00m\u001b[38;5;124mipykernel_11792\u001b[39m\u001b[38;5;130;01m\\\\\u001b[39;00m\u001b[38;5;124m978269780.py\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2509\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;31mType:\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m      function\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2510\u001b[0m       ]\n\u001b[0;32m   2511\u001b[0m      },\n\u001b[0;32m   2512\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   2513\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdisplay_data\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2514\u001b[0m     }\n\u001b[0;32m   2515\u001b[0m    ],\n\u001b[0;32m   2516\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2517\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mprintS2?\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2518\u001b[0m    ]\n\u001b[0;32m   2519\u001b[0m   },\n\u001b[0;32m   2520\u001b[0m   {\n\u001b[0;32m   2521\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2522\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m143\u001b[39m,\n\u001b[0;32m   2523\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m3712f85e-2fb5-46ba-b474-77829ffe10b0\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2524\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   2525\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2526\u001b[0m     {\n\u001b[0;32m   2527\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {\n\u001b[0;32m   2528\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext/plain\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2529\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;31mSignature:\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m \u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0mprintS2\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;33m(\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;33m)\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;33m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;33m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2530\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;31mSource:\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m   \u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2531\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;32mdef\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m \u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0mprintS2\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;33m(\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;33m)\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;33m:\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;33m\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2532\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m    \u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;34m\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mthis function is doing nothing except\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2533\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    printing a message. that message is \u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mhello\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2534\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    \u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;33m\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2535\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m    \u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0mprint\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;33m(\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;34m\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mhello\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;33m)\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;33m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;33m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2536\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;31mFile:\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m      c:\u001b[39m\u001b[38;5;130;01m\\\\\u001b[39;00m\u001b[38;5;124musers\u001b[39m\u001b[38;5;130;01m\\\\\u001b[39;00m\u001b[38;5;124manush\u001b[39m\u001b[38;5;130;01m\\\\\u001b[39;00m\u001b[38;5;124mappdata\u001b[39m\u001b[38;5;130;01m\\\\\u001b[39;00m\u001b[38;5;124mlocal\u001b[39m\u001b[38;5;130;01m\\\\\u001b[39;00m\u001b[38;5;124mtemp\u001b[39m\u001b[38;5;130;01m\\\\\u001b[39;00m\u001b[38;5;124mipykernel_11792\u001b[39m\u001b[38;5;130;01m\\\\\u001b[39;00m\u001b[38;5;124m978269780.py\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2537\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;31mType:\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m      function\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2538\u001b[0m       ]\n\u001b[0;32m   2539\u001b[0m      },\n\u001b[0;32m   2540\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   2541\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdisplay_data\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2542\u001b[0m     }\n\u001b[0;32m   2543\u001b[0m    ],\n\u001b[0;32m   2544\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2545\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mprintS2??\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2546\u001b[0m    ]\n\u001b[0;32m   2547\u001b[0m   },\n\u001b[0;32m   2548\u001b[0m   {\n\u001b[0;32m   2549\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2550\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m144\u001b[39m,\n\u001b[0;32m   2551\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m1aaa0d82-5c4f-4907-be52-ff417ef68118\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2552\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   2553\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2554\u001b[0m     {\n\u001b[0;32m   2555\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {\n\u001b[0;32m   2556\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext/plain\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2557\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;31mSignature:\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m \u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0mlen\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;33m(\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0mobj\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;33m,\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m \u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;33m/\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;33m)\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;33m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;33m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2558\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;31mDocstring:\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m Return the number of items in a container.\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2559\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;31mType:\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m      builtin_function_or_method\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2560\u001b[0m       ]\n\u001b[0;32m   2561\u001b[0m      },\n\u001b[0;32m   2562\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   2563\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdisplay_data\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2564\u001b[0m     }\n\u001b[0;32m   2565\u001b[0m    ],\n\u001b[0;32m   2566\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2567\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mlen?\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2568\u001b[0m    ]\n\u001b[0;32m   2569\u001b[0m   },\n\u001b[0;32m   2570\u001b[0m   {\n\u001b[0;32m   2571\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2572\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m145\u001b[39m,\n\u001b[0;32m   2573\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mce8a69d1-6ea8-420e-acd1-cee065ae084f\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2574\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   2575\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2576\u001b[0m     {\n\u001b[0;32m   2577\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {\n\u001b[0;32m   2578\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext/plain\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2579\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;31mSignature:\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m \u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0mlen\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;33m(\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0mobj\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;33m,\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m \u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;33m/\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;33m)\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;33m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;33m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2580\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;31mDocstring:\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m Return the number of items in a container.\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2581\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;31mType:\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m      builtin_function_or_method\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2582\u001b[0m       ]\n\u001b[0;32m   2583\u001b[0m      },\n\u001b[0;32m   2584\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   2585\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdisplay_data\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2586\u001b[0m     }\n\u001b[0;32m   2587\u001b[0m    ],\n\u001b[0;32m   2588\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2589\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mlen??\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2590\u001b[0m    ]\n\u001b[0;32m   2591\u001b[0m   },\n\u001b[0;32m   2592\u001b[0m   {\n\u001b[0;32m   2593\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2594\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m146\u001b[39m,\n\u001b[0;32m   2595\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m782d7772-2e28-4372-a6f7-e4c804ab170a\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2596\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   2597\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2598\u001b[0m     {\n\u001b[0;32m   2599\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2600\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2601\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2602\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mHelp on function printS2 in module __main__:\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2603\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2604\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mprintS2()\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2605\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    this function is doing nothing except\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2606\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    printing a message. that message is \u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mhello\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2607\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2608\u001b[0m      ]\n\u001b[0;32m   2609\u001b[0m     }\n\u001b[0;32m   2610\u001b[0m    ],\n\u001b[0;32m   2611\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2612\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mhelp(printS2)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2613\u001b[0m    ]\n\u001b[0;32m   2614\u001b[0m   },\n\u001b[0;32m   2615\u001b[0m   {\n\u001b[0;32m   2616\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2617\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m147\u001b[39m,\n\u001b[0;32m   2618\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m208cabc5-8e97-4e00-84e4-f936ef80e9e8\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2619\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   2620\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2621\u001b[0m     {\n\u001b[0;32m   2622\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2623\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2624\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2625\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mhello\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2626\u001b[0m      ]\n\u001b[0;32m   2627\u001b[0m     }\n\u001b[0;32m   2628\u001b[0m    ],\n\u001b[0;32m   2629\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2630\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mprintS2()\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2631\u001b[0m    ]\n\u001b[0;32m   2632\u001b[0m   },\n\u001b[0;32m   2633\u001b[0m   {\n\u001b[0;32m   2634\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2635\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m151\u001b[39m,\n\u001b[0;32m   2636\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m7e84bfd6-8191-4072-8b43-d73a57d9d410\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2637\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   2638\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [],\n\u001b[0;32m   2639\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2640\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdef printMsg(msg):\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2641\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    \u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mthe function prints the message supplied by the user or \u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2642\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    prints that msg is not in the form of string\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2643\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    if isinstance(msg,str):\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2644\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m        print(msg)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2645\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    else:\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2646\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m        print(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mYour input agrument is not a string\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2647\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m        print(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mhere is the type of what you have supplied \u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m,type(msg))\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2648\u001b[0m    ]\n\u001b[0;32m   2649\u001b[0m   },\n\u001b[0;32m   2650\u001b[0m   {\n\u001b[0;32m   2651\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2652\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m152\u001b[39m,\n\u001b[0;32m   2653\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124ma8c7ce0b-03a1-4482-8944-b291e14c8959\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2654\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   2655\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2656\u001b[0m     {\n\u001b[0;32m   2657\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2658\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2659\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2660\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mHelp on function printMsg in module __main__:\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2661\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2662\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mprintMsg(msg)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2663\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    the function prints the message supplied by the user or\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2664\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    prints that msg is not in the form of string\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2665\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2666\u001b[0m      ]\n\u001b[0;32m   2667\u001b[0m     }\n\u001b[0;32m   2668\u001b[0m    ],\n\u001b[0;32m   2669\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2670\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mhelp(printMsg)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2671\u001b[0m    ]\n\u001b[0;32m   2672\u001b[0m   },\n\u001b[0;32m   2673\u001b[0m   {\n\u001b[0;32m   2674\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2675\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m153\u001b[39m,\n\u001b[0;32m   2676\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m4c373c4e-a957-4783-b685-ff1770d11a24\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2677\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   2678\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2679\u001b[0m     {\n\u001b[0;32m   2680\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {\n\u001b[0;32m   2681\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext/plain\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2682\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;31mSignature:\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m \u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0mprintMsg\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;33m(\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0mmsg\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;33m)\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;33m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;33m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2683\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;31mSource:\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m   \u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2684\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;32mdef\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m \u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0mprintMsg\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;33m(\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0mmsg\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;33m)\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;33m:\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;33m\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2685\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m    \u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;34m\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mthe function prints the message supplied by the user or \u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2686\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    prints that msg is not in the form of string\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;33m\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2687\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m    \u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;32mif\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m \u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0misinstance\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;33m(\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0mmsg\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;33m,\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0mstr\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;33m)\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;33m:\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;33m\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2688\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m        \u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0mprint\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;33m(\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0mmsg\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;33m)\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;33m\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2689\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m    \u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;32melse\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;33m:\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;33m\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2690\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m        \u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0mprint\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;33m(\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;34m\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mYour input agrument is not a string\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;33m)\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;33m\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2691\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m        \u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0mprint\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;33m(\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;34m\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mhere is the type of what you have supplied \u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;33m,\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0mtype\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;33m(\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0mmsg\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;33m)\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;33m)\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;33m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;33m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2692\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;31mFile:\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m      c:\u001b[39m\u001b[38;5;130;01m\\\\\u001b[39;00m\u001b[38;5;124musers\u001b[39m\u001b[38;5;130;01m\\\\\u001b[39;00m\u001b[38;5;124manush\u001b[39m\u001b[38;5;130;01m\\\\\u001b[39;00m\u001b[38;5;124mappdata\u001b[39m\u001b[38;5;130;01m\\\\\u001b[39;00m\u001b[38;5;124mlocal\u001b[39m\u001b[38;5;130;01m\\\\\u001b[39;00m\u001b[38;5;124mtemp\u001b[39m\u001b[38;5;130;01m\\\\\u001b[39;00m\u001b[38;5;124mipykernel_11792\u001b[39m\u001b[38;5;130;01m\\\\\u001b[39;00m\u001b[38;5;124m1949362964.py\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2693\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;31mType:\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m      function\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2694\u001b[0m       ]\n\u001b[0;32m   2695\u001b[0m      },\n\u001b[0;32m   2696\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   2697\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdisplay_data\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2698\u001b[0m     }\n\u001b[0;32m   2699\u001b[0m    ],\n\u001b[0;32m   2700\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2701\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mprintMsg??\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2702\u001b[0m    ]\n\u001b[0;32m   2703\u001b[0m   },\n\u001b[0;32m   2704\u001b[0m   {\n\u001b[0;32m   2705\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2706\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m154\u001b[39m,\n\u001b[0;32m   2707\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124md6916560-502f-4ad6-938a-f269e0212eba\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2708\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   2709\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2710\u001b[0m     {\n\u001b[0;32m   2711\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2712\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2713\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2714\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mthis is the message\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2715\u001b[0m      ]\n\u001b[0;32m   2716\u001b[0m     }\n\u001b[0;32m   2717\u001b[0m    ],\n\u001b[0;32m   2718\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2719\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mprintMsg(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mthis is the message\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2720\u001b[0m    ]\n\u001b[0;32m   2721\u001b[0m   },\n\u001b[0;32m   2722\u001b[0m   {\n\u001b[0;32m   2723\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2724\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m155\u001b[39m,\n\u001b[0;32m   2725\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m408c5127-f6cd-4a9e-b371-c06f2df1386e\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2726\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   2727\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2728\u001b[0m     {\n\u001b[0;32m   2729\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2730\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2731\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2732\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mYour input agrument is not a string\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2733\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mhere is the type of what you have supplied  <class \u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mint\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124m>\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2734\u001b[0m      ]\n\u001b[0;32m   2735\u001b[0m     }\n\u001b[0;32m   2736\u001b[0m    ],\n\u001b[0;32m   2737\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2738\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mprintMsg(34)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2739\u001b[0m    ]\n\u001b[0;32m   2740\u001b[0m   },\n\u001b[0;32m   2741\u001b[0m   {\n\u001b[0;32m   2742\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2743\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m156\u001b[39m,\n\u001b[0;32m   2744\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m45c1d5b2-bb71-4624-8b37-c40f32a88858\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2745\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   2746\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2747\u001b[0m     {\n\u001b[0;32m   2748\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2749\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2750\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2751\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mhello there\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2752\u001b[0m      ]\n\u001b[0;32m   2753\u001b[0m     }\n\u001b[0;32m   2754\u001b[0m    ],\n\u001b[0;32m   2755\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2756\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124my=\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mhello there\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2757\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mprintMsg(y)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2758\u001b[0m    ]\n\u001b[0;32m   2759\u001b[0m   },\n\u001b[0;32m   2760\u001b[0m   {\n\u001b[0;32m   2761\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2762\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m157\u001b[39m,\n\u001b[0;32m   2763\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m7f2be684-76b2-419e-9e36-c95a31adba7e\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2764\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   2765\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [],\n\u001b[0;32m   2766\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2767\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdef mypow(a,b):\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2768\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    \u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mthis function computes power just like builtin\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2769\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    pow function\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2770\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    c=a**b\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2771\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    print(c)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2772\u001b[0m    ]\n\u001b[0;32m   2773\u001b[0m   },\n\u001b[0;32m   2774\u001b[0m   {\n\u001b[0;32m   2775\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2776\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m158\u001b[39m,\n\u001b[0;32m   2777\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m094aded9-7bba-4a71-975c-50a21fb929ea\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2778\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   2779\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2780\u001b[0m     {\n\u001b[0;32m   2781\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {\n\u001b[0;32m   2782\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext/plain\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2783\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;31mSignature:\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m \u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0mmypow\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;33m(\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0ma\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;33m,\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m \u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0mb\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;33m)\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;33m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;33m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2784\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;31mDocstring:\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2785\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mthis function computes power just like builtin\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2786\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mpow function\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2787\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;31mFile:\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m      c:\u001b[39m\u001b[38;5;130;01m\\\\\u001b[39;00m\u001b[38;5;124musers\u001b[39m\u001b[38;5;130;01m\\\\\u001b[39;00m\u001b[38;5;124manush\u001b[39m\u001b[38;5;130;01m\\\\\u001b[39;00m\u001b[38;5;124mappdata\u001b[39m\u001b[38;5;130;01m\\\\\u001b[39;00m\u001b[38;5;124mlocal\u001b[39m\u001b[38;5;130;01m\\\\\u001b[39;00m\u001b[38;5;124mtemp\u001b[39m\u001b[38;5;130;01m\\\\\u001b[39;00m\u001b[38;5;124mipykernel_11792\u001b[39m\u001b[38;5;130;01m\\\\\u001b[39;00m\u001b[38;5;124m1501445254.py\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2788\u001b[0m        \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[1;31mType:\u001b[39m\u001b[38;5;130;01m\\u001b\u001b[39;00m\u001b[38;5;124m[0m      function\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2789\u001b[0m       ]\n\u001b[0;32m   2790\u001b[0m      },\n\u001b[0;32m   2791\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   2792\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdisplay_data\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2793\u001b[0m     }\n\u001b[0;32m   2794\u001b[0m    ],\n\u001b[0;32m   2795\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2796\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmypow?\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2797\u001b[0m    ]\n\u001b[0;32m   2798\u001b[0m   },\n\u001b[0;32m   2799\u001b[0m   {\n\u001b[0;32m   2800\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2801\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m159\u001b[39m,\n\u001b[0;32m   2802\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m00ca3e95-7f4f-47f0-9d56-f438aedf67bd\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2803\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   2804\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2805\u001b[0m     {\n\u001b[0;32m   2806\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2807\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2808\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2809\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m81\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2810\u001b[0m      ]\n\u001b[0;32m   2811\u001b[0m     }\n\u001b[0;32m   2812\u001b[0m    ],\n\u001b[0;32m   2813\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2814\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmypow(3,4)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2815\u001b[0m    ]\n\u001b[0;32m   2816\u001b[0m   },\n\u001b[0;32m   2817\u001b[0m   {\n\u001b[0;32m   2818\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2819\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m168\u001b[39m,\n\u001b[0;32m   2820\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m55868970-beef-4f16-a326-1c6a34cde102\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2821\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   2822\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [],\n\u001b[0;32m   2823\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2824\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdef checkArgs(a,b,c):\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2825\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    if isinstance(a,(int,float)) and isinstance(b,(int,float)) and isinstance(c,(int,float)):\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2826\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m        print((a+b+c)**2)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2827\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    else:\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2828\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m        print(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mError: the input arg are not of the expected types\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2829\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    \u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2830\u001b[0m    ]\n\u001b[0;32m   2831\u001b[0m   },\n\u001b[0;32m   2832\u001b[0m   {\n\u001b[0;32m   2833\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2834\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m169\u001b[39m,\n\u001b[0;32m   2835\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m4bd4d666-b9db-4db4-a225-ce00ca5be266\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2836\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   2837\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2838\u001b[0m     {\n\u001b[0;32m   2839\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2840\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2841\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2842\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m144\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2843\u001b[0m      ]\n\u001b[0;32m   2844\u001b[0m     }\n\u001b[0;32m   2845\u001b[0m    ],\n\u001b[0;32m   2846\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2847\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcheckArgs(3,4,5)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2848\u001b[0m    ]\n\u001b[0;32m   2849\u001b[0m   },\n\u001b[0;32m   2850\u001b[0m   {\n\u001b[0;32m   2851\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2852\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m170\u001b[39m,\n\u001b[0;32m   2853\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m655506c2-714a-4213-9f11-8a0900dfbf5f\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2854\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   2855\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2856\u001b[0m     {\n\u001b[0;32m   2857\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2858\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2859\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2860\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mError: the input arg are not of the expected types\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2861\u001b[0m      ]\n\u001b[0;32m   2862\u001b[0m     }\n\u001b[0;32m   2863\u001b[0m    ],\n\u001b[0;32m   2864\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2865\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcheckArgs(3,4,\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mg\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2866\u001b[0m    ]\n\u001b[0;32m   2867\u001b[0m   },\n\u001b[0;32m   2868\u001b[0m   {\n\u001b[0;32m   2869\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2870\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m174\u001b[39m,\n\u001b[0;32m   2871\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m9c2b510b-626c-4e28-830b-62b94716f67f\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2872\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   2873\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2874\u001b[0m     {\n\u001b[0;32m   2875\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2876\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2877\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2878\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m196\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2879\u001b[0m      ]\n\u001b[0;32m   2880\u001b[0m     }\n\u001b[0;32m   2881\u001b[0m    ],\n\u001b[0;32m   2882\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2883\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcheckArgs(3,8,3)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2884\u001b[0m    ]\n\u001b[0;32m   2885\u001b[0m   },\n\u001b[0;32m   2886\u001b[0m   {\n\u001b[0;32m   2887\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2888\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m175\u001b[39m,\n\u001b[0;32m   2889\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mc55e821b-2196-4078-93d3-7cd9415f5ec9\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2890\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   2891\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [],\n\u001b[0;32m   2892\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2893\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdef f(a,b,c):\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2894\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    print(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mA is :\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m,a)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2895\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    print(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mB is :\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m,b)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2896\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    print(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mC is :\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m,c)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2897\u001b[0m    ]\n\u001b[0;32m   2898\u001b[0m   },\n\u001b[0;32m   2899\u001b[0m   {\n\u001b[0;32m   2900\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2901\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m176\u001b[39m,\n\u001b[0;32m   2902\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m0b83cea2-679d-4c61-84da-310e7a19432f\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2903\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   2904\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2905\u001b[0m     {\n\u001b[0;32m   2906\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2907\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2908\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2909\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mA is : 2\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2910\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mB is : 10.3\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2911\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mC is : game\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2912\u001b[0m      ]\n\u001b[0;32m   2913\u001b[0m     }\n\u001b[0;32m   2914\u001b[0m    ],\n\u001b[0;32m   2915\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2916\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mf(2,10.3,\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mgame\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2917\u001b[0m    ]\n\u001b[0;32m   2918\u001b[0m   },\n\u001b[0;32m   2919\u001b[0m   {\n\u001b[0;32m   2920\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2921\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m177\u001b[39m,\n\u001b[0;32m   2922\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m32fe206c-5a62-4a28-a3d2-15929c22cdfc\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2923\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   2924\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2925\u001b[0m     {\n\u001b[0;32m   2926\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2927\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2928\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2929\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mA is : 2\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2930\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mB is : 3\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2931\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mC is : game\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2932\u001b[0m      ]\n\u001b[0;32m   2933\u001b[0m     }\n\u001b[0;32m   2934\u001b[0m    ],\n\u001b[0;32m   2935\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2936\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mf(a=2,b=3,c=\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mgame\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2937\u001b[0m    ]\n\u001b[0;32m   2938\u001b[0m   },\n\u001b[0;32m   2939\u001b[0m   {\n\u001b[0;32m   2940\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2941\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m180\u001b[39m,\n\u001b[0;32m   2942\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m54912cb9-5ee6-4d24-8102-5a4bcf09cb16\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2943\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   2944\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [],\n\u001b[0;32m   2945\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2946\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdef myadd(a,b):\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2947\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    Value=a+b\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2948\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    return Value\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2949\u001b[0m    ]\n\u001b[0;32m   2950\u001b[0m   },\n\u001b[0;32m   2951\u001b[0m   {\n\u001b[0;32m   2952\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2953\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m182\u001b[39m,\n\u001b[0;32m   2954\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m35a682c2-0525-4078-91ca-daddd613e8d5\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2955\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   2956\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2957\u001b[0m     {\n\u001b[0;32m   2958\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2959\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2960\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2961\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m5\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2962\u001b[0m      ]\n\u001b[0;32m   2963\u001b[0m     }\n\u001b[0;32m   2964\u001b[0m    ],\n\u001b[0;32m   2965\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2966\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124md=myadd(2,3)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2967\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mprint(d)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2968\u001b[0m    ]\n\u001b[0;32m   2969\u001b[0m   },\n\u001b[0;32m   2970\u001b[0m   {\n\u001b[0;32m   2971\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2972\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m183\u001b[39m,\n\u001b[0;32m   2973\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124md25c8af5-19c7-480b-9d78-0bc083eb1ebc\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2974\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   2975\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [],\n\u001b[0;32m   2976\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2977\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mVarOutSideTheFunction=3\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2978\u001b[0m    ]\n\u001b[0;32m   2979\u001b[0m   },\n\u001b[0;32m   2980\u001b[0m   {\n\u001b[0;32m   2981\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2982\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m187\u001b[39m,\n\u001b[0;32m   2983\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mf22c80b2-e665-47f2-9698-7f59eadd8d18\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2984\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   2985\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [],\n\u001b[0;32m   2986\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2987\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdef j():\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2988\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    VarOutSideTheFunction=7\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2989\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    print(VarOutSideTheFunction)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   2990\u001b[0m    ]\n\u001b[0;32m   2991\u001b[0m   },\n\u001b[0;32m   2992\u001b[0m   {\n\u001b[0;32m   2993\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2994\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m188\u001b[39m,\n\u001b[0;32m   2995\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m843a0492-c785-4caf-a818-04b374622fa7\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   2996\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   2997\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   2998\u001b[0m     {\n\u001b[0;32m   2999\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3000\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3001\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   3002\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m7\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   3003\u001b[0m      ]\n\u001b[0;32m   3004\u001b[0m     }\n\u001b[0;32m   3005\u001b[0m    ],\n\u001b[0;32m   3006\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   3007\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mj()\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   3008\u001b[0m    ]\n\u001b[0;32m   3009\u001b[0m   },\n\u001b[0;32m   3010\u001b[0m   {\n\u001b[0;32m   3011\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3012\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m189\u001b[39m,\n\u001b[0;32m   3013\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124me4fa988d-90dc-4e55-8687-e1c9a63c1ebc\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3014\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   3015\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   3016\u001b[0m     {\n\u001b[0;32m   3017\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3018\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3019\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   3020\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m3\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   3021\u001b[0m      ]\n\u001b[0;32m   3022\u001b[0m     }\n\u001b[0;32m   3023\u001b[0m    ],\n\u001b[0;32m   3024\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   3025\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mprint(VarOutSideTheFunction)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   3026\u001b[0m    ]\n\u001b[0;32m   3027\u001b[0m   },\n\u001b[0;32m   3028\u001b[0m   {\n\u001b[0;32m   3029\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3030\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m190\u001b[39m,\n\u001b[0;32m   3031\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mf85052d3-5214-468e-8a1d-86b1a24dcfc0\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3032\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   3033\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [],\n\u001b[0;32m   3034\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   3035\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdef j():\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3036\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    VarOutSideTheFunction=7\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3037\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    #print(VarOutSideTheFunction)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   3038\u001b[0m    ]\n\u001b[0;32m   3039\u001b[0m   },\n\u001b[0;32m   3040\u001b[0m   {\n\u001b[0;32m   3041\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3042\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m191\u001b[39m,\n\u001b[0;32m   3043\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mbe495ff3-3526-4b3e-9499-15f1bd194532\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3044\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   3045\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   3046\u001b[0m     {\n\u001b[0;32m   3047\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3048\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3049\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   3050\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mNone\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   3051\u001b[0m      ]\n\u001b[0;32m   3052\u001b[0m     }\n\u001b[0;32m   3053\u001b[0m    ],\n\u001b[0;32m   3054\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   3055\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mprint(j())\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   3056\u001b[0m    ]\n\u001b[0;32m   3057\u001b[0m   },\n\u001b[0;32m   3058\u001b[0m   {\n\u001b[0;32m   3059\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3060\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m195\u001b[39m,\n\u001b[0;32m   3061\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m7d6f47bf-4b1f-4e75-9050-73f9d7b77f64\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3062\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   3063\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   3064\u001b[0m     {\n\u001b[0;32m   3065\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3066\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3067\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   3068\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m<class \u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mNoneType\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124m>\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   3069\u001b[0m      ]\n\u001b[0;32m   3070\u001b[0m     }\n\u001b[0;32m   3071\u001b[0m    ],\n\u001b[0;32m   3072\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   3073\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mprint(type(j()))\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   3074\u001b[0m    ]\n\u001b[0;32m   3075\u001b[0m   },\n\u001b[0;32m   3076\u001b[0m   {\n\u001b[0;32m   3077\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3078\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m196\u001b[39m,\n\u001b[0;32m   3079\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124ma7ddd493-3d33-4ec4-88fa-bd8ede1fecf9\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3080\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   3081\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   3082\u001b[0m     {\n\u001b[0;32m   3083\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3084\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3085\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   3086\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m3\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   3087\u001b[0m      ]\n\u001b[0;32m   3088\u001b[0m     }\n\u001b[0;32m   3089\u001b[0m    ],\n\u001b[0;32m   3090\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   3091\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mprint(VarOutSideTheFunction)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   3092\u001b[0m    ]\n\u001b[0;32m   3093\u001b[0m   },\n\u001b[0;32m   3094\u001b[0m   {\n\u001b[0;32m   3095\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3096\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m197\u001b[39m,\n\u001b[0;32m   3097\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mca06b34a-7b96-4364-b9c5-f576d7be7f0e\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3098\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   3099\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [],\n\u001b[0;32m   3100\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   3101\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdef h():\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3102\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    print(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mA\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3103\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    a=3\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3104\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    b=5\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3105\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    c=a+b\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3106\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    print(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124msomething\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3107\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    return\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3108\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    print(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mb\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3109\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    print(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mc\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   3110\u001b[0m    ]\n\u001b[0;32m   3111\u001b[0m   },\n\u001b[0;32m   3112\u001b[0m   {\n\u001b[0;32m   3113\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3114\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m198\u001b[39m,\n\u001b[0;32m   3115\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mda720f4a-cbd1-4054-9f12-fa43e80850d3\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3116\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   3117\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   3118\u001b[0m     {\n\u001b[0;32m   3119\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3120\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3121\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   3122\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mA\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3123\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msomething\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   3124\u001b[0m      ]\n\u001b[0;32m   3125\u001b[0m     }\n\u001b[0;32m   3126\u001b[0m    ],\n\u001b[0;32m   3127\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   3128\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mh()\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   3129\u001b[0m    ]\n\u001b[0;32m   3130\u001b[0m   },\n\u001b[0;32m   3131\u001b[0m   {\n\u001b[0;32m   3132\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3133\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m199\u001b[39m,\n\u001b[0;32m   3134\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m912418e0-1467-40ea-8120-2b88678b1049\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3135\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   3136\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   3137\u001b[0m     {\n\u001b[0;32m   3138\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3139\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3140\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   3141\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mA\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3142\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msomething\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3143\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mNone\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   3144\u001b[0m      ]\n\u001b[0;32m   3145\u001b[0m     }\n\u001b[0;32m   3146\u001b[0m    ],\n\u001b[0;32m   3147\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   3148\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mprint(h())\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   3149\u001b[0m    ]\n\u001b[0;32m   3150\u001b[0m   },\n\u001b[0;32m   3151\u001b[0m   {\n\u001b[0;32m   3152\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3153\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m200\u001b[39m,\n\u001b[0;32m   3154\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m043dcd73-0892-4a44-be3b-b80d1e94f045\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3155\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   3156\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [],\n\u001b[0;32m   3157\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   3158\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdef h():\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3159\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    print(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mA\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3160\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    a=3\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3161\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    b=5\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3162\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    c=a+b\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3163\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    print(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124msomething\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3164\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    return c\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3165\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    print(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mb\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3166\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    print(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mc\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   3167\u001b[0m    ]\n\u001b[0;32m   3168\u001b[0m   },\n\u001b[0;32m   3169\u001b[0m   {\n\u001b[0;32m   3170\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3171\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m201\u001b[39m,\n\u001b[0;32m   3172\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124md8f496ca-fe12-4b41-82ec-86447b38d969\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3173\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   3174\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   3175\u001b[0m     {\n\u001b[0;32m   3176\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3177\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3178\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   3179\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mA\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3180\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msomething\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3181\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m<class \u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mint\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124m>\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   3182\u001b[0m      ]\n\u001b[0;32m   3183\u001b[0m     }\n\u001b[0;32m   3184\u001b[0m    ],\n\u001b[0;32m   3185\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   3186\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mprint(type(h()))\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   3187\u001b[0m    ]\n\u001b[0;32m   3188\u001b[0m   },\n\u001b[0;32m   3189\u001b[0m   {\n\u001b[0;32m   3190\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3191\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m202\u001b[39m,\n\u001b[0;32m   3192\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124ma09485f7-aefd-4b62-a367-0c40fd0ca9fe\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3193\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   3194\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [],\n\u001b[0;32m   3195\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   3196\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdef k():\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3197\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    a=5\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3198\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    b=7\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3199\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    d=\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124msomething\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3200\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    return a,b,d\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   3201\u001b[0m    ]\n\u001b[0;32m   3202\u001b[0m   },\n\u001b[0;32m   3203\u001b[0m   {\n\u001b[0;32m   3204\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3205\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m205\u001b[39m,\n\u001b[0;32m   3206\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m6a41bf3e-5809-408e-b526-1d88b5d0efd5\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3207\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   3208\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   3209\u001b[0m     {\n\u001b[0;32m   3210\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3211\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3212\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   3213\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m5 7 something\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   3214\u001b[0m      ]\n\u001b[0;32m   3215\u001b[0m     }\n\u001b[0;32m   3216\u001b[0m    ],\n\u001b[0;32m   3217\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   3218\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mx,y,z=k()\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3219\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mprint(x,y,z)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   3220\u001b[0m    ]\n\u001b[0;32m   3221\u001b[0m   },\n\u001b[0;32m   3222\u001b[0m   {\n\u001b[0;32m   3223\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3224\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m206\u001b[39m,\n\u001b[0;32m   3225\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m062a18e6-0417-47a2-a79d-d22c6194e9e6\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3226\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   3227\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [],\n\u001b[0;32m   3228\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   3229\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdef MyAddUniversity(*args):\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3230\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    s=0\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3231\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    for i in range(len(args)):\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3232\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m        s+=args[i]\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3233\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m        return s\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3234\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m        \u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   3235\u001b[0m    ]\n\u001b[0;32m   3236\u001b[0m   },\n\u001b[0;32m   3237\u001b[0m   {\n\u001b[0;32m   3238\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3239\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m207\u001b[39m,\n\u001b[0;32m   3240\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m8d0c1473-7bbd-43db-b3e0-1e383dec3991\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3241\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   3242\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   3243\u001b[0m     {\n\u001b[0;32m   3244\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3245\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3246\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   3247\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m2\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   3248\u001b[0m      ]\n\u001b[0;32m   3249\u001b[0m     }\n\u001b[0;32m   3250\u001b[0m    ],\n\u001b[0;32m   3251\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   3252\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mprint(MyAddUniversity(2,4,5,4.6,78))\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   3253\u001b[0m    ]\n\u001b[0;32m   3254\u001b[0m   },\n\u001b[0;32m   3255\u001b[0m   {\n\u001b[0;32m   3256\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3257\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m208\u001b[39m,\n\u001b[0;32m   3258\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m83ac7596-80b7-4d53-9d71-741227d16a2b\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3259\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   3260\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [],\n\u001b[0;32m   3261\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   3262\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdef printAllVarNamesAndValues(**args):\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3263\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    for x in args:\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3264\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m        print(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mvariable name is: \u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m,x , \u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mand value is : \u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m,args[x])\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   3265\u001b[0m    ]\n\u001b[0;32m   3266\u001b[0m   },\n\u001b[0;32m   3267\u001b[0m   {\n\u001b[0;32m   3268\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3269\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m209\u001b[39m,\n\u001b[0;32m   3270\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124ma7a57398-2b34-4cbf-b76b-951ddc2e446c\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3271\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   3272\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   3273\u001b[0m     {\n\u001b[0;32m   3274\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3275\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3276\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   3277\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mvariable name is:  a and value is :  3\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3278\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mvariable name is:  b and value is :  b\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3279\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mvariable name is:  c and value is :  aaa\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3280\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mvariable name is:  y and value is :  8.7\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   3281\u001b[0m      ]\n\u001b[0;32m   3282\u001b[0m     }\n\u001b[0;32m   3283\u001b[0m    ],\n\u001b[0;32m   3284\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   3285\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mprintAllVarNamesAndValues(a=3,b=\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mb\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m,c=\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124maaa\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m,y=8.7)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   3286\u001b[0m    ]\n\u001b[0;32m   3287\u001b[0m   },\n\u001b[0;32m   3288\u001b[0m   {\n\u001b[0;32m   3289\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3290\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m210\u001b[39m,\n\u001b[0;32m   3291\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m5b96f6e2-f3a6-4b62-a5ff-f2c4d0b3ab62\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3292\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   3293\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [],\n\u001b[0;32m   3294\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   3295\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdef aa(s=4):\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3296\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    print(s)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   3297\u001b[0m    ]\n\u001b[0;32m   3298\u001b[0m   },\n\u001b[0;32m   3299\u001b[0m   {\n\u001b[0;32m   3300\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3301\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m211\u001b[39m,\n\u001b[0;32m   3302\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mf42cd539-91ca-4e98-98b2-20f591a96bf5\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3303\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   3304\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   3305\u001b[0m     {\n\u001b[0;32m   3306\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3307\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3308\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   3309\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m4\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   3310\u001b[0m      ]\n\u001b[0;32m   3311\u001b[0m     }\n\u001b[0;32m   3312\u001b[0m    ],\n\u001b[0;32m   3313\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   3314\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124maa()\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   3315\u001b[0m    ]\n\u001b[0;32m   3316\u001b[0m   },\n\u001b[0;32m   3317\u001b[0m   {\n\u001b[0;32m   3318\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3319\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m212\u001b[39m,\n\u001b[0;32m   3320\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m4150267d-b728-4f97-b0be-4945665e69dd\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3321\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   3322\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   3323\u001b[0m     {\n\u001b[0;32m   3324\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3325\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3326\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   3327\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m32\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   3328\u001b[0m      ]\n\u001b[0;32m   3329\u001b[0m     }\n\u001b[0;32m   3330\u001b[0m    ],\n\u001b[0;32m   3331\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   3332\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124maa(32)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   3333\u001b[0m    ]\n\u001b[0;32m   3334\u001b[0m   },\n\u001b[0;32m   3335\u001b[0m   {\n\u001b[0;32m   3336\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3337\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m214\u001b[39m,\n\u001b[0;32m   3338\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m444f274a-f522-41ed-b38c-0f21e3527a9e\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3339\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   3340\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   3341\u001b[0m     {\n\u001b[0;32m   3342\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3343\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3344\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   3345\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m[-9, 2, 3]\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   3346\u001b[0m      ]\n\u001b[0;32m   3347\u001b[0m     }\n\u001b[0;32m   3348\u001b[0m    ],\n\u001b[0;32m   3349\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   3350\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mList=[1,2,3]\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3351\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124ml1=List\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3352\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124ml1[0]=-9\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3353\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mprint(List)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   3354\u001b[0m    ]\n\u001b[0;32m   3355\u001b[0m   },\n\u001b[0;32m   3356\u001b[0m   {\n\u001b[0;32m   3357\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3358\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m219\u001b[39m,\n\u001b[0;32m   3359\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m10e4c13b-e3a1-4fa7-adda-2dfead4628bb\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3360\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   3361\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [],\n\u001b[0;32m   3362\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   3363\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdef qq(List=[1,2]):\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3364\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    for i in List:\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3365\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m        print(i)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   3366\u001b[0m    ]\n\u001b[0;32m   3367\u001b[0m   },\n\u001b[0;32m   3368\u001b[0m   {\n\u001b[0;32m   3369\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3370\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m221\u001b[39m,\n\u001b[0;32m   3371\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124me20016bc-95d3-4e23-b1e9-1cd5f9daeb03\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3372\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   3373\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   3374\u001b[0m     {\n\u001b[0;32m   3375\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3376\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3377\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   3378\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m1\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3379\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m2\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   3380\u001b[0m      ]\n\u001b[0;32m   3381\u001b[0m     }\n\u001b[0;32m   3382\u001b[0m    ],\n\u001b[0;32m   3383\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   3384\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124ml1=[12,32,1]\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3385\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mqq()\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   3386\u001b[0m    ]\n\u001b[0;32m   3387\u001b[0m   },\n\u001b[0;32m   3388\u001b[0m   {\n\u001b[0;32m   3389\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3390\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m222\u001b[39m,\n\u001b[0;32m   3391\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m805e963e-5af1-4e6d-bbd2-43dd14502dc3\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3392\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   3393\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   3394\u001b[0m     {\n\u001b[0;32m   3395\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3396\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3397\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   3398\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m12\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3399\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m32\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3400\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m1\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   3401\u001b[0m      ]\n\u001b[0;32m   3402\u001b[0m     }\n\u001b[0;32m   3403\u001b[0m    ],\n\u001b[0;32m   3404\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   3405\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mqq(l1)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   3406\u001b[0m    ]\n\u001b[0;32m   3407\u001b[0m   },\n\u001b[0;32m   3408\u001b[0m   {\n\u001b[0;32m   3409\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[1;32m-> 3410\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: null,\n\u001b[0;32m   3411\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mfd89dd40-1dc9-4dfd-bacf-7fe655cca49f\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3412\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m   3413\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [],\n\u001b[0;32m   3414\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m   3415\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdef checkIfNotNum(**args):\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3416\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    retVal= True\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3417\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    for x in args:\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3418\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m        if not (isinstance(x,(int,float))):\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3419\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m            return False\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3420\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    return True\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3421\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3422\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdef addAllNum(*args):\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3423\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    s=0\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3424\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    for x in args:\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3425\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m        s+=x\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3426\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m        \u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3427\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    \u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   3428\u001b[0m    ]\n\u001b[0;32m   3429\u001b[0m   }\n\u001b[0;32m   3430\u001b[0m  ],\n\u001b[0;32m   3431\u001b[0m  \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {\n\u001b[0;32m   3432\u001b[0m   \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mkernelspec\u001b[39m\u001b[38;5;124m\"\u001b[39m: {\n\u001b[0;32m   3433\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdisplay_name\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mPython 3 (ipykernel)\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3434\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mlanguage\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mpython\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3435\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mpython3\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   3436\u001b[0m   },\n\u001b[0;32m   3437\u001b[0m   \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mlanguage_info\u001b[39m\u001b[38;5;124m\"\u001b[39m: {\n\u001b[0;32m   3438\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcodemirror_mode\u001b[39m\u001b[38;5;124m\"\u001b[39m: {\n\u001b[0;32m   3439\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mipython\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3440\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mversion\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m3\u001b[39m\n\u001b[0;32m   3441\u001b[0m    },\n\u001b[0;32m   3442\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mfile_extension\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m.py\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3443\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmimetype\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext/x-python\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3444\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mpython\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3445\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mnbconvert_exporter\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mpython\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3446\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mpygments_lexer\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mipython3\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   3447\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mversion\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m3.12.7\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   3448\u001b[0m   }\n\u001b[0;32m   3449\u001b[0m  },\n\u001b[0;32m   3450\u001b[0m  \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mnbformat\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m4\u001b[39m,\n\u001b[0;32m   3451\u001b[0m  \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mnbformat_minor\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m5\u001b[39m\n\u001b[0;32m   3452\u001b[0m }\n",
      "\u001b[1;31mNameError\u001b[0m: name 'null' is not defined"
     ]
    }
   ],
   "source": [
    "import python11.py as pp"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 232,
   "id": "e221618f-56f7-49c7-b9bf-c82233b21119",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'given a list of numbers ie [1,2,4,=5,7,9,3,2], make another list that \\ncontains all the items in sorted order from min to max ie your result will \\nbe another list like [-5,1,2,2,3,7,9]'"
      ]
     },
     "execution_count": 232,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\"\"\"given a list of numbers ie [1,2,4,=5,7,9,3,2], make another list that \n",
    "contains all the items in sorted order from min to max ie your result will \n",
    "be another list like [-5,1,2,2,3,7,9]\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 235,
   "id": "f30e1f28-e424-454f-918f-423155adb5a3",
   "metadata": {},
   "outputs": [],
   "source": [
    "def findMin(l):\n",
    "    m=l[0]\n",
    "    idx=0\n",
    "    i=0\n",
    "    for x in l:\n",
    "        if x<m:\n",
    "            m=x\n",
    "            idx=i\n",
    "        else:\n",
    "            pass\n",
    "        i+=1\n",
    "    return m,idx"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 236,
   "id": "8cc8fe7b-cadb-46ac-b906-39ebc095234d",
   "metadata": {},
   "outputs": [],
   "source": [
    "a,b=findMin([2,3,4,0,9])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 237,
   "id": "4941056f-f9d5-49e6-b6b4-3d6c7aaab063",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0 3\n"
     ]
    }
   ],
   "source": [
    "print(a,b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 242,
   "id": "354676cb-5013-4d20-ab68-608a5a7c8baa",
   "metadata": {},
   "outputs": [],
   "source": [
    "def swapVal(l,idx1,idx2):\n",
    "    tmp=l[idx1]\n",
    "    l[idx1]=l[idx2]\n",
    "    l[idx2]=tmp\n",
    "    return l"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 244,
   "id": "53afc003-9945-410d-a9fa-168c46c512f2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2, 7, 6, 3]\n"
     ]
    }
   ],
   "source": [
    "l=[2,3,6,7]\n",
    "l2=swapVal(l,1,3)\n",
    "print(l2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 245,
   "id": "2dc590b1-3bdd-4b44-8cde-aa34a7f1c8ef",
   "metadata": {},
   "outputs": [],
   "source": [
    "k=\"python is a good language\"\n",
    "kk=\"its good for data science\"    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 246,
   "id": "0b7079a0-5346-4d96-98a2-ac3e0f321b19",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "str"
      ]
     },
     "execution_count": 246,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(k)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 249,
   "id": "352a731f-e4dd-4187-a359-44b514a5aa4d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "python is a good language\n"
     ]
    }
   ],
   "source": [
    "print(k)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 250,
   "id": "3c9d3f07-6ecc-4540-a907-1bde24cb7303",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "python is a good languageits good for data science\n"
     ]
    }
   ],
   "source": [
    "v=k+kk\n",
    "print(v)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 252,
   "id": "af51e708-1f89-4e05-b075-b9340284dac9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "python is a good language its good for data science\n"
     ]
    }
   ],
   "source": [
    "v=k+\" \"+kk\n",
    "print(v)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 255,
   "id": "ec04500a-1eb9-4efd-88d2-698aadb80e94",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "the price of this book is: 12\n"
     ]
    }
   ],
   "source": [
    "price=12\n",
    "p=\"the price of this book \"\n",
    "cc=p+\"is: \"+str(price)\n",
    "print(cc)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 256,
   "id": "7921d42b-9a1e-4d3f-b4b2-5896bd3093a1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "this is the line1\n",
      "this is line 2\n",
      "this is last line and this line is 3\n"
     ]
    }
   ],
   "source": [
    "a11=\"\"\"this is the line1\n",
    "this is line 2\n",
    "this is last line and this line is 3\"\"\"\n",
    "print(a11)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 257,
   "id": "9df17348-4ba9-4e92-96af-7a8bd61e42b1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "the following options are available:\n",
      "        -a        :does nothing\n",
      "        -b        :also does nothing\n",
      "\n"
     ]
    }
   ],
   "source": [
    "print(\"\"\"the following options are available:\n",
    "        -a        :does nothing\n",
    "        -b        :also does nothing\n",
    "\"\"\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 258,
   "id": "8d094e8c-c219-4224-9f9a-12d2d951a3a6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "r\n"
     ]
    }
   ],
   "source": [
    "t=\"how are you and who are you\"\n",
    "print(t[5])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 259,
   "id": "a37cf5fb-0ce5-4bd8-afc8-05761fb1845e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "str"
      ]
     },
     "execution_count": 259,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(t[5])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 260,
   "id": "7fe8689b-0974-4e95-96f9-46c1190171dd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "' are yo'"
      ]
     },
     "execution_count": 260,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "t[3:10]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 261,
   "id": "50da44d2-5cbc-4408-b805-906afd1a2d96",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'u'"
      ]
     },
     "execution_count": 261,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "t[-1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 262,
   "id": "07defb67-e826-4f19-9ffe-6474b69c9e9e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "' are yo'"
      ]
     },
     "execution_count": 262,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "t[-8:-1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 263,
   "id": "68067e6a-ab05-4e18-81a6-b67ef2e82be7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'hwaeyu'"
      ]
     },
     "execution_count": 263,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "t[0:12:2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 264,
   "id": "0f03f796-d66e-4e7a-88c1-53d0b8f9887d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "abd    ofiwdkdnfnkd\n"
     ]
    }
   ],
   "source": [
    "rr=\"        abd    ofiwdkdnfnkd     \"\n",
    "b=rr.strip()\n",
    "print(b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 265,
   "id": "fd8b8061-38ab-48ab-b514-87165be8f52d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "aaaa bbb jjjjk sssss\n"
     ]
    }
   ],
   "source": [
    "sa=\"AAAA BBB jjjjk sssss\"\n",
    "c=sa.lower()\n",
    "print(c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 267,
   "id": "551250c8-275a-4f37-b0c8-2f52fc1dfc19",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "AAAA BBB JJJJK SSSSS\n"
     ]
    }
   ],
   "source": [
    "cc=sa.upper()\n",
    "print(cc)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 269,
   "id": "2b24f428-01da-4a1d-8cf9-b64499aa3350",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "***** BBB JJJJK SSSSS\n"
     ]
    }
   ],
   "source": [
    "vv=cc.replace(\"AAAA\",\"*****\")\n",
    "print(vv)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 270,
   "id": "618fce32-a084-49b3-88a9-d67a92aa2b8e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['ansb', 'nsand', 'njskdan', 'dfds']\n"
     ]
    }
   ],
   "source": [
    "ll=\"ansb:nsand:njskdan:dfds\"\n",
    "kj=ll.split(\":\")\n",
    "print(kj)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 271,
   "id": "3ca6ccfd-1d1f-4b3b-88e9-f072e2cebd36",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'dfds'"
      ]
     },
     "execution_count": 271,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "kj[3]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 272,
   "id": "58d28a0b-5319-4e3c-914a-3cf63e6bb759",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Ansb:nsand:njskdan:dfds'"
      ]
     },
     "execution_count": 272,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ll.capitalize()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 273,
   "id": "2d8029e2-e541-4dae-8fa2-59325ce73ac0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Help on built-in function count:\n",
      "\n",
      "count(...) method of builtins.str instance\n",
      "    S.count(sub[, start[, end]]) -> int\n",
      "\n",
      "    Return the number of non-overlapping occurrences of substring sub in\n",
      "    string S[start:end].  Optional arguments start and end are\n",
      "    interpreted as in slice notation.\n",
      "\n"
     ]
    }
   ],
   "source": [
    "help(ll.count)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 274,
   "id": "14e68888-a970-4929-a3ab-b1bf233112d1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 274,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\"abc\" in \"sdksnakbcjabjkdcjkfsdf\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 275,
   "id": "a2040b41-ff67-48b8-ad61-0787a01c4c5f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 275,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\"abc\" in \"abcjkhdsfirfs\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 276,
   "id": "b1ed50c7-f19c-49cb-950f-b0b9b296f646",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 276,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\"abc\"==\"abc\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 277,
   "id": "68379984-ee7e-403e-85fb-fd59ae48e052",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 277,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\"abc\"<\"def\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 278,
   "id": "8c77d24e-3851-4de8-af50-ebfbe629f088",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 278,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\"mklfndskjfn\"<\"def\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 279,
   "id": "0c5ab964-a10b-4fad-a1c5-e16d29fb454a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 279,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\"^&*^7\"<\"&*\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 280,
   "id": "99e6ae52-081e-4be6-9fe6-9959ca6bce66",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax. Perhaps you forgot a comma? (3062796511.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[280], line 1\u001b[1;36m\u001b[0m\n\u001b[1;33m    print(\"we r learing \"python \"here\")\u001b[0m\n\u001b[1;37m          ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax. Perhaps you forgot a comma?\n"
     ]
    }
   ],
   "source": [
    "print(\"we r learing \"python \"here\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 281,
   "id": "6f9505e6-89e3-43c2-b02b-eec3caddf4e6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "we r learing \"python here\"\n"
     ]
    }
   ],
   "source": [
    "print('we r learing \"python here\"')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 282,
   "id": "c8d74cc7-a38b-4069-a7ce-4288b068d37b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "we are learning\n",
      " python\n"
     ]
    }
   ],
   "source": [
    "print(\"we are learning\\n python\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 283,
   "id": "ed1e3fe4-55c5-44ae-bcbc-931250632ff0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "c\n",
      "ame\\drive\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "<>:1: SyntaxWarning: invalid escape sequence '\\d'\n",
      "<>:1: SyntaxWarning: invalid escape sequence '\\d'\n",
      "C:\\Users\\anush\\AppData\\Local\\Temp\\ipykernel_11792\\1232697684.py:1: SyntaxWarning: invalid escape sequence '\\d'\n",
      "  print(\"c\\name\\drive\")\n"
     ]
    }
   ],
   "source": [
    "print(\"c\\name\\drive\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 284,
   "id": "4cde237c-7a4e-460e-9d57-50a2cd535d23",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "c\\name\\drive\n"
     ]
    }
   ],
   "source": [
    "print(r\"c\\name\\drive\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "96d8612f-f48d-43a5-bb92-8e32968e9225",
   "metadata": {},
   "source": [
    "# DATA STRUCTURE(LIST,TUPLE ETC..)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 285,
   "id": "22b5c398-c26f-43dc-8da5-35a2dfce74f6",
   "metadata": {},
   "outputs": [],
   "source": [
    "list1=[1,3,4.9,\"name\",7]\n",
    "tuple1=(1,3,4.9,\"name\",7)\n",
    "set1={1,3,4.9,\"name\",7}\n",
    "dic={23:\"twothree\",'h':42,\"v\":\"fd\"}\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 286,
   "id": "863f066b-30ae-4bbc-9f2a-bda3c8fee8a1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "the type of list1 is :  <class 'list'>\n",
      "the type of tuple is :  <class 'tuple'>\n",
      "the type of set is :  <class 'set'>\n",
      "the type of dic is :  <class 'dict'>\n"
     ]
    }
   ],
   "source": [
    "print(\"the type of list1 is : \",type(list1))\n",
    "print(\"the type of tuple is : \",type(tuple1))\n",
    "print(\"the type of set is : \",type(set1))\n",
    "print(\"the type of dic is : \",type(dic))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 290,
   "id": "75b767be-08bc-46b4-8dba-7c0339d2b0e9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "name\n",
      "3\n",
      "True\n",
      "twothree\n"
     ]
    }
   ],
   "source": [
    "print(list1[3])\n",
    "print(tuple1[1])\n",
    "print(3 in set1)\n",
    "print(dic[23])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 291,
   "id": "e3d68c5f-c1cc-4940-951f-f29544492f26",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "42\n"
     ]
    }
   ],
   "source": [
    "print(dic['h'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 292,
   "id": "2dd31fb8-050f-449c-862e-8dbdfc31ba4d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{1, 3, 4.9, 7, 'name'}"
      ]
     },
     "execution_count": 292,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "set1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 293,
   "id": "0763abbb-9627-433f-a24e-89a0e5b0f2b7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 3, 4.9, 'name', 7]"
      ]
     },
     "execution_count": 293,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 294,
   "id": "c7b18003-0a19-4da7-bef8-114ba7289d4a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "list[slice(1, 3, None)]"
      ]
     },
     "execution_count": 294,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list[1:3]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 295,
   "id": "1cb73019-82c5-4694-96d4-b43384cfb6d7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 3, 4.9, 'name', 7]"
      ]
     },
     "execution_count": 295,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list1[:]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 296,
   "id": "992aeceb-5240-44eb-9aa7-8def0811de2c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[7, 'name', 4.9, 3, 1]"
      ]
     },
     "execution_count": 296,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list1[::-1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 297,
   "id": "d43a1515-fcfb-4543-a5db-3374a7bef34d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(1, 3, 4.9)"
      ]
     },
     "execution_count": 297,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tuple1[:3]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 299,
   "id": "d12e57f9-a37c-43a6-bcd8-3eee26d33b64",
   "metadata": {},
   "outputs": [],
   "source": [
    "list1=list1+[\"how\",\"are\",8,\"your\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 300,
   "id": "4b5e0d20-075e-4921-9a23-38e50b449fc8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 3, 4.9, 'name', 7, 'how', 'are', 8, 'your']"
      ]
     },
     "execution_count": 300,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 301,
   "id": "b560b0c0-d237-4100-83a8-09a2e887bb53",
   "metadata": {},
   "outputs": [],
   "source": [
    "t2=('a','v','s',45)\n",
    "t3=tuple1+t2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 302,
   "id": "f71ac54d-f8ce-4dc3-ab5e-de8e86124682",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(1, 3, 4.9, 'name', 7, 'a', 'v', 's', 45)"
      ]
     },
     "execution_count": 302,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "t3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 303,
   "id": "9d573c49-943a-477c-96da-d2050c63c8e4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{4.9, 'apple', 'cherry'}"
      ]
     },
     "execution_count": 303,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 304,
   "id": "47287b6c-0109-4971-ab5c-7f6f97491b10",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{1, 3, 4.9, 7, 'name'}"
      ]
     },
     "execution_count": 304,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "set1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 306,
   "id": "8872982f-a838-4e97-85d2-d3d9f9a2d7e8",
   "metadata": {},
   "outputs": [],
   "source": [
    "set1.update({32,\"hdsg\"})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 307,
   "id": "169430bd-506b-43c6-b322-8359b3b33c0b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{1, 3, 32, 4.9, 7, 'hdsg', 'name'}"
      ]
     },
     "execution_count": 307,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "set1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 308,
   "id": "1dda4b22-8002-4e44-aad0-f477c7412966",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{23: 'twothree', 'h': 42, 'v': 'fd'}"
      ]
     },
     "execution_count": 308,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dic"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 311,
   "id": "a20e7ecf-987e-432a-b089-eb78bfb3cbb0",
   "metadata": {},
   "outputs": [],
   "source": [
    "d2={\"16\":\"rhkh\",\"srjgsf\":\"srdbjf\"}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 312,
   "id": "61d61845-be50-4fcd-8139-256635cc237f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{23: 'twothree', 'h': 42, 'v': 'fd'}"
      ]
     },
     "execution_count": 312,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dic"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 313,
   "id": "1b3a8299-c445-46ed-95c8-c7778d212acb",
   "metadata": {},
   "outputs": [],
   "source": [
    "dic.update(d2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 314,
   "id": "fcb2ebb2-eb40-4c84-a1f3-81f58d8c1f82",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{23: 'twothree', 'h': 42, 'v': 'fd', '16': 'rhkh', 'srjgsf': 'srdbjf'}"
      ]
     },
     "execution_count": 314,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dic"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 315,
   "id": "d824d094-8ec0-4187-9565-28147ebfff22",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 3, 4.9, 'name', 7, 'how', 'are', 8, 'your']"
      ]
     },
     "execution_count": 315,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 316,
   "id": "419f1e28-96d7-4e4f-9f93-7103b78d7398",
   "metadata": {},
   "outputs": [],
   "source": [
    "l2=list1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 317,
   "id": "40b324df-502e-4bde-9ba2-1e0d2306394a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 3, 4.9, 'name', 7, 'how', 'are', 8, 'your']"
      ]
     },
     "execution_count": 317,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 318,
   "id": "a9892c3a-5b8d-4b44-8798-261d6520df03",
   "metadata": {},
   "outputs": [],
   "source": [
    "l2=list1.copy()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 319,
   "id": "babff3db-2600-40d1-8722-4d9dad7d72c8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 3, 4.9, 'name', 7, 'how', 'are', 8, 'your']"
      ]
     },
     "execution_count": 319,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 320,
   "id": "ea701b4a-746f-48bf-8002-dd330a7e3714",
   "metadata": {},
   "outputs": [],
   "source": [
    "l3=list1[1:5]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 321,
   "id": "d9e98b10-8ac9-4400-8ab7-a866b4b315f7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[3, 4.9, 'name', 7]"
      ]
     },
     "execution_count": 321,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 322,
   "id": "073cd9f0-1647-4424-8b5a-26acae7ad5b4",
   "metadata": {},
   "outputs": [],
   "source": [
    "l3[0]=\"three\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 323,
   "id": "346f3333-5862-4bb9-91d6-f06b92ebc8c1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['three', 4.9, 'name', 7]"
      ]
     },
     "execution_count": 323,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 332,
   "id": "b448c0ca-eae5-486b-a854-bf682a93da28",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Help on built-in function append:\n",
      "\n",
      "append(object, /) method of builtins.list instance\n",
      "    Append object to the end of the list.\n",
      "\n"
     ]
    }
   ],
   "source": [
    "help(list1.append)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2e33e45d-113e-4c4e-a2c4-b98a3d8cf373",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "89eb42b3-d0d9-421c-ad52-5b46cbe2feb3",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 333,
   "id": "a6655867-ec32-464a-bd25-2881a8f368e2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 3, 4.9, 'name', 7, 'how', 'are', 8, 'your']"
      ]
     },
     "execution_count": 333,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 335,
   "id": "c0f733e9-a073-45ee-86a0-d474fc1e981a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "None\n"
     ]
    }
   ],
   "source": [
    "print(list1.reverse())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 336,
   "id": "5a329930-6c56-4b42-8880-ad354255bf02",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 3, 4.9, 'name', 7, 'how', 'are', 8, 'your']"
      ]
     },
     "execution_count": 336,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 337,
   "id": "bcecf8b6-6487-45ac-9321-0f8af1ad3684",
   "metadata": {},
   "outputs": [],
   "source": [
    "d2={'hh':v,'gf':g,'d':dic}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 339,
   "id": "a711debf-98a6-4b1a-8d87-150c98381288",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'h'"
      ]
     },
     "execution_count": 339,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d2[\"hh\"][3]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 341,
   "id": "20ebab96-90d7-489a-bfaf-38abf0e6444c",
   "metadata": {},
   "outputs": [],
   "source": [
    "cv=d2['d']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 342,
   "id": "803cf518-f989-4bae-b982-6da5484282ca",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{23: 'twothree', 'h': 42, 'v': 'fd', '16': 'rhkh', 'srjgsf': 'srdbjf'}"
      ]
     },
     "execution_count": 342,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 343,
   "id": "beb6990e-0130-4b71-9de8-29a88306a4d3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "23 twothree\n",
      "h 42\n",
      "v fd\n",
      "16 rhkh\n",
      "srjgsf srdbjf\n"
     ]
    }
   ],
   "source": [
    "for x in cv:\n",
    "    print(x,cv[x])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 344,
   "id": "8e1a25a2-aa2c-40ed-a1c0-4703bd327cdc",
   "metadata": {},
   "outputs": [],
   "source": [
    "l3=[list1,tuple1,dic,23,\"game\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 346,
   "id": "a410832a-62e7-4dd3-afd0-dccf5a5ab37e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dict"
      ]
     },
     "execution_count": 346,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(l3[2])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 347,
   "id": "21c4f6c5-83a5-427b-a566-1514b1baa4c2",
   "metadata": {},
   "outputs": [],
   "source": [
    "l3=[x**2 for x in range(10)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 348,
   "id": "b2d1aedd-5ee9-40fa-9111-ba40f6fbd7d8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]"
      ]
     },
     "execution_count": 348,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 349,
   "id": "89958412-9212-43e0-a291-363eff61104b",
   "metadata": {},
   "outputs": [],
   "source": [
    "s3={x**2 for x in range(2,30,3)}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 350,
   "id": "300fe125-05db-4c49-9f9d-80cea16673d6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{4, 25, 64, 121, 196, 289, 400, 529, 676, 841}"
      ]
     },
     "execution_count": 350,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 351,
   "id": "a2433a1a-e18b-4dc3-813a-11e4b64aba2c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 351,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "23 in dic"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 352,
   "id": "90376841-97ae-4d71-b7da-3b57fd5260e3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 352,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "43 in dic"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 355,
   "id": "bd70676f-1921-4463-9bad-e48e98e53444",
   "metadata": {},
   "outputs": [],
   "source": [
    "\"\"\"lets say u are a teacher and you have diff stude records\n",
    "containing id of a stud and the mrks list in each sub\n",
    "where diff student taken differ number of sub.all these records are in \n",
    "hard copy.you want to enter all the data in comp and want to compute\n",
    "the avg marks of each student and display\"\"\"\n",
    "\n",
    "def getDataFromUser():\n",
    "    d={}\n",
    "    while True:\n",
    "        studId=input(\"Enter student ID: \")\n",
    "        mrksList=input(\"enter marks by comma seperated values : \")\n",
    "        moreStu=input(\"Enter no to quit inserted: \")\n",
    "        if studId in d:\n",
    "            print(studId,\"is already inserted\")\n",
    "        else:\n",
    "            d[studId]=mrksList.split(\",\")\n",
    "        if moreStu.lower()==\"no\":\n",
    "            return d\n",
    "            "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 356,
   "id": "f94f457b-4705-44ad-b1ce-4cd2414b787d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter student ID:  12\n",
      "enter marks by comma seperated values :  24,77,88\n",
      "Enter no to quit inserted:  no\n"
     ]
    }
   ],
   "source": [
    "studData=getDataFromUser()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 357,
   "id": "0042965f-51ee-4740-b601-f19d459dd64e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter student ID:  11\n",
      "enter marks by comma seperated values :  32,54,2,87,54\n",
      "Enter no to quit inserted:  gfhsf\n",
      "Enter student ID:  5\n",
      "enter marks by comma seperated values :  77,56,8,4,90,45\n",
      "Enter no to quit inserted:  gdhf\n",
      "Enter student ID:  9\n",
      "enter marks by comma seperated values :  90,4,6,76\n",
      "Enter no to quit inserted:  no\n"
     ]
    }
   ],
   "source": [
    "studData=getDataFromUser()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 358,
   "id": "1f247699-e0f6-4360-9fce-f8a215317306",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'11': ['32', '54', '2', '87', '54'],\n",
       " '5': ['77', '56', '8', '4', '90', '45'],\n",
       " '9': ['90', '4', '6', '76']}"
      ]
     },
     "execution_count": 358,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "studData"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 368,
   "id": "6f647406-2e35-415d-a307-8a9db7df087d",
   "metadata": {},
   "outputs": [],
   "source": [
    "def getAvgMrks(d):\n",
    "    avgMrks={}\n",
    "    for x in d:\n",
    "        L=d[x]\n",
    "        s=0\n",
    "        for marks in L:\n",
    "            s+= int(marks)\n",
    "        avgMrks[x]=s/len(L)\n",
    "    return avgMrks\n",
    "        \n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 369,
   "id": "89e1dfda-04ba-45a1-8bff-c07aef8dce06",
   "metadata": {},
   "outputs": [],
   "source": [
    "avgMrks=getAvgMrks(studData)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 370,
   "id": "72a65102-48a6-495b-8346-24e7443023e7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'11': 45.8, '5': 46.666666666666664, '9': 44.0}"
      ]
     },
     "execution_count": 370,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "avgMrks"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 372,
   "id": "2b75be52-d919-4a68-848e-793632d21a36",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "student :  11 got avg marks as :  45.8\n",
      "student :  5 got avg marks as :  46.666666666666664\n",
      "student :  9 got avg marks as :  44.0\n"
     ]
    }
   ],
   "source": [
    "for x in avgMrks:\n",
    "    print(\"student : \",x,\"got avg marks as : \",avgMrks[x])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6eb84737-6bb3-440f-9437-b850e88efc8d",
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
