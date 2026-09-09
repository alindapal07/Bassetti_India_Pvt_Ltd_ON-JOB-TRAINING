# Question 3:
#
# Now create an async job runner function named `run_jobs()`.
#
# The following conditions must be met:
#
# 1. All 20 jobs must eventually be processed.
#
# 2. A maximum of 3 jobs may run simultaneously.
#
# 3. Collect and return the results of all completed jobs.
#
# 4. Print the total execution time.
#
# Given:
#
# jobs = list(range(1, 21))
#
# Use the `process_job(job_id)` function from Question 2.
#
# Hint:
# Use `asyncio.Semaphore(3)` to limit the number of
# simultaneously running jobs to 3.
#
# The program should process all 20 jobs, but never allow
# more than 3 jobs to execute at the same time.



import time
import asyncio
import random


async def process_job(job_id):

    print(f"Job {job_id} started")

    duration = random.randint(1, 3)

    await asyncio.sleep(duration)

    print(f"Job {job_id} completed")

    return job_id


async def run_jobs():

    jobs = list(range(1, 21))
    semaphore= asyncio.Semaphore(3)
    async def limited_job(job_id):
        async with semaphore:
            return await process_job(job_id)
    
    task=[limited_job(job_id) for job_id in jobs]
    
    result= await asyncio.gather(*task)
    return result
    
async def main():

    start_time = time.perf_counter()

    results = await run_jobs()

    end_time = time.perf_counter()

    print("\nCompleted Job IDs:")
    print(results)

    print(f"\nTotal execution time: {end_time - start_time:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())