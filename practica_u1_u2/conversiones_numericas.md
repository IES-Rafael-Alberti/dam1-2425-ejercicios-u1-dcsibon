# Conversiones numéricas.

1. Crear una función que convierta un número de base binaria a base decimal. Para ello debemos poedir un número, comprobar que es válido para la base binaria y después llamaríamos a la función convertir_binario_decimal(numero) o damos el mensaje de error correspondiente.

2. Crear una función que convierta un número de base decimal a binaria.

3. Realizar un bucle en el main para realizar conversiones de números de binario a decimal o al revés hasta que pulsen ENTER con la cadena vacía... entonces preguntaremos si desean salir de la app. Podemos hacer una función preguntar_salir() y convertir_numero(). La función convertir_numero() retornará si la conversión se ha realizado con éxito (True) o se produjo algún error. También retornará None si se introdujo la cadena vacía para que en el main podamos llamar a preguntar_salir().
También hacer una función limpiar_pantalla() y realizar_pausa() que hará una pausa de 2 segundos por defecto o del tiempo que le pasemos como argumento.

4. Vamos a realizar las conversiones de un número de cualquier base (binaria, octal, decimal o hexadecimal) a otra base distinta. 

    * Crear constantes con los símbolos que pueden existir y utilizar su posición para proporcionar su valor numérico.

    * Crear una constante para cada base con su valor, por ejemplo BASE_BINARIA = 2, ... También crearla constante BASES_VALIDAS como una tupla de las bases convertidas a str para poder validar una base válida.

    * Vamos a crear constantes para los mensajes:

        - MENSAJE_ERROR_BASE_GENERAL = "\n**ERROR** no ha introducido una base correcta!"
        - MENSAJE_ERROR_BASE_IGUAL = "\n**ERROR** La base de destino no puede ser igual a la base de origen ({base})."
        - MENSAJE_ERROR_NUMERO = "\n**ERROR** el número '{numero}' no es válido para la base {base}!"
        - MENSAJE_ERROR_CONVERSION = "\n**ERROR** en la conversión: {error}"



