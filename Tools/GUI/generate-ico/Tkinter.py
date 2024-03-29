import os, asyncio
from favicons import Favicons
from tkinter import filedialog

user_name = os.getlogin()

YOUR_ICON = filedialog.askopenfilename(
    title="Select image file to generate favicon files:",
    filetypes=[("Image Files", [".svg", ".jpeg", ".jpg", ".png", ".tiff", ".tif"])],
)  # img file location
WEB_SERVER_ROOT = rf"C:\Users\{user_name}\Documents\generate-ico\{os.path.split(YOUR_ICON)[1]}"  # destination folder for files location

try:
    os.mkdir(rf"C:\Users\{user_name}\Documents\generate-ico")
except FileExistsError:
    pass

try:
    os.mkdir(rf"{WEB_SERVER_ROOT}")
except FileExistsError:
    pass


def sync_fvcon():
    with Favicons(YOUR_ICON, WEB_SERVER_ROOT) as favicons:
        favicons.generate()
        for icon in favicons.filenames():
            print(icon)


sync_fvcon()


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


loop = asyncio.get_event_loop()

loop.run_until_complete(async_fvcon())
loop.run_until_complete(html_fvcon())
loop.run_until_complete(tuple_fvcon())
loop.run_until_complete(json_fvcon())

loop.close()
