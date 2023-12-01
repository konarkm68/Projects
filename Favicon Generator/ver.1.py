import asyncio
from favicons import Favicons

loop = asyncio.get_event_loop()

YOUR_ICON = '' # jpg file location
WEB_SERVER_ROOT = '' # destination folder location

def sync_fvcon():
    with Favicons(YOUR_ICON, WEB_SERVER_ROOT) as favicons:
        favicons.generate()
        for icon in favicons.filenames():
            print(icon)

async def async_fvcon():
    async with Favicons(YOUR_ICON, WEB_SERVER_ROOT) as favicons:
        await favicons.generate()
        for icon in favicons.filenames():
            print(icon)

async def html_fvcon():
    async with Favicons(YOUR_ICON, WEB_SERVER_ROOT) as favicons:
        await favicons.generate()
        # As generator
        html = favicons.html_gen()
        # As tuple
        html = favicons.html()
    print(html)

async def tuple_fvcon():
    async with Favicons(YOUR_ICON, WEB_SERVER_ROOT) as favicons:
        await favicons.generate()
        as_tuple = favicons.formats()
        print(as_tuple)

async def json_fvcon():
    async with Favicons(YOUR_ICON, WEB_SERVER_ROOT) as favicons:
        await favicons.generate()
        as_json = favicons.json(indent=2)
        print(as_json)

##sync_fvcon()
##loop.run_until_complete(async_fvcon())
##loop.run_until_complete(html_fvcon())
##loop.run_until_complete(tuple_fvcon())
##loop.run_until_complete(json_fvcon())

loop.close()
