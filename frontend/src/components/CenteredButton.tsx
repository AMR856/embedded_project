import { FC } from 'react';
import { Button } from '@/components/ui/button'; // Adjust import based on your setup

interface CenteredButtonInterface {
  onProgram: () => void;
}

export const CenteredButton: FC<CenteredButtonInterface> = ({
  onProgram,
}) => {
  return (
    <div className="flex items-center justify-center max-h-screen white">
      <Button
        onClick={onProgram}
        variant="default"
        className="px-4 py-2 text-sm"
      >
        Program
      </Button>
    </div>
  );
};
