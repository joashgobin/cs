import os
import shutil
import marko
import html
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
    shutil.copytree("./static/","./presentation/static/",dirs_exist_ok=True)
    f = open("./presentation/index.html",'w')
    link_list = [f"<a href='{os.path.splitext(file)[0]}.html'>{os.path.splitext(os.path.basename(file))[0]}</a>" for file in file_list]
    link_text = ""
    for link in link_list:
        link_text+=f"{link}<br>\n"
    f.write(f"<div class='links'>{link_text}</div>")

    f.close()
    for file in file_list:
        create_html_file(file)

def wrap_with_markdown_boilerplate(text):
    
    start = f"""
<!DOCTYPE html><html lang='en'>
<head>
<meta charset='UTF-8'>
    <meta http-equiv='X-UA-Compatible' content='IE=edge'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Asynchronous Learning</title>
    <!-- <link rel='stylesheet' href='/static/katex/katex.min.css'> -->
    <link rel='stylesheet' href='/static/style.css'>
</head>
<body> 
"""
    end = f"""

<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.10.1/dist/katex.min.css" integrity="sha384-dbVIfZGuN1Yq7/1Ocstc1lUEm+AT+/rCkibIcC/OmWo5f0EA48Vf8CytHzGrSwbQ" crossorigin="anonymous">
<script defer="" src="https://cdn.jsdelivr.net/npm/katex@0.10.1/dist/katex.min.js" integrity="sha384-2BKqo+exmr9su6dir+qCw08N2ZKRucY4PrGQPPWU1A7FtlCGjmEGFqXCv5nyM5Ij" crossorigin="anonymous"></script>
<script defer="" src="https://cdn.jsdelivr.net/npm/katex@0.10.1/dist/contrib/auto-render.min.js" integrity="sha384-kWPLUVMOks5AQFrykwIup5lo0m3iMkkHrD0uJ4H5cjeGihAutqP0yW0J6dpFiVkI" crossorigin="anonymous" onload="renderMathInElement(document.body);"></script>
</body>
</html>
"""
    return start+marko.convert(text)+end

def wrap_with_code_block_boilerplate(text,orig_file:str):
    extension = os.path.splitext(orig_file)[1]
    basename = os.path.basename(orig_file)
    dir = orig_file.removesuffix(f"/{basename}").removeprefix("./")
    hljs_lib = "c"
    match(extension):
        case '.py':
            hljs_lib = 'python'

    print(f"Using hljs library: {hljs_lib}.min.js")
    start = f"""
<!DOCTYPE html><html lang='en'>
<head>
<meta charset='UTF-8'>
    <meta http-equiv='X-UA-Compatible' content='IE=edge'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Code Snippets</title>
    <link rel='stylesheet' href='/static/highlight/styles/base16/ros-pine.css'>
</head>
<body style='background-color:black'>
<small style='color:darkgray'>{dir}</small>
<h2 style='color:orange'>{basename}</h2>
<pre>
<code class='{hljs_lib}'>
"""
    end = f"""

</code>
</pre>
<script src='/static/highlight/highlight.min.js'></script>
<script src='/static/highlight/languages/{hljs_lib}.min.js'></script>
<script>
    hljs.highlightAll();
</script>
</body>
</html>
"""
    return start+html.escape(text)+end

def create_html_file(file_path):
    base, ext = os.path.splitext(file_path)
    old_path = file_path
    new_path = os.path.splitext(file_path)[0]+".html"
    ext = os.path.splitext(file_path)[1]
    new_path = new_path.replace("./","./presentation/")
    print_fancy(f"CREATE {new_path}")
    new_dir = os.path.dirname(new_path)
    print(f"Creating directory: {new_dir}")
    os.makedirs(new_dir,exist_ok=True)
    
    with open(old_path,'r') as old_file:
        new_file = open(new_path,'w')
        match(ext):
            case '.md':
                new_file.write(wrap_with_markdown_boilerplate(old_file.read()))
            case _:
                new_file.write(wrap_with_code_block_boilerplate(old_file.read(),old_path))
        new_file.close()


files = find_files_recursively()
create_file_tree_html(files)

