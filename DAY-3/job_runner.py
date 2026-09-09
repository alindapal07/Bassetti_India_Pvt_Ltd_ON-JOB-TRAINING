# Question 2:
#
# You are given 20 jobs. Each job takes a different amount of time to process.
#
# Implement an async function named `process_job(job_id)` that does the following:
#
# 1. Print when the job starts.
# 2. Wait for a random duration between 1 and 3 seconds.
# 3. Print when the job completes.
# 4. Return the process/job ID.

import time
import asyncio
import random


async def process_job(job_id):

    print(f"Job {job_id} started")

    duration = random.randint(1, 3)

    await asyncio.sleep(duration)

    print(f"Job {job_id} completed")

    return job_id

async def job_creation():

    jobs = []

    for i in range(1, 21):
        jobs.append(process_job(i))

    results = await asyncio.gather(*jobs)

    return results



async def main():

    start_time = time.perf_counter()

    results = await job_creation()

    end_time = time.perf_counter()

    print("\nCompleted Job IDs:")
    print(results)

    print(f"\nTotal execution time: {end_time - start_time:.2f} seconds")
    
if __name__ == "__main__":
    asyncio.run(main())

