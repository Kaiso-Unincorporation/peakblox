const express = require('express');
const path = require('path');
const app = express();
const port = 3000;

app.use(express.static(__dirname));

app.get('/api/games', (req, res) => {
  res.json([
    { id: 1, name: 'Natural Disaster Survival', desc: 'Classic survival chaos' },
    { id: 2, name: 'Boombox Hangout', desc: 'Music and chill' },
    { id: 3, name: 'Ragdoll Engine', desc: 'Physics fun' }
  ]);
});

app.get('/download/launcher', (req, res) => {
  res.download(path.join(__dirname, 'launcher/PeakBlox.exe'));
});

app.listen(port, () => {
  console.log(`🚀 PeakBlox server running at http://localhost:${port}`);
  console.log('Open index.html or the server for full experience.');
});