import React from 'react';
import {Grid2} from "@mui/material";
import './ProfilePage.css';
import {AnalysisDescription} from "./components/AnalysisDescription";

export const ProfilePage: React.FC = () => {
    return (
        <div>
            <Grid2 container direction="row" justifyContent="center">
                <AnalysisDescription/>
            </Grid2>
        </div>
    );
};
