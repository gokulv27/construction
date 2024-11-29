import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Sidebar from './components/Sidebar';
import TopNav from './components/TopNav';
import Dashboard from './pages/Dashboard';
import EmployeeTypeManagement from './pages/EmployeeTypeManagement';
import './App.css';

function App() {
  const [isNewEntryModalOpen, setIsNewEntryModalOpen] = useState(false);

  const handleNewEntryClick = () => {
    setIsNewEntryModalOpen(true);
  };

  return (
    <Router>
      <div className="app">
        <TopNav onNewEntryClick={handleNewEntryClick} />
        <div className="content-wrapper">
          <Sidebar />
          <main className="main-content">
            <div className="centered-container">
              <Routes>
                <Route path="/" element={<Dashboard />} />
                <Route 
                  path="/masters/employee-type" 
                  element={
                    <EmployeeTypeManagement 
                      isNewEntryModalOpen={isNewEntryModalOpen}
                      setIsNewEntryModalOpen={setIsNewEntryModalOpen}
                    />
                  } 
                />
              </Routes>
            </div>
          </main>
        </div>
      </div>
    </Router>
  );
}

export default App;

