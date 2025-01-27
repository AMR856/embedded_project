import { FC, useEffect, useState } from "react";
import {
    Select,
    SelectContent,
    SelectItem,
    SelectTrigger,
    SelectValue,
} from "./ui/select";
import axios from "axios";

interface SelectProgramInterface {
    selectedProgram: string;
    onProgramChange : (value: string) => void;
}

export const SelectProgram: FC<SelectProgramInterface> = ({
    selectedProgram,
    onProgramChange
}) => {
    const [programs, setPrograms] = useState<string[]>([]);
    const [loading, setLoading] = useState<boolean>(true);

    useEffect(() => {
        axios
            .get("http://127.0.0.1:3000/all-codes")
            .then((response) => {
                setPrograms(response.data);
                setTimeout(() => setLoading(false), 2000);
            })
            .catch((error) => {
                console.error(error);
                setLoading(false);
            });
    }, []);

    return (
        <div className="flex items-center gap-4 p-4 bg-secondary border-b border-border">
            {loading ? (
                <div>Loading programs...</div>
            ) : (
                <Select value={selectedProgram} onValueChange={onProgramChange}>
                    <SelectTrigger className="w-[200px]">
                        <SelectValue placeholder="Select Program" />
                    </SelectTrigger>
                    <SelectContent>
                        {programs.map((program) => (
                            <SelectItem key={program} value={program}>
                                {program}
                            </SelectItem>
                        ))}
                    </SelectContent>
                </Select>
            )}
        </div>
    );
};
// arduino-cli compile --fqbn <FQBN> --build-path <output_directory> <path_to_sketch>
// arduino-cli compile --fqbn arduino:avr:uno --build-path hex_files sample_code
