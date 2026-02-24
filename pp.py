def parse_json(s):
    i = 0

    def skip_spaces():
        nonlocal i
        while i < len(s) and s[i].isspace():
            i += 1

    def parse_string():
        nonlocal i
        i += 1  # skip opening quote
        start = i
        while s[i] != '"':
            i += 1
        value = s[start:i]
        i += 1  # skip closing quote
        return value

    def parse_number():
        nonlocal i
        start = i
        while i < len(s) and (s[i].isdigit() or s[i] == '.'):
            i += 1
        num_str = s[start:i]
        if '.' in num_str:
            return float(num_str)
        return int(num_str)

    def parse_value():
        nonlocal i
        skip_spaces()

        if s[i] == '"':
            return parse_string()
        elif s[i].isdigit():
            return parse_number()
        elif s[i] == '{':
            return parse_object()
        elif s[i:i+4] == "true":
            i += 4
            return True
        elif s[i:i+5] == "false":
            i += 5
            return False
        elif s[i:i+4] == "null":
            i += 4
            return None

    def parse_object():
        nonlocal i
        obj = {}
        i += 1  # skip {

        while True:
            skip_spaces()

            if s[i] == '}':
                i += 1
                break

            key = parse_string()
            skip_spaces()

            if s[i] == ':':
                i += 1

            value = parse_value()
            obj[key] = value

            skip_spaces()
            if s[i] == ',':
                i += 1
            elif s[i] == '}':
                i += 1
                break

        return obj

    return parse_object()


# Test input
json_text = input("Enter JSON string: ")
result = parse_json(json_text)

print("Parsed output:")
print(result)