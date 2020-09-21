import os
import re

from django_sass import compile_sass, find_static_paths, find_static_scss
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

for file in find_static_scss():
    matches = re.search(r"((_\w*\.scss)$)", file)
    if matches:
        continue
    
    compile_sass(
        inpath=file,             
        outpath=file.replace('scss', 'css'),
        output_style="compressed",
        precision=8,
        source_map=True
    )
    

