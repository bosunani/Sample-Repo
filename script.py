
import requests

print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


print(greet("World"))
print(greet("Bosun"))
r = requests.get("https://coreyms.com")
print(r.status_code)
print (r.ok)


