from datetime import datetime


def my_cp(request):
    cp_ctx = {
        "now": datetime.now(),
    }
    return cp_ctx