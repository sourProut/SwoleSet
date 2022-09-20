import random
num = 1
workout_a = ['pushups','situps','crucnches','squats']
workout_b = ['swings','squats','presses','circles']
workout_c = ['jump_jacks','burpees','jump_rope','shadow_box']
print("Hello and glad to see you're  getting swole")
sets = int(input("how many sets?"))
while sets > 0:
    print("set",num)
    print(random.choice(workout_a))
    print(random.choice(workout_b))
    print(random.choice(workout_c))
    sets = sets-1
    num = num + 1
