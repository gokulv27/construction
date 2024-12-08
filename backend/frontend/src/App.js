import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Sidebar from './components/Sidebar';
import Dashboard from './pages/Dashboard';
import EmployeeTypeManagement from './pages/EmployeeTypeManagement';
import DocumentTypeManagement from './pages/DocumentTypeManagement';
import VendorTypesManagement from './pages/VendorTypesManagement';
import UserManagement from './pages/userManagement'; // Corrected capitalization
import AddUser from './components/authentication/AddUser';
import LaborManagement from './pages/LaborManagement';
import LaborSkillManagement from './pages/LaborSkillManagement'; // Import Labor Skill Management
import './App.css';

function App() {
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
                <Route path="/masters/employee-type" element={<EmployeeTypeManagement />} />

                {/* Document Type Management Route */}
                <Route path="/masters/document-type" element={<DocumentTypeManagement />} />

                {/* Vendor Types Management Route */}
                <Route path="/masters/vendor-types" element={<VendorTypesManagement />} />

                {/* User Management Route */}
                <Route path="/masters/user-management" element={<UserManagement />} />

                {/* Labor Skill Management Route */}
                <Route path="/masters/labor-skill-management" element={<LaborSkillManagement />} />

                {/* Add User Route */}
                <Route path="/add-user" element={<AddUser />} />

                {/* Labor Management Route */}
                <Route path="/labor-management" element={<LaborManagement />} />
              </Routes>
            </div>
          </main>
        </div>
      </div>
    </Router>
  );
}

export default App;
