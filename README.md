# Owl In Tech

Tech reviews, guides, and tips. Built with [Hugo](https://gohugo.io/) and [PaperMod](https://github.com/adityatelange/hugo-PaperMod), deployed on [GitHub Pages](https://pages.github.com/).

**Live at [owlintech.com](https://owlintech.com)**

## Writing a new post

```bash
# Create a new post
hugo new content posts/my-new-post.md
```

Edit the file — fill in the front matter and write your content in markdown:

```markdown
---
title: "My New Post"
date: 2026-04-15T12:00:00+00:00
draft: false
summary: "A short description for the post list"
cover:
  image: "/content/images/my-image.jpg"
  alt: "My New Post"
  relative: false
---

Your content here in markdown.
```

### Embedding YouTube videos

```markdown
{{< youtube VIDEO_ID >}}
```

### Adding images

Drop image files into `static/content/images/`, then reference them in your post:

```markdown
![alt text](/content/images/my-image.jpg)
```

### Cover images

Cover images should be **1200×630px** (1.91:1 ratio). This looks great on the blog and is the standard Open Graph size for social media previews. Preferred format is **WebP** or PNG — keep file size under 200KB.

## Local preview

```bash
hugo server
```

Open [http://localhost:1313](http://localhost:1313) to preview.

## Publishing

```bash
git add -A
git commit -m "New post: My New Post"
git push
```

GitHub Actions builds the site and deploys to GitHub Pages automatically. The site updates in ~30 seconds.

## Updating Hugo

Hugo is pinned to a specific version in `.github/workflows/deploy.yml`. To upgrade:

1. Install the new version locally: `brew upgrade hugo`
2. Test the build: `hugo server`
3. Update the version in `.github/workflows/deploy.yml`
4. Commit and push
