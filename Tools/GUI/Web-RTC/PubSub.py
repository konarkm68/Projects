import flet

class Message():
    def __init__(self, user_name: str, text: str, message_type: str):
        self.user_name = user_name
        self.text = text
        self.message_type = message_type

class ChatMessage(flet.Row):
    def __init__(self, message: Message):
        super().__init__()
        self.vertical_alignment="start"
        self.controls=[
            flet.Stack([
                flet.CircleAvatar(
                    content=flet.Text(message.user_name[0],), color=flet.colors.WHITE, 
                    bgcolor=self.get_avatar_color(message.user_name)),
                flet.Container(
                    content=flet.CircleAvatar(bgcolor=flet.colors.GREEN, radius=7), 
                    alignment=flet.alignment.bottom_right) ],
                    width=40, height=40),
            flet.Column([               
                    flet.Text(message.user_name, weight="bold"), 
                    flet.Text(message.text, selectable=True) ]) ]

    def get_avatar_color(self, user_name: str):
        colors_lookup = [
            flet.colors.AMBER, flet.colors.BLUE, flet.colors.BROWN, flet.colors.CYAN,
            flet.colors.INDIGO, flet.colors.LIME, flet.colors.ORANGE, flet.colors.PINK, 
            flet.colors.PURPLE, flet.colors.RED, flet.colors.TEAL, flet.colors.YELLOW, ]
        return colors_lookup[hash(user_name) % len(colors_lookup)]

def main(page: flet.Page):
    page.title = "Local-System-Apps Pub-Sub Chat"
    page.window_height = 650
    page.window_width = 450

    def join_chat_click(e):
        if not join_user_name.value:
            join_user_name.error_text = "Name cannot be blank!"
            join_user_name.update()
        elif join_user_name.value.isalpha() == False:
            join_user_name.error_text = "Name cannot contain numbers or special characters!"
            join_user_name.update()
        else:
            join_user_name.value = join_user_name.value.capitalize(); join_user_name.disabled = True; join_user_name.error_text = None
            send_button.disabled = True
            options.disabled = False; chat.disabled = False; new_message.disabled = False

            page.session.set("user_name", join_user_name.value)

            new_message.prefix = flet.Text(f"{join_user_name.value}: ")
            page.pubsub.send_all(
                Message(user_name=join_user_name.value, 
                text=f"{join_user_name.value} has joined the chat.", message_type="log_msg"))

            page.update()

    def send_message_click(e):
        if new_message.value != "":
            page.pubsub.send_all(
                Message(page.session.get("user_name"), new_message.value, message_type="chat_msg"))
            
            new_message.value = ""
            new_message.focus()

            page.update()

    def on_message(message: Message):
        if message.message_type == "chat_msg":
            msg = ChatMessage(message)
        elif message.message_type == "log_msg":
            msg = flet.Text(message.text, italic=True, color=flet.colors.WHITE, size=12)
        
        chat.controls.append(msg)

        page.update()

    page.pubsub.subscribe(on_message)

    def clear_chat():
        chat.controls.clear()

        info_text = "Chat cleared successfully!"
        info_banner(info_text)

        page.update()

        page.pubsub.send_all(
            Message(page.session.get("user_name"), 
            f"{page.session.get('user_name')} has cleared the chat.", message_type="log_msg"))

    def save_chat():
        with open(r"Local-System-Apps Pub-Sub Chat-History.txt", "w") as f:
            f.write("Chat History:\n")
            for msg in chat.controls:
                if isinstance(msg, ChatMessage):
                    f.writelines(f"\n{msg.controls[1].controls[0].value}: {msg.controls[1].controls[1].value}")
                else:
                    f.writelines(f"\n{msg.value}")  

        info_text = "Chat saved successfully!"
        info_banner(info_text)

        page.update()

        page.pubsub.send_all(Message(page.session.get("user_name"), f"{page.session.get('user_name')} has saved the chat.", message_type="log_msg"))

    def info_banner(info_text: str):
        def close_banner(e):
            page.banner.open = False
            page.update()
        
        page.banner = flet.Banner(open=True,
            leading=flet.Icon(flet.icons.INFO, color=flet.colors.WHITE, size=40),
            content=flet.Text(info_text, color=flet.colors.WHITE, size=20, weight="bold",),
            actions=[flet.TextButton("OK", on_click=close_banner, ),],)

    def exit_app():
        page.pubsub.send_all(Message(page.session.get("user_name"), f"{page.session.get('user_name')} has left the chat.", message_type="log_msg"))
        page.window_close()

    # A dialog asking for a user display name
    join_user_name = flet.TextField(
        label="Enter your name to join the chat", autofocus=True, on_submit=join_chat_click, max_length=15)

    send_button = flet.IconButton(
        icon=flet.icons.ADD_IC_CALL_ROUNDED, tooltip="Join Text-Chat", on_click=join_chat_click, height=100)

    # A menu button with options to clear, save and leave the chat
    options = flet.PopupMenuButton(
                icon=flet.icons.MORE_VERT, tooltip="Options", disabled=True, height=100, items=[
                    flet.PopupMenuItem(text="Clear Chat", on_click=lambda e: clear_chat(),),
                    flet.PopupMenuItem(text="Leave Chat", on_click=lambda e: exit_app() ,),
                    flet.PopupMenuItem(text="Save Chat", on_click=lambda e: save_chat() ,)
                ],)

    # Chat messages
    chat = flet.ListView(expand=True, spacing=10, auto_scroll=True, disabled=True,)

    # A new message entry form
    new_message = flet.TextField(
        hint_text="Write a message...", autofocus=True, shift_enter=True,
        min_lines=1, max_lines=5, filled=True, expand=True, on_submit=send_message_click, disabled=True,)

    # Add everything to the page
    page.add(
        flet.Row([join_user_name, send_button, options, ], ),
        flet.Container(
            content=chat, border=flet.border.all(1, flet.colors.OUTLINE), border_radius=5,
            padding=20, expand=True,),
        flet.Row([
            new_message, flet.IconButton(
                icon=flet.icons.SEND_ROUNDED, tooltip="Send message", on_click=send_message_click,),]),)

flet.app(target=main)#, view=flet.WEB_BROWSER)