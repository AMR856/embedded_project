import { FC } from 'react';

interface HeaderInterface{}

export const Header: FC<HeaderInterface> = () => {
  return (
    <div className="flex items-center gap-4 p-8 bg-secondary border-b border-border w-full h-16">
      {/* <img 
        src="../imgs/490-4900697_arduino-logo-black-and-white-ihs-markit-logo.png"
        className="h-12 w-12 rounded-full object-cover" 
      /> */}
    </div>
  );
};