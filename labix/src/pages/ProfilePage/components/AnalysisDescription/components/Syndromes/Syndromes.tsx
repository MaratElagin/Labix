import React from 'react';
import TableContainer from "@mui/material/TableContainer";
import Table from "@mui/material/Table";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import TableCell from "@mui/material/TableCell";
import TableBody from "@mui/material/TableBody";
import Paper from "@mui/material/Paper";
import {IconButton, Tooltip} from "@mui/material";
import {ReactComponent as Icon} from '../../../../../../svg/info.svg';

interface SyndromesProps {
    syndromes: Array<{
        system: string;
        problems: Array<string>
    }>
}

export const Syndromes: React.FC<SyndromesProps> = ({syndromes}) => {
    return (
        <>
            <h4 style={{marginBottom: 0}}>
                Синдромы
            </h4>
            <TableContainer component={Paper} style={{marginBottom: '20px'}}>
                <Table>
                    <TableHead>
                        <TableRow>
                            <TableCell sx={{fontWeight: 'bold'}}>Система</TableCell>
                            <TableCell sx={{fontWeight: 'bold'}}>Проблемы</TableCell>
                            <TableCell sx={{ fontWeight: 'bold' }}>
                                Рекомендации
                                <Tooltip title="Эти рекомендации не являются окончательными, проконсультируйтесь с врачом.">
                                    <IconButton>
                                        <Icon className="icon"/>
                                    </IconButton>
                                </Tooltip>
                            </TableCell>
                        </TableRow>
                    </TableHead>
                    <TableBody>
                        {syndromes.map((syndrome, index) => (
                            <TableRow key={index}>
                                <TableCell>{syndrome.system}</TableCell>
                                <TableCell>
                                    {syndrome.problems.map((problem, i) => (
                                        <div key={i}>{problem}</div>
                                    ))}
                                </TableCell>
                                <TableCell>
                                    Сдать общий биохимический анализ крови
                                </TableCell>
                            </TableRow>
                        ))}
                    </TableBody>
                </Table>
            </TableContainer>
        </>
    );
}