{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e4fb3a7c-2e84-496a-9da6-4014d51eddbd",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Define a classe Cliente\n",
    "class Cliente:\n",
    "\n",
    "    #Metodo construtor que inicializa os atribuitodos da classe\n",
    "    def.__init__(self, nome: str, cpf: str):\n",
    "\n",
    "        #Atributos para armazenar o nome do Cliente\n",
    "        self.nome = nome\n",
    "\n",
    "        #Atribuito para armacenar o cpf do Cliente\n",
    "        self.cpf = cpf\n",
    "\n",
    "        #Lista vazia par aarmazenas as contas associadas ao Cliente\n",
    "        self.contas = []\n",
    "\n",
    "    #Metodo para adicionar uma conta a lista de contas ao Cliente\n",
    "    def adicionar_conta(self, conta):\n",
    "\n",
    "        #Inserir o objeto conta na lista de contas\n",
    "        self.contas.append(conta)\n",
    "\n",
    "    #Metodo especial que define a representação em string do objeto\n",
    "    def __str__(self):\n",
    "\n",
    "        #Retornar uma string formatada com o nome e CPF do Cliente\n",
    "        return f\"Cliente: {self.nome} CPF: {self.cpf}\""
   ]
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
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
