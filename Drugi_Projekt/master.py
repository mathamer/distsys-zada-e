import random
import logging

PORT = 31310
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
)

SAMPLE_SIZE = 1000
MAX_NUM_REQUESTS = 10000
num_received_requests = 0
num_returned_responses = 0
num_sent_tasks = 0
num_completed_tasks = 0

num_workers = random.randint(5, 10)
print("Broj workera:", num_workers)

workers = {"worker_{}".format(id): [] for id in range(1, num_workers + 1)}
print("Workers:", workers)
