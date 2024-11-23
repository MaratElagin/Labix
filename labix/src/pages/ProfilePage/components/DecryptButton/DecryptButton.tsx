import React from 'react';
import Button from '@mui/material/Button';
import axios from 'axios';

interface DecryptButtonProps {
    snils: string;
    onReceiveData: (data: any) => void;
}

export const DecryptButton: React.FC<DecryptButtonProps> = ({snils, onReceiveData}) => {
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
        <Button
            variant="contained"
            color="primary"
            onClick={handleDecryptResponse}
            disabled={!snils.match(/^\d{3}-\d{3}-\d{3} \d{2}$/)}
        >
            Расшифровать
        </Button>
    );
};
