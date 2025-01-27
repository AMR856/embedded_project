import { FC, useState } from "react";

interface InputFieldProps {
    label?: string; // Label to display above the input
    placeholder?: string;
    onChange?: (value: string) => void;
}

export const InputField: FC<InputFieldProps> = ({
    label = "Label",
    placeholder = "Enter text",
    onChange,
}) => {
    const [inputValue, setInputValue] = useState<string>("");

    const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        const value = e.target.value;
        setInputValue(value);
        if (onChange) onChange(value); // Pass the value to the parent if `onChange` is provided
    };

    return (
        <div className="flex flex-col items-start gap-2 p-4">
            <label className="text-sm font-medium text-gray-700">{label}</label>
            <input
                type="text"
                value={inputValue}
                onChange={handleChange}
                placeholder={placeholder}
                className="px-4 py-2 w-full border border-gray-300 rounded-md focus:outline-none focus:ring focus:ring-blue-300"
            />
        </div>
    );
};
