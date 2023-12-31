import os
import hashlib
import re
import shutil
import marko
import html
from colorama import init, Fore
import pythonbible as bible
import argparse

parser = argparse.ArgumentParser(description="Build static site")
parser.add_argument('--no-refresh',action='store_true',help='Disable frequent webpage refresh')
args = parser.parse_args()
refresh = not args.no_refresh

init(autoreset=True)

page_header = """
<header style='position:fixed;top:0;left:0;margin:0px;padding:4px;width:100%;background-color:darkgrey;color:black;z-index:9999;'>
    <div style='display:flex;align-items:center'>
        <div style='width:10px'></div>
        <a href='/'>
            <img src='/static/TeamLogo.png' height=40px>
        </a>
        <div style='width:20px'></div>
        <p style='line-height:1.2;color:#f4f4f4;font-size:1.0rem;font-weight:700'>CFBS NibbleSprouts Project</p>
    </div>
</header>
<div style='height:40px'></div>
"""
page_footer = """
<hr>
<footer style='padding:30px;font-size:0.7rem;color:darkgrey'>
Generated using ChickenFryBytes Studios' static site generator
</footer>
"""

start = f"""
<!DOCTYPE html><html lang='en'>
<head>
<meta charset='UTF-8'>
    <meta http-equiv='X-UA-Compatible' content='IE=edge'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    {'<meta http-equiv="refresh" content="3">' if refresh else ''}
    <title>Asynchronous Learning</title>
    <!-- <link rel='stylesheet' href='/static/katex/katex.min.css'> -->
    <link rel='stylesheet' href='/static/highlight/styles/base16/ros-pine.css'>
    <link rel='stylesheet' href='/static/style.css'>
</head>
<body>
{page_header}
<main>
"""
plain_end = f"""
</main>
{page_footer}
</body>
</html>
"""

def wrap_with_code_block_boilerplate(text,orig_file:str):
    extension = os.path.splitext(orig_file)[1]
    basename = os.path.basename(orig_file)
    dir = orig_file.removesuffix(f"/{basename}").removeprefix("./")
    hljs_lib = "c"
    match(extension):
        case '.py':
            hljs_lib = 'python'

    #print(f"Using hljs library: {hljs_lib}.min.js")
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

target_folders = ["content/"]

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
            # print_fancy(f"ALLOW {path}") if len(cf)>0 else print_fancy(f"REJECT {path}",'red')
            if len(cf)>0:
                file_list.append(path)
    return file_list

def get_readable_name(file_name:str):
    spaced_text = file_name.replace("_"," ")
    capitalized_text = ' '.join(word.capitalize() for word in spaced_text.split())
    return capitalized_text

def create_file_tree_html(file_list):
    # creating new list to use ./ instead of ./content/
    new_file_list = ["./"+file.removeprefix("./content/") for file in file_list]
    # print(new_file_list)
    declare_action("Creating home page...")
    os.makedirs("./presentation/",exist_ok=True)
    os.makedirs("./content/",exist_ok=True)
    shutil.copytree("./static/","./presentation/static/",dirs_exist_ok=True)
    f = open("./presentation/index.html",'w')
    lesson_link_list = [f"<a href='{os.path.splitext(file)[0]}.html'>{get_readable_name(os.path.splitext(os.path.basename(file))[0])}</a>" for file in new_file_list if str(file).endswith(".md")]
    snippet_link_list = [f"<a href='{os.path.splitext(file)[0]}.html'>{os.path.basename(file)}</a>" for file in new_file_list if str(file).endswith(".md")==False]

    f.write(start)
    f.write("<h1>Welcome Home</h1>")
    f.write("<p>This is where your journey begins. It is our hope that you will learn something valuable from this website. <em>Project NibbleSprouts</em> is an attempt to provide a scalable STEM education to students across the globe for free.</p>")
    f.write(f"<h2>Lessons ({len(lesson_link_list)})</h2>")
    f.write(f"<div class='links'><ul>")
    for link in lesson_link_list:
        f.write(f"<li>{link}</li>\n")
    f.write("</ul></div>")
    f.write(f"<h2>Code snippets ({len(snippet_link_list)})</h2>")
    f.write(f"<div class='links'><ul>");
    for link in snippet_link_list:
        f.write(f"<li>{link}</li>\n")
    f.write("</ul></div>")
    f.write(plain_end)
    f.close()
    for file in file_list:
        create_html_file(file)

