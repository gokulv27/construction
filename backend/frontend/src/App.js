import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Sidebar from './components/Sidebar';
import Dashboard from './pages/Dashboard';
import EmployeeTypeManagement from './pages/EmployeeTypeManagement';
import DocumentTypeManagement from './pages/DocumentTypeManagement';
import VendorTypesManagement from './pages/VendorTypesManagement';
import UserManagement from './pages/userManagement'; // Import UserManagement

import './App.css';

function App() {
  const [isModalOpen, setIsModalOpen] = useState(false);

  return (
    <Router>
      <div className="app">
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
                      isModalOpen={isModalOpen}
                      setIsModalOpen={setIsModalOpen}
                    />
                  }
                />

                <Route
                  path="/masters/document-type"
                  element={
                    <DocumentTypeManagement
                      isModalOpen={isModalOpen}
                      setIsModalOpen={setIsModalOpen}
                    />
                  }
                />

                <Route
                  path="/masters/vendor-types"
                  element={
                    <VendorTypesManagement
                      isModalOpen={isModalOpen}
                      setIsModalOpen={setIsModalOpen}
                    />
                  }
                />

                {/* User Management route */}
                <Route
                  path="/masters/user-management"
                  element={
                    <UserManagement
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
