import React, {useState} from 'react';
import axios from 'axios';
import MockAdapter from 'axios-mock-adapter';
import {SnilsInput} from "../SnilsInput";
import {DecryptButton} from "../Button";
import {Grid2} from "@mui/material";

const mock = new MockAdapter(axios);

// Мокаем ответ для тестирования
mock.onGet(/get-analysis-description\/\d{3}-\d{3}-\d{3} \d{2}/).reply(200, {
    description: 'Пример расшифровки СНИЛС'
});

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
            const response = await axios.get(`/get-analysis-description/${snils}`);
            onReceiveData(response.data); // Передаем данные в родительский компонент
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