from logging import basicConfig, getLogger, INFO
from os import getenv
from subprocess import PIPE, run

from cli import check_for_updates, check_inhibitors


"""Setup logging"""
basicConfig(
    format="[%(asctime)s] %(name)s:%(levelname)s | %(message)s",
    level=getenv("UBLUE_LOG", default=INFO),
)
log = getLogger(__name__)


def connectivity_check():
    """Check connectivity with GitHub"""
    con_check = "wget -q --spider https://github.com"
    proc = run(
        con_check,
        stdout=PIPE,
        shell=True
    )
    if proc.returncode == 0:
        log.info(f"Connectivity check passed.")
        return True
    else:
        log.info(f"Connectivity check failed")
        return False


def steam_update_check():
    """Check system state"""
    check_inhibitors(True)
    """Check connection"""
    connected = connectivity_check()
    if connected:
        update_available = check_for_updates(False)
        if update_available:
            """Inform Steam an update is available"""
            exit(0)
    """Inform Steam no updates are available"""
    exit(7)
