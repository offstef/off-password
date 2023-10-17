# off-password

Simple manager de contraseñas en español

#### Instalación:

Clona el repositorio:

```sh
git clone https://github.com/offstef/off-password
```

Instala todas las dependencias con pip:

```python
pip install -r requirements.txt
```

#### Uso:

corre el archivo:

```python
python offpsswd.py
```

#### Descripción:

- Un simple gestor de contraseñas que ejecuta todas las funciones CRUD.
- Las contraseñas estan encriptadas en un fichero Elara DB.

#### Disclaimer:

- Esta versión es open source y debe usarse con precaución.

#### Opcional:

- Esto sirve para crear un .bat que ejecute el script solo.
- Se crea un archivo de texto, se copia este código y se siguen las instrucciones de las comillas.

```bat
@echo off
"Path where your Python exe is stored\python.exe" "Path where your Python script is stored\script_name.py"
pause
```

##### Muy opcional

- Al crear el .bat puedes moverlo a otra carpeta para crear más gestores de contraseñas
- Es muy útil si quieres tener uno para uso personal y otro para empresarial.
