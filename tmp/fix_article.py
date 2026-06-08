import os
os.chdir('/home/almaz/StatSites/Astro/fastry')
with open('src/components/blog/ArticleHero.astro', 'r') as f:
    content = f.read()

# 1. Add locale
old1 = """} = Astro.props;

// Estimate reading time"""
new1 = """} = Astro.props;

const locale = getLocaleFromPath(Astro.url.pathname);

// Estimate reading time"""
content = content.replace(old1, new1)

# 2. Fix formatDate(publishedAt)
content = content.replace('{formatDate(publishedAt)}', '{formatDate(publishedAt, locale)}')

# 3. Fix formatDate(updatedAt)
content = content.replace('{formatDate(updatedAt)}', '{formatDate(updatedAt, locale)}')

# 4. Fix Updated prefix
old4 = 'Updated {formatDate(updatedAt, locale)}'
new4 = "{t('blog.updatedOn', locale, { date: formatDate(updatedAt, locale) })}"
content = content.replace(old4, new4)

# 5. Fix reading time
old5 = '{readingTime} min read'
new5 = "{t('blog.readingTime', locale, { minutes: readingTime })}"
content = content.replace(old5, new5)

with open('src/components/blog/ArticleHero.astro', 'w') as f:
    f.write(content)
print('Done')