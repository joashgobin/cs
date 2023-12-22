import os
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

target_folders = ["c/","python/"]

def find_files_recursively(directory_path="."):

    declare_action("Detecting files...")
    file_list = []
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            path = os.path.join(root,file)
            if ".mypy_cache" in path:
                continue
            if "__pycache__" in path:
                continue
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
    for file in file_list:
        create_html_file(file)

def wrap_with_html_boilerplate(text):
    start = """<!DOCTYPE html>
    <html lang='en'>
    <head>
        <meta charset='UTF-8'>
        <meta http-equiv='X-UA-Compatible' content='IE=edge'>
        <meta name='viewport' content='width=device-width, initial-scale=1.0'>
        <title>Code tree generator</title>
        <link rel='stylesheet' href='/highlight/styles/default.min.css'>
    </head>
    <body>
    <pre><code>
    """
    end = """
    </code></pre>
    <script src='/highlight/highlight.min.js'></script>
    <script>
        hljs.highlightAll();
    </script>
    </body>
    </html>
    """
    return start+text+end

def create_html_file(file_path):
    old_path = file_path
    new_path = os.path.splitext(file_path)[0]+".html"
    new_path = new_path.replace("./","./presentation/")
    print_fancy(f"CREATE {new_path}")
    new_dir = os.path.dirname(new_path)
    print(f"Creating directory: {new_dir}")
    os.makedirs(new_dir,exist_ok=True)
    
    with open(old_path,'r') as old_file:
        new_file = open(new_path,'w')
        new_file.write(wrap_with_html_boilerplate(old_file.read()))
        new_file.close()


files = find_files_recursively()
create_file_tree_html(files)

