# Tercera-Pre-Entrega-Landart
Las funcionalidades de la web creada son las siguientes:
Tener una base de datos que registre exitosamente los datos pedidos mediante formularios en los tres modelos creados.
Creé un buscador que permite al usuario buscar Cursos, y al encontrar una coincidencia, devuelve el nombre del curso junto con la modalidad del mismo. 

Para poder ingresar a la web, debemos ejecutar el servidor utilizando python manage.py, y una vez que abrimos el link que nos permite ingresar a la web, debemos agregarle la url /AppCoder, de manera que quede http://127.0.0.1:8000/AppCoder/ . Esto nos permite visualizar el inicio de la página web, donde pedimos ya visualizar un mensaje de bienvenida. Si presionamos el botón "Empecemos", nos enviará para abajo, al buscador. En la parte superior derecha, podemos visualizar los botones de "inicio", "cursos", "servicios", y "carreras". Al ingresar a cada uno de ellos, nos enviará a las urls correspondientes, que nos mostraran un texto diferente según cada model, acompañado de un formulario que nos pedirá ciertos datos. Una vez que introduzca los datos, se guardarán en la base de datos. Para visualizar estos datos, puede dirigirse a http://127.0.0.1:8000/admin , e ingresar con el superuser ya creado: username: german   password: millonario97 .

Saludos, 

Germán Landart.

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣴⣦⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣴⣶⣿⣿⣿⣿⣿⣿⣿⣷⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠿⣿⣿⡂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⠟⠉⠀⠐⠀⠀⠀⠀⠈⢿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⢿⣿⣿⡆⠀⢀⣠⣄⣤⣀⡄⣀⣀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣎⠀⠀⣾⡷⣯⣿⡟⠀⢿⣯⣍⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡏⡏⡛⠇⠀⠀⠀⠈⠉⢈⡠⢀⣈⠍⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣥⣷⣋⢸⣆⠀⠀⢀⠠⢟⣻⣿⣟⡃⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢣⣷⡎⣿⣿⣾⡁⣴⣿⣿⢿⠿⣷⡀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠈⠁⢹⣿⣿⣿⣿⣿⣾⣶⡆⣼⡵⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⢠⢸⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⠀⠀⢣⣾⣿⢿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣮⢻⣷⣄⠀⢉⡞⣯⢷⡿⣿⣭⡀⠀⢤⠄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡴⣿⣿⣿⣷⣝⢿⣆⠰⢨⢅⠂⡹⣆⡍⡀⢀⣎⣮⢱⣉⢆⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣐⣾⣟⣾⣿⣿⣿⣿⣿⣶⣿⣿⣧⣎⣧⠀⢡⠆⢀⣰⡽⣯⣿⣟⣮⣶⣩⣆⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣔⣺⡽⣳⣯⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣟⣿⣽⣟⣿⣻⣿⣷⣾⠰⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣜⣳⣞⣷⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⢾⡽⣟⣿⣯⣿⣽⣿⣯⣿⣞⣷⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⠾⣼⣳⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⣟⣿⣯⣟⣿⣷⣿⢾⣷⣿⣟⣾⣟⣾⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⡿⣾⣻⣷⣿⣿⣿⣾⣿⣷⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣀⠒⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣽⣿⢿⣿⣷⣻⣿⣾⣷⡬⡪⡴⢎⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠬⠁⢃⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠹⠿⢛⣩⣽⣾⣿⣻⣞⣷⣻⣷⣿⣄⠻⢅⣼⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠸⣦⡀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣾⣿⣿⣿⣽⣿⣽⣿⣳⢿⣿⣾⣿⣿⣺⢿⣿⣿⣇⢀⠀⠀⠀⠀⠀⠀
⠀⠀⡸⣦⣀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣷⣯⢿⣟⣾⣿⣿⣿⣻⣿⣿⣣⣷⡄⠀⠀⠀⠀⠀
⠀⣰⣻⡽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡿⣟⣿⣞⣯⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣁⠤⠀⠂⠀⠀
⠠⢿⣼⣿⣿⣿⣿⣿⣿⣿⠟⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢠⣌⠹⡟⢛⠛⡇⠺⢉⠉⣎⢋⢈⡻⡉⠏⢹⣿⣿⣷⣿⣍⡶⠆⠈⢀⠆
⢻⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠨⣍⠰⡀⢿⠇⠁⢀⠻⡆⠿⢸⠸⢇⠤⠆⣿⣿⣿⣿⣿⣽⡴⠆⠐⠁⠤
⠸⡭⢟⣿⣿⣿⣿⣿⣇⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⣶⣷⣶⠶⠾⠚⠓⠚⢒⣚⣓⣾⣶⣿⣿⣿⣿⣿⣿⣿⣷⣗⡈⢀⠀
⠀⠑⣫⣾⣿⣿⣿⣿⣿⣆⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⣿⣿⣿⡿⣿⣿⣿⣿⣿⠻⠿⠿⠿⠿⠿⠿⠟⠋⠀⠀
⠀⠀⠐⠝⣾⣿⣿⣿⣿⣿⣆⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⢻⣞⣿⣿⢿⣿⣿⣧⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠹⣟⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⢿⣿⣻⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⡟⠉⠀⡀⠀⠱⣍⠛⢛⣛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣾⣹⢿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠙⠻⣿⣾⠏⠀⣤⣄⡑⣧⡄⠈⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣿⢷⣿⣽⣿⡙⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠱⡀⠰⣦⣙⡻⣿⣿⣿⣦⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣻⢿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⢮⣝⠻⠭⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⡿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠊⠙⠛⠚⠋⠛⠛⠛⠛⠛⠛⠛⠛⠛⠙⠛⠛⠙⠛⠛⠛⠃⠉⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
