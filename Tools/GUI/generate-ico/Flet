import os, flet, asyncio
from favicons import Favicons
from tkinter import filedialog

def main(page: flet.Page):
    page.title = "Icon File (.ico) Generator"
    page.window_width = 320
    page.window_height = 218
    page.window_resizable = False
    page.window_maximizable = False
    page.theme_mode = flet.ThemeMode.DARK

    def generate_ico():
        user_name = os.getlogin()

        #YOUR_ICON = filedialog.askopenfilename(title='Select image file to generate favicon files:', filetypes=[('Image Files',
        #['.svg', '.jpeg', '.jpg', '.png', '.tiff', '.tif'])]) # img file location
        WEB_SERVER_ROOT = fr"C:\Users\{user_name}\Documents\generate-ico\{os.path.split(YOUR_ICON)[1]}" # destination folder for files location

        try:
            os.mkdir(fr"C:\Users\{user_name}\Documents\generate-ico")
        except FileExistsError:
            pass

        try:
            os.mkdir(fr"{WEB_SERVER_ROOT}")
        except FileExistsError:
            pass
        
        def ico_generator():
            with Favicons(YOUR_ICON, WEB_SERVER_ROOT) as favicons:
                favicons.generate()
                for icon in favicons.filenames():
                    print(icon)
            '''
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

            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)

            loop.run_until_complete(async_fvcon())
            loop.run_until_complete(html_fvcon())
            loop.run_until_complete(tuple_fvcon())
            loop.run_until_complete(json_fvcon())

            loop.close()
            '''
            return 0 

        if image_file.value == 'None':
            page.snack_bar.content = flet.Text(f'Error! - Please select an Image-File!', size=10, color='red', weight='bold')
            page.snack_bar.open = True
            page.update()
        else:
            try:
                progress_bar.value = None
                gen_ico_btn.disabled = True
                page.update()

                result = ico_generator()
                if result == 0:
                    progress_bar.value = 1.0
                    gen_ico_btn.disabled = False

                    page.snack_bar.content = flet.Text(f'Success! - Your .ico file is located in {WEB_SERVER_ROOT}', size=10, color='green')
                    page.snack_bar.action='Open Directory!'
                    page.snack_bar.on_action=lambda _: os.startfile(WEB_SERVER_ROOT)               
                    page.snack_bar.open = True
                    page.update()
            except Exception as e: 
                progress_bar.value = 0.0
                gen_ico_btn.disabled = False
                page.snack_bar.content = flet.Text(f'Error! - {e}', size=10, color='red', weight='bold')
                page.snack_bar.open = True
                page.update()  

    def select_img(e: flet.FilePickerResultEvent):
        try:
            global YOUR_ICON
            YOUR_ICON = e.files[0].path
            image_file.value = str(os.path.split(YOUR_ICON)[1])
            page.update()
        except TypeError:
            page.snack_bar.content = flet.Text(f'Error! - Please select an Image-File!', size=10, color='red', weight='bold')
            page.snack_bar.open = True
            page.update()
        except Exception as e:
            page.snack_bar.content = flet.Text(f'Error! - {e}', size=10, color='red')
            page.snack_bar.open = True
            page.update()

    select_img_dialog = flet.FilePicker(on_result = select_img)
    page.overlay.append(select_img_dialog)

    image_file = flet.Text('None', width=400)

    gen_ico_btn = flet.FilledButton('Generate Icon File (.ico)!', on_click=lambda _: generate_ico(), width=400, height=40)
    
    progress_bar = flet.ProgressBar(value = 0.0, width = 360)
    page.snack_bar = flet.SnackBar(open=False, duration=15000, content=flet.Text(''), show_close_icon=True)
    
    page.add(
        flet.Column([
            flet.Text('Icon File (.ico) Generator', weight='bold', text_align='center', width=400, size=18),
            flet.Row([
                flet.Text('Image-File ?', font_family='consolas'),
                flet.IconButton(
                    icon=flet.icons.FILE_OPEN, tooltip="Browse Image-File",
                    on_click=lambda _: select_img_dialog.pick_files(
                        allow_multiple=False, allowed_extensions=["svg", "jpg", "jpeg", "png"], dialog_title="Select Image-File")) ]),
            flet.Row([
                flet.Text('Selected Image File:'), image_file]),
            gen_ico_btn,
            progress_bar,   
            ]) )

flet.app(main)