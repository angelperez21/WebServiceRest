# WebServiceRest
# Bienvenido

Para poder utilzar y desarrollar con el framework Django es necesario contar con python instalado, así como del gestor de paquetes de python, pip.

En linux se puede instalar desde linea de comandos de las siguietes maneras

Derivados de Debian o con gestor de paquetes apt:
sudo apt install python3-pip

Derivados de Centos o con gestor de paquetes yum:
sudo yum install epel-release
sudo yum install python-pip

Derivados de Arch linux 
sudo pacman -Sy python-pip

Una vez instalado el gestor de paquetes pip procederemos a instalar virtualenv el cual nos premitira tener separadas nuestras dependencias entre aplicaciones python, se puede instalar con el gestor pip o con el de la distribución que se este utilizando

Con el gestor de paquetes de python
pip install virtualenv

Con el gestor de paquetes apt (derivados de Debian)
sudo apt-get install python-virtualenv 

Con gestor de paquetes yum (Derivados de Centos) es con el mismo pip 

Con gestor de paquetes pacman (Derivados de Arch Linux) 
sudo pacman -S python2-virtualenv python-virtualenv

Una vez instalado virtualenv se debe de crear el entorno virtual de python de la siguiente manera
virtualenv nameproject --python=python3

y activamos el entorno de virtual de las siguente manera 
source nameproject/bin/activate

y finalmete instalamos el framework Django y sus dependencias las cuales se encuentran el archivo requirements.txt para poder hacer esto lo realizamos de la siguiente manera

pip install -r requirements.txt

