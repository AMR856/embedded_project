import { useState } from 'react';
import { Editor } from './components/Editor';
import { Toolbar } from './components/Toolbar';
import { StatusBar } from './components/StatusBar';
import axios from 'axios';

const DEFAULT_SKETCH = `void setup() {
  // put your setup code here, to run once:
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(LED_BUILTIN, HIGH);
  delay(1000);
  digitalWrite(LED_BUILTIN, LOW);
  delay(1000);
}`;

function App() {
  const [code, setCode] = useState(DEFAULT_SKETCH);
  const [selectedBoard, setSelectedBoard] = useState('uno');
  const [selectedPort, setSelectedPort] = useState('COM1');
  const [status, setStatus] = useState('Ready');

const handleVerify = () => {
    setStatus('Verfiying...');
    axios.post('http://127.0.0.1:3000/verfiy', {
        code: code,
        board: selectedBoard
    })
    .then(response => {
        console.log(response.data);
        setStatus('Verfiying was successful');
        setTimeout(() => setStatus('Ready'), 2000);
    })
    .catch(error => {
        console.error(error);
    });
};

const handleUpload = () => {
    setStatus('Uploading...');
    axios.post('http://127.0.0.1:3000/upload', {
        code: code,
        board: selectedBoard,
        port: selectedPort
    })
    .then(response => {
        console.log(response.data);
        setStatus('Uploading was successful');
        setTimeout(() => setStatus('Ready'), 2000);
    })
    .catch(error => {
        console.error(error);
    });
};

return (
    <div className="flex flex-col h-screen bg-background text-foreground">
    <Toolbar
        onVerify={handleVerify}
        onUpload={handleUpload}
        selectedBoard={selectedBoard}
        onBoardChange={setSelectedBoard}
        selectedPort={selectedPort}
        onPortChange={setSelectedPort}
    />
      <div className="flex-1 overflow-hidden">
        <Editor value={code} onChange={(value) => setCode(value || '')} />
      
      </div>
      <StatusBar
        status={status}
        boardInfo={`Board: Arduino ${selectedBoard.charAt(0).toUpperCase() + selectedBoard.slice(1)}`}
        portInfo={`Port: ${selectedPort}`}
      />
    </div>
  );
}

export default App;