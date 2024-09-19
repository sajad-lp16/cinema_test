def normalize_mobile(mobile: str) -> str:
    if not mobile.startswith("+98"):
        return mobile
    return "0" + mobile[3:]
