{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "0e4bfd1b-dd49-419f-90d2-35100d60686a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[2 5 7]\n",
      " [1 2 3]\n",
      " [7 4 2]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "A=np.array([\n",
    "    [2,5,7],\n",
    "    [1,2,3],\n",
    "    [7,4,2]\n",
    "])\n",
    "print(A)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "9a4dc025-e988-46df-a972-f5a76a36004a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[10  5 12]\n",
      " [ 1  6 11]\n",
      " [ 8  4  8]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "A=np.array([\n",
    "    [2,5,7],\n",
    "    [1,2,3],\n",
    "    [7,4,2]\n",
    "])\n",
    "B=np.array([\n",
    "    [8,0,5],\n",
    "    [0,4,8],\n",
    "    [1,0,6]\n",
    "])\n",
    "print(          A+B       )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "18c5ce79-39c9-4c00-b1ca-1187c22d4356",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[10  5 12]\n",
      " [ 1  6 11]\n",
      " [ 8  4  8]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "A=np.array([\n",
    "    [2,5,7],\n",
    "    [1,2,3],\n",
    "    [7,4,2]\n",
    "])\n",
    "B=np.array([\n",
    "    [8,0,5],\n",
    "    [0,4,8],\n",
    "    [1,0,6]\n",
    "])\n",
    "print(          A+B       )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "472ebf99-90e5-4cc9-9ad6-ef1f8d404e6a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[23 20 92]\n",
      " [11  8 39]\n",
      " [58 16 79]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "A=np.array([\n",
    "    [2,5,7],\n",
    "    [1,2,3],\n",
    "    [7,4,2]\n",
    "])\n",
    "B=np.array([\n",
    "    [8,0,5],\n",
    "    [0,4,8],\n",
    "    [1,0,6]\n",
    "])\n",
    "print(          A.dot(B)       )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "2cf30fa3-deb1-4968-861d-40cc70baf49f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[23 20 92]\n",
      " [11  8 39]\n",
      " [58 16 79]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "A=np.array([\n",
    "    [2,5,7],\n",
    "    [1,2,3],\n",
    "    [7,4,2]\n",
    "])\n",
    "B=np.array([\n",
    "    [8,0,5],\n",
    "    [0,4,8],\n",
    "    [1,0,6]\n",
    "])\n",
    "print(          np.dot(A,B)       )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "a7374e8a-0627-481f-9950-eb5a17cd71d0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[23 20 92]\n",
      " [11  8 39]\n",
      " [58 16 79]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "A=np.array([\n",
    "    [2,5,7],\n",
    "    [1,2,3],\n",
    "    [7,4,2]\n",
    "])\n",
    "B=np.array([\n",
    "    [8,0,5],\n",
    "    [0,4,8],\n",
    "    [1,0,6]\n",
    "])\n",
    "print(          np.matmul(A,B)       )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "6321704b-3570-411a-b505-10b7b4fcd6c2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[-0.88888889  2.          0.11111111]\n",
      " [ 2.11111111 -5.          0.11111111]\n",
      " [-1.11111111  3.         -0.11111111]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "A=np.array([\n",
    "    [2,5,7],\n",
    "    [1,2,3],\n",
    "    [7,4,2]\n",
    "])\n",
    "print(      np.linalg.inv(A)   )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "36222afb-e393-43e1-a09c-21f811d65dcc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[16  0 35]\n",
      " [ 0  8 24]\n",
      " [ 7  0 12]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "A=np.array([\n",
    "    [2,5,7],\n",
    "    [1,2,3],\n",
    "    [7,4,2]\n",
    "])\n",
    "B=np.array([\n",
    "    [8,0,5],\n",
    "    [0,4,8],\n",
    "    [1,0,6]\n",
    "])\n",
    "print(A*B)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "468c3521-c276-4a59-b1c2-0cd9e5a9acab",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[10.98868103 -4.81871355 -0.16996748]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "A=np.array([\n",
    "    [2,5,7],\n",
    "    [1,2,3],\n",
    "    [7,4,2]\n",
    "])\n",
    "print(         np.linalg.eigvals(A)         )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2efb15b3-a9a4-4b9b-866e-01bc663feac7",
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
