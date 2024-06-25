import React, { useState, useEffect } from 'react';
import axios from 'axios';

const WeeklyReport = () => {
  const [weeklyRecord, setWeeklyRecord] = useState(null);

  useEffect(() => {
    axios.get('/api/weekly-records')
      .then(response => {
        setWeeklyRecord(response.data);
      })
      .catch(error => {
        console.error('There was an error fetching the weekly records!', error);
      });
  }, []);

  if (!weeklyRecord) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <h2>Weekly Sales Report</h2>
      <p>Week Start: {weeklyRecord.week_start}</p>
      <p>Week End: {weeklyRecord.week_end}</p>
      <p>Total Sales: ${weeklyRecord.total_sales.toFixed(2)}</p>
    </div>
  );
};

export default WeeklyReport;
