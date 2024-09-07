# AccuKnox-Project

Question 1: By default, are Django signals executed synchronously or asynchronously?
Answer:
By default, Django signals are executed synchronously. This means that when a signal is triggered, the receivers connected to it are executed in sequence, and the sender waits for all receivers to finish before continuing execution.

<img width="454" alt="image" src="https://github.com/user-attachments/assets/f80d933b-e271-4679-956c-6fc48d4372ae">

In this example, the post_save signal is triggered synchronously. The print("Object created") statement will only be executed after the signal handler my_signal_handler finishes executing.

<img width="428" alt="image" src="https://github.com/user-attachments/assets/04c85f84-0090-4d22-8449-41b7cb5de700">

Question 2: Do Django signals run in the same thread as the caller?

Answer:
Yes, by default, Django signals run in the same thread as the caller. However, Django allows signals to be executed asynchronously by using the async=True parameter in the @receiver decorator.

<img width="432" alt="image" src="https://github.com/user-attachments/assets/57d2588a-739f-4bca-9cc6-83186a9b52be">
In this code, both the main thread and the thread inside the signal handler have the same thread ID, indicating that the signal is running in the same thread as the caller.

Question 3: Question 3: By default, do Django signals run in the same database transaction as the caller?
Answer:
Yes, Django signals run in the same database transaction as the caller. This means that any changes made in the signal handler are part of the same atomic transaction as the initial operation that triggered the signal.
<img width="454" alt="image" src="https://github.com/user-attachments/assets/d8c81d58-d830-47e4-b571-9d5931b9b535">
In this example, the instance.save() inside the signal handler happens within the same transaction as the object creation, proving that Django signals run within the same database transaction.

Output of the given project -:
<img width="342" alt="image" src="https://github.com/user-attachments/assets/19679090-479f-42e6-908a-fc28e1479389">










