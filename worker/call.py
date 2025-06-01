from tasks import add

result = add.delay(4, 4)
print("Task submitted.")

# Wait for the result to be ready
result_value = result.get(timeout=10)  # waits up to 10 seconds
print("Result:", result_value)
