# OTP_Decoder
Windows python + proto
Si estás en Windows y no tienes el compilador de Protocol Buffers (protoc) instalado, aquí hay pasos detallados para instalarlo y compilar tu archivo .proto:

    Descarga el compilador de Protocol Buffers para Windows:
        Visita la página de liberación de Protocol Buffers en GitHub. https://github.com/protocolbuffers/protobuf/releases
        Encuentra la última versión estable para Windows y descarga el archivo zip correspondiente, como protoc-3.x.x-win64.zip.

    Descomprime el archivo zip:
        Descomprime el archivo zip descargado en una ubicación de tu elección. Por ejemplo, puedes crear una carpeta llamada protobuf en tu directorio C:\ y descomprimir los archivos allí.

    Agrega la ruta del compilador a la variable de entorno PATH:
        Haz clic con el botón derecho en "Este PC" o "Mi PC" y selecciona "Propiedades".
        Haz clic en "Configuración avanzada del sistema" en el panel izquierdo.
        Haz clic en "Variables de entorno".
        En la sección "Variables del sistema", encuentra la variable PATH y haz clic en "Editar".
        Agrega la ruta al directorio que contiene protoc.exe al final de la lista, separada por un punto y coma (;). Por ejemplo, si descomprimiste protoc en C:\protobuf, agrega C:\protobuf a la ruta.
        Haz clic en "Aceptar" para cerrar las ventanas y guardar los cambios.

    Verifica la instalación:
        Abre una nueva ventana de símbolo del sistema (cmd) y escribe protoc --version. Deberías ver la versión del compilador de Protocol Buffers que instalaste.

Una vez que hayas instalado protoc, puedes usar el comando protoc --python_out=. migration.proto en el directorio que contiene tu archivo migration.proto para compilarlo y generar los archivos Python correspondientes (migration_pb2.py y migration_pb2_grpc.py). Luego, puedes importar y utilizar las clases generadas en tu script Python.

Hacemos cd a nuestra carpeta del proyecto.
Despues lanzamos el siguiente comando:
protoc --python_out=. --proto_path="Project folder path" migration.prot

Sustituimos "qr_code_data_url" por nuestra variable de exportacion, es recomendable no exportar mas de 3 QR de Google Authenticator a la vez.
Recibimos los datos en consola
