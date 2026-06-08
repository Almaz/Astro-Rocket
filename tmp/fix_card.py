import os
os.chdir('/home/almaz/StatSites/Astro/fastry')
with open('src/components/blog/BlogCard.astro', 'r') as f:
    content = f.read()

# Add imports
old_imports = """import { Image } from 'astro:assets';
import type { ImageMetadata } from 'astro';
import { formatDate } from '@/lib/utils';"""
new_imports = """import { Image } from 'astro:assets';
import type { ImageMetadata } from 'astro';
import { formatDate } from '@/lib/utils';
import { t, getLocaleFromPath } from '@/i18n';"""
content = content.replace(old_imports, new_imports)

# Add locale after Astro.props destructuring
old_props = """} = Astro.props;

// Estimate reading time"""
new_props = """} = Astro.props;

const locale = getLocaleFromPath(Astro.url.pathname);

// Estimate reading time"""
content = content.replace(old_props, new_props)

# Fix formatDate(publishedAt) to pass locale
content = content.replace('{formatDate(publishedAt)}', '{formatDate(publishedAt, locale)}')

# Fix reading time
old_rt = '{readingTime} min read'
new_rt = "{t('blog.readingTime', locale, { minutes: readingTime })}"
content = content.replace(old_rt, new_rt)

with open('src/components/blog/BlogCard.astro', 'w') as f:
    f.write(content)
print('Done')