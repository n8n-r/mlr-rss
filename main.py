import asyncio
from datetime import datetime
from parse_comments import *

async def main():
    data_setup()

    print(f"{datetime.now().strftime('%m/%d/%Y %H:%M:%S')} Reddit post watcher starting with the following searches:")

    for r in rss_feeds:
        print(f"     * {r['search']} -- ping: {r['ping']}")

    while True:
        try:
            await asyncio.gather(
                parse_comments(),
                check_timers(),
                return_exceptions=False
            )
        except Exception as e:
            print(f"Error in main loop: {e}")
            print("Restarting tasks in 15 seconds...")
            await asyncio.sleep(15)

asyncio.run(main())