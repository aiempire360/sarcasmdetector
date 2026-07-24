import React, { useState } from 'react';
import './App.css';

function App() {
  const [text, setText] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!text.trim()) return;

    setLoading(true);
    try {
      const response = await fetch('http://127.0.0.1:8000/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text }),
      });

      const data = await response.json();
      setResult(data);
    } catch (error) {
      alert('Unable to connect backend. Backend is running?');
    }
    setLoading(false);
  };

  return (
    <div className="App">
      <h1>🕵️ Sarcasm Detector</h1>
      <p>Type your message and check how sarcastic it is!</p>

      <form onSubmit={handleSubmit}>
        <textarea
          value={text}
          onChange={(e) => setText(e.target.value)}
          placeholder="Type message here..."
          rows="5"
        />
        <button type="submit" disabled={loading}>
          {loading ? 'Checking...' : '🔍 Detect Sarcasm'}
        </button>
      </form>

      {result && (
        <div className={`result ${result.label === 1 ? 'sarcastic' : 'normal'}`}>
          <h2>Result: {result.prediction}</h2>
          <p><strong>Message:</strong> "{result.text}"</p>
          {result.error && <p style={{color: 'red'}}>{result.error}</p>}
        </div>
      )}
    </div>
  );
}

export default App;