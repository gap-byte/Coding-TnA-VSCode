# 1. First, we import the Flet library so we can use its "building blocks"
import flet as ft

# 2. This is the main function where we design our app's "Brain"
def main(page: ft.Page):
    # 'page' is like a blank white board where we place our buttons and text
    
    # 3. Setting up the appearance of the app window
    page.title = "Simple To-Do List"      # The name shown at the top of the window
    page.theme_mode = ft.ThemeMode.LIGHT  # Use light mode (white background)
    page.window_width = 450               # Set the width of the app in pixels
    page.window_height = 600              # Set the height of the app in pixels
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER # Center everything horizontally

    # 4. Create a Title (like a big header in Scratch)
    title = ft.Text("My Tasks", size=30, weight=ft.FontWeight.BOLD)

    # 5. Create an Input area (where the user types)
    # 'expand=True' makes it stretch to fill the available space in a row
    task_field = ft.TextField(hint_text="Write a task...", expand=True)
    
    # 6. Create a 'Column' to store our tasks
    # Think of this as an empty vertical stack or a list container
    tasks_column = ft.Column(spacing=10)

    # 7. Define what happens when we click the "Add" button
    def add_task_clicked(e):
        # Check if the user actually typed something (strip removes empty spaces)
        if task_field.value.strip():
            
            # Create a new Checkbox control using the text from the input box
            new_checkbox = ft.Checkbox(label=task_field.value)
            
            # Add that checkbox into our vertical stack (tasks_column)
            tasks_column.controls.append(new_checkbox)
            
            # Clear the input box so it's empty for the next task
            task_field.value = ""
            
            # IMPORTANT: The page doesn't change until we tell it to "Update"
            # This is like refreshing a website to see new content
            page.update()

    # 8. Create a 'Row' to put the input box and button side-by-side
    input_row = ft.Row(
        controls=[
            task_field,
            # This is a circular button with a "+" icon
            # 'on_click' tells the button to run our 'add_task_clicked' function
            ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=add_task_clicked)
        ]
    )

    # 9. Finally, we push all our created parts onto the visible page
    page.add(
        title,                                # The big text
        ft.Divider(height=20, color="transparent"), # A small invisible gap
        input_row,                            # The input box + button row
        tasks_column                          # The list of checkboxes
    )

# 10. This line actually starts the application
ft.app(target=main)
