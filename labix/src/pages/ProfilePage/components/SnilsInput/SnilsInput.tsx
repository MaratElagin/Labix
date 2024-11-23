import React from 'react';
import TextField from '@mui/material/TextField';

interface SnilsInputProps {
    snils: string;
    onChange: (formattedSnils: string) => void;
}

export const SnilsInput: React.FC<SnilsInputProps> = ({snils, onChange}) => {
    const formatSnils = (value: string): string => {
        const digits = value.replace(/\D/g, '');

        return digits
            .replace(/^(\d{3})(\d)/, '$1-$2')
            .replace(/^(\d{3})-(\d{3})(\d)/, '$1-$2-$3')
            .replace(/^(\d{3})-(\d{3})-(\d{3})(\d)/, '$1-$2-$3 $4');
    };

    const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        const value = e.target.value;
        onChange(formatSnils(value));
    };

    return (
        <TextField
            label="СНИЛС"
            variant="outlined"
            value={snils}
            onChange={handleChange}
            inputProps={{maxLength: 14}}
            placeholder="126-029-036 24"
            margin="normal"
        />
    );
};