import React from 'react';
import './App.css';
import {ProfilePage} from "./pages/ProfilePage/ProfilePage";
import {Navbar} from "./components/Navbar";

function App() {
    return (
        <>
            <Navbar/>
            <div className="container">
                <ProfilePage/>
            </div>
        </>
    );
}

export default App;
