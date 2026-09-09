# Question 1:
#
# You are building a dashboard that needs data from three independent services.
# The following functions simulate those services:
#
# import asyncio
#
#
# async def fetch_user():
#     await asyncio.sleep(2)
#     return {
#         "id": 101,
#         "name": "Poku"
#     }
#
#
# async def fetch_orders():
#     await asyncio.sleep(3)
#     return [
#         {"id": 1, "amount": 1200},
#         {"id": 2, "amount": 800}
#     ]
#
#
# async def fetch_notifications():
#     await asyncio.sleep(1)
#     return [
#         "Payment received",
#         "New login detected"
#     ]
#
#
# Task:
#
# Implement an async function named `fetch_dashboard_data()` that:
#
# 1. Fetches the user, orders, and notifications.
# 2. Executes all three operations concurrently.
# 3. Uses asyncio.gather() to achieve concurrency.
# 4. Returns a single dictionary in the following format:
#
# {
#     "user": {
#         "id": 101,
#         "name": "Poku"
#     },
#     "orders": [
#         {"id": 1, "amount": 1200},
#         {"id": 2, "amount": 800}
#     ],
#     "notifications": [
#         "Payment received",
#         "New login detected"
#     ]
# }
#
# 5. Measure and print the total execution time.
#
# Expected:
# Since the three operations run concurrently, the total execution
# time should be approximately 3 seconds instead of 6 seconds.






import time
import asyncio

async def fetch_user():
    await asyncio.sleep(2)

    return {
        "id": 101,
        "name": "Poku"
    }


async def fetch_orders():
    await asyncio.sleep(3)

    return [
        {"id": 1, "amount": 1200},
        {"id": 2, "amount": 800}
    ]


async def fetch_notifications():
    await asyncio.sleep(1)

    return [
        "Payment received",
        "New login detected"
    ]


async def fetch_dashboard_data():
    """
    Fetch user, orders, and notifications concurrently
    and return them as a single dictionary.
    """

    users,orders,notification= await asyncio.gather(
         fetch_user(),
         fetch_orders(),
         fetch_notifications()
     )

    return{
        "users":users,
        "orders":orders,
        "notifications":notification
    }




async def main():
    start_time = time.perf_counter()

    result = await fetch_dashboard_data()

    end_time = time.perf_counter()

    print("Dashboard Data:")
    print(result)

    print(f"\nTotal execution time: {end_time - start_time:.2f} seconds")


if __name__== "__main__":
    asyncio.run(main())