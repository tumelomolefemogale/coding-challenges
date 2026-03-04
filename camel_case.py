# Given a string, this program returns its camel case version
# All spaces and separators should be removed

def to_camel_case(s):
    s = s.lower()
    for char in s:
        if char in [" ", "-", "_"]:
            s = s.replace(char, "\n")

    string_list = s.splitlines()

    for i in range(1, len(string_list)):
        string_list[i] = string_list[i].capitalize()

    new_string = "".join(string_list)

    return new_string


print(to_camel_case("hello world"))
print(to_camel_case("HELLO WORLD"))
print(to_camel_case("secret agent-X"))
print(to_camel_case("FREE cODE cAMP"))
print(to_camel_case("ye old-_-sea  faring_buccaneer_-_with a - peg__leg----and a_parrot_ _named- _squawk"))
