# Don't compare boolean values to True or False

count = 0
playing = True
# Pythonic

while playing:
    print("Playing")
    count += 1
    if count == 3:
        break

finished = False
while not finished:
    pass

# Avoid Complex Loop Conditions

# Not Pythonic
temperature = 85 # Degrees Celisu
pressure = 120 # PSI
error_code = "E02" # Represents a detected fault
shutdown_signal = False # External shutdown trigger

while (temperature > 80 and pressure > 100 and error_code != "OK" and not shutdown_signal and len(error_code) > 1):
    print("System running despite multiple checks...")
    
    # Simulate system changes
    temperature -= 2
    pressure -= 5
    if temperature < 75:
        error_code = "OK"
    if pressure < 90:
        shutdown_signal = True
    
# Pythonic
while True:
    print("System running...")

    # Simulate system changes
    temperature -= 2
    pressure -= 5

    if temperature < 75 or pressure < 90:
        shutdown_signal = True

    if error_code == "OK" or shutdown_signal:
        break


# General Loop Guidelines
# a. Don't use while True
#    unless the loop condition is very complicated
# b. Use break and continue sparingly,
#    and make sure the loop logic remains clear
# c. Avoid else clauses on while and for loops
#    unless it makes the loop logic clearer