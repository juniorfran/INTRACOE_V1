import requests
import json

def send_whatsapp_message_with_attachment(to_phone_number, template_name, variables, pdf_url, language_code="es"):
    # URL del endpoint para enviar mensajes
    url = "https://graph.facebook.com/v20.0/461495207047495/messages"
    
    # Token de acceso
    access_token = "EAAHmK0fOvhoBOZCEa8zjvUgI7iKSzRwib3ZCLpqmZB8uG7lcGV3PUJ9uIihOUdcZB9zIZAhqDqFRuOMRpFXo5uQRv8ZCthmRugOjHnfD2m3EvIK7umzdJgXuS5h7sTDxNk4c7NzUrsaD4xMZBTcKvO2rUqiduyDzlFDCKdHZCFQejSmvze59G47KiyC4rYCMSq0hQUZBLmeeUZAMIcWvnMy6tPpzY9pRPZBKD0uMKLWXaZCXcXQZD"

    # Encabezados de la solicitud
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    # Cuerpo de la solicitud con variables y el archivo adjunto
    payload = {
        "messaging_product": "whatsapp",
        "to": to_phone_number,
        "type": "template",
        "template": {
            "name": template_name,
            "language": {
                "code": language_code
            },
            "components": [
                {
                    "type": "body",
                    "parameters": [
                        {"type": "text", "text": variables[0]},
                        {"type": "text", "text": variables[1]},
                        {"type": "text", "text": variables[2]},
                    ]
                },
                {
                    "type": "button",
                    "sub_type": "url",
                    "index": "0",
                    "parameters": [
                        {"type": "text", "text": pdf_url}  # Enlace al PDF
                    ]
                }
            ]
        }
    }

    # Realizar la solicitud POST
    response = requests.post(url, headers=headers, json=payload)

    # Verificar la respuesta
    if response.status_code == 200:
        print("Mensaje enviado correctamente.")
    else:
        print(f"Error al enviar el mensaje: {response.status_code}")
        print("Detalles:", response.json())

# Ejemplo de uso
variables = ["Nombre del Empleado", "14.25", "450.00"]
pdf_url = "file://200.31.164.66/boletas/Boleta_Pago_Francisco%20antonio_flores%20plantilla.pdf"  # URL pública del PDF
send_whatsapp_message_with_attachment("50377462310", "boleta_pago2", variables, pdf_url)
