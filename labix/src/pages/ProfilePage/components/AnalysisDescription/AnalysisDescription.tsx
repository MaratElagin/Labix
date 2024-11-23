import React, {useState} from 'react';
import {Grid2} from "@mui/material";
import {PatientSearchForm} from "../PatientSearchForm";
import {AnalysisTable} from "./components/AnalysisTable";
import MockAdapter from "axios-mock-adapter";
import axios from "axios";
import {Syndromes} from "./components/Syndromes";

export const AnalysisDescription: React.FC = () => {
    const [analysisData, setAnalysisData] = useState<any>(null);

    const handleReceiveData = (data: any) => {
        setAnalysisData(data);
    };

    return (
        <Grid2 container direction="row" justifyContent="center">
            <Grid2>
                <PatientSearchForm onReceiveData={handleReceiveData}/>
                {analysisData != null && (
                    <Grid2 rowGap="XL">
                        <Grid2>
                            <strong style={{marginBottom: '16px'}}>ФИО: {analysisData.fio}</strong>
                            <Syndromes syndromes={analysisData.syndromes}/>
                        </Grid2>
                        <Grid2 sx={{marginTop: '20px'}}>
                            <AnalysisTable data={analysisData}/>
                        </Grid2>
                    </Grid2>
                )}
            </Grid2>
        </Grid2>
    );
};
