import aiohttp
import asyncio


def filter_currencies(all_prices, tax):
    main_currencies = ["USDT", "BTC", "ETH", "BNB", "EUR"]
    currencies = ["EUR", "BTC", "ETH", "BNB", "SOL", "ADA", "XRP", "LUNA", "DOT", "DOGE", "AVAX", "MATIC"]
    new_all_prices = dict()
    for d in all_prices:
        flag = True
        for main_cur in main_currencies:
            end = d['symbol'].endswith(main_cur)
            if end and flag:
                for curr in currencies:
                    start = d['symbol'].startswith(curr)
                    if start and curr != main_cur and float(d['bidPrice']) != 0.00000000 and \
                            float(d['askPrice']) != 0.00000000 and flag and \
                            len(curr) + len(main_cur) == len(d['symbol']):
                        bid_symbol = f"{curr}-{main_cur}"
                        bid_price, ask_price = float(d['bidPrice']) * tax, 1 / float(d['askPrice']) * tax
                        new_all_prices[bid_symbol] = (bid_price, ask_price)
                        flag = False
                    elif not flag:
                        break
            elif not flag:
                break
    return new_all_prices


async def get_json(session, url, all_prices):
    async with session.get(url) as resp:
        result = await resp.json()
        all_prices.append(result)


async def get_all_currencies():
    all_prices = []
    tax = 0.999
    async with aiohttp.ClientSession() as session:
        tasks = []
        url = f"https://api.binance.com/api/v3/ticker/bookTicker"
        tasks.append(asyncio.ensure_future(get_json(session, url, all_prices)))
        await asyncio.gather(*tasks)
    new_all_prices = filter_currencies(all_prices[0], tax)
    return new_all_prices