def wrap_with_markdown_boilerplate(text,path):
    
    copy_functionality = r"""
    function copyToClipboard(id){
        var copyText = document.getElementById(id).innerText;
        navigator.clipboard.writeText(copyText).then(function(){
            console.log("Copied "+id+" to clipboard");        
        }).catch(function(error){
            console.log("Error copying "+id+" to clipboard; Error: "+error);        
        });
    }

    """

    end = f"""

<link rel="stylesheet" href="/static/katex/katex.min.css">
<script defer="" src="/static/katex/katex.min.js"></script>
<script defer="" src="/static/katex/contrib/auto-render.min.js" crossorigin="anonymous"
onload="
    renderMathInElement(
        document.body,
        {{
            delimiters: [
                {{left:'$$', right:'$$', display:true}},
                {{left:'$', right:'$', display:false}}
            ]
          }}
    );
"></script>
</main>
{page_footer}
<script>{copy_functionality}</script>
</body>
</html>
"""
    path_trimmed = path.removeprefix("./content/").removesuffix(".md").replace("/"," > ").replace("_"," ")
    path_display = f"<p style='darkgrey;opacity:0.5;font-size:0.6rem'>{path_trimmed}</p>"
    s = re.sub(r"\[.*?\]\((.*?.md)\)",to_html_link,text)
    s = marko.convert(s)
    cur_dir = os.path.dirname(path)

    result = re.sub(r"!\{\{(\S*)\}\}",lambda match:to_code_attachment(match,cur_dir+"/"),s)
    result = re.sub(r"!bible\{\{\s*(.*?)\s*\}\}",to_bible_verse,result)
    
    deps = re.finditer(r"!\{\{(\S*)\}\}",s)
    dep_string = ""
    for match in deps:
        dep = get_code_hljslib(os.path.splitext(os.path.basename(match.group(1)))[1])
        if dep in dep_string:
            continue
        dep_string+=dep
    # print(f"Adding dep string: {dep_string}")
    return start+path_display+result+dep_string+end

def to_html_link(match):
    prev_link:str = match.group(1)
    # print(f"Converting .md link to .html: {prev_link}")
    new_link = prev_link.removesuffix(".md")+".html"
    return match.group(0).replace(prev_link,new_link)

def to_bible_verse(match):
    text = match.group(1)
    refs = bible.get_references(text)
    compiled_text = ""

    if len(refs)==0:
        return "No Bible verse references found..."
    
    verse_ids = bible.convert_references_to_verse_ids(refs)
    for verse_id in verse_ids:
        vnum = bible.get_verse_number(verse_id)
        vtext = bible.get_verse_text(verse_id)
        compiled_text+=f"<blockquote><span style='font-size:0.7rem'>{vnum} </span>{vtext}</blockquote>"
    return f"<div style='border:2px solid purple;border-radius:10px;padding:20px'><p style='color:purple;padding-top:0;margin-top:0'>{text}</p>"+compiled_text+"</div>"

def to_code_attachment(match,cur_dir="some directory"):
    link = cur_dir+match.group(1).removeprefix("./")
    # return "<<"+match.group(1)+">>"
    if os.path.exists(link)==False:
        return f"<small style='color:red'>{link} not found...</small>"
    # return f"File found: {link}"
    return get_code_snippet(link)

def get_code_snippet(file_path:str):
    file = open(file_path,'r')
    content = file.read()
    file.close()
    file_id = os.path.basename(file_path)
    tag = f"""
<pre><code class='{get_code_class(file_path)}' id='{file_id}'>
{html.escape(content)}
</code></pre>
<strong style='color:darkgrey;margin-bottom:0;padding-bottom:0;font-size:0.7rem'>
    <a href='/{file_path.removeprefix("./content/").replace(os.path.splitext(file_path)[1],".html")}' target='_blank' style='width:18px;border:5px solid #007BFF;border-radius:5px;color:white;background-color:#007BFF;text-decoration:none'>&#8599; Open</a>
    <a href='#{file_id}' onclick='copyToClipboard("{file_id}")' style='width:18px;border:5px solid #007BFF;border-radius:5px;color:white;background-color:#007BFF;text-decoration:none'>&#128203; Copy</a>
</strong>
<strong style='color:darkgrey;margin-bottom:0;padding-bottom:0;font-size:0.7rem'>{file_path.removeprefix('./content/')} </strong>

"""
    return tag

def get_hash(input_string):
    return hashlib.sha256(input_string.encode()).hexdigest()

def get_code_class(file_path):
    extension = os.path.splitext(file_path)[1]
    hljs_lib = "c"
    match(extension):
        case '.py':
            hljs_lib = 'python'
    return hljs_lib


def get_code_hljslib(file_path):
    extension = os.path.splitext(file_path)[1]
    if extension=='.md':
        print("No need for highlight js...")
        return ""
    hljs_lib = "c"
    match(extension):
        case '.py':
            hljs_lib = 'python'
    dep = f"""
<script src='/static/highlight/highlight.min.js'></script>
<script src='/static/highlight/languages/{hljs_lib}.min.js'></script>
<script>
    hljs.highlightAll();
</script>
"""
    return dep

def create_html_file(file_path):
    base, ext = os.path.splitext(file_path)
    old_path = file_path
    new_path = os.path.splitext(file_path)[0]+".html"
    ext = os.path.splitext(file_path)[1]
    new_path = new_path.replace("./content/","./presentation/")
    # print_fancy(f"CREATE {new_path}")
    new_dir = os.path.dirname(new_path)
    # print(f"Creating directory: {new_dir}")
    os.makedirs(new_dir,exist_ok=True)
    
    with open(old_path,'r') as old_file:
        new_file = open(new_path,'w')
        match(ext):
            case '.md':
                new_file.write(wrap_with_markdown_boilerplate(old_file.read(),old_path))
            case _:
                new_file.write(wrap_with_code_block_boilerplate(old_file.read(),old_path))
        new_file.close()


files = find_files_recursively("./content/")
create_file_tree_html(files)
declare_action(f"Site generation finished ({'refresh' if refresh else 'no refresh'})")

