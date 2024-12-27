import { FC } from 'react';
import { Button } from './ui/button';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from './ui/select';
import { Play, Upload } from 'lucide-react';

interface ToolbarProps {
  onVerify: () => void;
  onUpload: () => void;
  selectedBoard: string;
  onBoardChange: (value: string) => void;
  selectedPort: string;
  onPortChange: (value: string) => void;
}

export const Toolbar: FC<ToolbarProps> = ({
  onVerify,
  onUpload,
  selectedBoard,
  onBoardChange,
  selectedPort,
  onPortChange,
}) => {
  return (
    <div className="flex items-center gap-4 p-4 bg-secondary border-b border-border">
      <Button onClick={onVerify} variant="default" className="flex items-center gap-2">
        <Play className="w-4 h-4" />
        Verify
      </Button>
      <Button onClick={onUpload} variant="default" className="flex items-center gap-2">
        <Upload className="w-4 h-4" />
        Upload
      </Button>
      <Select value={selectedBoard} onValueChange={onBoardChange}>
        <SelectTrigger className="w-[200px]">
          <SelectValue placeholder="Select Board" />
        </SelectTrigger>
        <SelectContent>
          <SelectItem value="uno">Arduino Uno</SelectItem>
          <SelectItem value="mega">Arduino Mega</SelectItem>
          <SelectItem value="nano">Arduino Nano</SelectItem>
          <SelectItem value="leonardo">Arduino Leonardo</SelectItem>
        </SelectContent>
      </Select>
      <Select value={selectedPort} onValueChange={onPortChange}>
        <SelectTrigger className="w-[200px]">
          <SelectValue placeholder="Select Port" />
        </SelectTrigger>
        <SelectContent>
          <SelectItem value="COM1">COM1</SelectItem>
          <SelectItem value="COM2">COM2</SelectItem>
          <SelectItem value="COM3">COM3</SelectItem>
          <SelectItem value="COM4">COM4</SelectItem>
          <SelectItem value="COM5">COM5</SelectItem>
          <SelectItem value="/dev/ttyUSB0">/dev/ttyUSB0</SelectItem>
          <SelectItem value="/dev/ttyUSB1">/dev/ttyUSB1</SelectItem>
        </SelectContent>
      </Select>
    </div>
  );
}