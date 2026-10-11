// Publish only the self-contained book. Source artwork stays in the repository.
const fs = require('node:fs');
const path = require('node:path');
const root = path.resolve(__dirname, '..');
fs.mkdirSync(path.join(root, 'public'), { recursive: true });
fs.copyFileSync(path.join(root, 'index.html'), path.join(root, 'public', 'index.html'));
console.log('Prepared public/index.html for Vercel.');
