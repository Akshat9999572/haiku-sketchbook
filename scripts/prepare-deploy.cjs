// Publish the lightweight web edition and optimized artwork.
const fs = require('node:fs');
const path = require('node:path');
const root = path.resolve(__dirname, '..');
fs.mkdirSync(path.join(root, 'public'), { recursive: true });
fs.copyFileSync(path.join(root, 'web.html'), path.join(root, 'public', 'index.html'));
fs.mkdirSync(path.join(root, 'public', 'assets'), { recursive: true });
for (const name of fs.readdirSync(path.join(root, 'assets', 'web'))) {
  if (name.endsWith('.webp')) fs.copyFileSync(path.join(root, 'assets', 'web', name), path.join(root, 'public', 'assets', name));
}
console.log('Prepared mobile-friendly web edition for Vercel.');
