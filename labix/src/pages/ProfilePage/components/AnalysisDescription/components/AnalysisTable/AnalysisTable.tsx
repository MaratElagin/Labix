import React from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import {Grid2} from "@mui/material";

interface AnalysisTableProps {
    data: {
        analysis: Array<{
            Маркеры: string;
            Значение: number;
            Норма: string;
            'Ед.изм.': string;
            Отклонение: string | null;
        }>;
    } | null;
}

export const AnalysisTable: React.FC<AnalysisTableProps> = ({data}) => {
    if (!data) {
        return <div></div>;
    }

    return (
        <Grid2>
            <h4 style={{marginBottom: 0}}>
                Результаты анализа
            </h4>
            <TableContainer component={Paper}>
                <Table sx={{minWidth: 650}} aria-label="analysis table">
                    <TableHead>
                        <TableRow>
                            <TableCell sx={{fontWeight: 'bold', width: 150}}>Маркеры</TableCell>
                            <TableCell align="left" sx={{fontWeight: 'bold'}}>Значение</TableCell>
                            <TableCell align="left" sx={{fontWeight: 'bold'}}>Норма</TableCell>
                            <TableCell align="left" sx={{fontWeight: 'bold'}}>Ед.изм.</TableCell>
                            <TableCell align="left" sx={{fontWeight: 'bold'}}>Отклонение</TableCell>
                        </TableRow>
                    </TableHead>
                    <TableBody>
                        {data.analysis.map((row, index) => (
                            <TableRow
                                key={index}
                            >
                                <TableCell
                                    component="th"
                                    scope="row"
                                    sx={{
                                        whiteSpace: 'nowrap',
                                        overflow: 'hidden',
                                        textOverflow: 'ellipsis',
                                        maxWidth: 500,
                                    }}
                                    title={row.Маркеры}
                                >
                                    {row.Маркеры}
                                </TableCell>
                                <TableCell align="left">{row.Значение}</TableCell>
                                <TableCell align="left">{row.Норма}</TableCell>
                                <TableCell align="left">{row['Ед.изм.']}</TableCell>
                                <TableCell align="left">{row.Отклонение || 'Нет'}</TableCell>
                            </TableRow>
                        ))}
                    </TableBody>
                </Table>
            </TableContainer>
        </Grid2>
    );
};
