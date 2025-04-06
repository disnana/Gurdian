import time
import sys
from module import gurdian


def detected():
    print("デバッグまたは仮想化を検知しました")

def startup_check():
    if (not module.check_connection() or
        module.check_blacklisted_names() or
        not module.check_usb() or
        module.triage_check() or
        module.vm_artifacts() or
        module.vmware_graphics() or
        module.virtualbox_graphics() or
        module.qemu_check() or
        module.parallels_check() or
        module.is_screen_small() or
        module.check_for_kvm() or
        module.parent_anti_debug() or
        module.detect_vm() or
        module.detect_sandbox()):
        module.force_kill()
        sys.exit(1)

module = gurdian.Security(
    anti_debugger=True,
    kill_on_debug=True,
    detect_vm=True,
    detect_sandbox=True,
    detect_debugger_attach=True,
    check_titles=True,
    is_debugger_present=True,
    check_remote_debugger=True,
    kill_bad_processes=True,
    on_detection=detected
)

# 仮想化などをチェック
startup_check()
# デバッガの監視をループ
detect = module.check_security()

time.sleep(300)
