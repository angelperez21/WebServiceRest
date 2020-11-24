# Web service REST sencillo con Flask

## Bienvenido

### Instalación de Python Package Installer

Para que puedas activar tu entorno virtual y que de esta manera no tengas problemas con dependencias de otros proyecto que pudieras tener, es necesario tener instalado virtualenv el cual se instala con el Python Package Installer o mejor conocido como pip, este lo puedes intalar de las siguientes maneras:

#### Para linux

Derivados de Debian o con gestor de paquetes apt:

- sudo apt install python3-pip

Derivados de Centos o con gestor de paquetes yum:

- sudo yum install epel-release
- sudo yum install python-pip

Derivados de Arch linux

- sudo pacman -Sy python-pip

#### Para windows

Es recomendable dirigirse al path donde se encuentra instalado python y continuar con los siguientes comandos

- curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
- python get-pip.py

Aunque en algunas ocasiones el instalador de python para windows viene por defecto con pip, si es el caso se puede omitir esta parte.

### Instalación de virtualenv

Una vez instalado el gestor de paquetes pip procederemos a instalar virtualenv el cual nos permitirá tener separadas nuestras dependencias entre aplicaciones python, se puede instalar con el mismo gestor pip o con el de la distribución que se esté utilizando

#### Con el gestor de paquetes de python

Para windows y derivados de Centos es con el mismo pip

- pip install virtualenv

#### Para linux

##### Con el gestor de paquetes apt (derivados de Debian)

- sudo apt-get install python-virtualenv

##### Con gestor de paquetes pacman (Derivados de Arch Linux)

- sudo pacman -S python2-virtualenv python-virtualenv

### Activación del entorno virtual

Una vez instalado virtualenv se debe de crear el entorno virtual de python de la siguiente manera

- virtualenv nameproject --python=python3

donde nameproject es el nombre de tu proyecto. Activamos el entorno de virtual de las siguiente manera

- source nameproject/bin/activate

y finalmente instalamos el framework Flask y sus dependencias las cuales se encuentran el archivo requirements.txt para poder hacer esto lo realizamos de la siguiente manera

- pip install -r requirements.txt

### Levantamiento del servidor

Para este apartado se puede hacer de dos formas.

Para la primera y se recomienda descomentar el if que viene al final:

- python app.py

Para la segunda es de la siguiente forma:

exportamos las variables de entorno

- export FLASK_APP=app.py FLASK_ENV=development FLASK_RUN_PORT=8000

y a continuación activamos el servidor

- flask run

cabe mencionar que para ambas formas es necesario indicar la ruta en donde se encuentre el fichero app.py o dirigese al directorio donde se encuentre para poder ejecutarla
