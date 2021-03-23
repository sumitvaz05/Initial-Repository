{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "myfile=open('a.txt')\n",
    "contents=myfile.readlines()\n",
    "myfile.seek(0)\n",
    "myfile.close()\n",
    "\n",
    "output=open('a2.txt', 'w+')\n",
    "\n",
    "for line in contents:\n",
    "    m=line.lstrip()\n",
    "    output.write(m)\n",
    "output.close()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [],
   "source": [
    "myfile=open('a.txt')\n",
    "contents=myfile.readlines()\n",
    "myfile.seek(0)\n",
    "myfile.close()\n",
    "del contents[0]\n",
    "output=open('a2.txt', 'w+')\n",
    "\n",
    "import re\n",
    "for line in contents:\n",
    "    m=re.sub(\"\\s+\", \",\", line.strip())\n",
    "    output.write(m+'\\n')\n",
    "output.close()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "test=pd.read_csv(\"a2.txt\", header=None)\n",
    "test.columns= [\"Proto\", \"Local Address\", \"Foreign Address\", \"State\"]\n",
    "test.to_csv(\"a_excel.csv\", index=None)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
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
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
