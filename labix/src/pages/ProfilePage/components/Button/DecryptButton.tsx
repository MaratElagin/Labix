import React from 'react';
import Button from '@mui/material/Button';
import axios from 'axios';

interface DecryptButtonProps {
    snils: string;
    onDecrypt: (description: string) => void;
}

export const DecryptButton: React.FC<DecryptButtonProps> = ({ snils, onDecrypt }) => {
    const handleDecrypt = async () => {
        try {
            const response = await axios.get(`/get-analysis-description/${snils}`);
            onDecrypt(response.data.description);
        } catch (error) {
            console.error('Ошибка при расшифровке СНИЛС:', error);
        }
    };

    return (
        <Button
            variant="contained"
            color="primary"
            onClick={handleDecrypt}
            disabled={!snils.match(/^\d{3}-\d{3}-\d{3} \d{2}$/)}
        >
            Расшифровать
        </Button>
    );
};
