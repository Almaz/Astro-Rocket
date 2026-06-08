import os
os.chdir('/home/almaz/StatSites/Astro/fastry')
with open('src/pages/ru/index.astro', 'r') as f:
    content = f.read()
old = "project.id.replace(/\\.mdx?$/, '')"
new = "project.id.replace(/\\.mdx?$/, '').replace('ru/', '')"
content = content.replace(old, new)
with open('src/pages/ru/index.astro', 'w') as f:
    f.write(content)
print('Done')