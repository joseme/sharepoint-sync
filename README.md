# 📁 SharePoint Sync with Basic Credentials

Este proyecto permite sincronizar archivos desde una carpeta de SharePoint Online a una carpeta local en Ubuntu, utilizando autenticación directa con usuario y contraseña en Python — sin necesidad de Azure AD ni OAuth.

---

## 🚀 Características

- Sincronización unidireccional desde SharePoint ➡️ carpeta local
- Descarga de archivos con extensiones `.pdf`, `.docx`, y `.txt`
- Autenticación simple mediante usuario y contraseña
- Integración con `cron` para ejecución automática diaria
- Modular y listo para expandirse

---

## 🗂️ Estructura del Proyecto

```plaintext
sharepoint_sync_basic/
├── main.py              # Script principal
├── sync_logic.py        # Lógica de descarga
├── config.py            # Carga de configuración desde .env
├── requirements.txt     # Dependencias del proyecto
├── .env                 # Credenciales y rutas (privado)
└── README.md            # Documentación del proyecto
