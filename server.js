const express = require('express');
const bodyParser = require('body-parser');
const { PythonShell } = require('python-shell');
const Pusher = require('pusher');

// Initialize Express
const app = express();
app.use(bodyParser.json());

// Initialize Pusher
const pusher = new Pusher({
  appId: 'YOUR_APP_ID',
  key: 'YOUR_APP_KEY',
  secret: 'YOUR_APP_SECRET',
  cluster: 'YOUR_APP_CLUSTER',
  useTLS: true
});

// Endpoint to classify messages
app.post('/classify', (req, res) => {
  const message = req.body.message;

  PythonShell.run('classify_message.py', { args: [message] }, (err, results) => {
    if (err) {
      res.status(500).send(err);
    } else {
      const isSpam = results[0].trim() === '1';
      pusher.trigger('messages', 'new-message', {
        message,
        spam: isSpam
      });
      res.json({ spam: isSpam });
    }
  });
});

app.listen(3001, () => {
  console.log('Server is running on port 3001');
});
