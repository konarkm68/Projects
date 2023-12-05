import flet 

class Task(flet.UserControl):
    def __init__(self, task_name, task_status_change, task_delete):
        super().__init__()

        self.completed = False
        self.task_name = task_name
        self.task_status_change = task_status_change
        self.task_delete = task_delete

    def build(self):
        self.display_task = flet.Checkbox(
            value=False, label=self.task_name, on_change=self.status_changed)
        self.edit_name = flet.TextField(max_length=15)

        self.display_view = flet.Row(
            alignment=flet.MainAxisAlignment.SPACE_BETWEEN, vertical_alignment=flet.CrossAxisAlignment.START,
            controls=[self.display_task, flet.Row(controls=[
                flet.IconButton(
                    icon=flet.icons.CREATE_OUTLINED, icon_color=flet.colors.BLUE, 
                    tooltip="Edit Task", on_click=self.edit_clicked,),
                flet.IconButton(
                    icon=flet.icons.DELETE_OUTLINE, icon_color=flet.colors.RED, 
                    tooltip="Delete Task", on_click=self.delete_clicked, ), ], ), ], )

        self.edit_view = flet.Row(visible=False, 
            alignment=flet.MainAxisAlignment.SPACE_BETWEEN, vertical_alignment=flet.CrossAxisAlignment.START,
            controls=[
                self.edit_name, flet.IconButton(
                    icon=flet.icons.DONE_OUTLINE_OUTLINED, icon_color=flet.colors.GREEN, 
                    tooltip="Modify Task", on_click=self.save_clicked, ), ], )
        
        return flet.Column(controls=[self.display_view, self.edit_view])

    async def edit_clicked(self, e):
        self.edit_name.value = self.display_task.label
        self.display_view.visible = False
        self.edit_view.visible = True
        
        await self.update_async()

    async def save_clicked(self, e):
        self.display_task.label = self.edit_name.value
        self.display_view.visible = True
        self.edit_view.visible = False
        
        await self.update_async()

    async def status_changed(self, e):
        self.completed = self.display_task.value
        
        await self.task_status_change(self)

    async def delete_clicked(self, e):
        await self.task_delete(self)

class TDApp(flet.UserControl):
    def build(self):
        self.new_task = flet.TextField(
            hint_text="What needs to be done?", on_submit=self.add_clicked, max_length=15,)
        self.tasks = flet.Column()
        self.filter = flet.Tabs(
            scrollable=False, selected_index=1, on_change=self.tabs_changed,
            tabs=[flet.Tab(text="All"), flet.Tab(text="Active"), flet.Tab(text="Completed")], )
        self.items_left = flet.Text("0 Active Task(s)")

        # application's root control (i.e. "view") containing all other controls
        return flet.Column(controls=[
            flet.Row(
                [flet.Text(value="To-Do App", style=flet.TextThemeStyle.HEADLINE_MEDIUM)],
                alignment=flet.MainAxisAlignment.CENTER, ),
            flet.Row(controls=[
                self.new_task, flet.FloatingActionButton(icon=flet.icons.ADD, on_click=self.add_clicked, height=80), ], ),
            flet.Column(controls=[
                self.filter, self.tasks, flet.Row(
                    alignment=flet.MainAxisAlignment.SPACE_BETWEEN, vertical_alignment=flet.CrossAxisAlignment.CENTER,
                    controls=[self.items_left, flet.OutlinedButton(
                        text="Clear Completed Task(s)", icon=flet.icons.DELETE_OUTLINE,
                        icon_color=flet.colors.RED, on_click=self.clear_clicked), ], ), ], ), ], )

    async def add_clicked(self, e):
        if self.new_task.value:
            task = Task(self.new_task.value, self.task_status_change, self.task_delete)
            self.tasks.controls.append(task)
            self.new_task.value = ""
            
            await self.new_task.focus_async()
            await self.update_async()

    async def task_status_change(self, task):
        await self.update_async()

    async def task_delete(self, task):
        self.tasks.controls.remove(task)
        
        await self.update_async()

    async def tabs_changed(self, e):
        await self.update_async()

    async def clear_clicked(self, e):
        for task in self.tasks.controls[:]:
            if task.completed:
                await self.task_delete(task)

    async def update_async(self):
        status = self.filter.tabs[self.filter.selected_index].text
        count = 0
        for task in self.tasks.controls:
            task.visible = (
                status == "All"
                or (status == "Active" and task.completed == False) 
                or (status == "Completed" and task.completed) )
            if not task.completed:
                count += 1
        self.items_left.value = f"{count} Active Task(s)"
        
        await super().update_async()

async def main(page: flet.Page):
    page.title = "To-Do App"
    page.window_width = 400
    page.window_height = 650
    page.window_maximizable = False
    page.window_resizable = False
    page.horizontal_alignment = flet.CrossAxisAlignment.START
    page.scroll = flet.ScrollMode.HIDDEN
    # create app control and add it to the page
    await page.add_async(TDApp())

flet.app(main)