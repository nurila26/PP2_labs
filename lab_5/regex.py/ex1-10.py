import re 

with open("row.txt", "r", encoding="utf-8") as f:
    data = f.read()

print("Task 1")
matches = re.findall(r"a.*?b", data)
print(matches)


print("Task 2")
matches = re.findall(r"ab{2,3}", data)
print(matches)


print("Task 3")
matches = re.findall(r"[a-z]+_[a-z]+", data)
print(matches)


print("Task 4")
matches = re.findall(r"[A-Z][a-z]+", data)
print(matches)


print("Task 5")
matches = re.findall(r"a.*b$", data)
print(matches)


print("Task 6")
matches = re.sub(r"[., ]", ":", data)
print(matches)


def snake_to_camel(s):
    return ''.join(word.capitalize() for word in s.split('_'))

print("Task 7")
print(snake_to_camel(data))


print("Task 8")
matches = re.findall(r"[A-Z][^A-Z]*", data)
print(matches)


print("Task 9")
matches = re.sub(r"([A-Z])", r" \1", data).strip()
print(matches)


def camel_to_snake(s):
    return re.sub(r"([a-z])([A-Z])", r"\1_\2", s).lower()

print("Task 10")
print(camel_to_snake(data))