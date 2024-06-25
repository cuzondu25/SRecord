import React from 'react';
import { BrowserRouter as Router, Route, Switch, Link } from 'react-router-dom';
import SalesEntryForm from './components/SalesEntryForm';
import WeeklyReport from './components/WeeklyReport';
import './App.css';

function App() {
  return (
    <Router>
      <div>
        <nav>
          <ul>
            <li>
              <Link to="/">Sales Entry</Link>
            </li>
            <li>
              <Link to="/weekly-report">Weekly Report</Link>
            </li>
          </ul>
        </nav>

        <Switch>
          <Route path="/" exact component={SalesEntryForm} />
          <Route path="/weekly-report" component={WeeklyReport} />
        </Switch>
      </div>
    </Router>
  );
}

export default App;
