from os import environ


class Config:

    # ============================== Global Configuration ==============================

    FILE_PATH = environ.get("ARTIFACT_FILE_PATH", "/tmp/debug")


    # ============================= NextCloud Configuration =============================

    NEXTCLOUD_PATH = environ.get("ARTIFACT_NEXTCLOUD_PATH", "/DEvops")

    NEXTCLOUD_URL = environ.get("NEXTCLOUD_URL", "http://share.br-group.ir")
   
    NEXTCLOUD_USER = environ.get("PUSH_NEXTCLOUD_USER", "admin")

    NEXTCLOUD_PASS = environ.get("PUSH_NEXTCLOUD_PASS", "Cyber@123QAZ")

