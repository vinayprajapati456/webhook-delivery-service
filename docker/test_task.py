# test_task.py

from webhook_service.tasks import deliver_webhook

# Trigger the task
result = deliver_webhook.delay({'message': 'Hello from test!'})

# Print the task ID and result (optional wait for result)
print("Task sent with ID:", result.id)
print("Waiting for result...")
print("Result:", result.get(timeout=10))  # this will block until it's done
