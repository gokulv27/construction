import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Sidebar from './components/Sidebar';
import Dashboard from './pages/Dashboard';
import EmployeeTypeManagement from './pages/EmployeeTypeManagement';
import DocumentTypeManagement from './pages/DocumentTypeManagement';
import VendorTypesManagement from './pages/VendorTypesManagement';
import UserManagement from './pages/userManagement'; // Corrected import
import AddUser from './components/authentication/AddUser';
import LaborManagement from './pages/LaborManagement';
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
                {/* Dashboard Route */}
                <Route path="/" element={<Dashboard />} />

                {/* Employee Type Management Route */}
                <Route
                  path="/masters/employee-type"
                  element={
                    <EmployeeTypeManagement
                      isModalOpen={isModalOpen}
                      setIsModalOpen={setIsModalOpen}
                    />
                  }
                />

                {/* Document Type Management Route */}
                <Route
                  path="/masters/document-type"
                  element={
                    <DocumentTypeManagement
                      isModalOpen={isModalOpen}
                      setIsModalOpen={setIsModalOpen}
                    />
                  }
                />

                {/* Vendor Types Management Route */}
                <Route
                  path="/masters/vendor-types"
                  element={
                    <VendorTypesManagement
                      isModalOpen={isModalOpen}
                      setIsModalOpen={setIsModalOpen}
                    />
                  }
                />

                {/* User Management Route */}
                <Route
                  path="/masters/user-management"
                  element={
                    <UserManagement
                      isModalOpen={isModalOpen}
                      setIsModalOpen={setIsModalOpen}
                    />
                  }
                />

                {/* Add User Route */}
                <Route path="/add-user" element={<AddUser />} />
                {/* Labormanagement */}
                <Route path="/Labor_management" element={<LaborManagement />} />
              </Routes>
            </div>
          </main>
        </div>
      </div>
    </Router>
  );
}

export default App;
