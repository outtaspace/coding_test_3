import re

city_info_regex = re.compile("""
    ^
    (\d+)
    \.
    \s+
    ([^;,]+)[;,.]?
    \s+
    ([^;,]+)[;,.]?
    \s-\s
    (.+)
    $
""", flags=re.X)


def parse_line(raw_line: str) -> dict:
    match = city_info_regex.findall(raw_line)
    result = None
    if len(match):
        match = match[0]
        result = dict(
            id=match[0],
            city=match[1],
            country=match[2],
            population=match[3]
        )
    return result
