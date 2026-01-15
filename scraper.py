import re
import os
from pathlib import Path
import sys
import subprocess


def main():
    downloader(os.getcwd())

    # print(f"Successfully wrote{count} files")


def downloader(directory):
    count = 0
    trinkets = search_files(directory)
    for trinket in trinkets:
        # if count > 2:
        #     sys.exit()
        # else:
        #     print(trinket)
        ids = extract_trinket_ids(trinket)
        if not ids:
            continue
        # else:
        #     print(ids)
        for index, id in enumerate(ids):
            try:
                url = f"https://trinket.io/python/{id}"
                print(f"  Downloading: {url}")
                # response = requests.get(url)
                filename = sanitize_filename(trinket)
                if index > 0:
                    file = f"{filename}_{index}.py"
                else:
                    file = f"{filename}.py"
                path = f"{os.getcwd()}/sketches"
                filepath = os.path.join(path, file)
                
                subprocess.run(["curl", f"https://trinket.io/python/{id}/", "-o", filepath])
                print(f"Saved {filepath}")
                replacement(file, id, trinket)
                result = clean_script(file)
        #         # if result:
        #         #     count += 1
                count += 1
            except Exception as e:
                print(f"  Unexpected error for {id}: {e}")
                return None



def search_files(directory):
    path = Path(directory)
    return list(path.rglob("*.html"))

def extract_trinket_ids(html_file):
        """Extract Trinket IDs from HTML file"""
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Find trinket iframe URLs
            # Patterns to match:
            # https://trinket.io/embed/python3/TRINKET_ID
            pattern = r'trinket\.io/embed/python3?/([a-zA-Z0-9]+)'
            matches = re.findall(pattern, content)
            
            if matches:
                print(f"Found {len(matches)} Trinket(s) in: {html_file.name}")
                return matches
            return []
            
        except Exception as e:
            print(f"Error reading {html_file}: {e}")
            return []

def sanitize_filename(filename):
        """Create a safe filename from HTML filename"""
        # Remove .html extension and path
        name = Path(filename).stem
        # Replace spaces and special chars with underscores
        name = re.sub(r'[^\w\-]', '_', name)
        # Remove multiple underscores
        name = re.sub(r'_+', '_', name)
        return name.lower()

def replacement(file, id, html_file):
    # print("entered replacement function")
    pattern = r'https://trinket\.io/embed/python3?/([a-zA-Z0-9]+)'
    # original = f"https://trinket.io/embed/python/{id}"
    original = rf'https://trinket\.io/embed/python3?/{re.escape(id)}'
    script_replacement = f'../python-widget.html?src=../sketches/{file}'
    # print(file)
    # print(id)
    # print(html_file)
    
    try:
        with open(html_file, 'r', encoding='utf-8') as input:
            # content = input.read()
            content = input.readlines()
        
        # content.replace(original, script_replacement)
        # print(content)
        modified_content = []
        for line in content:
            # if re.search(pattern, line):
            #     print(f"pattern found for {id}")
            if re.search(original, line):
                new_line = re.sub(original, script_replacement, line)
                modified_content.append(new_line)
            else:
                modified_content.append(line)
        
        # print(modified_content)
        #     new_line = line.replace(original, script_replacement)
        #     if line != new_line:
        #         print(new_line)
        #     modified_content.append(new_line)
        
        with open(html_file, "w") as new:
            for line in modified_content:
                new.write(line)

        # with open(html_file, "w") as new:
        #     new.write(content)
        
    except Exception as e:
        print(f"Error reading {html_file}: {e}")
        return
    
def clean_script(file):
    filepath = r"sketches"
    directory = os.listdir(filepath)

    lines = []
    try:
        with open(os.path.join(filepath,file), "r") as input:
            lines = input.readlines()
            line_count = len(lines)
            print(line_count)
    except Exception as e:
        print(e)
        return False

    if not lines:
        print(f"did not output {file}")
        return False


    new_lines = []
    for line in lines:
        print(line)
        if line.strip() == "from processing import *":
            print("skipped import")
            continue
        elif line.strip() == "run()":
            print("breaking at run")
            break
        else:
            print(line)
            new_lines.append(line)

    index = 0
    for line in new_lines:
        if line == "" or line == "\n":
            index += 1
        else:
            break

    output = new_lines[index:]
    # print(output)
    new_directory = r"new_sketches"
    try:
        with open(file, "w") as f:
            f.writelines(output)
    except Exception as e:
        print(e)
        return False
    print(f"Wrote {file}")
    return True



if __name__ == "__main__":
    main()