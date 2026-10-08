// Frame capture for the how-to videos.
// Opens an HTML scene in headless Chrome, calls window.render(t) for each
// frame, and saves one PNG per frame. Time is stepped, not recorded, so
// every frame is exact.
//
// Usage: node cap.js <scene.html> <out-dir> <width> <height> [query]
//   Example: node cap.js v1.html out/frames-wide 1920 1080
//            node cap.js v1.html out/frames-square 1080 1080 '?sq'
// Env:   DUR          loop length in seconds (default 10)
//        FPS          frames per second (default 30)
//        CHROME_PATH  path to a Chrome or Chromium binary
//                     (default /usr/bin/google-chrome)
const path = require('path');
const { pathToFileURL } = require('url');
const { chromium } = require('playwright-core');

(async () => {
  const [, , file, outdir, w, h, q] = process.argv;
  const fps = +(process.env.FPS || 30);
  const D = +(process.env.DUR || 10);
  const b = await chromium.launch({
    executablePath: process.env.CHROME_PATH || '/usr/bin/google-chrome',
    args: ['--force-color-profile=srgb'],
  });
  const p = await b.newPage({ viewport: { width: +w, height: +h } });
  await p.goto(pathToFileURL(path.resolve(file)).href + (q || ''));
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(300);
  for (let i = 0; i < fps * D; i++) {
    await p.evaluate((t) => render(t), i / fps);
    await p.screenshot({ path: `${outdir}/f${String(i).padStart(4, '0')}.png` });
  }
  await b.close();
})();
