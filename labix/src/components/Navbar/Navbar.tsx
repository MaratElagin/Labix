import React from 'react'
import './Navbar.css';
import {ReactComponent as Icon} from '../../svg/logo.svg';

export const Navbar: React.FC = () => {
    return (
        <div>
            <header className="header">
                <a href="">
                    <div className="logo">
                        <Icon className="icon"/>
                        <h1 className="title">Labix</h1>
                    </div>
                </a>
                <a href="">
                    <h2 className="profile-nav-link">Профиль</h2>
                </a>
            </header>
        </div>
    )
}