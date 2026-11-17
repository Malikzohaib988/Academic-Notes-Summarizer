def clean_text(value):
    """Return safe, trimmed text for the study notes field."""
    if not isinstance(value, str):
        return ""
    return value.replace("\x00", "").strip()
