motor = {
    "nume": "Shoot",
    "rpm": 5000,
    "putere": 100
}

print(motor["nume"])
print(motor.get("rpm", -1))
print(motor.get("putere", -1))   
print(motor.get("cuplu", -1))