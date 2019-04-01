import sys
# Ваши импорты
import asyncio
import aiohttp
import csv
from bs4 import BeautifulSoup


def parsing(data):
    out_dict = {}
    soup = BeautifulSoup(data, 'html.parser')
    username = "user-info__nickname_comment"
    result = soup.findAll('span', {'class': username})
    for user in result:
        if user.contents[0] in out_dict:
            out_dict[user.contents[0]] += 1
        else:
            out_dict[user.contents[0]] = 1
    return out_dict


async def get_request(l, o, lp):
    async with aiohttp.ClientSession(loop=lp) as session:
        async with session.get(l) as resp:
            o[l] = parsing(await resp.text())


if __name__ == '__main__':
    filename = 'top_user_comments.csv'
    links = sys.argv[1:4]
    loop = asyncio.get_event_loop()
    out = {link: {} for link in links}
    tasks = [loop.create_task(get_request(link, out, loop)) for link in links]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
    out_l = []
    for link in links:
        out_list = []
        for user in out[link]:
            out_list.append([link, user, out[link][user]])
        out_l += sorted(out_list, reverse=True, key=lambda x: x[2])
    with open(filename, 'w', newline="") as file:
        csv.writer(file).writerows(out_l)
        file.close()
