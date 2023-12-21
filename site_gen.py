import os
from re import A
from colorama import init, Fore

init(autoreset=True)

def print_fancy(message,fore_color='green'):
    fore = Fore.GREEN
    match(fore_color):
        case 'red':
            fore = Fore.RED
        case 'yellow':
            fore = Fore.YELLOW
    print(fore+message)

def declare_action(action):
    print_fancy(action,'yellow')

target_folders = ["c","python"]

def find_files_recursively(directory_path):

    declare_action("Detecting files...")
    file_list = []
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            path = os.path.join(root,file)
            cf = [fo for fo in target_folders if path.startswith("./"+fo)]
            print_fancy(f"ALLOW {path}") if len(cf)>0 else print_fancy(f"REJECT {path}",'red')
            if len(cf)>0:
                file_list.append(path)
    return file_list

def create_file_tree_html(file_list):
    declare_action("Creating home page...")
    os.makedirs("./presentation/",exist_ok=True)
    f = open("./presentation/index.html",'w')
    link_list = [f"<a href='{os.path.splitext(file)[0]}.html'>{os.path.splitext(os.path.basename(file))[0]}</a>" for file in file_list]
    link_text = ""
    for link in link_list:
        link_text+=f"{link}<br>\n"
    f.write(f"<div class='links'>{link_text}</div>")

    f.close()

files = find_files_recursively(".")
create_file_tree_html(files)

