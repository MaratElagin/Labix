import React, {useState} from 'react';
import {Grid2} from "@mui/material";
import {SnilsInput} from "../SnilsInput";
import {DecryptButton} from "../DecryptButton";

interface PatientSearchFormProps {
    onReceiveData: (data: any) => void;
}

export const PatientSearchForm: React.FC<PatientSearchFormProps> = ({onReceiveData}) => {
    const [snils, setSnils] = useState<string>('');

    const handleSnilsChange = (formattedSnils: string) => {
        setSnils(formattedSnils);
    };

    return (
        <Grid2 container justifyContent="center" alignItems="center" direction="column" spacing="XS">
            <Grid2>
                <SnilsInput snils={snils} onChange={handleSnilsChange}/>
            </Grid2>
            <Grid2>
                <DecryptButton snils={snils} onReceiveData={onReceiveData}/>
            </Grid2>
        </Grid2>
    );
};
