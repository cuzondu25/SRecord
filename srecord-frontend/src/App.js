import React, { useState } from 'react';
import SalesEntryForm from './components/SalesEntryForm';
import WeeklyReport from './components/WeeklyReport';
import Login from './components/Login';
import Register from './components/Register';
import { BrowserRouter as Router, Route, Routes, Link, Navigate } from 'react-router-dom';
import { AuthProvider, AuthContext } from './AuthContext';
import './App.css';

function App() {
    const [isAuthenticated, setIsAuthenticated] = useState(!!localStorage.getItem('token'));

    return (
        <AuthProvider value={{ isAuthenticated, login: () => setIsAuthenticated(true), logout: () => setIsAuthenticated(false) }}>
            <div className="App">
                <header className="App-header">
                    <h1>SRecord</h1>
                </header>
                <main>
                    <Router>
                        <div>
                            <nav className="navbar">
                                <ul className="nav-tabs">
                                    <li className="nav-tab">
                                        <Link to="/">Home</Link>
                                    </li>
                                    {isAuthenticated && (
                                        <>
                                            <li className="nav-tab">
                                                <Link to="/sales-entry">Sales Entry</Link>
                                            </li>
                                            <li className="nav-tab">
                                                <Link to="/weekly-report">Weekly Report</Link>
                                            </li>
                                            <li className="nav-tab">
                                                <Link to="/logout">Logout</Link>
                                            </li>
                                        </>
                                    )}
                                    {!isAuthenticated && (
                                        <>
                                            <li className="nav-tab">
                                                <Link to="/login">Login</Link>
                                            </li>
                                            <li className="nav-tab">
                                                <Link to="/register">Register</Link>
                                            </li>
                                        </>
                                    )}
                                </ul>
                            </nav>

                            <Routes>
                                <Route path="/login" element={<Login />} />
                                <Route path="/register" element={<Register />} />
                                <Route path="/sales-entry" element={isAuthenticated ? <SalesEntryForm /> : <Navigate to="/login" />} />
                                <Route path="/weekly-report" element={isAuthenticated ? <WeeklyReport /> : <Navigate to="/login" />} />
                                <Route path="/logout" element={<Logout />} />
                            </Routes>
                        </div>
                    </Router>
                </main>
            </div>
        </AuthProvider>
    );
}

function Logout() {
    const { logout } = React.useContext(AuthContext);
    React.useEffect(() => {
        localStorage.removeItem('token');
        logout();
    }, [logout]);
    return <Navigate to="/login" />;
}

export default App;
