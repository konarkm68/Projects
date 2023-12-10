import os, flet, PyInstaller.__main__

def main(page: flet.Page):
    page.title = "Pack PyScript!"
    page.window_width = 320
    page.window_height = 360
    page.window_resizable = False
    page.window_maximizable = False
    page.theme_mode = flet.ThemeMode.DARK

    def pack(py_script, exe_name):  
        try:
            user_name = os.getlogin()

            pyexe_path = fr"C:\Users\{user_name}\Documents\PyInstaller"
        
            os.mkdir(fr"{pyexe_path}")
            os.mkdir(fr"{pyexe_path}\dist")
            os.mkdir(fr"{pyexe_path}\build")
            os.mkdir(fr"{pyexe_path}\spec")
        except FileExistsError:
            pass

        try:    
            if console.value == True:
                windowed = '--console'
            elif console.value == False:
                windowed = '--noconsole'

            if icon.value == False:
                icon_query = 'NONE'
            elif icon.value == True:
                icon_query = icon_file

            if not exe_name.value or exe_name.value == '':
                page.snack_bar.content = flet.Text(f'Error! - Please select a Python-Script!', size=10, color='red', weight='bold')
                page.snack_bar.open = True
                page.update()
            
            query = [
                fr"{py_script}",
                '--icon', fr"{icon_query}",
                FileDIR.value, windowed, '--name', exe_name.value, 
                '--specpath', fr"{pyexe_path}\spec",
                '--workpath', fr"{pyexe_path}\build",
                '--distpath', fr"{pyexe_path}\dist",
                '--clean', '--noconfirm', '--log-level=ERROR'
                ]

            progress_bar.value = None
            pack_btn.disabled = True
            page.update()

            result = PyInstaller.__main__.run(query)
            if result == None:
                progress_bar.value = 1.0
                pack_btn.disabled = False

                page.snack_bar.content = flet.Text(f'Success! - Your .exe file is located in Documents/PyInstaller/dist/ OR ./{exe_name.value}', size=10, color='green')
                page.snack_bar.action='Open Directory!'
                page.snack_bar.on_action=lambda _: os.startfile(r"C://Users//{}//Documents//PyInstaller//dist".format(os.getlogin()) )               
                page.snack_bar.open = True
                page.update()
        except Exception as e:
            progress_bar.value = 0.0
            page.snack_bar.content = flet.Text(f'Error! - {e}', size=10, color='red', weight='bold')
            page.snack_bar.open = True
            page.update()

    console = flet.Checkbox(value=False, tooltip='Console or Windowed ?')
    icon = flet.Checkbox(value=True, tooltip='Icon or no Icon ?')
    FileDIR = flet.RadioGroup(content=flet.Row([
        flet.Radio(value='--onedir', label='--one-directory ?', width=160, label_position = 'right'),
        flet.Radio(value='--onefile', label='--one-file ?', width=160 , label_position = 'right')
        ]), value='--onefile' )
    exe_name = flet.TextField(width=185, height=60, max_length=15, hint_text='Default: PyScript-Name', text_size=12)
    
    def select_py(e: flet.FilePickerResultEvent):
        try:
            global py_script
            py_script = e.files[0].path
            exe_name.value = e.files[0].name.split('.')[0]
            page.update()
        except TypeError:
            page.snack_bar.content = flet.Text(f'Error! - Please select a Python-Script!', size=10, color='red', weight='bold')
            page.snack_bar.open = True
            page.update()
        except Exception as e:
            page.snack_bar.content = flet.Text(f'Error! - {e}', size=10, color='red')
            page.snack_bar.open = True
            page.update()
       
    def select_ico(e: flet.FilePickerResultEvent):
        try:
            global icon_file
            icon_file = e.files[0].path
        except TypeError:
            page.snack_bar.content = flet.Text(f'Error! - Please select an Icon-File!', size=10, color='red', weight='bold')
            page.snack_bar.open = True
            page.update()
        except Exception as e:
            page.snack_bar.content = flet.Text(f'Error! - {e}', size=10, color='red')
            page.snack_bar.open = True
            page.update()

    select_py_dialog = flet.FilePicker(on_result = select_py)
    page.overlay.append(select_py_dialog)
    select_ico_dialog = flet.FilePicker(on_result = select_ico) 
    page.overlay.append(select_ico_dialog)
    
    pack_btn = flet.FilledButton('Pack PyScript! (.py --> .exe)', on_click=lambda _: pack(py_script, exe_name), width=400, height=50)
    
    progress_bar = flet.ProgressBar(value = 0.0, width = 360)
    page.snack_bar = flet.SnackBar(open=False, duration=15000, content=flet.Text(''), show_close_icon=True)
                
    page.add(
        flet.Column([
        flet.Text('PyInstaller', weight='bold', text_align='center', width=400, size=24),
        flet.Row([
            flet.Text('--console ?', width=90, font_family='consolas'), console,
            flet.Text('--icon ?', width=100, font_family='consolas'), icon]),
        FileDIR,
        flet.Row([
            flet.Text('PyScript ?', width=85, font_family='consolas'),
            flet.IconButton(
                icon=flet.icons.FILE_OPEN, tooltip="Browse Python-Script",
                on_click=lambda _: select_py_dialog.pick_files(
                    allow_multiple=False, allowed_extensions=["py"], dialog_title="Select Python-Script") ),
            flet.Text('icon-file ?', width=90, font_family='consolas'),
            flet.IconButton(
                icon=flet.icons.FILE_OPEN, tooltip="Browse Icon-File",
                on_click=lambda _: select_ico_dialog.pick_files(
                    allow_multiple=False, allowed_extensions=["ico"], dialog_title="Select Icon-File")) ]),       
        flet.Row([flet.Text('exe-name ?', width=85, font_family='consolas'), exe_name]),
        pack_btn,
        progress_bar,
        ] ))

flet.app(main)