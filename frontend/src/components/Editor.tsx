import { Editor as MonacoEditor } from '@monaco-editor/react';
import { FC } from 'react';

interface EditorProps {
  value: string;
  onChange: (value: string | undefined) => void;
}

export const Editor: FC<EditorProps> = ({ value, onChange }) => {
  return (
    <MonacoEditor
      height="70vh"
      defaultLanguage="cpp"
      theme="dark" // Changed to light theme
      value={value}
      onChange={onChange}
      options={{
        minimap: { enabled: false },
        fontSize: 14,
        wordWrap: 'on',
        automaticLayout: true,
        fontFamily: "'Monaco', 'Menlo', 'Ubuntu Mono', 'Consolas', 'source-code-pro', monospace",
      }}
    />
  );
}