import os
from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.authentication_context import AuthenticationContext
from config import *

VALID_EXTENSIONS = [".pdf", ".docx", ".txt"]

def sync_files():
    ctx_auth = AuthenticationContext(SHAREPOINT_URL)
    if ctx_auth.acquire_token_for_user(USERNAME, PASSWORD):
        ctx = ClientContext(SHAREPOINT_URL, ctx_auth)
        folder = ctx.web.get_folder_by_server_relative_url(SHAREPOINT_FOLDER)
        files = folder.files
        ctx.load(files)
        ctx.execute_query()

        for file in files:
            name = file.properties["Name"]
            ext = os.path.splitext(name)[1].lower()
            if ext in VALID_EXTENSIONS:
                local_file = os.path.join(LOCAL_PATH, name)
                with open(local_file, "wb") as output:
                    file.download(output)
                ctx.execute_query()
                print(f"Descargado: {name}")
    else:
        print("⚠️ Autenticación fallida.")
