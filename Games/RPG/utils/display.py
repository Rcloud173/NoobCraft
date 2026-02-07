def stat_line(label, value, max_value=10):
    return f"{label} " + "●" * value + "○" * (max_value - value)
