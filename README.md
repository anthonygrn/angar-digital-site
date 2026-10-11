# angardigital.com

Website of Angar Digital LLC. Plain static HTML/CSS, no build step, hosted on GitHub Pages at https://angardigital.com.

## Structure

| File | Page / role |
| --- | --- |
| `index.html` | Home (What we do, Our apps, Contact) |
| `privacy/index.html` | Privacy Policy → https://angardigital.com/privacy/ |
| `terms/index.html` | Terms of Use → https://angardigital.com/terms/ |
| `404.html` | Not found page |
| `assets/css/style.css` | All styles (colors are variables at the top, light and dark) |
| `assets/js/site.js` | Light/dark toggle |
| `sitemap.xml`, `robots.txt` | SEO |
| `CNAME` | Custom domain for GitHub Pages — do not delete |
| `tools/generate_images.py` | Regenerates favicon, icons and `og-image.png` |

The header and footer are repeated in each HTML page: if you change them, change them in all four pages.

## Edit the site

1. Edit the HTML files in any text editor.
2. Preview locally:
   ```bash
   python3 -m http.server 8000
   ```
   then open http://localhost:8000.
3. When you change a legal page, update its “Last updated” date and the `<lastmod>` in `sitemap.xml`.
4. To regenerate the images (after changing the colors or the tagline): `python3 tools/generate_images.py` (needs `pip install Pillow`).

## Publish

```bash
git add -A
git commit -m "Describe the change"
git push
```

GitHub Pages republishes automatically from the `main` branch in about a minute.

## Fonts

Fraunces and Hanken Grotesk, from Google Fonts, under the SIL Open Font License. They are self-hosted in `assets/fonts/`, so the site makes no request to third-party servers.
