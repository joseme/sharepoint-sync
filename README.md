# sharepoint-sync
# 🔄 SharePoint Sync with OAuth

Sincroniza archivos desde una carpeta de SharePoint Online a una ubicación local en Ubuntu, usando autenticación moderna OAuth y Python.

---

## 🚀 Características

- Autenticación segura mediante OAuth 2.0 (Azure AD)
- Descarga unidireccional de archivos (`.pdf`, `.docx`, `.txt`)
- Compatible con tareas programadas usando `cron`
- Estructura modular para escalabilidad
- Registro de sincronización en consola

---

## 🗂️ Estructura del Proyecto

```plaintext
sharepoint_sync/
│
├── main.py                # Script principal
├── auth_config.py         # Autenticación OAuth
├── sharepoint_sync.py     # Lógica de sincronización
├── requirements.txt       # Dependencias
├── .env                   # Configuración privada
└── README.md              # Documentación
