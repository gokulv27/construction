import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Sidebar from './components/Sidebar';
import TopNav from './components/TopNav';
import Dashboard from './pages/Dashboard';
import EmployeeTypeManagement from './pages/EmployeeTypeManagement';
import './App.css';

function App() {
  // Modal state to control visibility
  const [isModalOpen, setIsModalOpen] = useState(false);

  return (
    <Router>
      <div className="app">
        {/* Pass modal handler to TopNav */}
        <TopNav onNewEntryClick={() => setIsModalOpen(true)} />
        <div className="content-wrapper">
          <Sidebar />
          <main className="main-content">
            <div className="centered-container">
              <Routes>
                {/* Dashboard route */}
                <Route path="/" element={<Dashboard />} />

                {/* Employee Type Management route */}
                <Route
                  path="/masters/employee-type"
                  element={
                    <EmployeeTypeManagement
                      isModalOpen={isModalOpen}
                      setIsModalOpen={setIsModalOpen}
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
