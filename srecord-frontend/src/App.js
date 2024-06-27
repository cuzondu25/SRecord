import React from 'react';
import SalesEntryForm from './components/SalesEntryForm';
import WeeklyReport from './components/WeeklyReport';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import './App.css';

function App() {
    return (
        <div className="App">
            <header className="App-header">
                <h1>SRecord</h1>
            </header>
            <main>
                <Router>
                    <div >
                        <nav className="navbar">
                            <ul className="nav-tabs">
	                        <li className="nav-tab">
	                            <Link to="/">Home</Link>
	                        </li>
                                <li className="nav-tab">
                                    <Link to="/sales-entry">Sales Entry</Link>
                                </li>
                                <li className="nav-tab">
                                    <Link to="/weekly-report">Weekly Report</Link>
                                </li>
                            </ul>
                        </nav>

                        <Routes>
                            <Route path="/sales-entry" element={<SalesEntryForm />} />
                            <Route path="/weekly-report" element={<WeeklyReport />} />
                        </Routes>
                    </div>
                </Router>
            </main>
        </div>
    );
}

export default App;
