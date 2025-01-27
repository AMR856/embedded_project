import { useState } from "react";
import { Header } from "./components/Header";
import { StatusBar } from "./components/StatusBar";
import { CenteredButton } from "./components/CenteredButton";
import { SelectProgram } from "./components/SelectProgram";
import { InputField } from "./components/InputField";
import axios from "axios";

function App() {
    const [status, setStatus] = useState("Ready");
    const [selectedProgram, setProgram] = useState("Nothing");
    const [email, setEmail] = useState('amer.live477@gmail.com');
    const [username, setUsername] = useState('AmrAlnas');

    const handleEmailChange = (value: string) => {
        setEmail(value);
    };
    const handleUsernameChange = (value: string) => {
        setUsername(value);
    };

    const handleProgramChange = (value: string) => {
        setProgram(value);
    };
    
    const handleProgram = () => {
        setStatus("Uploading...");
        axios
            .post("http://127.0.0.1:3000/program", {
                email: email,
                username: username,
                filename: selectedProgram
            })
            .then((response) => {
                console.log(response.data);
                setStatus("Uploading was completed");
                setTimeout(() => setStatus("Ready"), 2000);
            })
            .catch((error) => {
                console.error(error);
            });
    };

    return (
        <div className="flex flex-col h-screen bg-background text-foreground">
            <Header />
            <SelectProgram selectedProgram={selectedProgram} onProgramChange={handleProgramChange} />
            <InputField onChange={handleEmailChange} label="Email" placeholder="Enter your email"/>
            <InputField onChange={handleUsernameChange} label="Username" placeholder="Enter your password"/>
            <CenteredButton onProgram={handleProgram}/>
            <StatusBar status={status} />
        </div>
    );
}

export default App;
