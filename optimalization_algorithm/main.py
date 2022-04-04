import asyncio
from get_all_currencies import get_all_currencies
from queue import PriorityQueue


def create_graph(currency_dict):
    graph = {}
    for specified_currencies in currency_dict:
        currency_list = specified_currencies.split("-")
        first_currency, second_currency = currency_list[0], currency_list[1]
        if first_currency not in graph:
            graph[first_currency] = [[second_currency, currency_dict[specified_currencies][1]]]
        else:
            graph[first_currency].append([second_currency, currency_dict[specified_currencies][1]])
        if second_currency not in graph:
            graph[second_currency] = [[first_currency, currency_dict[specified_currencies][0]]]
        else:
            graph[second_currency].append([first_currency, currency_dict[specified_currencies][0]])
    return graph


def dijkstra(graph, start, end):
    distances = {key: float('inf') for key in graph}
    visited = {key: False for key in graph}
    parents = {key: None for key in graph}
    distances[start] = -1
    queue = PriorityQueue()
    queue.put((distances[start], start))

    while not queue.empty():
        distance, currentVertex = queue.get()
        if visited[currentVertex]:
            continue
        if currentVertex == end:
            return distances[end], parents
        visited[currentVertex] = True
        for nextVertex, edgeWeight in graph[currentVertex]:
            if not visited[nextVertex] and distances[nextVertex] > distance / edgeWeight:
                distances[nextVertex] = distance / edgeWeight
                parents[nextVertex] = currentVertex
                queue.put((distances[nextVertex], nextVertex))


def create_exchange_path(parent_list, end):
    res = []
    while (parent_list[end] != None):
        res.append(end)
        end = parent_list[end]
    res.append(end)
    return res[::-1]


def get_bid_symbol(start, end, currency_dict):
    if f"{end}-{start}" in currency_dict.keys():
        return currency_dict[f"{end}-{start}"]
    else:
        return currency_dict[f"{start}-{end}"]


def optimal_currency_exchange(starting_amount, start, end):
    currency_dict = asyncio.run(get_all_currencies())
    graph = create_graph(currency_dict)
    dijkstra_distance, parent_list = dijkstra(graph, start, end)
    bid_symbol = get_bid_symbol(start, end, currency_dict)
    normal_quantity = starting_amount * bid_symbol[1]
    end_quantity = starting_amount * (-dijkstra_distance)
    if end != "USDT":
        normal_value_in_usd = normal_quantity / currency_dict[f"{end}-USDT"][1]
    else:
        normal_value_in_usd = starting_amount
    end_value_in_usd = end_quantity * bid_symbol[0]
    total_profit = end_value_in_usd - normal_value_in_usd
    return normal_quantity, end_quantity, end_value_in_usd, total_profit, create_exchange_path(parent_list, end)


print(optimal_currency_exchange(2, "ETH", "BTC"))
