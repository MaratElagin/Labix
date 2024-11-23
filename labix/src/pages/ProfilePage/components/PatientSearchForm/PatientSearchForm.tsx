import React, {useState} from 'react';
import axios from 'axios';
import {Grid2} from "@mui/material";
import {SnilsInput} from "../SnilsInput";
import {DecryptButton} from "../Button";

interface PatientSearchFormProps {
    onReceiveData: (data: any) => void;
}

export const PatientSearchForm: React.FC<PatientSearchFormProps> = ({onReceiveData}) => {
    const [snils, setSnils] = useState<string>('');

    const handleSnilsChange = (formattedSnils: string) => {
        setSnils(formattedSnils);
    };

    const handleDecryptResponse = async () => {
        try {
            const numericSnils = snils.replace(/\D/g, '');
            const response = await axios.get(`/get-patient-data/${numericSnils}`);
            onReceiveData(response.data);
        } catch (error) {
            console.error('Ошибка при получении данных:', error);
        }
    };

    return (
        <Grid2 container justifyContent="center" alignItems="center" direction="column" spacing="XS">
            <Grid2>
                <SnilsInput snils={snils} onChange={handleSnilsChange}/>
            </Grid2>
            <Grid2>
                <DecryptButton snils={snils} onDecrypt={handleDecryptResponse}/>
            </Grid2>
        </Grid2>
    );
};
