import base64
import urllib.parse
import base64
import urllib.parse
import migration_pb2  # Importa las clases generadas

# Tu string de exportación del código QR
qr_code_data_url = "otpauth-migration://offline?data=YOURTEXT"

# Extrae el parámetro de datos del URL
data_url_parts = urllib.parse.urlsplit(qr_code_data_url)
query_params = urllib.parse.parse_qs(data_url_parts.query)
data_param = query_params.get('data', [''])[0]

try:
    # Decodifica la cadena base64 (datos binarios)
    decoded_data = base64.b64decode(data_param)

    # Intenta parsear los datos usando las clases generadas
    migration_payload = migration_pb2.MigrationPayload()
    migration_payload.ParseFromString(decoded_data)

    # Accede a los campos del mensaje protobuf
    for otp_parameter in migration_payload.otp_parameters:
        base32_encoded_data = base64.b32encode(otp_parameter.secret).decode('utf-8')

        print("Name: {}".format(otp_parameter.name))
        # print("Secret Key (b32): {}".format(otp_parameter.secret))
        print("Secret Key (final): {}".format(base32_encoded_data))
        print("Emisor: {}".format(otp_parameter.issuer))
        if otp_parameter.algorithm == 1:
            print("Algoritmo: {}".format("SHA1"))
        else:
            print("Algoritmo: {}".format("Invalid"))
        print("Dígitos: {}".format(otp_parameter.digits))
        if otp_parameter.type == 1:
            print("Tipo: {}".format("HOTP"))
        elif otp_parameter.type == 2:
            print("Tipo: {}".format("TOTP"))
        else:
            print("Tipo: {}".format("Invalid"))
        print("Counter: {}".format(otp_parameter.counter))
        print("-------------------")

    print("Versión: {}".format(migration_payload.version))
    print("Tamaño del lote: {}".format(migration_payload.batch_size))
    print("Índice del lote: {}".format(migration_payload.batch_index))
    print("ID del lote: {}".format(migration_payload.batch_id))

except Exception as e:
    print("Error:", str(e))
