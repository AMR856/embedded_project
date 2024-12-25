import { FC } from 'react';

interface StatusBarProps {
  status: string;
  boardInfo: string;
  portInfo: string;
}

export const StatusBar: FC<StatusBarProps> = ({ status, boardInfo, portInfo }) => {
  return (
    <div className="flex items-center gap-4 px-4 py-2 text-sm bg-secondary text-foreground border-t border-border">
      <div>{status}</div>
      <div className="flex-1" />
      <div>{boardInfo}</div>
      <div>{portInfo}</div>
    </div>
  );
}