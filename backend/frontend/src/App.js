import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Sidebar from './components/Sidebar';
import Dashboard from './pages/Dashboard';
import EmployeeTypeManagement from './pages/EmployeeTypeManagement';
import DocumentTypeManagement from './pages/DocumentTypeManagement';
import  VendorTypesManagement from './pages/VendorTypesManagement';

import './App.css';

function App() {
  // Modal state to control visibility
  const [isModalOpen, setIsModalOpen] = useState(false);

  return (
    <Router>
      <div className="app">
        {/* Sidebar and main content */}
        <div className="content-wrapper">
          <Sidebar />
          <main className="main-content">
            <div className="centered-container">
              {/* All Routes must be inside this <Routes> component */}
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

                {/* Document Type Management route */}
                <Route
                  path="/masters/document-type"
                  element={
                    <DocumentTypeManagement
                      isModalOpen={isModalOpen}
                      setIsModalOpen={setIsModalOpen}
                    />
                  }
                />
                 {/* Document Type Management route */}
                 <Route
                  path="/masters/vendor-types"
                  element={
                    <VendorTypesManagement
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
