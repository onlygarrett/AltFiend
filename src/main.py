import subprocess
import tomllib
from pathlib import Path

from time import sleep
import time
from pip._vendor.urllib3.util import timeout
import pywinauto
from pywinauto.application import Application
from pywinauto.timings import Timings
from pywinauto.keyboard import send_keys

from error_handling import base_logger

conf_logger = base_logger("parsingConfiguration")

# Timings.slow()


if __name__ == "__main__":
    # parse configuration
    try:
        with open("src/data.toml", "rb") as f:
            config = tomllib.load(f)

    except tomllib.TOMLDecodeError:
        conf_logger.error(
            "An Error occurred when decoding the Config file in the project dir"
        )
        exit(1)

    if (
        config["SYSTEM"]["riot_dir"]
        and Path(config["SYSTEM"]["riot_dir"]).absolute().exists()
    ):
        conf_logger.info("Found RIOT directory in config file")

        riot_client_dir = Path(config["SYSTEM"]["riot_dir"]).absolute()
        cmd = [riot_client_dir]
    else:
        conf_logger.error(
            "RIOT directory not found in config file or it does not exist"
        )
        exit(1)

    ## maybe
    app = Application(backend="win32")
    app.start(cmd_line=f"{riot_client_dir}", wait_for_idle=True)
    app.wait_for_process_exit()

    riot_app = Application().connect(title="Riot Client", timeout=20)
    time.sleep(5)

    running = False
    idle = False

    app_dlg = riot_app["Riot Client"].wrapper_object()
    while not running:
        if riot_app.is_process_running():
            app_dlg.wait_for_idle()
            running = True

            app_dlg.set_focus()

            app_dlg.type_keys("RarkGrames69")
            app_dlg.type_keys("{TAB}")
            app_dlg.type_keys("IanIsLiterallyTheBestDogEver42069")
            app_dlg.type_keys("{ENTER}")
