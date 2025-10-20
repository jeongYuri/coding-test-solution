s = input().strip()

def is_cpp(s):
    return (
        s.islower()
        and "__" not in s
        and not s.startswith("_")
        and not s.endswith("_")
    )

def is_java(s):
    return (
        "_" not in s
        and s[0].islower()
    )

def cpp_to_java(s):
    parts = s.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])

def java_to_cpp(s):
    res = ""
    for ch in s:
        if ch.isupper():
            res += "_" + ch.lower()
        else:
            res += ch
    return res

if "_" in s and any(ch.isupper() for ch in s):
    print("Error!")
elif is_cpp(s):
    print(cpp_to_java(s))
elif is_java(s):
    print(java_to_cpp(s))
else:
    print("Error!")
