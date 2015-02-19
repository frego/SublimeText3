import sublime, sublime_plugin

#############################################################################
# PythonCommand                                                             #
#############################################################################

class PromptPythonCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.window.show_input_panel("Python:", "", self.on_done, None, None)

    def on_done(self, text):
        try:
            output = eval(text)
            if self.window.active_view():
                self.window.active_view().run_command("execute_python", {"text": output} )
        except Exception as e:
            print(e)
            self.window.run_command("show_panel", {"panel": "console", "toggle": True})

class ExecutePythonCommand(sublime_plugin.TextCommand):
    def run(self, edit, text):
        self.view.insert(edit, self.view.sel()[0].begin(), str(text))

#############################################################################
# Divers                                                                    #
#############################################################################

# class Rot13Command(sublime_plugin.TextCommand):  
#     def run(self, view, args):  
#         for region in view.sel():  
#             if not region.empty():  
#                 # Get the selected text  
#                 s = view.substr(region)  
#                 # Transform it via rot13  
#                 s = s.encode('rot13')  
#                 # Replace the selection with transformed text  
#                 view.replace(region, s)  
