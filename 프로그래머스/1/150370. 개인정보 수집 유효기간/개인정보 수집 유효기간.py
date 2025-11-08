def solution(today, terms, privacies):
    def to_days(date_str):
        y, m, d = map(int, date_str.split('.'))
        return y * 12 * 28 + m * 28 + d
    term_map = {}
    for t in terms:
        typ, months = t.split()
        term_map[typ] = int(months)

    today_days = to_days(today)
    expired = []

    for i, p in enumerate(privacies, start=1):
        date_str, typ = p.split()
        p_days = to_days(date_str)
        expire_threshold = p_days + term_map[typ] * 28 
        if today_days >= expire_threshold:
            expired.append(i)

    return expired